# Ações Práticas de Melhoria Técnica (ISO/IEC 25040)

**Responsáveis:** Toda a Equipe Kay McNulty  
**Objeto:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Fase Normativa:** Fase 4 (Execução, Julgamento e Melhorias – ISO/IEC 25040, Seção 6.5)  
**Marco de Referência:** Ponto de Controle 2 (Entrega 2)

---

## 1. Contextualização das Intervenções Técnicas

A avaliação da qualidade de software fundamentada na norma ISO/IEC 25040 atinge seu valor máximo ao orientar intervenções tangíveis na arquitetura e na interface do produto. Em conformidade com o **Critério F4-C5**, a equipe Kay McNulty traduziu as fragilidades mais críticas diagnosticadas na Fase 4 em entregas técnicas concretas, funcionais e plenamente verificadas.

As intervenções dividem-se em duas frentes de engenharia de software desenvolvidas pelas respectivas duplas de especialistas:

| Dimensão da Melhoria | Característica e Escopo | Responsáveis Técnicos | Entrega Técnica Concreta | Documento Detalhado |
| :--- | :--- | :--- | :--- | :---: |
| **Melhoria da Compatibilidade e Responsividade** | Coexistência e Interoperabilidade (Módulos Infração, Atendimento, Protocolo e Chatbot) | Artur Fernandes Galdino e Nicole Jovita Fernandes | Protótipo interativo funcional, patch CSS responsivo (`detran-responsive-patch.css`), script de resiliência assíncrona (`chatbot-resilience-fallback.js`) e testes automatizados. | [Acessar Melhoria de Compatibilidade](melhoria-compatibilidade.md) |
| **Melhoria da Confiabilidade** | Recuperabilidade e Tolerância a Falhas (Módulos Atendimento e Protocolo) | Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo | Protótipo funcional de persistência e restauração de estado de formulários (`rascunho.js`), harness de teste e script Playwright de validação. | [Acessar Melhoria de Confiabilidade](melhoria-confiabilidade.md) |

**Tabela 1 – Síntese das ações técnicas de melhoria desenvolvidas pela equipe.** Fonte: Elaborado pelos autores.

---

## 2. Visão Consolidada dos Resultados Antes versus Depois

A tabela a seguir sumariza a evolução quantitativa das métricas formais das características antes e após a aplicação das soluções técnicas propostas:

| Característica / Métrica | Valor Original (Antes) | Nível Original | Valor Pós-Melhoria | Nível Pós-Melhoria | Impacto Direto no Cidadão |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Índice de Conformidade Responsiva ($ICR$)** | $70,00\%$ | Satisfatório | **$100,00\%$** | **Excelente** | Desobstrução total dos botões "Consultar", "Confirmar" e "Acessar" em telas de 360px a 768px, garantindo alvos de toque WCAG 2.1 ($\ge 44\times 44\,\text{px}$). |
| **Taxa de Compatibilidade de Navegadores ($TCBN$)** | $75,00\%$ | Satisfatório | **$100,00\%$** | **Excelente** | Tratamento do erro `ERR_CONNECTION_RESET` em navegadores baseados em Chromium (Edge e Chrome) via degradação graciosa com atendimento nativo Detran-DF. |
| **Taxa de Recuperabilidade de Interrupções ($TRTI$)** | $20,00\%$ | Insuficiente | **$100,00\%$** | **Excelente** | Restauração instantânea dos dados digitados em agendamentos e petições após recargas acidentais de página (F5) ou navegação pelo botão voltar. |

**Tabela 2 – Matriz consolidada de evolução de métricas com as ações de melhoria.** Fonte: Elaborado pelos autores.

---

## 3. Acesso aos Artefatos Práticos no Repositório

Todos os artefatos técnicos desenvolvidos foram incorporados ao repositório institucional sob versionamento semântico:

* **Diretório de Compatibilidade:**
  * Protótipo Interativo: [`docs/assets/melhorias/compatibilidade/layout_responsivo/index.html`](../assets/melhorias/compatibilidade/layout_responsivo/index.html)
  * Folha de Estilos Responsiva: [`docs/assets/melhorias/compatibilidade/layout_responsivo/detran-responsive-patch.css`](../assets/melhorias/compatibilidade/layout_responsivo/detran-responsive-patch.css)
  * Resiliência JavaScript: [`docs/assets/melhorias/compatibilidade/layout_responsivo/chatbot-resilience-fallback.js`](../assets/melhorias/compatibilidade/layout_responsivo/chatbot-resilience-fallback.js)
  * Script de Teste Automatizado: [`docs/assets/melhorias/compatibilidade/layout_responsivo/validar_melhoria.py`](../assets/melhorias/compatibilidade/layout_responsivo/validar_melhoria.py)
  * Script de Captura Comparativa: [`docs/assets/melhorias/compatibilidade/layout_responsivo/capture_comparative_screenshots.py`](../assets/melhorias/compatibilidade/layout_responsivo/capture_comparative_screenshots.py)
  * Script de Gravação de Vídeo: [`docs/assets/melhorias/compatibilidade/layout_responsivo/record_complete_flow_video.py`](../assets/melhorias/compatibilidade/layout_responsivo/record_complete_flow_video.py)
  * Vídeo de Demonstração do Fluxo Completo: [`docs/assets/melhorias/compatibilidade/layout_responsivo/videos/demonstracao_fluxo_completo.mp4`](../assets/melhorias/compatibilidade/layout_responsivo/videos/demonstracao_fluxo_completo.mp4)
  * Dados Empíricos de Validação: [`docs/dados/compatibilidade/melhoria/validacao_melhoria.csv`](../dados/compatibilidade/melhoria/validacao_melhoria.csv)
* **Diretório de Confiabilidade:**
  * Protótipo de Rascunho: [`docs/assets/melhorias/confiabilidade/rascunho/index.html`](../assets/melhorias/confiabilidade/rascunho/index.html)
  * Script de Persistência: [`docs/assets/melhorias/confiabilidade/rascunho/rascunho.js`](../assets/melhorias/confiabilidade/rascunho/rascunho.js)
  * Script de Teste Automatizado: [`docs/assets/melhorias/confiabilidade/rascunho/validar.py`](../assets/melhorias/confiabilidade/rascunho/validar.py)
  * Dados Empíricos de Validação: [`docs/dados/confiabilidade/melhoria/validacao.csv`](../dados/confiabilidade/melhoria/validacao.csv)

Para orientações detalhadas de arquitetura, riscos de integração e recomendações ao Detran-DF, consulte os relatórios técnicos específicos de cada característica no menu lateral.
