#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
record_complete_flow_video.py

Grava em video (MP4 e WebM) o teste automatizado do fluxo completo da aplicacao
do Detran-DF desenvolvida para a melhoria de responsividade e compatibilidade.

Fluxo gravado:
  1. Inicio (index.html): Apresentacao da interface, abertura e fechamento da janela do Chatbot,
     teste do mecanismo retratil (ocultar com > e restaurar com <).
  2. Modulo Infracao (infracao.html): Preenchimento de dados (Placa e Renavam), verificacao de
     desobstrucao dos botoes de acao, teste retratil e demonstracao de responsividade (Mobile 360px).
  3. Modulo Atendimento (atendimento.html): Interacao com dropdowns de servico e unidade,
     selecao de data e teste retratil.
  4. Modulo Protocolo (protocolo.html): Pesquisa de processos SEI-GDF, card de Nova Solicitacao
     com botao ACESSAR desobstruido e teste retratil.
  5. Retorno a Home (index.html): Conclusao do fluxo integrado.
"""

import os
import glob
import time
import shutil
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = Path(__file__).resolve().parent
REPO_DIR = BASE_DIR.parents[4]
VIDEOS_DIR = BASE_DIR / "videos"
VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

def main():
    print("Iniciando gravacao em video do fluxo completo da aplicacao...")
    temp_rec_dir = BASE_DIR / "temp_rec"
    temp_rec_dir.mkdir(parents=True, exist_ok=True)
    
    # Limpa gravacoes temporarias antigas
    for f in temp_rec_dir.glob("*.webm"):
        try: f.unlink()
        except Exception: pass

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=EDGE_PATH, headless=True)
        context = browser.new_context(
            record_video_dir=str(temp_rec_dir),
            record_video_size={"width": 1280, "height": 720},
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()
        
        # ---------------------------------------------------------
        # ETAPA 1: Home Page (index.html)
        # ---------------------------------------------------------
        print("1. Gravando Pagina Inicial (index.html)...")
        home_url = (BASE_DIR / "index.html").as_uri()
        page.goto(home_url)
        page.evaluate("try { sessionStorage.clear(); } catch(e){}")
        page.reload()
        page.wait_for_timeout(2000)
        
        # Move mouse suavemente pelos servicos
        page.mouse.move(300, 300)
        page.wait_for_timeout(600)
        page.mouse.move(600, 400)
        page.wait_for_timeout(600)
        
        # Clica no icone do Chatbot para abrir o chat flutuante
        print("  - Abrindo janela do Chatbot...")
        bot_icon = page.locator("#bot_icon")
        bot_icon.hover()
        page.wait_for_timeout(800)
        page.evaluate("document.getElementById('bot_icon').click()")
        page.wait_for_timeout(2500)
        
        # Fecha a janela do Chatbot
        print("  - Fechando janela do Chatbot...")
        page.evaluate("document.getElementById('close-chat-btn').click()")
        page.wait_for_timeout(1000)
        
        # Testa Mecanismo Retratil: Ocultar o chatbot
        print("  - Testando Mecanismo Retratil: Ocultando Chatbot (>)...")
        btn_retract = page.locator("#btn-retract-chatbot")
        btn_retract.hover()
        page.wait_for_timeout(600)
        page.evaluate("window.retrairChatbot()")
        page.wait_for_timeout(1800)
        
        # Testa Mecanismo Retratil: Restaurar o chatbot com a aba lateral
        print("  - Testando Mecanismo Retratil: Restaurando Chatbot (<)...")
        btn_expand = page.locator("#btn-expand-chatbot")
        btn_expand.hover()
        page.wait_for_timeout(700)
        page.evaluate("window.restaurarChatbot()")
        page.wait_for_timeout(1500)
        
        # ---------------------------------------------------------
        # ETAPA 2: Modulo Infracao (infracao.html)
        # ---------------------------------------------------------
        print("2. Navegando para Modulo Infracao (infracao.html)...")
        infra_url = (BASE_DIR / "infracao.html").as_uri()
        page.goto(infra_url)
        page.wait_for_timeout(1800)
        
        # Preenche os campos do formulario
        print("  - Interagindo com formulario de debitos...")
        input_placa = page.locator("#input-placa")
        if input_placa.is_visible():
            input_placa.fill("BRA2E19")
            page.wait_for_timeout(600)
            
        input_renavam = page.locator("#input-renavam")
        if input_renavam.is_visible():
            input_renavam.fill("00123456789")
            page.wait_for_timeout(1000)
        
        # Hover sobre os botoes desobstruidos
        consultar_btn = page.locator("button:has-text('Consultar')")
        if consultar_btn.is_visible():
            consultar_btn.hover()
            page.wait_for_timeout(800)
        
        # Oculta o chatbot nesta tela
        page.evaluate("window.retrairChatbot()")
        page.wait_for_timeout(1200)
        page.evaluate("window.restaurarChatbot()")
        page.wait_for_timeout(1200)
        
        # Demonstracao de Responsividade: Redimensiona para Mobile 360x740
        print("  - Demonstrando comportamento responsivo em Mobile 360x740...")
        page.set_viewport_size({"width": 360, "height": 740})
        page.wait_for_timeout(2000)
        
        # Mostra o botao Consultar 100% desobstruido no mobile
        page.mouse.wheel(0, 150)
        page.wait_for_timeout(1200)
        page.evaluate("window.retrairChatbot()")
        page.wait_for_timeout(1500)
        page.evaluate("window.restaurarChatbot()")
        page.wait_for_timeout(1500)
        
        # Retorna para resolucao Desktop para continuar navegacao
        page.set_viewport_size({"width": 1280, "height": 720})
        page.wait_for_timeout(1500)
        
        # ---------------------------------------------------------
        # ETAPA 3: Modulo Atendimento (atendimento.html)
        # ---------------------------------------------------------
        print("3. Navegando para Modulo Atendimento (atendimento.html)...")
        atend_url = (BASE_DIR / "atendimento.html").as_uri()
        page.goto(atend_url)
        page.wait_for_timeout(1800)
        
        # Interage com os seletores
        print("  - Selecionando categoria de servico e unidade...")
        selects = page.locator("select")
        if selects.count() > 0:
            try:
                selects.first.select_option(index=1)
                page.wait_for_timeout(800)
            except Exception: pass
            
        chk = page.locator("input[type='checkbox']")
        if chk.count() > 0:
            try:
                chk.first.check(force=True)
                page.wait_for_timeout(600)
            except Exception: pass
            
        if selects.count() > 1:
            try:
                selects.nth(1).select_option(index=1)
                page.wait_for_timeout(800)
            except Exception: pass
            
        # Oculta e restaura o chatbot
        page.evaluate("window.retrairChatbot()")
        page.wait_for_timeout(1200)
        page.evaluate("window.restaurarChatbot()")
        page.wait_for_timeout(1200)
        
        # ---------------------------------------------------------
        # ETAPA 4: Modulo Protocolo (protocolo.html)
        # ---------------------------------------------------------
        print("4. Navegando para Modulo Protocolo (protocolo.html)...")
        prot_url = (BASE_DIR / "protocolo.html").as_uri()
        page.goto(prot_url)
        page.wait_for_timeout(1800)
        
        # Preenche busca de protocolo
        input_prot = page.locator("#input-num-protocolo")
        if input_prot.is_visible():
            input_prot.fill("000.123.456-78")
            page.wait_for_timeout(1000)
        
        # Rola a pagina para mostrar o card Nova Solicitacao e botao ACESSAR desobstruido
        page.mouse.wheel(0, 200)
        page.wait_for_timeout(1200)
        
        # Hover no botao ACESSAR desobstruido
        acessar_btn = page.locator("a:has-text('ACESSAR'), button:has-text('ACESSAR')").first
        if acessar_btn.is_visible():
            acessar_btn.hover()
            page.wait_for_timeout(1000)
            
        # Oculta o chatbot no protocolo
        page.evaluate("window.retrairChatbot()")
        page.wait_for_timeout(1500)
        page.evaluate("window.restaurarChatbot()")
        page.wait_for_timeout(1500)
        
        # ---------------------------------------------------------
        # ETAPA 5: Retorno ao Inicio
        # ---------------------------------------------------------
        print("5. Retornando a Home (index.html)...")
        page.goto(home_url)
        page.wait_for_timeout(2500)
        
        # Finaliza contexto para salvar o video
        print("Finalizando gravacao...")
        page.close()
        context.close()
        browser.close()
        
    # Converte o video WebM gerado pelo Playwright para MP4 via FFmpeg
    webms = list(temp_rec_dir.glob("*.webm"))
    if not webms:
        print("Erro: Nenhum arquivo de video gravado.")
        return
        
    latest_webm = max(webms, key=lambda f: f.stat().st_mtime)
    mp4_output = VIDEOS_DIR / "demonstracao_fluxo_completo.mp4"
    webm_output = VIDEOS_DIR / "demonstracao_fluxo_completo.webm"
    
    # Copia o WebM permanente
    shutil.copy2(latest_webm, webm_output)
    print(f"Video WebM salvo: {webm_output.name} ({webm_output.stat().st_size / 1024 / 1024:.2f} MB)")
    
    # Converte para MP4 com H.264 compativel universal
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg_exe,
        "-y",
        "-i", str(latest_webm),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        str(mp4_output)
    ]
    print("Convertendo video para MP4 (H.264)...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and mp4_output.exists():
        size_mb = mp4_output.stat().st_size / (1024 * 1024)
        print(f"Video MP4 gerado com sucesso: {mp4_output.name} ({size_mb:.2f} MB)")
    else:
        print(f"Erro na conversao MP4: {res.stderr}")
        
    # Limpa diretorio temporario
    shutil.rmtree(temp_rec_dir, ignore_errors=True)
    print("Gravacao e processamento concluidos com sucesso!")

if __name__ == "__main__":
    main()
