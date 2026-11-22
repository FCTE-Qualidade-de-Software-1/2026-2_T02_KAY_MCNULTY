#!/usr/bin/env python3
"""Valida o protótipo de rascunho de formulário nos cenários de interrupção da M5.

Cada cenário é repetido com o rascunho desativado (comportamento atual do portal,
?rascunho=off) e ativado. O resultado de cada repetição vai para o CSV.

Uso:
  pip install playwright && playwright install chromium
  python validar.py
  python validar.py --repeticoes 10 --saida validacao.csv

Para usar um Chrome já instalado, defina CHROME_PATH com o caminho do executável.
"""
import argparse
import csv
import http.server
import os
import socketserver
import threading
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

PASTA = Path(__file__).resolve().parent
EVIDENCIAS = PASTA / "evidencias"
CAMPOS = ["cenario", "modo", "repeticao", "recuperado", "tempo_restauracao_ms"]
LIMITE_ESPERA_MS = 3000

TEXTO_OBJETO = "Teste de avaliação acadêmica"
AGENDAMENTO = {
    "categoria": "Habilitação",
    "unidade": "Brazlândia",
    "data": "04/12/2026",
    "hora": "08:20",
}

JS_VALORES = """() => {
  const saida = {};
  document.querySelectorAll('form [name]').forEach(c => {
    saida[c.name] = c.type === 'checkbox' ? c.checked : c.value;
  });
  return saida;
}"""


class Servidor(socketserver.TCPServer):
    allow_reuse_address = True


def iniciar_servidor():
    class Manipulador(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(PASTA), **kwargs)

        def log_message(self, *args):
            pass

    servidor = Servidor(("127.0.0.1", 0), Manipulador)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    return servidor


def preencher_agendamento(page):
    page.select_option("#categoria", AGENDAMENTO["categoria"])
    page.check("input[name=declaro]")
    page.check("input[name=ciente]")
    page.select_option("#unidade", AGENDAMENTO["unidade"])
    page.select_option("#data", AGENDAMENTO["data"])
    page.select_option("#hora", AGENDAMENTO["hora"])


def preencher_requerimento(page):
    page.fill("#objeto", TEXTO_OBJETO)


def esperar_gravacao(page):
    """Dá tempo ao rascunho de gravar, como um cidadão que lê a tela antes de recarregar."""
    page.wait_for_timeout(400)


def esperar_restauracao(page, esperado):
    """Mede quanto tempo leva para os campos voltarem aos valores preenchidos."""
    inicio = time.perf_counter()
    while (time.perf_counter() - inicio) * 1000 < LIMITE_ESPERA_MS:
        valores = page.evaluate(JS_VALORES)
        if all(valores.get(nome) == valor for nome, valor in esperado.items()):
            return True, round((time.perf_counter() - inicio) * 1000)
        page.wait_for_timeout(20)
    return False, ""


def cenario_b4(page, base):
    """Recarga com o agendamento preenchido."""
    page.goto(base + "#/agendamento")
    preencher_agendamento(page)
    esperado = page.evaluate(JS_VALORES)
    esperar_gravacao(page)
    page.reload(wait_until="load")
    return esperado


def cenario_b5(page, base):
    """Recarga com o Requerimento Geral preenchido, antes de Avançar."""
    page.goto(base + "#/requerimento")
    preencher_requerimento(page)
    esperado = page.evaluate(JS_VALORES)
    esperar_gravacao(page)
    page.reload(wait_until="load")
    return esperado


def cenario_a6(page, base):
    """Botão voltar e avançar do navegador com o agendamento preenchido."""
    page.goto(base + "#/inicio")
    page.click("nav a[href='#/agendamento']")
    page.wait_for_selector("#form-agendamento")
    preencher_agendamento(page)
    esperado = page.evaluate(JS_VALORES)
    esperar_gravacao(page)
    page.go_back()
    page.wait_for_selector("text=Início")
    page.go_forward()
    page.wait_for_selector("#form-agendamento")
    return esperado


def cenario_b3(page, base):
    """Sessão limpa (limpar os dados do site) com o agendamento preenchido."""
    page.goto(base + "#/agendamento")
    preencher_agendamento(page)
    esperado = page.evaluate(JS_VALORES)
    esperar_gravacao(page)
    page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); }")
    page.context.clear_cookies()
    page.reload(wait_until="load")
    return esperado


CENARIOS = {"B3": cenario_b3, "B4": cenario_b4, "B5": cenario_b5, "A6": cenario_a6}


def main():
    analisador = argparse.ArgumentParser()
    analisador.add_argument("--repeticoes", type=int, default=5)
    analisador.add_argument("--saida", default=str(PASTA / "validacao.csv"))
    argumentos = analisador.parse_args()

    EVIDENCIAS.mkdir(exist_ok=True)
    servidor = iniciar_servidor()
    porta = servidor.server_address[1]
    linhas = []

    with sync_playwright() as p:
        caminho = os.environ.get("CHROME_PATH")
        navegador = p.chromium.launch(executable_path=caminho) if caminho else p.chromium.launch()
        for modo, parametro in (("sem_rascunho", "?rascunho=off"), ("com_rascunho", "")):
            base = f"http://127.0.0.1:{porta}/index.html{parametro}"
            for nome, funcao in CENARIOS.items():
                for repeticao in range(1, argumentos.repeticoes + 1):
                    contexto = navegador.new_context(viewport={"width": 1280, "height": 800})
                    page = contexto.new_page()
                    esperado = funcao(page, base)
                    recuperado, tempo = esperar_restauracao(page, esperado)
                    if repeticao == 1:
                        page.screenshot(path=str(EVIDENCIAS / f"{nome}_{modo}.png"))
                    contexto.close()
                    linhas.append({
                        "cenario": nome, "modo": modo, "repeticao": repeticao,
                        "recuperado": "sim" if recuperado else "nao",
                        "tempo_restauracao_ms": tempo,
                    })
        navegador.close()
    servidor.shutdown()

    with open(argumentos.saida, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(linhas)

    print(f"{'cenario':8}{'modo':14}{'recuperado':12}{'tempo medio (ms)':>18}")
    for modo in ("sem_rascunho", "com_rascunho"):
        for nome in CENARIOS:
            grupo = [l for l in linhas if l["cenario"] == nome and l["modo"] == modo]
            ok = sum(1 for l in grupo if l["recuperado"] == "sim")
            tempos = [l["tempo_restauracao_ms"] for l in grupo if l["tempo_restauracao_ms"] != ""]
            medio = round(sum(tempos) / len(tempos)) if tempos else "-"
            print(f"{nome:8}{modo:14}{ok}/{len(grupo):<10}{medio:>18}")


if __name__ == "__main__":
    main()
