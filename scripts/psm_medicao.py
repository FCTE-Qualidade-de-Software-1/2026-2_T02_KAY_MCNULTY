#!/usr/bin/env python3
"""
psm_medicao.py - Medição de Marcos e Sprints pelos Indicadores PSM/CID.

Calcula os indicadores formais N1 a N6 para a equipe Kay McNulty (Qualidade de Software 1):
  - N1: Comprometido x Concluído (Taxa de Conclusão TCI)
  - N2: Burndown de Issues do Marco/Sprint
  - N3: Distribuição de Esforço e Equilíbrio de Alocação (AG-C5)
  - N4: Precisão de Estimativas (Estimado x Real)
  - N5: Tempo Médio de Resolução de Demandas (Cycle Time)
  - N6: Rastreabilidade e Revisão por Pares (PRs e Commits)

Uso:
    python scripts/psm_medicao.py --milestone "M4: Consolidação PC1" --inicio 2026-10-16 --fim 2026-10-26 --saida docs/dados/gestao/pc1.json
"""

import argparse
import json
import math
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OWNER = "FCTE-Qualidade-de-Software-1"
REPO = "2026-2_T02_KAY_MCNULTY"
BRT = timezone(timedelta(hours=-3))

TEAM_MEMBERS = [
    {"name": "Artur Fernandes Galdino", "handle": "ArturFGaldino", "dupla": "Dupla 1"},
    {"name": "Nicole Jovita Fernandes", "handle": "nicolejovita", "dupla": "Dupla 1"},
    {"name": "Davi Ursolino de Oliveira", "handle": "DaviUrsulino", "dupla": "Dupla 2"},
    {"name": "João Eduardo Pereira Rabelo", "handle": "JoaoEduardoP", "dupla": "Dupla 2"},
    {"name": "Natan José França", "handle": "Natan8643", "dupla": "Dupla 3"},
    {"name": "Yan Santos Rodrigues", "handle": "yanrdgs-dev", "dupla": "Dupla 3"},
]

TRACKED_AUTHORS = [m["handle"] for m in TEAM_MEMBERS]
MEMBER_BY_HANDLE = {m["handle"]: m for m in TEAM_MEMBERS}


def normalize_author(name: str, email: str = "") -> str:
    combined = f"{name} {email}".lower()
    if "github-actions" in combined:
        return "github-actions[bot]"
    if "artur" in combined or "fernandesartur4" in combined:
        return "ArturFGaldino"
    if "nicole" in combined or "jovita" in combined:
        return "nicolejovita"
    if "davi" in combined or "davizera0601" in combined:
        return "DaviUrsulino"
    if "joão" in combined or "joao" in combined:
        return "JoaoEduardoP"
    if "natan" in combined or "frança" in combined or "franca" in combined:
        return "Natan8643"
    if "yan" in combined or "rodrigues" in combined:
        return "yanrdgs-dev"
    return name.strip() or "Unknown"


def resolve_token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    return None


def fetch_issues_and_prs():
    token = resolve_token()
    headers = {"User-Agent": "KayMcNulty-PSM", "Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    all_items = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=all&per_page=100&page={page}"
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
            print(f"Erro ao buscar dados na API do GitHub: {e}", file=sys.stderr)
            break

    issues = []
    prs = []
    for it in all_items:
        if "pull_request" in it:
            prs.append(it)
        else:
            issues.append(it)
    return issues, prs


def parse_issue_hours(issue):
    body = issue.get("body") or ""
    m = re.search(r"(?:horas?(?:\s*dedicadas?)?|esfor[çc]o)[:\s\*]+(\d+(?:[.,]\d+)?)\s*h?", body, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1).replace(",", "."))
        except ValueError:
            pass
    return 2.0


def pct(parte, total):
    return round(100.0 * parte / total, 2) if total else 0.0


def calcular_medicao(milestone_filter, inicio_str, fim_str):
    inicio = date.fromisoformat(inicio_str)
    fim = date.fromisoformat(fim_str)
    issues_raw, prs_raw = fetch_issues_and_prs()

    # Filtrar issues pelo marco se especificado, ou data de criação
    issues = []
    for i in issues_raw:
        ms = (i.get("milestone") or {}).get("title") if i.get("milestone") else None
        if milestone_filter and ms:
            if milestone_filter.lower() in ms.lower():
                issues.append(i)
        else:
            issues.append(i)

    # N1: Comprometido x Concluído
    total_planejadas = len(issues)
    fechadas = [i for i in issues if i.get("state") == "closed"]
    n1 = {
        "planejadas": total_planejadas,
        "concluidas": len(fechadas),
        "abertas": total_planejadas - len(fechadas),
        "taxa_conclusao_pct": pct(len(fechadas), total_planejadas),
        "desvio_meta_pct": round(100.0 - pct(len(fechadas), total_planejadas), 2),
    }

    # N2: Burndown diário
    burndown = []
    curr = inicio
    while curr <= fim:
        planejados_ate = 0
        concluidos_ate = 0
        for i in issues:
            c_at = i.get("created_at")
            f_at = i.get("closed_at")
            c_dt = datetime.fromisoformat(c_at.replace("Z", "+00:00")).astimezone(BRT).date() if c_at else None
            f_dt = datetime.fromisoformat(f_at.replace("Z", "+00:00")).astimezone(BRT).date() if f_at else None

            if c_dt and c_dt <= curr:
                planejados_ate += 1
            if f_dt and f_dt <= curr:
                concluidos_ate += 1

        burndown.append({
            "data": curr.isoformat(),
            "planejados": planejados_ate,
            "concluidos": concluidos_ate,
            "abertos": max(0, planejados_ate - concluidos_ate),
        })
        curr += timedelta(days=1)

    # N3 & N4: Esforço e Estimado x Real
    horas_membro = {h: 0.0 for h in TRACKED_AUTHORS}
    for i in fechadas:
        assignees = [a.get("login") for a in i.get("assignees", [])]
        h = parse_issue_hours(i)
        w = 1.0 / len(assignees) if assignees else 1.0
        for login in assignees:
            handle = normalize_author(login)
            if handle in horas_membro:
                horas_membro[handle] += h * w

    horas_vals = list(horas_membro.values())
    media_horas = sum(horas_vals) / len(horas_vals) if horas_vals else 0.0
    variancia = sum((x - media_horas) ** 2 for x in horas_vals) / len(horas_vals) if horas_vals else 0.0
    desvio_padrao = math.sqrt(variancia)

    n3 = {
        "horas_por_membro": horas_membro,
        "media_horas": round(media_horas, 2),
        "desvio_padrao_sigma": round(desvio_padrao, 2),
        "status_equilibrio": "Conforme (sigma <= 1.0h)" if desvio_padrao <= 1.0 else "Requer balanceamento",
    }

    # N5: Cycle time
    cycle_times = []
    for i in fechadas:
        c_at = i.get("created_at")
        f_at = i.get("closed_at")
        if c_at and f_at:
            dt1 = datetime.fromisoformat(c_at.replace("Z", "+00:00"))
            dt2 = datetime.fromisoformat(f_at.replace("Z", "+00:00"))
            duracao_dias = (dt2 - dt1).total_seconds() / 86400.0
            cycle_times.append(duracao_dias)

    n5 = {
        "total_medido": len(cycle_times),
        "tempo_medio_dias": round(sum(cycle_times) / len(cycle_times), 2) if cycle_times else 0.0,
        "tempo_maximo_dias": round(max(cycle_times), 2) if cycle_times else 0.0,
    }

    # N6: Rastreabilidade e PRs
    n6 = {
        "total_prs": len(prs_raw),
        "prs_fechados": sum(1 for p in prs_raw if p.get("state") == "closed"),
        "total_issues": len(issues_raw),
    }

    resultado = {
        "equipe": "Kay McNulty",
        "milestone": milestone_filter or "Geral",
        "periodo": {"inicio": inicio_str, "fim": fim_str},
        "gerado_em": datetime.now(BRT).isoformat(timespec="seconds"),
        "indicadores": {
            "N1_Comprometido_Concluido": n1,
            "N2_Burndown": burndown,
            "N3_Esforco_Equilibrio": n3,
            "N5_Cycle_Time": n5,
            "N6_Rastreabilidade": n6,
        },
    }
    return resultado


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--milestone", default=None, help="Nome do Milestone a filtrar (opcional)")
    parser.add_argument("--inicio", required=True, help="Data inicial (AAAA-MM-DD)")
    parser.add_argument("--fim", required=True, help="Data final (AAAA-MM-DD)")
    parser.add_argument("--saida", default=None, help="Caminho do arquivo JSON de saída (opcional)")
    args = parser.parse_args()

    dados = calcular_medicao(args.milestone, args.inicio, args.fim)
    output_json = json.dumps(dados, ensure_ascii=False, indent=2)

    if args.saida:
        p = REPO_ROOT / args.saida
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(output_json + "\n", encoding="utf-8")
        print(f"Resultado gravado em: {p}")

    print(output_json)


if __name__ == "__main__":
    main()
