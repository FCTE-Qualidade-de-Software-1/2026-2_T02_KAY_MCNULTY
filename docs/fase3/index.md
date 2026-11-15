# Projeto da Avaliação (Fase 3 – ISO/IEC 25040)

**Disciplina:** Qualidade de Software 1 (FGA0315) – Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 02)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Norma Base:** ABNT NBR ISO/IEC 25040:2011 (Processo de Avaliação de Produto de Software, Seção 6.3 – *Design the evaluation*)  
**Marcos de Referência:** Marco M4 (*Plano de Avaliação e Metodologia Operacional*)

---

## 1. Visão Geral da Fase de Projeto da Avaliação

A Fase 3 da norma ISO/IEC 25040 tem como objetivo transformar as especificações conceituais e métricas abstratas definidas na [Fase 2](../fase2/index.md) em um **Plano de Avaliação Operacional**. Neste estágio, estabelecem-se os procedimentos detalhados de medição, a seleção e configuração de ferramentas de suporte, a delimitação de ambientes operacionais e o cronograma para execução em produção real.

A abordagem adotada pela equipe Kay McNulty é estritamente de **auditoria diagnóstica externa em nível de caixa-preta**, observando o comportamento empírico do Portal Detran Digital DF nos quatro módulos centrais de escopo: **Infração**, **Atendimento**, **Protocolo** e **Chatbot**. Nenhuma atividade avaliativa realiza intervenções destrutivas, estresse de infraestrutura ou testes de carga não autorizados, preservando a estabilidade dos serviços públicos e a privacidade dos cidadãos.

---

## 2. Atribuição das Características e Responsáveis

Para assegurar profundidade técnica, rigor estatístico e rastreabilidade metodológica, o plano de avaliação foi particionado entre as duplas da equipe, contemplando as três características de qualidade selecionadas no modelo da ISO/IEC 25010:

| Característica Avaliada | Subcaracterísticas Focadas | Responsáveis Técnicos | Documento Operacional |
| :--- | :--- | :--- | :---: |
| **Compatibilidade** | Coexistência (*Cross-browser* e Responsividade) e Interoperabilidade | Artur Fernandes Galdino e Nicole Jovita Fernandes | [Acessar Plano](../fase3/compatibilidade.md) |
| **Usabilidade** | Aprendibilidade, Operabilidade e Proteção contra Erros de Usuário | Natan França e Yan | [Acessar Plano](../fase3/usabilidade.md) |
| **Confiabilidade** | Disponibilidade, Ausência de Falhas, Tolerância a Falhas e Recuperabilidade | Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo | [Acessar Plano](../fase3/confiabilidade.md) |

**Tabela 1 – Matriz de atribuição de características na Fase 3.** Fonte: Elaborado pelos autores.

---

## 3. Diretrizes Metodológicas Gerais do Plano

O planejamento operacional estabelecido para as medições da Fase 3 orienta-se pelos seguintes princípios:

1. **Reprodutibilidade dos Procedimentos:** Todos os roteiros contêm passos detalhados de pré-condição, execução, inspeção e pós-condição, permitindo que qualquer membro da equipe ou auditor externo replique as aferições.
2. **Coleta Padronizada de Evidências:** Cada verificação requer registro de evidência verificável (telas gravadas, capturas de tela com timestamp legível, logs da aba *Network* das ferramentas de desenvolvimento ou saídas de consoles de automação).
3. **Mapeamento Direto com a Fase 2 (GQM):** Toda métrica executada possui correspondência unívoca com as medidas básicas, fórmulas e níveis de pontuação aprovados na especificação formal.
4. **Isolamento de Interferências Externas:** Fatores fora do controle do portal (tais como instabilidades do Gov.br, SEI-GDF ou variações em conexões residenciais de rede) são explicitamente monitorados e catalogados para prevenir distorções nos dados brutos.

---

## 4. Ferramental e Instrumentos de Apoio

As coletas empíricas utilizam ferramentas padronizadas para cada modalidade de inspeção:

* **Inspeção Cross-Browser e Responsividade:** Navegadores estáveis em suas versões de produção (Google Chrome, Mozilla Firefox, Microsoft Edge e Apple Safari via WebKit), associados às ferramentas integradas do *DevTools* (emulação de viewports móveis de 360px a 1920px).
* **Monitoramento Automatizado de Disponibilidade:** Scripts baseados em Playwright e Python executados periodicamente a partir de ambientes controlados.
* **Inspeção de Rede e Interoperabilidade:** Monitoramento dos cabeçalhos HTTP, códigos de resposta (status 2xx, 3xx, 4xx, 5xx) e tempos de resposta via aba *Rede (Network)* do navegador e Postman.
* **Avaliação Heurística e Percepção do Usuário:** Formulários estruturados de severidade com base nas 10 Heurísticas de Nielsen e questionários padronizados *System Usability Scale* (SUS).

---

## 5. Cronograma Integrado do Marco M4

| Data / Período | Atividade Metodológica | Envolvidos | Entrega Associada |
| :--- | :--- | :--- | :---: |
| 10/11 a 12/11 | Definição da metodologia operacional e elaboração dos roteiros iniciais | Todas as duplas | Estrutura Fase 3 |
| 13/11 a 15/11 | Homologação dos roteiros técnicos, pilotos de coleta e calibração de ferramentas | Duplas específicas | Planos detalhados |
| 15/11 a 16/11 | Integração na GitPage, verificação de links e consolidação do Marco M4 | Equipe Kay McNulty | Ponto de Controle 2 |
| 16/11 a 20/11 | Execução sistemática dos roteiros e consolidação dos dados brutos | Todas as duplas | Início da Fase 4 |

**Tabela 2 – Cronograma operacional integrado do Marco M4.** Fonte: Elaborado pelos autores.
