#!/usr/bin/env python3
"""Coleta do A03 (widget do chatbot montado na pagina) com Playwright.

Uso:
  python monitor_playwright.py --saida teste.csv
  python monitor_playwright.py --saida dados/disponibilidade.csv --intervalo-min 15 --ate "2026-11-20 18:00"
"""
import argparse
import csv
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from playwright.sync_api import sync_playwright

CAMPOS = [
    "timestamp_utc", "timestamp_brasilia", "alvo_id", "modulo", "url",
    "http_status", "tempo_ms", "elemento_ok", "ok", "erro",
]
FUSO = ZoneInfo("America/Sao_Paulo")
TIMEOUT_MS = 20000
JS_A03 = (
    "() => { const e = document.querySelector('#divtoincludechat');"
    " return !!e && e.innerHTML.trim().length > 0; }"
)

ALVOS = [
    {"id": "A03", "modulo": "Chatbot (widget montado na pagina)",
     "url": "https://portal.detran.df.gov.br/", "tipo": "seletor"},
    {"id": "C01", "modulo": "Controle (fora do portal)",
     "url": "https://example.com/", "tipo": "texto", "esperado": "Example Domain"},
]


def verificar(browser, alvo):
    contexto = browser.new_context()  # perfil limpo a cada verificacao
    page = contexto.new_page()
    inicio = time.monotonic()
    status, erro, elemento_ok = "", "", False
    try:
        resp = page.goto(alvo["url"], timeout=TIMEOUT_MS, wait_until="domcontentloaded")
        status = resp.status if resp else ""
        if alvo["tipo"] == "seletor":
            page.wait_for_function(JS_A03, timeout=TIMEOUT_MS)
            elemento_ok = True
        else:
            elemento_ok = alvo["esperado"].lower() in page.content().lower()
    except Exception as e:
        erro = f"{type(e).__name__}: {str(e).splitlines()[0]}"
    finally:
        contexto.close()
    tempo_ms = round((time.monotonic() - inicio) * 1000)
    status_ok = isinstance(status, int) and 200 <= status < 400
    ok = status_ok and elemento_ok
    if status_ok and not elemento_ok and not erro:
        erro = "elemento esperado ausente"
    return status, tempo_ms, elemento_ok, ok, erro


def ciclo(browser, saida):
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
        for i, alvo in enumerate(ALVOS):
            if i:
                time.sleep(2)
            status, ms, el, ok, erro = verificar(browser, alvo)
            w.writerow({
                "timestamp_utc": ts_utc, "timestamp_brasilia": ts_br,
                "alvo_id": alvo["id"], "modulo": alvo["modulo"], "url": alvo["url"],
                "http_status": status, "tempo_ms": ms,
                "elemento_ok": int(el), "ok": int(ok), "erro": erro,
            })
            print(f"{alvo['id']:>5} ok={int(ok)} http={status} {ms} ms {erro}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--saida", required=True)
    p.add_argument("--intervalo-min", type=float, default=0,
                   help="0 = uma verificacao e sai; >0 = repete ate --ate")
    p.add_argument("--ate", help='corte em horario de Brasilia, ex.: "2026-11-20 18:00"')
    args = p.parse_args()
    limite = None
    if args.ate:
        limite = datetime.strptime(args.ate, "%Y-%m-%d %H:%M").replace(tzinfo=FUSO)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        while True:
            ciclo(browser, args.saida)
            if not args.intervalo_min:
                break
            if limite and datetime.now(FUSO) >= limite:
                break
            time.sleep(args.intervalo_min * 60)
        browser.close()


if __name__ == "__main__":
    main()