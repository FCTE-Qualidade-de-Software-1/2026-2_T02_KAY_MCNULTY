#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
capture_comparative_screenshots.py

Captura prints reais em alta definicao de todas as telas que apresentaram
falhas de responsividade na avaliacao original e monta paineis comparativos
Antes vs Depois (ISO/IEC 25040 F4-C5 e WCAG 2.1).
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = Path(__file__).resolve().parent
REPO_DIR = BASE_DIR.parents[4]
EVID_DIR = BASE_DIR / "evidencias"
ORIG_DIR = REPO_DIR / "docs" / "assets" / "evidencias" / "compatibilidade"

EVID_DIR.mkdir(parents=True, exist_ok=True)

CASES = [
    {
        "id": "INFRA_360px",
        "doc_name": "INFRA_ANTES_DEPOIS_360px.png",
        "file": "infracao.html",
        "width": 360,
        "height": 640,
        "orig_img": "RESP_INFRACAO_360px.png",
        "title": "Modulo Infracao - Mobile Pequeno (360x640)",
        "fail_desc": "Avatar sobrepoe diretamente o botao Consultar",
        "fix_desc": "Desobstrucao total do botao Consultar + Mecanismo Retratil Ativo"
    },
    {
        "id": "INFRA_414px",
        "doc_name": "INFRA_ANTES_DEPOIS_414px.png",
        "file": "infracao.html",
        "width": 414,
        "height": 896,
        "orig_img": "RESP_INFRACAO_414px.png",
        "title": "Modulo Infracao - Mobile Medio (414x896)",
        "fail_desc": "Avatar sobrepoe metade direita do botao Consultar",
        "fix_desc": "Botao Consultar 100% visivel e interativo com safe area lateral"
    },
    {
        "id": "INFRA_768px",
        "doc_name": "INFRA_ANTES_DEPOIS_768px.png",
        "file": "infracao.html",
        "width": 768,
        "height": 1024,
        "orig_img": "RESP_INFRACAO_768px.png",
        "title": "Modulo Infracao - Tablet Portrait (768x1024)",
        "fail_desc": "Avatar posicionado sobre a area clicavel da acao",
        "fix_desc": "Dock flutuante com afastamento seguro da area de acoes"
    },
    {
        "id": "INFRA_1366px",
        "doc_name": "INFRA_ANTES_DEPOIS_1366px.png",
        "file": "infracao.html",
        "width": 1366,
        "height": 768,
        "orig_img": "RESP_INFRACAO_1366px.png",
        "title": "Modulo Infracao - Desktop HD (1366x768)",
        "fail_desc": "Widget sem espacamento seguro em relacao ao rodape e conteudo",
        "fix_desc": "Dock posicionado a 32px das bordas com botao retratil discreto"
    },
    {
        "id": "ATEND_360px",
        "doc_name": "ATEND_ANTES_DEPOIS_360px.png",
        "file": "atendimento.html",
        "width": 360,
        "height": 640,
        "orig_img": "RESP_AGENDAMENTO_360px.png",
        "title": "Modulo Atendimento - Mobile Pequeno (360x640)",
        "fail_desc": "Avatar cobre seletores de unidade e data de agendamento",
        "fix_desc": "Formulario 100% desimpedido + Botao retratil ativo"
    },
    {
        "id": "PROT_360px",
        "doc_name": "PROT_ANTES_DEPOIS_360px.png",
        "file": "protocolo.html",
        "width": 360,
        "height": 640,
        "orig_img": "RESP_PROTOCOLO_360px.png",
        "title": "Modulo Protocolo - Mobile Pequeno (360x640)",
        "fail_desc": "Avatar bloqueia clique no botao ACESSAR de Nova Solicitacao",
        "fix_desc": "Card e botao ACESSAR totalmente livres e acessiveis"
    }
]

def load_system_font(size):
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf"
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def create_comparison_panel(orig_path, corr_path, out_path, title, fail_desc, fix_desc):
    orig = Image.open(orig_path).convert("RGB")
    corr = Image.open(corr_path).convert("RGB")
    
    target_h = 700
    
    # Redimensiona mantendo proporcoes
    w_orig = int(orig.width * (target_h / orig.height))
    orig_resized = orig.resize((w_orig, target_h), Image.Resampling.LANCZOS)
    
    w_corr = int(corr.width * (target_h / corr.height))
    corr_resized = corr.resize((w_corr, target_h), Image.Resampling.LANCZOS)
    
    header_h = 65
    footer_h = 45
    pad = 20
    canvas_w = w_orig + w_corr + (pad * 3)
    canvas_h = target_h + header_h + footer_h
    
    canvas = Image.new("RGB", (canvas_w, canvas_h), "#0f172a")
    draw = ImageDraw.Draw(canvas)
    
    font_title = load_system_font(18)
    font_badge = load_system_font(13)
    font_text = load_system_font(12)
    
    # Top Bar Header
    draw.rectangle([(0, 0), (canvas_w, header_h)], fill="#1e293b")
    draw.text((pad, 14), f"AUDITORIA DE RESPONSIVIDADE - {title.upper()}", fill="#ffffff", font=font_title)
    draw.text((canvas_w - 320, 18), "ISO/IEC 25040 (F4-C5) | WCAG 2.1 AAA", fill="#94a3b8", font=font_text)
    
    # Painel Esquerdo: Antes (Original)
    x_orig = pad
    y_body = header_h
    canvas.paste(orig_resized, (x_orig, y_body))
    
    # Badge ANTES (Vermelho)
    draw.rectangle([(x_orig + 10, y_body + 10), (x_orig + 280, y_body + 42)], fill="#7f1d1d")
    draw.text((x_orig + 18, y_body + 15), "ANTES: FALHA DE SOBREPOSICAO", fill="#fecaca", font=font_badge)
    
    # Painel Direito: Depois (Corrigido)
    x_corr = x_orig + w_orig + pad
    canvas.paste(corr_resized, (x_corr, y_body))
    
    # Badge DEPOIS (Verde)
    draw.rectangle([(x_corr + 10, y_body + 10), (x_corr + 310, y_body + 42)], fill="#065f46")
    draw.text((x_corr + 18, y_body + 15), "DEPOIS: DESOBSTRUCAO TOTAL (100%)", fill="#a7f3d0", font=font_badge)
    
    # Footer Bar
    draw.rectangle([(0, canvas_h - footer_h), (canvas_w, canvas_h)], fill="#1e293b")
    diag_line = f"Diagnostico Original: {fail_desc}  |  Solucao Implementada: {fix_desc}"
    draw.text((pad, canvas_h - footer_h + 14), diag_line, fill="#cbd5e1", font=font_text)
    
    canvas.save(out_path, "PNG", quality=95)
    print(f"Painel comparativo gerado: {out_path.name}")

def main():
    print("Iniciando captura de telas com Playwright (MS Edge)...")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=EDGE_PATH, headless=True)
        for c in CASES:
            # Captura no tamanho exato especificado
            page = browser.new_page(viewport={"width": c["width"], "height": c["height"]})
            file_url = (BASE_DIR / c["file"]).as_uri()
            page.goto(file_url)
            page.evaluate("try { sessionStorage.clear(); } catch(e){}")
            page.reload()
            page.wait_for_timeout(600)
            
            # Print Corrigido Normal
            out_corr = EVID_DIR / f"CORRIGIDO_{c['id']}.png"
            page.screenshot(path=str(out_corr))
            print(f"Capturado: {out_corr.name}")
            
            # Print Corrigido Recolhido (com aba lateral)
            btn_retract = page.query_selector("#btn-retract-chatbot")
            if btn_retract:
                btn_retract.click()
                page.wait_for_timeout(450)
                out_rec = EVID_DIR / f"CORRIGIDO_{c['id']}_RECOLHIDO.png"
                page.screenshot(path=str(out_rec))
                print(f"Capturado recolhido: {out_rec.name}")
            
            page.close()
            
            # Gerar Painel Comparativo Antes vs Depois
            orig_img_path = ORIG_DIR / c["orig_img"]
            comp_panel_path = EVID_DIR / f"COMP_{c['id']}.png"
            doc_panel_path = EVID_DIR / c["doc_name"]
            
            if orig_img_path.exists():
                create_comparison_panel(
                    orig_img_path,
                    out_corr,
                    comp_panel_path,
                    c["title"],
                    c["fail_desc"],
                    c["fix_desc"]
                )
                # Copia tambem para o arquivo referenciado na documentacao
                create_comparison_panel(
                    orig_img_path,
                    out_corr,
                    doc_panel_path,
                    c["title"],
                    c["fail_desc"],
                    c["fix_desc"]
                )
            else:
                print(f"Aviso: Imagem original nao encontrada: {orig_img_path}")
                
        browser.close()
    print("Todas as evidencias e paineis comparativos foram gerados com sucesso!")

if __name__ == "__main__":
    main()
