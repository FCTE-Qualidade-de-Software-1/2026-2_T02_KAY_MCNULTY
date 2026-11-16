#!/usr/bin/env python3
"""Monitoramento de disponibilidade para a metrica M1 (TDO) de Confiabilidade.

Uso:
  python monitor_m1.py coletar --config m1_alvos.json --saida dados/m1/disponibilidade.csv
  python monitor_m1.py resumo  --saida dados/m1/disponibilidade.csv [--ate "2026-11-20 18:00"]

Cada execucao de "coletar" faz UMA verificacao por alvo e acrescenta linhas ao CSV.
Uma verificacao e considerada bem-sucedida (ok) quando o HTTP final e 2xx/3xx
e o texto esperado aparece no conteudo retornado. Nao ha nova tentativa: uma
falha e registrada como falha, para nao mascarar instabilidade.

O alvo de controle (C01) nao entra no TDO. No "resumo", todo ciclo em que o
controle falhou e descartado como falha local do monitor.

Somente biblioteca padrao (Python 3.9+).
"""
import argparse
import csv
import gzip
import json
import socket
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

USER_AGENT = (
    "Mozilla/5.0 (compatible; UnB-FGA0315-Monitoramento-Academico; "
    "verificacao leve a cada 15 min, sem carga)"
)
CAMPOS = [
    "timestamp_utc", "timestamp_brasilia", "alvo_id", "modulo", "url",
    "http_status", "tempo_ms", "elemento_ok", "ok", "erro",
]
FUSO = ZoneInfo("America/Sao_Paulo")
LIMITE_CORPO = 2_000_000  # bytes lidos por resposta
PAUSA_ENTRE_ALVOS_S = 2


def carregar_alvos(caminho):
    dados = json.loads(Path(caminho).read_text(encoding="utf-8"))
    alvos = dados["alvos"]
    pendentes = [a["id"] for a in alvos if "PREENCHER" in (a["url"] + a["esperado"])]
    if pendentes:
        sys.exit(f"Config incompleta: preencha url/esperado dos alvos {pendentes}")
    return alvos, int(dados.get("timeout_s", 20))


def verificar(alvo, timeout_s):
    inicio = time.monotonic()
    status, erro, elemento_ok = "", "", False
    try:
        req = urllib.request.Request(
            alvo["url"],
            headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/json,*/*"},
        )
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            status = resp.status
            bruto = resp.read(LIMITE_CORPO)
            if bruto[:2] == b"\x1f\x8b":  # resposta em gzip (ex.: arquivos .gz.js no S3)
                try:
                    bruto = gzip.decompress(bruto)
                except OSError:
                    pass
            corpo = bruto.decode("utf-8", errors="replace")
            elemento_ok = alvo["esperado"].lower() in corpo.lower()
    except urllib.error.HTTPError as e:  # precisa vir antes de URLError
        status, erro = e.code, f"HTTPError {e.code}"
    except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as e:
        erro = f"{type(e).__name__}: {getattr(e, 'reason', e)}"
    except Exception as e:  # qualquer outra falha tambem e dado
        erro = f"{type(e).__name__}: {e}"
    tempo_ms = round((time.monotonic() - inicio) * 1000)
    status_ok = isinstance(status, int) and 200 <= status < 400
    ok = status_ok and elemento_ok
    if status_ok and not elemento_ok and not erro:
        erro = "elemento esperado ausente"
    return status, tempo_ms, elemento_ok, ok, erro


def coletar(config, saida):
    alvos, timeout_s = carregar_alvos(config)
    agora = datetime.now(timezone.utc)
    ts_utc = agora.strftime("%Y-%m-%dT%H:%M:%SZ")
    ts_br = agora.astimezone(FUSO).strftime("%Y-%m-%d %H:%M:%S")

    caminho = Path(saida)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    novo = not caminho.exists()
    with caminho.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if novo:
            w.writeheader()
        for i, alvo in enumerate(alvos):
            if i:
                time.sleep(PAUSA_ENTRE_ALVOS_S)
            status, ms, el, ok, erro = verificar(alvo, timeout_s)
            w.writerow({
                "timestamp_utc": ts_utc, "timestamp_brasilia": ts_br,
                "alvo_id": alvo["id"], "modulo": alvo["modulo"], "url": alvo["url"],
                "http_status": status, "tempo_ms": ms,
                "elemento_ok": int(el), "ok": int(ok), "erro": erro,
            })
            print(f"{alvo['id']:>5} ok={int(ok)} http={status} {ms} ms {erro}")


def _parse_br(texto):
    for formato in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(texto, formato)
        except ValueError:
            pass
    sys.exit(f"Data invalida: {texto!r} (use AAAA-MM-DD HH:MM, horario de Brasilia)")


def resumo(saida, ate=None, controle="C01"):
    limite = _parse_br(ate) if ate else None
    ciclos = defaultdict(list)
    with open(saida, newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            if limite and _parse_br(linha["timestamp_brasilia"]) > limite:
                continue
            ciclos[linha["timestamp_utc"]].append(linha)
    if not ciclos:
        sys.exit("CSV sem dados no periodo.")

    cok, ctot = defaultdict(int), defaultdict(int)
    descartados = 0
    for linhas in ciclos.values():
        ctl = [x for x in linhas if x["alvo_id"] == controle]
        if ctl and int(ctl[0]["ok"]) == 0:
            descartados += 1  # falha local do monitor, fora de C_tot
            continue
        for x in linhas:
            if x["alvo_id"] == controle:
                continue
            ctot[x["alvo_id"]] += 1
            cok[x["alvo_id"]] += int(x["ok"])
    if not ctot:
        sys.exit("Nenhum ciclo valido.")

    print(f"{'alvo':<8}{'C_ok':>8}{'C_tot':>8}{'TDO (%)':>10}")
    for alvo in sorted(ctot):
        print(f"{alvo:<8}{cok[alvo]:>8}{ctot[alvo]:>8}{100 * cok[alvo] / ctot[alvo]:>10.2f}")
    total_ok, total = sum(cok.values()), sum(ctot.values())
    print(f"{'GERAL':<8}{total_ok:>8}{total:>8}{100 * total_ok / total:>10.2f}")
    print(f"\nCiclos no periodo: {len(ciclos)}; descartados por falha local ({controle}): {descartados}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("coletar")
    c.add_argument("--config", required=True)
    c.add_argument("--saida", required=True)
    r = sub.add_parser("resumo")
    r.add_argument("--saida", required=True)
    r.add_argument("--ate", help='corte em horario de Brasilia, ex.: "2026-11-20 18:00"')
    args = p.parse_args()
    if args.cmd == "coletar":
        coletar(args.config, args.saida)
    else:
        resumo(args.saida, args.ate)


if __name__ == "__main__":
    main()