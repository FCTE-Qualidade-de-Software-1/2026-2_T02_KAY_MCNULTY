#!/usr/bin/env python3
"""
update_metrics.py

Extrai métricas do histórico Git (commits, adições, remoções) e da API de Issues do GitHub
para gerar automaticamente gráficos Mermaid (xychart-beta) e tabelas Markdown alinhadas
ao modelo PSM/CID e à rubrica AG-C5 da equipe Kay McNulty (Turma 01 - 2026.2).
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

# Diretórios principais
REPO_ROOT = Path(__file__).resolve().parents[2]
SNIPPETS_DIR = REPO_ROOT / "snippets"

REPO_OWNER = "FCTE-Qualidade-de-Software-1"
REPO_NAME = "2026-2_T02_KAY_MCNULTY"
VALOR_HORA_BRL = 50.0  # R$ 50,00/h conforme Tabela 3 da documentação da equipe

# Definição dos integrantes e duplas conforme docs/gestao/metricas-psm.md
TEAM_MEMBERS = [
    {
        "name": "Artur Fernandes Galdino",
        "handle": "ArturFGaldino",
        "matricula": "241010923",
        "dupla": "Dupla 1 (Compatibilidade)",
        "papel": "Analista de Compatibilidade / Arquitetura e Escopo",
    },
    {
        "name": "Nicole Jovita Fernandes",
        "handle": "nicolejovita",
        "matricula": "241012347",
        "dupla": "Dupla 1 (Compatibilidade)",
        "papel": "Analista de Requisitos / Stakeholders e ODS",
    },
    {
        "name": "Davi Ursolino de Oliveira",
        "handle": "DaviUrsulino",
        "matricula": "241012202",
        "dupla": "Dupla 2 (Confiabilidade)",
        "papel": "Analista de Confiabilidade / GQM e Métricas",
    },
    {
        "name": "João Eduardo Pereira Rabelo",
        "handle": "JoaoEduardoP",
        "matricula": "180053299",
        "dupla": "Dupla 2 (Confiabilidade)",
        "papel": "Analista de Confiabilidade / Metodologia PSM",
    },
    {
        "name": "Natan José França",
        "handle": "Natan8643",
        "matricula": "241011537",
        "dupla": "Dupla 3 (Usabilidade)",
        "papel": "Analista de Usabilidade / Diagrama GQM e Limiares",
    },
    {
        "name": "Yan Santos Rodrigues",
        "handle": "yanrdgs-dev",
        "matricula": "241025480",
        "dupla": "Dupla 3 (Usabilidade)",
        "papel": "Analista de Usabilidade / Especificação e Heurísticas",
    },
]

TRACKED_AUTHORS = [m["handle"] for m in TEAM_MEMBERS]
MEMBER_BY_HANDLE = {m["handle"]: m for m in TEAM_MEMBERS}

# Cores distintas e acessíveis para os 6 integrantes nos gráficos Mermaid
COLOR_PALETTE = "#2563eb, #7c3aed, #db2777, #ea580c, #16a34a, #0891b2"
MERMAID_INIT = f'%%{{init: {{"themeVariables": {{"xyChart": {{"plotColorPalette": "{COLOR_PALETTE}"}}}}}}}}%%\n'

# Horas de referência por issue homologadas no catálogo do PC1 (docs/gestao/metricas-psm.md)
DEFAULT_HOURS_CATALOG = {
    1: 4.0,  # Arquitetura e Escopo dos 4 módulos
    2: 2.0,  # Justificativa Compatibilidade
    3: 2.0,  # GQM Compatibilidade
    4: 2.0,  # Métricas Compatibilidade
    5: 2.0,  # Propósito e Stakeholders
    6: 2.0,  # Modelo ISO 25010
    7: 2.0,  # Escopo e Limites
    8: 2.0,  # Alinhamento ODS
    9: 4.0,  # Confiabilidade Fases 1 e 2
    10: 2.0, # Especificação GQM Confiabilidade
    11: 2.0, # Métricas Confiabilidade
    12: 2.0, # Diagrama Mermaid Confiabilidade
    13: 2.0, # Padronização LaTeX Confiabilidade
    14: 4.0, # Justificativa Usabilidade
    15: 2.0, # GQM e Heurísticas Usabilidade
    16: 2.0, # Métricas Usabilidade
    17: 2.0, # Redação Usabilidade
    18: 2.0, # Estruturação PSM
}


def normalize_author(name: str, email: str) -> str:
    """Normaliza o autor do Git para o handle oficial no GitHub da equipe."""
    combined = f"{name} {email}".lower()
    if "github-actions" in combined or "actions@github.com" in combined:
        return "github-actions[bot]"
    if "artur" in combined or "fernandesartur4" in combined or "arturfgaldino" in combined:
        return "ArturFGaldino"
    if "nicole" in combined or "jovita" in combined or "nicolejovita" in combined:
        return "nicolejovita"
    if "davi" in combined or "ursulino" in combined or "davizera0601" in combined or "daviursulino" in combined:
        return "DaviUrsulino"
    if "joão" in combined or "joao" in combined or "joaoeduardo" in combined or "joaoeduardop" in combined:
        return "JoaoEduardoP"
    if "natan" in combined or "frança" in combined or "franca" in combined or "natan8643" in combined:
        return "Natan8643"
    if "yan" in combined or "rodrigues" in combined or "yansantosrodrigues" in combined or "yanrdgs-dev" in combined:
        return "yanrdgs-dev"
    return name.strip() or "Unknown"


def get_git_log_data():
    """Extrai timestamps de commits, autores normalizados, adições e deleções."""
    cmd = [
        "git",
        "log",
        "--numstat",
        "--date=iso-strict",
        "--format=COMMIT|%ad|%an|%ae",
    ]
    try:
        result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
    except Exception as e:
        print(f"Aviso ao ler git log: {e}", file=sys.stderr)
        lines = []

    commits_by_week = defaultdict(lambda: defaultdict(int))
    additions_by_week = defaultdict(lambda: defaultdict(int))
    deletions_by_week = defaultdict(lambda: defaultdict(int))
    total_commits = defaultdict(int)
    total_additions = defaultdict(int)
    total_deletions = defaultdict(int)
    all_weeks = set()

    current_week = None
    current_author = None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("COMMIT|"):
            parts = line.split("|")
            date_str = parts[1]
            author_name = parts[2]
            author_email = parts[3] if len(parts) > 3 else ""

            dt = datetime.fromisoformat(date_str)
            iso_year, iso_week, _ = dt.isocalendar()
            week_key = f"{iso_year}-W{iso_week:02d}"

            current_week = week_key
            current_author = normalize_author(author_name, author_email)
            all_weeks.add(week_key)

            commits_by_week[week_key][current_author] += 1
            total_commits[current_author] += 1
        else:
            # linha do numstat: <adicionados> <removidos> <arquivo>
            parts = line.split("\t")
            if len(parts) >= 3 and current_week and current_author:
                added = int(parts[0]) if parts[0].isdigit() else 0
                deleted = int(parts[1]) if parts[1].isdigit() else 0
                additions_by_week[current_week][current_author] += added
                deletions_by_week[current_week][current_author] += deleted
                total_additions[current_author] += added
                total_deletions[current_author] += deleted

    if not all_weeks:
        now_year, now_week, _ = datetime.now().isocalendar()
        all_weeks.add(f"{now_year}-W{now_week:02d}")

    # Gerar sequência contínua de semanas
    sorted_weeks = sorted(all_weeks)
    earliest_yr, earliest_wk = [int(x) for x in sorted_weeks[0].split("-W")]
    latest_yr, latest_wk = [int(x) for x in sorted_weeks[-1].split("-W")]

    from datetime import date
    earliest_date = date.fromisocalendar(earliest_yr, earliest_wk, 1)
    latest_date = date.fromisocalendar(latest_yr, latest_wk, 1)

    full_weeks = []
    curr = earliest_date
    while curr <= latest_date or len(full_weeks) < 3:
        yr, wk, _ = curr.isocalendar()
        wk_str = f"{yr}-W{wk:02d}"
        if wk_str not in full_weeks:
            full_weeks.append(wk_str)
        curr += timedelta(days=7)

    totals = {
        "commits": total_commits,
        "additions": total_additions,
        "deletions": total_deletions,
    }

    return full_weeks, commits_by_week, additions_by_week, deletions_by_week, totals


def resolve_token(*env_names):
    """Obtém token do GitHub das variáveis de ambiente ou ferramentas configuradas."""
    for name in env_names:
        val = os.environ.get(name)
        if val:
            return val
    try:
        token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
        if token:
            return token
    except Exception:
        pass
    return None


def fetch_github_issues():
    """Consulta as issues do repositório via API REST do GitHub com paginação."""
    token = resolve_token("GITHUB_TOKEN", "GH_TOKEN")
    headers = {"User-Agent": "KayMcNulty-MetricsAutomation", "Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    all_items = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=all&per_page=100&page={page}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if not data:
                    break
                all_items.extend(data)
                if len(data) < 100:
                    break
                page += 1
        except Exception as e:
            print(f"Aviso ao consultar issues da API do GitHub: {e}", file=sys.stderr)
            break

    # Filtrar apenas issues legítimas (remover PRs)
    issues_only = [item for item in all_items if "pull_request" not in item]
    return issues_only


def extract_hours_from_issue(issue: dict) -> float:
    """Extrai horas estimadas/realizadas do corpo da issue ou do catálogo homologado."""
    num = issue.get("number")
    body = issue.get("body") or ""

    # Busca padrões como: 'Horas Dedicadas: 4h' ou 'Esforço: 2.5h'
    match = re.search(r"(?:horas?(?:\s*dedicadas?)?|esfor[çc]o)[:\s\*]+(\d+(?:[.,]\d+)?)\s*h?", body, re.IGNORECASE)
    if match:
        try:
            return float(match.group(1).replace(",", "."))
        except ValueError:
            pass

    # Fallback para o catálogo documentado de issues do PC1
    if num in DEFAULT_HOURS_CATALOG:
        return DEFAULT_HOURS_CATALOG[num]

    return 2.0  # estimativa padrão conservadora


def get_issue_and_effort_metrics():
    """Calcula estatísticas de issues abertas, fechadas e esforço (h) por membro."""
    issues = fetch_github_issues()

    counts = {
        author: {
            "total": 0,
            "closed": 0,
            "open": 0,
            "hours": 0.0,
        }
        for author in TRACKED_AUTHORS
    }

    for issue in issues:
        closed = issue.get("state") == "closed"
        assignees = [a.get("login") for a in issue.get("assignees", []) if a.get("login")]
        hours = extract_hours_from_issue(issue)

        # Se houver múltiplos responsáveis, o esforço é rateado igualmente
        weight = 1.0 / len(assignees) if assignees else 1.0

        for login in assignees:
            handle = normalize_author(login, "")
            if handle not in counts:
                continue
            c = counts[handle]
            c["total"] += 1
            if closed:
                c["closed"] += 1
                c["hours"] += hours * weight
            else:
                c["open"] += 1

    return counts


def calculate_upper_bound(values, min_bound=5):
    """Calcula o teto arredondado e elegante do eixo Y para gráficos Mermaid."""
    max_val = max(values) if values else 0
    if max_val <= 0:
        return min_bound
    if max_val <= 10:
        return 10
    if max_val <= 50:
        return ((int(max_val) // 5) + 1) * 5
    if max_val <= 200:
        return ((int(max_val) // 20) + 1) * 20
    return ((int(max_val) // 100) + 1) * 100


def render_timeline_chart(title: str, y_label: str, weeks: list, series_by_author: dict) -> str:
    """Gera gráfico Mermaid xychart-beta para evolução temporal por semana."""
    x_labels = [f'"{w}"' for w in weeks]
    x_axis_str = f'[{", ".join(x_labels)}]'

    all_vals = []
    lines = []
    for author in TRACKED_AUTHORS:
        vals = [series_by_author.get(w, {}).get(author, 0) for w in weeks]
        all_vals.extend(vals)
        lines.append(f"    line [{', '.join(str(v) for v in vals)}]")

    max_bound = calculate_upper_bound(all_vals, min_bound=10)

    chart = (
        MERMAID_INIT
        + "xychart-beta\n"
        + f'    title "{title}"\n'
        + f"    x-axis {x_axis_str}\n"
        + f'    y-axis "{y_label}" 0 --> {max_bound}\n'
        + "\n".join(lines)
    )
    return chart


def render_bar_chart(title: str, y_label: str, counts_by_author: dict, key: str = "total") -> str:
    """Gera gráfico Mermaid xychart-beta com barras coloridas por integrante."""
    x_labels = [f'"{author}"' for author in TRACKED_AUTHORS]
    vals = [counts_by_author.get(author, {}).get(key, 0) for author in TRACKED_AUTHORS]
    max_bound = calculate_upper_bound(vals, min_bound=5)

    bar_lines = []
    for i, author in enumerate(TRACKED_AUTHORS):
        author_val = counts_by_author.get(author, {}).get(key, 0)
        slot_vals = [author_val if j == i else 0 for j in range(len(TRACKED_AUTHORS))]
        bar_lines.append(f"    bar [{', '.join(str(v) for v in slot_vals)}]")

    chart = (
        MERMAID_INIT
        + "xychart-beta\n"
        + f'    title "{title}"\n'
        + f"    x-axis [{', '.join(x_labels)}]\n"
        + f'    y-axis "{y_label}" 0 --> {max_bound}\n'
        + "\n".join(bar_lines)
    )
    return chart


def generate_contributions_table(git_totals: dict, issue_counts: dict) -> str:
    """Gera tabela Markdown consolidada de contribuição e esforço individual (Critério AG-C5)."""
    lines = [
        "| Integrante (Nome e Matrícula) | Usuário GitHub | Dupla | Commits | Linhas (+/-) | Issues Fechadas | Horas (h) | Custo Total (R$) | % Esforço (AG-C5) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_commits = 0
    tot_adds = 0
    tot_dels = 0
    tot_closed = 0
    tot_hours = sum(issue_counts.get(h, {}).get("hours", 0.0) for h in TRACKED_AUTHORS)
    if tot_hours <= 0:
        tot_hours = 72.0  # Referência do PC1

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        matricula = m["matricula"]
        dupla = m["dupla"]

        c = git_totals["commits"].get(handle, 0)
        a = git_totals["additions"].get(handle, 0)
        d = git_totals["deletions"].get(handle, 0)
        net = a - d

        st = issue_counts.get(handle, {})
        closed_iss = st.get("closed", 0)
        hours = st.get("hours", 0.0)
        if hours == 0.0 and closed_iss > 0:
            hours = 12.0  # fallback proporcional

        custo = hours * VALOR_HORA_BRL
        pct_esforco = (hours / tot_hours * 100.0) if tot_hours > 0 else (100.0 / len(TEAM_MEMBERS))

        tot_commits += c
        tot_adds += a
        tot_dels += d
        tot_closed += closed_iss

        sign_net = f"+{net}" if net > 0 else str(net)
        lines.append(
            f"| **{name}**<br>Matrícula: `{matricula}` | [@{handle}](https://github.com/{handle}) | {dupla} | "
            f"{c} | +{a} / -{d} ({sign_net}) | {closed_iss} | {hours:.1f}h | R$ {custo:,.2f} | **{pct_esforco:.2f}%** |"
        )

    tot_net = tot_adds - tot_dels
    tot_sign_net = f"+{tot_net}" if tot_net > 0 else str(tot_net)
    tot_custo = tot_hours * VALOR_HORA_BRL

    lines.append(
        f"| **TOTAL CONSOLIDADO** | — | — | **{tot_commits}** | **+{tot_adds} / -{tot_dels} ({tot_sign_net})** | "
        f"**{tot_closed}** | **{tot_hours:.1f}h** | **R$ {tot_custo:,.2f}** | **100,00%** |"
    )

    return "\n".join(lines)


def generate_issues_table(issue_counts: dict) -> str:
    """Gera tabela Markdown com taxa de resolução de issues por membro."""
    lines = [
        "| Integrante | Usuário GitHub | Dupla | Issues Fechadas | Issues Abertas | Total de Issues | Taxa de Conclusão |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_closed = 0
    tot_open = 0
    tot_all = 0

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        dupla = m["dupla"]

        st = issue_counts.get(handle, {})
        closed = st.get("closed", 0)
        opened = st.get("open", 0)
        total = st.get("total", 0)
        rate = f"{(closed / total * 100):.1f}%".replace(".", ",") if total > 0 else "0,0%"

        tot_closed += closed
        tot_open += opened
        tot_all += total

        lines.append(
            f"| **{name}** | [@{handle}](https://github.com/{handle}) | {dupla} | {closed} | {opened} | {total} | {rate} |"
        )

    overall_rate = f"{(tot_closed / tot_all * 100):.1f}%".replace(".", ",") if tot_all > 0 else "0,0%"
    lines.append(
        f"| **TOTAL CONSOLIDADO** | — | — | **{tot_closed}** | **{tot_open}** | **{tot_all}** | **{overall_rate}** |"
    )

    return "\n".join(lines)


def main():
    SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)

    weeks, commits, additions, deletions, git_totals = get_git_log_data()
    issue_counts = get_issue_and_effort_metrics()

    # Gerar gráficos
    velocity_chart = render_timeline_chart(
        "Velocidade de Commits por Integrante ao Longo do Tempo",
        "Commits",
        weeks,
        commits,
    )
    additions_chart = render_timeline_chart(
        "Linhas Adicionadas por Integrante ao Longo do Tempo",
        "Linhas Adicionadas",
        weeks,
        additions,
    )
    deletions_chart = render_timeline_chart(
        "Linhas Removidas por Integrante ao Longo do Tempo",
        "Linhas Removidas",
        weeks,
        deletions,
    )
    issues_chart = render_bar_chart(
        "Issues Atribuídas por Integrante",
        "Issues",
        issue_counts,
        key="total",
    )
    resolved_chart = render_bar_chart(
        "Tarefas Resolvidas por Integrante",
        "Tarefas Resolvidas",
        issue_counts,
        key="closed",
    )

    # Gerar tabelas Markdown
    contributions_table = generate_contributions_table(git_totals, issue_counts)
    issues_table = generate_issues_table(issue_counts)

    # Escrever arquivos de snippet
    (SNIPPETS_DIR / "commit-velocity.mmd").write_text(velocity_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-additions.mmd").write_text(additions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-deletions.mmd").write_text(deletions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "assigned-issues.mmd").write_text(issues_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "resolved-issues.mmd").write_text(resolved_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "contributions-summary.md").write_text(contributions_table + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "issues-summary.md").write_text(issues_table + "\n", encoding="utf-8")

    print(f"Snippets gerados com sucesso em: {SNIPPETS_DIR}")
    print(f"Semanas mapeadas: {weeks}")
    print(f"Autores monitorados: {TRACKED_AUTHORS}")


if __name__ == "__main__":
    main()
