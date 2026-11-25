#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar.py

Valida o protótipo do Requerimento Geral e exporta as telas.

O que faz:
  1. Abre requerimento-geral.html?teste=1 (modo protótipo, em 360 px e em 1280 px)
     e ?teste=1&modo=atual (linha de base, que reproduz o comportamento observado
     no portal) em um Chrome sem interface e lê o resultado de
     requerimento-geral-testes.js. Inclui a medição da sobreposição do avatar do
     assistente sobre botões e campos.
  2. Grava os resultados em docs/dados/capacidade_interacao/melhoria/validacao_prototipo.csv.
  3. Exporta as telas (5 estados, em 360 px e em 1280 px, mais a linha de base)
     para docs/img/prototipo/.

Os testes medem o comportamento do protótipo. Não medem o portal em produção.

Requisitos: Google Chrome ou Chromium instalado e Pillow (para recortar as capturas).

Execução, na raiz do repositório:
  python3 docs/assets/melhorias/compatibilidade/layout_responsivo/validar_requerimento_geral.py
"""

import csv
import functools
import html
import json
import os
import re
import shutil
import subprocess
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image, ImageChops

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[4]
PAGINA = (BASE / "requerimento-geral.html").as_uri()
CSV_SAIDA = REPO / "docs" / "dados" / "capacidade_interacao" / "melhoria" / "validacao_prototipo.csv"
IMG_SAIDA = REPO / "docs" / "img" / "prototipo"

ESTADOS = ["vazio", "padrao", "erro", "revisao", "confirmacao"]
VIEWPORTS = {"mobile-360": (360, 2000), "desktop-1280": (1280, 1600)}
FUNDO = (255, 255, 255)  # fundo branco das telas do portal


def achar_chrome():
    for nome in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    sys.exit("Chrome ou Chromium não encontrado no PATH.")


CHROME = achar_chrome()
BASE_CMD = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars"]


class _Silencioso(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def iniciar_servidor():
    """Serve a pasta do protótipo em uma porta livre, para o harness e o iframe terem a mesma origem."""
    handler = functools.partial(_Silencioso, directory=str(BASE))
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    return servidor


def rodar_testes(servidor, modo, largura):
    """Roda os testes dentro de um iframe com a largura pedida (o Chrome sem interface não vai abaixo de 500 px)."""
    porta = servidor.server_address[1]
    url = f"http://127.0.0.1:{porta}/requerimento-geral-harness.html?w={largura}" + ("&modo=atual" if modo == "atual" else "")
    saida = subprocess.run(
        BASE_CMD + [f"--window-size={max(largura, 500)},900", "--virtual-time-budget=15000", "--dump-dom", url],
        capture_output=True, text=True, timeout=90, check=True,
    ).stdout
    achado = re.search(r'<pre id="resultado-testes">(.*?)</pre>', saida, re.S)
    if not achado:
        sys.exit(f"Não encontrei o resultado dos testes no modo {modo}.")
    return json.loads(html.unescape(achado.group(1)))


def altura_do_conteudo(caminho):
    """Altura do conteúdo na captura, sem contar o avatar do assistente (fixo no canto inferior direito)."""
    img = Image.open(caminho).convert("RGB")
    ignorar = Image.new("RGB", (130, 260), FUNDO)
    img.paste(ignorar, (img.width - 130, img.height - 260))
    caixa = ImageChops.difference(img, Image.new("RGB", img.size, FUNDO)).getbbox()
    return (caixa[3] if caixa else img.height) + 24


def exportar_telas():
    IMG_SAIDA.mkdir(parents=True, exist_ok=True)
    gerados = []
    for nome_vp, (largura, altura) in VIEWPORTS.items():
        alvos = [(f"{e}", f"?estado={e}") for e in ESTADOS]
        alvos.append(("linha-de-base-padrao", "?modo=atual&estado=padrao"))
        alvos.append(("linha-de-base-assinatura", "?modo=atual&estado=confirmacao"))
        for nome, consulta in alvos:
            destino = IMG_SAIDA / f"requerimento-{nome}-{nome_vp}.png"
            # 1ª passada, em janela alta, para medir o conteúdo; 2ª, na altura exata, para o avatar
            # (fixo no canto inferior) aparecer encostado no fim da tela, como em um aparelho.
            for alt in (altura, None):
                if alt is None:
                    alt = max(altura_do_conteudo(destino), 600)
                subprocess.run(
                    BASE_CMD + [f"--window-size={largura},{alt}", "--virtual-time-budget=4000", f"--screenshot={destino}", PAGINA + consulta],
                    capture_output=True, timeout=90, check=True,
                )
            gerados.append(destino.relative_to(REPO).as_posix())
    return gerados


def main():
    linhas = []
    servidor = iniciar_servidor()
    for modo, largura in (("prototipo", 360), ("prototipo", 414), ("prototipo", 500), ("prototipo", 768), ("prototipo", 1366), ("atual", 360)):
        for r in rodar_testes(servidor, modo, largura):
            r["largura"] = largura
            linhas.append(r)

    CSV_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_SAIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_teste", "modo", "largura_px", "descricao", "esperado", "obtido", "resultado"])
        for r in linhas:
            w.writerow([r["id"], r["modo"], r["largura"], r["descricao"], r["esperado"], r["obtido"],
                        "passou" if r["passou"] else "falhou"])

    total = len(linhas)
    ok = sum(1 for r in linhas if r["passou"])
    print(f"Testes: {ok} de {total} passaram. CSV: {CSV_SAIDA.relative_to(REPO)}")
    for r in linhas:
        if not r["passou"]:
            print("  FALHOU:", r["id"], r["modo"], r["largura"], r["descricao"], "| esperado", r["esperado"], "| obtido", r["obtido"])

    servidor.shutdown()
    imagens = exportar_telas()
    print(f"Capturas: {len(imagens)} arquivos em {IMG_SAIDA.relative_to(REPO)}")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
