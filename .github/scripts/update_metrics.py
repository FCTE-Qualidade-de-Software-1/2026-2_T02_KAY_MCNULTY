#!/usr/bin/env python3
"""
update_metrics.py

Extrai métricas do histórico Git (commits, adições, remoções) e da API de Issues/PRs do GitHub
para gerar dinamicamente os gráficos Mermaid (xychart-beta) e as tabelas Markdown de Gestão
(Tabela de Contribuição AG-C5, Recursos e Custos, Distribuição por Área Técnica e Desempenho de Processos)
para a equipe Kay McNulty (Turma 01 - 2026.2).
"""

import json
import math
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
VALOR_HORA_BRL = 50.0  # R$ 50,00/h conforme diretriz orçamentária da equipe

# Definição canônica dos integrantes, duplas e responsabilidades
TEAM_MEMBERS = [
    {
        "name": "Artur Fernandes Galdino",
        "handle": "ArturFGaldino",
        "matricula": "241010923",
        "dupla": "Dupla 1 (Compatibilidade)",
        "area": "Compatibilidade",
        "papel": "Analista de Compatibilidade / Mapeamento de Arquitetura e Escopo",
        "responsabilidades": "• Mapeamento arquitetural do Portal Detran Digital DF e delimitação dos 4 módulos avaliados: Infração, Atendimento, Protocolo e Chatbot (Issue #01).<br>• Especificação conceitual e operacional da árvore GQM de Compatibilidade (Issue #03).<br>• Formulação das métricas operacionais ($TCBN$, $ICR$, $TSIS$), procedimentos de coleta e limiares de decisão de Compatibilidade (Issue #04).<br>• Co-redação do propósito da avaliação, partes interessadas e limites de escopo (Issues #05 e #07).",
    },
    {
        "name": "Nicole Jovita Fernandes",
        "handle": "nicolejovita",
        "matricula": "241012347",
        "dupla": "Dupla 1 (Compatibilidade)",
        "area": "Compatibilidade",
        "papel": "Analista de Requisitos / Stakeholders, Modelo ISO 25010 e ODS",
        "responsabilidades": "• Justificativa e delimitação de profundidade de Compatibilidade cross-browser/cross-platform (Issue #02).<br>• Mapeamento formal de stakeholders e matriz de decisões apoiadas pela avaliação (Issue #05).<br>• Adaptação gráfica do modelo SQuaRE (ISO/IEC 25010) e matriz de priorização de características (Issue #06).<br>• Conexão dos serviços de trânsito aos Objetivos de Desenvolvimento Sustentável da ONU — ODS 9 (Meta 9.c) e ODS 16 (Meta 16.6) (Issue #08).",
    },
    {
        "name": "Davi Ursolino de Oliveira",
        "handle": "DaviUrsulino",
        "matricula": "241012202",
        "dupla": "Dupla 2 (Confiabilidade)",
        "area": "Confiabilidade",
        "papel": "Analista de Confiabilidade / Especificação GQM e Métricas",
        "responsabilidades": "• Especificação GQM formal da característica de Confiabilidade (Seção 4.3 do artigo) (Issue #10).<br>• Definição das métricas quantitativas de Confiabilidade ($TDO$, $TCFF$, $DFF$, $TTOA$, $TRTI$, $TMR$), procedimentos de cálculo e níveis de julgamento (Issue #11).<br>• Construção e validação do diagrama visual da árvore GQM de Confiabilidade em Mermaid (Issue #12).<br>• Padronização matemática das equações em LaTeX/MathJax e revisão de consistência teórica (Issue #13).",
    },
    {
        "name": "João Eduardo Pereira Rabelo",
        "handle": "JoaoEduardoP",
        "matricula": "180053299",
        "dupla": "Dupla 2 (Confiabilidade)",
        "area": "Confiabilidade",
        "papel": "Analista de Confiabilidade / Metodologia e Métricas PSM",
        "responsabilidades": "• Fundamentação e justificativa técnica da característica de Confiabilidade em serviços governamentais (Issue #09).<br>• Apoio na modelagem do processo de avaliação sob a ótica da norma ISO/IEC 25040.<br>• Estruturação das categorias de acompanhamento do modelo PSM/CID (Processos, Calendário e Recursos).<br>• Auditoria de conformidade das atas de reunião e governança de releases.",
    },
    {
        "name": "Natan José França",
        "handle": "Natan8643",
        "matricula": "241011537",
        "dupla": "Dupla 3 (Usabilidade)",
        "area": "Usabilidade",
        "papel": "Analista de Usabilidade / Diagrama GQM e Níveis de Julgamento",
        "responsabilidades": "• Delimitação de escopo e justificativa da característica de Usabilidade / Capacidade de Interação (Issue #14).<br>• Modelagem do objetivo, questões analíticas e hipóteses de Usabilidade nos 4 módulos (Issue #15).<br>• Estabelecimento das réguas de pontuação e critérios de julgamento para proteção contra erros ($TCAPA$, $IEFO$, $TPRE$) (Issue #16).<br>• Elaboração do diagrama visual GQM de Usabilidade e revisão do texto para o artigo (Issue #17).",
    },
    {
        "name": "Yan Santos Rodrigues",
        "handle": "yanrdgs-dev",
        "matricula": "241025480",
        "dupla": "Dupla 3 (Usabilidade)",
        "area": "Usabilidade",
        "papel": "Analista de Usabilidade / Especificação Operacional e Heurísticas",
        "responsabilidades": "• Justificativa ergonômica da avaliação diante do perfil de letramento digital dos condutores do DF (Issue #14).<br>• Especificação operacional dos procedimentos de inspeção por Heurísticas de Nielsen e questionário $SUS$ (Issue #15).<br>• Definição das métricas quantitativas de usabilidade e procedimentos de coleta (Issue #16).<br>• Redação e validação formal da documentação da Fase 2 de Usabilidade na GitPage (Issue #17).",
    },
]

TRACKED_AUTHORS = [m["handle"] for m in TEAM_MEMBERS]
MEMBER_BY_HANDLE = {m["handle"]: m for m in TEAM_MEMBERS}

# Paleta Mermaid acessível para 6 séries
COLOR_PALETTE = "#2563eb, #7c3aed, #db2777, #ea580c, #16a34a, #0891b2"
MERMAID_INIT = f'%%{{init: {{"themeVariables": {{"xyChart": {{"plotColorPalette": "{COLOR_PALETTE}"}}}}}}}}%%\n'

# Horas dedicadas homologadas no catálogo de issues do PC1
DEFAULT_HOURS_CATALOG = {
    1: 4.0,   # Arquitetura e Escopo dos 4 módulos (Artur & Nicole)
    2: 2.0,   # Justificativa Compatibilidade (Nicole)
    3: 3.0,   # GQM Compatibilidade (Artur)
    4: 3.0,   # Métricas Compatibilidade (Artur & Nicole)
    5: 2.0,   # Propósito e Stakeholders (Artur & Nicole)
    6: 2.0,   # Modelo ISO 25010 (Artur & Nicole)
    7: 2.0,   # Escopo e Limites (Artur & Nicole)
    8: 2.0,   # Alinhamento ODS (Artur & Nicole)
    9: 4.0,   # Confiabilidade Fases 1 e 2 (João Eduardo)
    10: 3.0,  # Especificação GQM Confiabilidade (Davi)
    11: 3.0,  # Métricas Confiabilidade (Davi)
    12: 2.0,  # Diagrama Mermaid Confiabilidade (Davi)
    13: 2.0,  # Padronização LaTeX Confiabilidade (Davi)
    14: 3.0,  # Justificativa Usabilidade (Natan & Yan)
    15: 3.0,  # GQM e Heurísticas Usabilidade (Natan & Yan)
    16: 3.0,  # Métricas Usabilidade (Natan & Yan)
    17: 3.0,  # Redação Usabilidade (Natan & Yan)
    18: 3.0,  # Estruturação PSM e Governança (Artur & João Eduardo)
}

# Responsáveis canônicos para issues/PRs caso o GitHub retorne sem assignees
FALLBACK_ASSIGNEES = {
    18: ["ArturFGaldino", "JoaoEduardoP"],
}


def fmt_br_currency(val: float) -> str:
    """Formata valor monetário no padrão BRL (R$ 1.200,00)."""
    formatted = f"{val:,.2f}"
    # Troca vírgula por ponto de milhar e ponto por vírgula decimal
    parts = formatted.split(".")
    integer_part = parts[0].replace(",", ".")
    decimal_part = parts[1]
    return f"R$ {integer_part},{decimal_part}"


def fmt_br_number(val: float, decimals: int = 1) -> str:
    """Formata número no padrão brasileiro com vírgula decimal."""
    return f"{val:.{decimals}f}".replace(".", ",")


def normalize_author(name: str, email: str = "") -> str:
    """Normaliza autor do Git para o handle correspondente."""
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
    """Extrai timestamps de commits, autores e co-autores (Co-authored-by), adições e deleções."""
    cmd = [
        "git",
        "log",
        "--numstat",
        "--date=iso-strict",
        "--format=@@@COMMIT|%ad|%an|%ae%n%B%n@@@END_COMMIT",
    ]
    try:
        result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        raw_output = result.stdout
    except Exception as e:
        print(f"Aviso ao ler git log: {e}", file=sys.stderr)
        raw_output = ""

    commits_by_week = defaultdict(lambda: defaultdict(int))
    additions_by_week = defaultdict(lambda: defaultdict(int))
    deletions_by_week = defaultdict(lambda: defaultdict(int))
    total_commits = defaultdict(int)
    total_additions = defaultdict(int)
    total_deletions = defaultdict(int)
    all_weeks = set()

    commit_blocks = raw_output.split("@@@COMMIT|")[1:]
    for block in commit_blocks:
        if "@@@END_COMMIT" not in block:
            continue
        header_and_body, numstat_part = block.split("@@@END_COMMIT", 1)
        lines = header_and_body.splitlines()
        if not lines:
            continue
        header = lines[0]
        body = "\n".join(lines[1:])
        header_parts = header.split("|")
        if len(header_parts) < 3:
            continue
        date_str = header_parts[0]
        an = header_parts[1]
        ae = header_parts[2] if len(header_parts) > 2 else ""

        try:
            dt = datetime.fromisoformat(date_str)
            iso_year, iso_week, _ = dt.isocalendar()
            week_key = f"{iso_year}-W{iso_week:02d}"
        except Exception:
            continue

        all_weeks.add(week_key)

        # Identificar autor principal e co-autores informados na mensagem do commit
        contributors = set()
        primary_handle = normalize_author(an, ae)
        if primary_handle != "Unknown" and primary_handle != "github-actions[bot]":
            contributors.add(primary_handle)

        coauthors_matches = re.findall(r"co-authored-by:\s*([^<\n\r]+)(?:<([^>\n\r]+)>)?", body, re.IGNORECASE)
        for ca_name, ca_email in coauthors_matches:
            ca_handle = normalize_author(ca_name.strip(), (ca_email or "").strip())
            if ca_handle != "Unknown" and ca_handle != "github-actions[bot]":
                contributors.add(ca_handle)

        if not contributors:
            continue

        # Registrar o commit para cada autor/co-autor
        for handle in contributors:
            commits_by_week[week_key][handle] += 1
            total_commits[handle] += 1

        # Somar numstat de adições e remoções
        tot_added = 0
        tot_deleted = 0
        for numline in numstat_part.strip().splitlines():
            parts = numline.split("\t")
            if len(parts) >= 2:
                tot_added += int(parts[0]) if parts[0].isdigit() else 0
                tot_deleted += int(parts[1]) if parts[1].isdigit() else 0

        # Ratear as linhas alteradas igualmente entre os participantes do commit
        weight = 1.0 / len(contributors)
        for handle in contributors:
            additions_by_week[week_key][handle] += int(round(tot_added * weight))
            deletions_by_week[week_key][handle] += int(round(tot_deleted * weight))
            total_additions[handle] += int(round(tot_added * weight))
            total_deletions[handle] += int(round(tot_deleted * weight))

    if not all_weeks:
        now_year, now_week, _ = datetime.now().isocalendar()
        all_weeks.add(f"{now_year}-W{now_week:02d}")

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
    """Obtém token de autorização do GitHub."""
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


def fetch_all_github_items():
    """Consulta todas as issues e pull requests da API REST do GitHub."""
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
            print(f"Aviso ao consultar API do GitHub: {e}", file=sys.stderr)
            break

    return all_items


def extract_hours_from_item(item: dict) -> float:
    """Extrai horas do corpo da issue ou do catálogo homologado."""
    num = item.get("number")
    body = item.get("body") or ""

    match = re.search(r"(?:horas?(?:\s*dedicadas?)?|esfor[çc]o)[:\s\*]+(\d+(?:[.,]\d+)?)\s*h?", body, re.IGNORECASE)
    if match:
        try:
            return float(match.group(1).replace(",", "."))
        except ValueError:
            pass

    if num in DEFAULT_HOURS_CATALOG:
        return DEFAULT_HOURS_CATALOG[num]

    return 2.0


def get_issue_and_effort_metrics():
    """Calcula estatísticas de issues/PRs abertas, fechadas e esforço real em horas por membro."""
    items = fetch_all_github_items()

    counts = {
        author: {
            "total": 0,
            "closed": 0,
            "open": 0,
            "hours": 0.0,
        }
        for author in TRACKED_AUTHORS
    }

    # Se não conseguirmos itens da API (offline), inicializa com o catálogo homologado
    if not items:
        for num, h in DEFAULT_HOURS_CATALOG.items():
            assignees = FALLBACK_ASSIGNEES.get(num, [])
            w = 1.0 / len(assignees) if assignees else 1.0
            for handle in assignees:
                if handle in counts:
                    counts[handle]["total"] += 1
                    counts[handle]["closed"] += 1
                    counts[handle]["hours"] += h * w
        return counts

    for item in items:
        closed = item.get("state") == "closed"
        num = item.get("number")

        assignees_raw = [a.get("login") for a in item.get("assignees", []) if a.get("login")]
        if not assignees_raw and num in FALLBACK_ASSIGNEES:
            assignees_raw = FALLBACK_ASSIGNEES[num]

        hours = extract_hours_from_item(item)
        weight = 1.0 / len(assignees_raw) if assignees_raw else 1.0

        for login in assignees_raw:
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
    """Calcula o teto elegante do eixo Y para gráficos Mermaid."""
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


def generate_tabela_contribuicao_matriz(issue_counts: dict) -> str:
    """
    Gera a Tabela 1 canônica de Matriz de Responsabilidades e Esforço para `tabela-contribuicao.md`,
    atualizada diretamente a partir das horas extraídas pela automação.
    """
    tot_hours = sum(issue_counts.get(h, {}).get("hours", 0.0) for h in TRACKED_AUTHORS)
    if tot_hours <= 0:
        tot_hours = 72.0

    lines = [
        "| Integrante (Nome e Matrícula) | Usuário GitHub | Papel Principal na Equipe | Principais Responsabilidades e Tarefas Realizadas no Ponto de Controle 1 | Horas (h) | % Esforço (AG-C5) | Status |",
        "| :--- | :---: | :--- | :--- | :---: | :---: | :---: |",
    ]

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        matricula = m["matricula"]
        papel = m["papel"]
        resp = m["responsabilidades"]

        st = issue_counts.get(handle, {})
        hours = st.get("hours", 0.0)
        pct = (hours / tot_hours * 100.0) if tot_hours > 0 else (100.0 / len(TEAM_MEMBERS))

        lines.append(
            f"| **{name}**<br>Matrícula: `{matricula}` | [@{handle}](https://github.com/{handle}) | "
            f"{papel} | {resp} | **{fmt_br_number(hours, 1)}h** | **{fmt_br_number(pct, 2)}%** | Concluído |"
        )

    lines.append(
        f"| **TOTAL CONSOLIDADO** | — | — | **Esforço Acumulado no Ponto de Controle 1 (Fases 1 e 2)** | "
        f"**{fmt_br_number(tot_hours, 1)}h** | **100,00%** | **Homologado** |"
    )

    return "\n".join(lines)


def generate_alocacao_recursos_custos(issue_counts: dict) -> str:
    """
    Gera a Tabela 3 de Alocação de Recursos, Esforço e Custos Individuais para `metricas-psm.md`,
    calculando horas realizadas, custo total e % de esforço a partir da automação.
    """
    tot_hours = sum(issue_counts.get(h, {}).get("hours", 0.0) for h in TRACKED_AUTHORS)
    if tot_hours <= 0:
        tot_hours = 72.0

    lines = [
        "| Integrante (Nome e Matrícula) | Usuário GitHub | Papel Principal na Avaliação | Horas Realizadas (h) | Valor / Hora (R$) | Custo Total (R$) | % Esforço (AG-C5) | Status |",
        "| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |",
    ]

    tot_custo = tot_hours * VALOR_HORA_BRL

    for m in TEAM_MEMBERS:
        handle = m["handle"]
        name = m["name"]
        matricula = m["matricula"]
        papel = m["papel"]

        st = issue_counts.get(handle, {})
        hours = st.get("hours", 0.0)
        custo = hours * VALOR_HORA_BRL
        pct = (hours / tot_hours * 100.0) if tot_hours > 0 else (100.0 / len(TEAM_MEMBERS))

        lines.append(
            f"| **{name}**<br>Matrícula: `{matricula}` | [@{handle}](https://github.com/{handle}) | {papel} | "
            f"**{fmt_br_number(hours, 1)}h** | R$ 50,00 | {fmt_br_currency(custo)} | **{fmt_br_number(pct, 2)}%** | Concluído |"
        )

    lines.append(
        f"| **TOTAL ACUMULADO (PC1)** | — | **Entregáveis Fases 1 e 2 Consolidados** | "
        f"**{fmt_br_number(tot_hours, 1)}h** | Média: R$ 50,00/h | **{fmt_br_currency(tot_custo)}** | **100,00%** | **100% Ativo** |"
    )

    return "\n".join(lines)


def generate_distribuicao_custos_areas(issue_counts: dict) -> str:
    """Gera o detalhamento dinâmico de custos por área técnica para a Seção 4.1 de `metricas-psm.md`."""
    tot_hours = sum(issue_counts.get(h, {}).get("hours", 0.0) for h in TRACKED_AUTHORS)
    if tot_hours <= 0:
        tot_hours = 72.0

    h_compat = issue_counts.get("ArturFGaldino", {}).get("hours", 0.0) + issue_counts.get("nicolejovita", {}).get("hours", 0.0)
    h_conf = issue_counts.get("DaviUrsulino", {}).get("hours", 0.0) + issue_counts.get("JoaoEduardoP", {}).get("hours", 0.0)
    h_usab = issue_counts.get("Natan8643", {}).get("hours", 0.0) + issue_counts.get("yanrdgs-dev", {}).get("hours", 0.0)

    c_compat = h_compat * VALOR_HORA_BRL
    c_conf = h_conf * VALOR_HORA_BRL
    c_usab = h_usab * VALOR_HORA_BRL
    tot_custo = tot_hours * VALOR_HORA_BRL

    pct_compat = (h_compat / tot_hours * 100.0) if tot_hours > 0 else 33.33
    pct_conf = (h_conf / tot_hours * 100.0) if tot_hours > 0 else 33.33
    pct_usab = (h_usab / tot_hours * 100.0) if tot_hours > 0 else 33.33

    lines = [
        f"* **Compatibilidade e Arquitetura (Artur e Nicole):** {fmt_br_number(h_compat, 1)}h dedicadas | {fmt_br_currency(c_compat)} ({fmt_br_number(pct_compat, 2)}% do orçamento total)",
        f"* **Usabilidade e Interação (Natan e Yan):** {fmt_br_number(h_usab, 1)}h dedicadas | {fmt_br_currency(c_usab)} ({fmt_br_number(pct_usab, 2)}% do orçamento total)",
        f"* **Confiabilidade e Métricas de Processo (Davi e João Eduardo):** {fmt_br_number(h_conf, 1)}h dedicadas | {fmt_br_currency(c_conf)} ({fmt_br_number(pct_conf, 2)}% do orçamento total)",
        f"* **Total Orçamentário Alocado para a Fase de Planejamento:** {fmt_br_currency(tot_custo)}",
    ]
    return "\n".join(lines)


def generate_contributions_table(git_totals: dict, issue_counts: dict) -> str:
    """Gera tabela consolidada de atividade Git e esforço computado (AG-C5)."""
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
        tot_hours = 72.0

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
        custo = hours * VALOR_HORA_BRL
        pct_esforco = (hours / tot_hours * 100.0) if tot_hours > 0 else (100.0 / len(TEAM_MEMBERS))

        tot_commits += c
        tot_adds += a
        tot_dels += d
        tot_closed += closed_iss

        sign_net = f"+{net}" if net > 0 else str(net)
        lines.append(
            f"| **{name}**<br>Matrícula: `{matricula}` | [@{handle}](https://github.com/{handle}) | {dupla} | "
            f"{c} | +{a} / -{d} ({sign_net}) | {closed_iss} | {fmt_br_number(hours, 1)}h | {fmt_br_currency(custo)} | **{fmt_br_number(pct_esforco, 2)}%** |"
        )

    tot_net = tot_adds - tot_dels
    tot_sign_net = f"+{tot_net}" if tot_net > 0 else str(tot_net)
    tot_custo = tot_hours * VALOR_HORA_BRL

    lines.append(
        f"| **TOTAL CONSOLIDADO** | — | — | **{tot_commits}** | **+{tot_adds} / -{tot_dels} ({tot_sign_net})** | "
        f"**{tot_closed}** | **{fmt_br_number(tot_hours, 1)}h** | **{fmt_br_currency(tot_custo)}** | **100,00%** |"
    )

    return "\n".join(lines)


def generate_issues_table(issue_counts: dict) -> str:
    """Gera tabela Markdown com taxa de conclusão de demandas por membro."""
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

    # 1. Gráficos Mermaid
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

    # 2. Tabelas e Trechos Markdown Dinâmicos
    tabela_contribuicao_matriz = generate_tabela_contribuicao_matriz(issue_counts)
    alocacao_recursos_custos = generate_alocacao_recursos_custos(issue_counts)
    distribuicao_custos_areas = generate_distribuicao_custos_areas(issue_counts)
    contributions_table = generate_contributions_table(git_totals, issue_counts)
    issues_table = generate_issues_table(issue_counts)

    tot_hours = sum(issue_counts.get(h, {}).get("hours", 0.0) for h in TRACKED_AUTHORS)
    tot_closed = sum(issue_counts.get(h, {}).get("closed", 0) for h in TRACKED_AUTHORS)
    tot_all = sum(issue_counts.get(h, {}).get("total", 0) for h in TRACKED_AUTHORS)
    media_horas = tot_hours / len(TRACKED_AUTHORS) if TRACKED_AUTHORS else 0.0
    taxa_conc = (tot_closed / tot_all * 100.0) if tot_all > 0 else 100.0

    resumo_processo = (
        f"* **Total de Tarefas no Repositório (Issues/PRs):** {tot_all} itens mapeados\n"
        f"* **Tarefas Concluídas e Homologadas:** {tot_closed} tarefas\n"
        f"* **Taxa de Conclusão de Demandas:** **{fmt_br_number(taxa_conc, 1)}% de eficácia de processo**\n"
        f"* **Média de Esforço por Integrante:** {fmt_br_number(media_horas, 1)} horas dedicadas\n"
        f"* **Esforço Total Consolidado da Equipe:** {fmt_br_number(tot_hours, 1)} horas profissionais"
    )

    # 3. Escrita dos arquivos na pasta snippets/
    (SNIPPETS_DIR / "commit-velocity.mmd").write_text(velocity_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-additions.mmd").write_text(additions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "code-deletions.mmd").write_text(deletions_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "assigned-issues.mmd").write_text(issues_chart + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "resolved-issues.mmd").write_text(resolved_chart + "\n", encoding="utf-8")

    (SNIPPETS_DIR / "resumo-processo.md").write_text(resumo_processo + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "tabela-contribuicao-matriz.md").write_text(tabela_contribuicao_matriz + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "alocacao-recursos-custos.md").write_text(alocacao_recursos_custos + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "distribuicao-custos-areas.md").write_text(distribuicao_custos_areas + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "contributions-summary.md").write_text(contributions_table + "\n", encoding="utf-8")
    (SNIPPETS_DIR / "issues-summary.md").write_text(issues_table + "\n", encoding="utf-8")

    resumo_horas = {k: f"{v['hours']:.1f}h" for k, v in issue_counts.items()}
    print(f"Snippets gerados com sucesso em: {SNIPPETS_DIR}")
    print(f"Horas computadas por membro: {resumo_horas}")


if __name__ == "__main__":
    main()
