# Resultados Empíricos e Julgamento – Característica: Compatibilidade

**Disciplina:** Qualidade de Software 1 (FGA0315) – Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 02)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Norma Base:** ABNT NBR ISO/IEC 25040:2011 (Processo de Avaliação de Produto de Software, Seções 6.4 e 6.5)  
**Característica:** Compatibilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Coexistência e Interoperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot  
**Responsáveis:** Artur Fernandes Galdino e Nicole Jovita Fernandes  
**Fase Normativa:** Fase 4 (Execução, Julgamento e Melhorias – ISO/IEC 25040)

!!! note "Status da Coleta de Dados"
    Página estruturada com modelos de dados e marcadores para inserção dos resultados empíricos, evidências visuais e dumps de rede coletados nos ensaios práticos do Portal Detran Digital DF.

---

## 1. Sumário dos Dados Brutos Coletados

### 1.1 Ensaios de Coexistência Cross-Browser (TCBN)

Os ensaios foram executados nos 4 navegadores homologados (Chrome, Firefox, Edge e Safari) seguindo os roteiros definidos na Fase 3. Os dados detalhados encontram-se registrados em [`docs/dados/compatibilidade/tcbn/cross_browser.csv`](../dados/compatibilidade/tcbn/cross_browser.csv).

| Módulo | Cenário de Teste | Google Chrome | Mozilla Firefox | Microsoft Edge | Apple Safari | Situação do Cenário |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Infração** | TC-CB-01 | Aprovado | Aprovado | Aprovado | Aprovado | **Aprovado** |
| **Atendimento** | TC-CB-02 | Aprovado | Aprovado | Aprovado | Aprovado | **Aprovado** |
| **Protocolo** | TC-CB-03 | Aprovado | Aprovado | Aprovado | Aprovado | **Aprovado** |
| **Chatbot** | TC-CB-04 | Reprovado | Aprovado | Reprovado | Aprovado | **Reprovado (Divergência)** |

*Tabela 1 — Matriz consolidada de execução Cross-Browser. Fonte: Dados coletados pelos autores.*

---

### 1.2 Ensaios de Conformidade Responsiva Multi-resolução (ICR)

As inspeções de layout cobriram as 5 viewports normatizadas (360px a 1920px). A relação de conformidade de cada um dos 20 pontos está disponível em [`docs/dados/compatibilidade/icr/responsividade.csv`](../dados/compatibilidade/icr/responsividade.csv).

| Viewport | Resolução (px) | Infração | Atendimento | Protocolo | Chatbot | Total de Conformidades |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Mobile Pequeno** | 360 × 640 | Não Conforme | Não Conforme | Não Conforme | Conforme | 1 / 4 |
| **Mobile Médio** | 414 × 896 | Não Conforme | Conforme | Conforme | Conforme | 3 / 4 |
| **Tablet** | 768 × 1024 | Não Conforme | Conforme | Conforme | Conforme | 3 / 4 |
| **Desktop HD** | 1366 × 768 | Não Conforme | Conforme | Conforme | Conforme | 3 / 4 |
| **Desktop Full HD** | 1920 × 1080 | Conforme | Conforme | Conforme | Conforme | 4 / 4 |
| **Total por Módulo** | — | **1 / 5** | **4 / 5** | **4 / 5** | **5 / 5** | **14 / 20** |

*Tabela 2 — Matriz consolidada de inspeção responsiva. Fonte: Dados coletados pelos autores.*

---

### 1.3 Ensaios de Interoperabilidade e Tráfego de Rede (TSIS)

Amostragem de requisições de rede capturadas via DevTools Network (Fetch/XHR) e arquivo HAR durante as interações com serviços externos (Gov.br, SEFAZ/Bancos, SEI-GDF e motor InBot/AWS). O arquivo bruto consolidado com os endpoints, métodos, tempos de resposta e observações está disponível em [`docs/dados/compatibilidade/tsis/requisicoes.csv`](../dados/compatibilidade/tsis/requisicoes.csv).

| Módulo | Serviço Externo Integrado | Total de Requisições | Requisições Sucesso (2xx/3xx) | Falhas (4xx/5xx/CORS) | Taxa de Sucesso |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Infração** | Consulta Veicular, Débitos e Proteção hCaptcha | 4 | 4 | 0 | 100,0% |
| **Atendimento** | Provedor Gov.br (Selos), Perfil e Habilitação | 5 | 5 | 0 | 100,0% |
| **Protocolo** | Peticionamento e Consulta SEI-GDF | 1 | 0 | 1 (HTTP 422) | 0,0% |
| **Chatbot** | Plataforma InBot (AWS / CDN) | 2 | 1 | 1 (Connection Reset) | 50,0% |
| **Total Consolidado** | **Amostra de Interoperabilidade** | **12** | **10** | **2** | **83,33%** |

*Tabela 3 — Síntese do tráfego de rede e interoperabilidade. Fonte: Dados coletados pelos autores.*

---

## 2. Medidas Básicas e Cálculo das Métricas

*(Esta seção destina-se à consolidação formal dos cálculos matemáticos das métricas TCBN, ICR e TSIS, a ser realizada na issue de consolidação e análise da Fase 4 após o fechamento da coleta de dados).*

### 2.1 Taxa de Compatibilidade Entre Navegadores (TCBN)
* Medida Básica $N_{ap}$ (Cenários aprovados em todos os 4 navegadores): `[Aguardando consolidação]`
* Medida Básica $N_{tot}$ (Total de cenários planejados): `4`

$$TCBN = \left(\frac{N_{ap}}{N_{tot}}\right) \times 100$$

---

### 2.2 Índice de Conformidade Responsiva (ICR)
* Medida Básica $T_{conf}$ (Pontos de inspeção conformes): `[Aguardando consolidação]`
* Medida Básica $T_{tot}$ (Total de pontos de inspeção): `20`

$$ICR = \left(\frac{T_{conf}}{T_{tot}}\right) \times 100$$

---

### 2.3 Taxa de Sucesso de Interoperabilidade de Serviços (TSIS)
* Medida Básica $Req_{ok}$ (Requisições com status HTTP 2xx/3xx): `[Aguardando consolidação]`
* Medida Básica $Req_{tot}$ (Total de requisições de rede monitoradas no escopo): `[Aguardando consolidação]`

$$TSIS = \left(\frac{Req_{ok}}{Req_{tot}}\right) \times 100$$

---

## 3. Aplicação dos Níveis de Pontuação e Julgamento

*(Esta seção destina-se ao enquadramento dos índices apurados nas escalas ordinais de qualidade da Fase 2, a ser realizada na issue subsequente de consolidação da Fase 4).*

| Métrica Avaliada | Valor Apurado | Nível de Julgamento Obtido | Situação de Conformidade |
| :--- | :---: | :---: | :---: |
| **M1 – TCBN (Cross-Browser)** | `[Pendente]` | `[Pendente]` | Aguardando cálculo |
| **M2 – ICR (Responsividade)** | `[Pendente]` | `[Pendente]` | Aguardando cálculo |
| **M3 – TSIS (Interoperabilidade)** | `[Pendente]` | `[Pendente]` | Aguardando cálculo |

*Tabela 4 — Julgamento das métricas de Compatibilidade. Fonte: Elaborado pelos autores.*

---

## 4. Respostas às Questões e Validação de Hipóteses GQM

*(As respostas técnicas formais e o confronto com as hipóteses H1, H2 e H3 serão redigidos no escopo da issue de consolidação e relatório final da Fase 4).*

### Questão Q1 (Coexistência / Cross-Browser)
* **Pergunta:** O sistema preserva a funcionalidade e a integridade de layout nos navegadores modernos mais difundidos no mercado (Chrome, Firefox, Edge e Safari)?
* **Resposta Técnica:** `[A ser preenchida após consolidação dos ensaios]`
* **Confronto com Hipótese H1:** `[A ser confrontada após consolidação]`

### Questão Q2 (Coexistência / Responsividade Multi-resolução)
* **Pergunta:** As páginas e componentes dos quatro módulos adaptam-se de forma consistente às dimensões de tela mobile (360px a 414px), tablet (768px) e desktop (1366px e 1920px)?
* **Resposta Técnica:** `[A ser preenchida após consolidação dos ensaios]`
* **Confronto com Hipótese H2:** `[A ser confrontada após consolidação]`

### Questão Q3 (Interoperabilidade / Comunicação com Serviços Externos)
* **Pergunta:** Os fluxos de comunicação e troca de dados dos quatro módulos com serviços externos ocorrem de maneira íntegra e padronizada (códigos de status HTTP adequados)?
* **Resposta Técnica:** `[A ser preenchida após consolidação dos ensaios]`
* **Confronto com Hipótese H3:** `[A ser confrontada após consolidação]`

---

## 5. Galeria de Evidências e Capturas de Tela

<!-- ================================================================= -->
<!-- SEÇÃO DE EVIDÊNCIAS: INSERÇÃO DE PRINTS E CAPTURAS PELOS AVALIADORES -->
<!-- Para adicionar novas fotos, salve a imagem em docs/assets/evidencias/compatibilidade/ -->
<!-- e insira a tag Markdown correspondente na seção desejada abaixo: -->
<!-- ================================================================= -->

### 5.1 Evidências dos Ensaios Cross-Browser (TCBN)

#### Mozilla Firefox (4 de 4 Aprovados)
* **Infração:**
  ![Consulta de Infrações no Mozilla Firefox](../assets/evidencias/compatibilidade/CB_INFRACAO_FIREFOX.png)
* **Atendimento:**
  ![Agendamento de Atendimento no Mozilla Firefox](../assets/evidencias/compatibilidade/CB_ATENDIMENTO_FIREFOX.png)
* **Protocolo:**
  ![Protocolo no Mozilla Firefox](../assets/evidencias/compatibilidade/CB_PROTOCOLO_FIREFOX.png)
* **Chatbot (Assistente Virtual Operacional com IA):**
  ![Chatbot Operacional no Mozilla Firefox](../assets/evidencias/compatibilidade/CB_CHATBOT_FIREFOX.png)

#### Microsoft Edge (3 de 4 Aprovados — Falha no Chatbot)
* **Infração:**
  ![Consulta de Infrações no Microsoft Edge](../assets/evidencias/compatibilidade/CB_INFRACAO_MICROSOFT_EDGE.png)
* **Atendimento:**
  ![Agendamento de Atendimento no Microsoft Edge](../assets/evidencias/compatibilidade/CB_ATENDIMENTO_MICROSOFT_EDGE.png)
* **Protocolo:**
  ![Protocolo no Microsoft Edge](../assets/evidencias/compatibilidade/CB_PROTOCOLO_MICROSOFT_EDGE.png)
* **Chatbot (Falha de Carregamento — Erro no Loader InBot):**
  ![Erro de Conexão do Chatbot no Microsoft Edge](../assets/evidencias/compatibilidade/CB_CHATBOT_MICROSOFT-EDGE.png)
  ![Aba Rede DevTools com Falha bot-loader no Microsoft Edge](../assets/evidencias/compatibilidade/CB_CHATBOT_MICROSOFT_EDGE_2.png)

#### Google Chrome (3 de 4 Aprovados — Falha no Chatbot)
* **Infração:**
  ![Consulta de Infrações no Google Chrome](../assets/evidencias/compatibilidade/CB_INFRACAO_CHROME.png)
* **Atendimento:**
  ![Agendamento de Atendimento no Google Chrome](../assets/evidencias/compatibilidade/CB_ATENDIMENTO_CHROME.png)
* **Protocolo:**
  ![Protocolo no Google Chrome](../assets/evidencias/compatibilidade/CB_PROTOCOLO_CHROME.png)
* **Chatbot (Falha de Carregamento de Asset do Bot):**
  ![Falha de Asset do Chatbot no Google Chrome](../assets/evidencias/compatibilidade/CB_CHATBOT_CHROME.png)
  ![Aba Rede DevTools no Google Chrome](../assets/evidencias/compatibilidade/CB_CHATBOT_CHROME_2.png)

#### Apple Safari (4 de 4 Aprovados)
* **Infração:**
  ![Consulta de Infrações no Apple Safari](../assets/evidencias/compatibilidade/CB_INFRACAO_SAFARI.png)
* **Atendimento:**
  ![Agendamento de Atendimento no Apple Safari](../assets/evidencias/compatibilidade/CB_ATENDIMENTO_SAFARI.png)
* **Protocolo:**
  ![Protocolo no Apple Safari](../assets/evidencias/compatibilidade/CB_PROTOCOLO_SAFARI.png)
* **Chatbot (Assistente Virtual Operacional com IA):**
  ![Chatbot Operacional no Apple Safari](../assets/evidencias/compatibilidade/CB_CHATBOT_SAFARI.png)

---

### 5.2 Evidências dos Ensaios de Responsividade (ICR)

As 20 capturas de tela registradas pela avaliadora Nicole Jovita comprovam o comportamento de layout em cada viewport normatizada:

#### Módulo Infração
* **360px (Mobile Pequeno — Sobreposição do Chatbot sobre botão Consultar):**
  ![Infração 360px](../assets/evidencias/compatibilidade/RESP_INFRACAO_360px.png)
* **414px (Mobile Médio — Sobreposição do Chatbot):**
  ![Infração 414px](../assets/evidencias/compatibilidade/RESP_INFRACAO_414px.png)
* **768px (Tablet — Sobreposição do Chatbot sobre botão Consultar):**
  ![Infração 768px](../assets/evidencias/compatibilidade/RESP_INFRACAO_768px.png)
* **1366px (Desktop HD — Sobreposição do Chatbot sobre card/Voltar):**
  ![Infração 1366px](../assets/evidencias/compatibilidade/RESP_INFRACAO_1366px.png)
* **1920px (Desktop Full HD — Conforme):**
  ![Infração 1920px](../assets/evidencias/compatibilidade/RESP_INFRACAO_1920px.png)

#### Módulo Atendimento (Agendamento)
* **360px (Mobile Pequeno — Sobreposição do Chatbot sobre formulário):**
  ![Atendimento 360px](../assets/evidencias/compatibilidade/RESP_AGENDAMENTO_360px.png)
* **414px (Mobile Médio — Conforme):**
  ![Atendimento 414px](../assets/evidencias/compatibilidade/RESP_AGENDAMENTO_414px.png)
* **768px (Tablet — Conforme):**
  ![Atendimento 768px](../assets/evidencias/compatibilidade/RESP_AGENDAMENTO_768px.png)
* **1366px (Desktop HD — Conforme):**
  ![Atendimento 1366px](../assets/evidencias/compatibilidade/RESP_AGENDAMENTO_1366px.png)
* **1920px (Desktop Full HD — Conforme):**
  ![Atendimento 1920px](../assets/evidencias/compatibilidade/RESP_AGENDAMENTO_1920px.png)

#### Módulo Protocolo
* **360px (Mobile Pequeno — Sobreposição do Chatbot sobre botão Acessar):**
  ![Protocolo 360px](../assets/evidencias/compatibilidade/RESP_PROTOCOLO_360px.png)
* **414px (Mobile Médio — Conforme):**
  ![Protocolo 414px](../assets/evidencias/compatibilidade/RESP_PROTOCOLO_414px.png)
* **768px (Tablet — Conforme):**
  ![Protocolo 768px](../assets/evidencias/compatibilidade/RESP_PROTOCOLO_768px.png)
* **1366px (Desktop HD — Conforme):**
  ![Protocolo 1366px](../assets/evidencias/compatibilidade/RESP_PROTOCOLO_1366px.png)
* **1920px (Desktop Full HD — Conforme):**
  ![Protocolo 1920px](../assets/evidencias/compatibilidade/RESP_PROTOCOLO_1920px.png)

#### Módulo Chatbot
* **360px (Mobile Pequeno — Conforme):**
  ![Chatbot 360px](../assets/evidencias/compatibilidade/RESP_CHATBOT_360px.png)
* **414px (Mobile Médio — Conforme):**
  ![Chatbot 414px](../assets/evidencias/compatibilidade/RESP_CHATBOT_414px.png)
* **768px (Tablet — Conforme):**
  ![Chatbot 768px](../assets/evidencias/compatibilidade/RESP_CHATBOT_768px.png)
* **1366px (Desktop HD — Conforme):**
  ![Chatbot 1366px](../assets/evidencias/compatibilidade/RESP_CHATBOT_1366px.png)
* **1920px (Desktop Full HD — Conforme):**
  ![Chatbot 1920px](../assets/evidencias/compatibilidade/RESP_CHATBOT_1920px.png)

---

### 5.3 Evidências de Interoperabilidade e Tráfego de Rede (TSIS)

* **Monitoramento de Requisições HTTP (DevTools Network Fetch/XHR):**
  ![Tabela de Rede DevTools Fetch/XHR](../assets/evidencias/compatibilidade/NET_DEVTOOLS_NETWORK.png)

* **Registro de Tráfego HTTP Estruturado (Arquivo HAR):**
  Arquivo de auditoria completo salvo no repositório: `docs/assets/evidencias/compatibilidade/NET_INFRACAO_DUD.har` (2,67 MB de requisições, tempos e cabeçalhos capturados).
