# Ação de Melhoria – Capacidade de Interação: Protótipo do Requerimento Geral

**Responsável:** Yan  
**Característica:** Capacidade de Interação (ISO/IEC 25010:2023), subcaracterísticas Operabilidade e Proteção contra Erros de Usuário  
**Módulo Afetado:** Protocolo (Requerimento Geral, tarefa T3)  
**Tipo de Ação:** Protótipo de alta fidelidade (HTML, CSS e JavaScript, sem dependências), integrado ao protótipo da melhoria de compatibilidade  
**Fase Normativa:** Fase 4 (Execução, Julgamento e Melhorias – ISO/IEC 25040)

!!! warning "O que este protótipo é e o que não é"
    É uma **proposta de projeto** do fluxo do Requerimento Geral. Não é o portal em produção, usa **somente dados fictícios** e **não faz assinatura**. Os testes desta página medem o comportamento do protótipo, e não o do portal. O efeito sobre as métricas M1, M2 e M3 só pode ser afirmado depois da validação com participantes (issue de validação do protótipo).

---

## 1. Problema e motivação

Na avaliação do módulo Protocolo, a T3 (abrir um requerimento) foi a tarefa com pior desempenho, e três cenários de erro avançaram até a etapa de assinatura sem nenhum alerta. A página de oportunidades de melhoria priorizou duas falhas do mesmo fluxo:

| ID | Problema | Evidência |
| :---: | :--- | :---: |
| **O1** | O formulário aceita campos inválidos (Objeto vazio, placa incompleta e Renavam curto) e avança sem alerta | EV-07 |
| **O3** | A prévia do documento chega à assinatura, que tem validade legal, sem revisão e sem aviso | EV-11 (a confirmar na inspeção) |
| **O2** | A T3 teve baixa autonomia, e a causa ainda não está documentada | EV-02 |

**Tabela 1 – Problemas atacados.** Fonte: Elaborado pelos autores, a partir da página de oportunidades de melhoria. Os IDs da inspeção heurística consolidada serão acrescentados quando a inspeção real estiver registrada.

---

## 2. O protótipo

O protótipo é uma página navegável com o teclado e com o toque, que cobre o caminho **Minhas Solicitações → Requerimento Geral → Revisão → Assinatura (simulada)**. Ele fica na mesma pasta do protótipo de compatibilidade e usa o mesmo visual das telas do portal.

* **Abrir:** [requerimento-geral.html](../assets/melhorias/compatibilidade/layout_responsivo/requerimento-geral.html)
* **Linha de base (portal atual):** [requerimento-geral.html?modo=atual](../assets/melhorias/compatibilidade/layout_responsivo/requerimento-geral.html?modo=atual), que reproduz o comportamento observado: sem validação e sem revisão.
* **Ponto de entrada:** na tela [protocolo.html](../assets/melhorias/compatibilidade/layout_responsivo/protocolo.html), o botão "Acessar" do card "Nova Solicitação" e o botão "Nova Solicitação" da barra azul levam ao Requerimento Geral. O "Cancelar" volta para o `protocolo.html`.

Os estados podem ser abertos direto por parâmetro (`?estado=vazio`, `padrao`, `erro`, `revisao` e `confirmacao`) e também pelos links no rodapé do protótipo.

### 2.1 Integração com a melhoria de compatibilidade

As duas ações compartilham os mesmos arquivos de base, para que o fluxo novo já nasça compatível com telas estreitas e com os navegadores Chromium:

| Parte da melhoria de compatibilidade | Como o Requerimento Geral usa |
| :--- | :--- |
| `detran-responsive-patch.css` | Barra de ações fixa na parte de baixo (`.detran-action-bar-wrapper`), botões (`.detran-btn`), campos (`.detran-input-control`) e posicionamento do avatar do assistente acima da barra |
| `chatbot-resilience-fallback.js` | Carregado na página. Se a CDN do assistente falhar, o avatar vira o atalho para a Central 154 e o WhatsApp |
| Telas do portal (`index`, `infracao`, `atendimento` e `protocolo`) | Mesmo cabeçalho, mesmo menu e mesma barra azul de ações. Em telas estreitas, o menu vira um botão, para não sobrepor o logotipo |
| `protocolo.html` | Dois botões passaram a abrir o Requerimento Geral (única alteração nesse arquivo) |

**Tabela 2 – Pontos de integração.** Fonte: Elaborado pelos autores.

### 2.2 Elementos do protótipo

| Elemento | Responde a | Heurística principal | Situação |
| :--- | :---: | :---: | :--- |
| Validação por campo (Objeto, placa e Renavam), com mensagem junto do campo e sem avançar com valor inválido | O1 | NH5 e NH9 | Decidido |
| Resumo de erros no topo, com links para cada campo | O1 | NH9 | Decidido |
| Tela de revisão com os dados informados e botão "Voltar e editar" | O3 | NH3 | Decidido |
| Aviso de que a assinatura tem validade legal e não pode ser desfeita, com ciência obrigatória antes de seguir | O3 | NH5 | Decidido |
| Indicação da etapa atual e do total ("Etapa 2 de 3") | O2 | NH1 | **Hipótese a testar** |
| Exemplo no campo Objeto | O2 | NH10 | **Hipótese a testar** |

**Tabela 3 – Elementos do protótipo.** Fonte: Elaborado pelos autores. As duas hipóteses não têm dado real que as sustente, e o resultado não deve ser atribuído a elas sem teste separado.

### 2.3 Regras de validação

| Campo | Obrigatório | Regra | Mensagem |
| :--- | :---: | :--- | :--- |
| Objeto | Sim | Mínimo de 10 caracteres | Diz o que fazer e dá um exemplo |
| Placa | Não | 7 caracteres, no formato antigo (ABC-1234) ou Mercosul (ABC1D23) | Mostra o formato esperado |
| Renavam | Não | 11 números e dígito verificador correto | Mostra quantos números foram digitados |

**Tabela 4 – Regras de validação.** Fonte: Elaborado pelos autores. Placa e Renavam são opcionais porque o requerimento da T3 não está ligado a um veículo.

### 2.4 Estados modelados

Os quatro estados pedidos pela issue estão em 360 px (mobile) e em 1280 px (desktop):

| Estado | Tela | Mobile | Desktop |
| :--- | :--- | :---: | :---: |
| Vazio | Minhas Solicitações, sem nenhum registro | ![Vazio mobile](../img/prototipo/requerimento-vazio-mobile-360.png) | ![Vazio desktop](../img/prototipo/requerimento-vazio-desktop-1280.png) |
| Padrão | Formulário em branco | ![Padrão mobile](../img/prototipo/requerimento-padrao-mobile-360.png) | ![Padrão desktop](../img/prototipo/requerimento-padrao-desktop-1280.png) |
| Erro | Formulário com os três campos inválidos | ![Erro mobile](../img/prototipo/requerimento-erro-mobile-360.png) | ![Erro desktop](../img/prototipo/requerimento-erro-desktop-1280.png) |
| Revisão | Dados conferidos e aviso da assinatura | ![Revisão mobile](../img/prototipo/requerimento-revisao-mobile-360.png) | ![Revisão desktop](../img/prototipo/requerimento-revisao-desktop-1280.png) |
| Confirmação | Pronto para assinar (simulado) | ![Confirmação mobile](../img/prototipo/requerimento-confirmacao-mobile-360.png) | ![Confirmação desktop](../img/prototipo/requerimento-confirmacao-desktop-1280.png) |

**Tabela 5 – Estados do protótipo.** Fonte: Elaborado pelos autores, a partir de capturas do próprio protótipo.

---

## 3. Antes e depois

| Aspecto | Antes (portal atual, conforme as evidências) | Depois (protótipo) |
| :--- | :--- | :--- |
| Objeto vazio | Avança até a assinatura sem alerta (EV-07) | Bloqueia e mostra a mensagem junto do campo |
| Placa incompleta | Avança sem alerta (EV-07) | Bloqueia e mostra o formato esperado |
| Renavam curto | Avança sem alerta (EV-07) | Bloqueia e mostra quantos números faltam |
| Antes da assinatura | Prévia do documento, sem aviso nem opção de editar (EV-11) | Tela de revisão, aviso da validade legal e botão para voltar e editar |
| Orientação de etapa | Não há indicação | "Etapa 1 de 3", "2 de 3" e "3 de 3" |

**Tabela 6 – Comparação antes e depois.** Fonte: Elaborado pelos autores. A coluna "Antes" vem das evidências da avaliação. O modo `?modo=atual` do protótipo **reproduz** esse comportamento para comparação, e não o mede no portal.

A linha de base reproduzida, em 360 px: formulário sem etapas e assinatura logo após o envio.

| Formulário (linha de base) | Assinatura (linha de base) |
| :---: | :---: |
| ![Linha de base, formulário](../img/prototipo/requerimento-linha-de-base-padrao-mobile-360.png) | ![Linha de base, assinatura](../img/prototipo/requerimento-linha-de-base-assinatura-mobile-360.png) |

**Figura 1 – Linha de base reproduzida no protótipo (mobile).** Fonte: Elaborado pelos autores.

---

## 4. Rastreabilidade

| Problema | Heurística | Solução no protótipo | Métrica acompanhada |
| :---: | :---: | :--- | :---: |
| O1 | NH5, NH9 | Validação por campo, mensagem junto do campo e resumo de erros | M3 (TPRE do Protocolo) |
| O3 | NH5, NH3 | Revisão, aviso da validade legal, ciência obrigatória e "Voltar e editar" | M3 |
| O2 | NH1, NH10 | Indicação de etapa e exemplo no Objeto (hipóteses) | M1 e M2 |

**Tabela 7 – Problema, heurística, solução e métrica.** Fonte: Elaborado pelos autores. As heurísticas seguem o código NH1 a NH10 do protocolo da Fase 3.

---

## 5. Verificação do protótipo

O script `validar_requerimento_geral.py` abre o protótipo em um Chrome sem interface, executa os cenários de `requerimento-geral-testes.js` e grava o resultado em [validacao_prototipo.csv](../dados/capacidade_interacao/melhoria/validacao_prototipo.csv). Os testes rodam dentro de uma moldura com a largura pedida (360, 414, 500, 768 e 1366 px), porque o Chrome sem interface não gera janelas abaixo de 500 px.

| Grupo | Testes por largura | Resultado |
| :--- | :---: | :---: |
| Cenários de erro da avaliação (E-PRO-01, 08 e 09), com mensagem junto do campo | 6 | 6 de 6 |
| Renavam com dígito verificador errado e campos opcionais vazios | 2 | 2 de 2 |
| Fluxo válido: revisão, aviso, ciência, "Voltar e editar" e chegada à assinatura | 7 | 7 de 7 |
| Acessibilidade verificável por código (`aria-invalid` e `role="alert"`) | 2 | 2 de 2 |
| Avatar do assistente sem sobrepor os botões de ação (formulário, revisão e assinatura, no topo e no fim da página) | 3 | 3 de 3 |
| **Subtotal por largura (modo protótipo)** | **20** | **20 de 20** |
| Linha de base reproduzida em 360 px (3 cenários avançam, e o fluxo válido vai direto à assinatura) | 4 | 4 de 4 |
| **Total (5 larguras × 20, mais 4)** | **104** | **104 de 104** |

**Tabela 8 – Resultado dos testes automáticos.** Fonte: Elaborado pelos autores, a partir de `validacao_prototipo.csv`.

Na linha de base reproduzida, os 3 cenários de erro avançam (0 de 3 bloqueados). No protótipo, os mesmos 3 são bloqueados (3 de 3). Esse contraste mostra que o **projeto** trata o problema, mas **não é uma medida do portal**. Os testes da linha de base conferem que a reprodução se comporta como a evidência descreve.

A sobreposição do avatar é **medida no navegador** (interseção, em px², entre o avatar e cada botão de ação, no topo e no fim da página). O mesmo critério da melhoria de compatibilidade se aplica aqui, mas apenas ao fluxo novo.

---

## 6. Limites

* O protótipo não é o portal em produção, e o resultado vale para o protótipo. O portal não foi alterado, e a equipe não tem acesso ao código dele.
* Os testes automáticos verificam regras de interface. Não substituem a re-inspeção heurística nem o teste com participantes.
* A medição do avatar considera só os **botões de ação**. Campos de texto podem ficar cobertos pelo avatar em alguns pontos da rolagem (por exemplo, em 768 px, com a página no topo). O botão de recolher o assistente, que existe nas telas do portal, não foi levado para este fluxo.
* O avatar real do assistente depende de uma CDN externa. Nos testes e em ambientes sem acesso a ela, aparece o atalho de atendimento do `chatbot-resilience-fallback.js`, que tem a mesma posição.
* A reprodução da linha de base segue as evidências EV-07 e EV-11. A EV-11 ainda precisa ser confirmada na inspeção heurística, e a EV-07 tem uma divergência registrada para o campo vazio (a Confiabilidade viu uma mensagem de erro no envio).
* A indicação de etapa e o exemplo no Objeto são hipóteses: não há dado real que mostre que melhoram a autonomia.
* A acessibilidade foi verificada só nos atributos testados. Não há auditoria completa nem teste com leitor de tela.
* Todos os dados são fictícios, inclusive a placa `ABC1D23` e o Renavam `12345678900`, que servem só de exemplo.

---

## 7. Como reproduzir

Na raiz do repositório, com Google Chrome (ou Chromium) e Pillow instalados:

```bash
python3 docs/assets/melhorias/compatibilidade/layout_responsivo/validar_requerimento_geral.py
```

O comando roda os 104 testes, regrava o CSV e as capturas em `docs/img/prototipo/` e termina com código diferente de zero se algum teste falhar.

## 8. Próximos passos

* Reexecutar o E-PRO-01 (Objeto vazio) no portal, para resolver a divergência com a Confiabilidade.
* Confirmar a EV-11 na inspeção heurística.
* Re-inspecionar o protótipo com o protocolo da Fase 3 e comparar o IPH com a linha de base.
* Testar a T3 no protótipo com ao menos 3 participantes que não fizeram as sessões, e registrar numeradores e denominadores.
