# Relatório de Planejamento e Acompanhamento — Ponto de Controle 1 (Entrega 1)

**Disciplina:** Qualidade de Software 1 (FGA0315) — Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 01)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Normas Base:** ISO/IEC 25010 (Modelo de Qualidade) e ISO/IEC 25040 (Processo de Avaliação)  
**Frameworks de Apoio:** GQM (*Goal-Question-Metric*) e PSM/CID (*Practical Software Measurement*)  
**Material de Apresentação:** [Download dos Slides da Apresentação (PDF)](../assets/Qualidade_do_Detran_Digital_Slides.pdf)

---

## 1. Linha do Tempo e Ponto Atual do Projeto (Calendário e Progresso — PSM/CID)

Esta seção formaliza a evolução cronológica do projeto da equipe Kay McNulty, permitindo o acompanhamento visual do estágio atual da equipe, do encadeamento das entregas e da preparação para o **Ponto de Controle 1 (Release E1)**.

### Tabela 1 — Matriz de Marcos, Fases Normativas e Status de Execução

| Marco (Milestone) | Etapa Relativa | Fase da ISO/IEC 25040 | Descrição das Atividades da Equipe | Status Atual |
| :--- | :--- | :--- | :--- | :--- |
| **M0: Setup Inicial e Governança** | Etapa 1 | Concepção e Governança | Definição do grupo, escolha do **Portal Detran Digital DF**, criação do repositório Git, configuração do MkDocs Material, templates de issues e governança de branches. | **CONCLUÍDO** |
| **M1: Requisitos da Avaliação** | Etapa 2 | **Fase 1 (ISO/IEC 25040)** | Definição do propósito da avaliação, mapeamento de stakeholders, delimitação arquitetural dos 4 módulos (**Infração, Atendimento, Protocolo e Chatbot**), justificativa do recorte ISO 25010 (Usabilidade, Compatibilidade e Confiabilidade), cortes metodológicos e alinhamento com ODS 9 (Meta 9.c) e 16 (Meta 16.6). | **CONCLUÍDO** |
| **M2: Especificação da Avaliação** | Etapa 3 | **Fase 2 (ISO/IEC 25040)** | Construção das árvores formais GQM para as três características selecionadas, definição das perguntas técnicas, hipóteses analíticas, métricas operacionais quantitativas e escalas de julgamento. | **CONCLUÍDO (Ponto de Controle 1)** |
| **M3: Projeto da Avaliação** | Etapa 4 | **Fase 3 (ISO/IEC 25040)** | Definição dos métodos de coleta em produção para ambiente governamental (caixa-preta), seleção de ferramentas (Lighthouse, Postman, validadores W3C/e-MAG) e roteiro de inspeção heurística. | **PLANEJADO** |
| **M4: Consolidação e Release E1** | Etapa 5 | **Entrega 1 (GitPage + Artigo v1 + Slides)** | Fechamento da 1ª versão do artigo científico (Fases 1 e 2), auditoria editorial de rubricas (zero emojis, declaração de IA, AG-C1 a AG-C5), preparação dos slides de apresentação e tag Git `v1.0.0-pc1`. | **EM ANDAMENTO (Onde Estamos)** |
| **M5: Execução e Conclusão** | Etapa Final | **Fases 4 e 5 (PC2 / Release E2)** | Coleta empírica de evidências no Portal Detran Digital DF, processamento dos dados brutos, análise de conformidade frente aos limiares e redação do parecer conclusivo na 2ª versão do artigo. | **FUTURO (Entrega 2)** |

*Fonte: Elaborado pelos autores conforme metodologia da disciplina FGA0315.*

---

## 2. Síntese do Planejamento Desenvolvido até o Ponto de Controle 1

### 2.1 Requisitos da Avaliação (Fase 1 ISO/IEC 25040)

* **Contextualização e Propósito:** O Portal Detran Digital DF centraliza serviços críticos para a população do Distrito Federal. A avaliação diagnóstica independente em nível de caixa-preta visa auditar a saúde técnica e a usabilidade do produto em produção real.
* **Módulos Centrais Avaliados:**
    1. **Infração:** Consulta de débitos, autos de infração e emissão de guias DUD/PIX.
    2. **Atendimento:** Agendamento de serviços presenciais e escolha de postos/vagas.
    3. **Protocolo:** Abertura de recursos administrativos e envio digital via SEI-GDF.
    4. **Chatbot:** Assistente virtual inteligente para orientação direta ao condutor/cidadão.
* **Partes Interessadas:** Cidadãos do DF (exigência de interfaces acessíveis e responsivas), Detran-DF e equipes de TI (foco em eficiência, redução de filas presenciais e integração com Gov.br/SEI) e Equipe UnB (auditoria empírica reprodutível e padronizada).
* **Recorte das Características e Métricas (ISO/IEC 25010):**
    * **Usabilidade:** Subcaracterísticas de *Aprendibilidade*, *Operabilidade* e *Proteção contra Erros*. Métricas: $TCAPA$ (Conclusão Autônoma no 1º Acesso), $IEFO$ (Eficiência no Fluxo), $TPRE$ (Prevenção e Recuperação de Erros), Avaliação Heurística de Nielsen e Escala $SUS$.
    * **Compatibilidade:** Subcaracterísticas de *Coexistência* e *Interoperabilidade*. Métricas: $TCBN$ (Compatibilidade Cross-Browser: Chrome, Firefox, Edge, Safari), $ICR$ (Conformidade Responsiva em viewports de 360px a 1920px) e $TSIS$ (Sucesso de Requisições com APIs externas).
    * **Confiabilidade:** Subcaracterísticas de *Disponibilidade*, *Ausência de Falhas*, *Tolerância* e *Recuperação*. Métricas: $TDO$ (Disponibilidade Observada via pings), $TCFF$ (Conclusão sem Falhas), $DFF$ (Densidade de Falhas), $TTOA$ (Operações Anômalas), $TRTI$ (Taxa de Recuperação) e $TMR$ (Tempo Médio de Recuperação).
* **Limites do Escopo (Cortes Metodológicos):**
    * Sem testes de carga massiva ou estresse destrutivo (prevenção contra sobrecarga/DoS em serviço público).
    * Sem inspeção direta de código-fonte backend ou bancos de dados internos (auditoria estritamente caixa-preta).
    * Exclusão de navegadores legados/descontinuados (recorte focado em navegadores modernos e estáveis).
    * Sem testes laboratoriais presenciais massivos com centenas de usuários (adoção de amostragem técnica especializada).
* **Alinhamento aos ODS da ONU:** **ODS 9** (Meta 9.c — Infraestrutura digital pública inclusiva, inovadora e acessível) e **ODS 16** (Meta 16.6 — Instituições governamentais eficazes, transparentes e responsáveis).

---

## 3. Gestão de Recursos, Esforço e Custos (PSM/CID e Critério AG-C5)

A Tabela 2 apresenta a alocação completa de responsabilidades, horas de trabalho dedicadas, valor por hora profissional e custos financeiros acumulados para a Entrega 1, totalizando rigorosamente 100,00% de esforço em conformidade com o **Critério AG-C5**.

### Tabela 2 — Alocação de Recursos, Esforço e Custos Consolidados (PC1)

| Integrante | Papel Principal na Equipe | Responsabilidades e Tarefas no Ponto de Controle 1 | Horas (h) | Valor / Hora (R$) | Custo Total (R$) | % de Esforço (AG-C5) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Artur Fernandes Galdino**<br>Matrícula: `241010923` | Analista de Compatibilidade / Mapeamento de Arquitetura e Escopo | Mapeamento dos módulos de Infração, Atendimento, Protocolo e Chatbot (Issue #01); especificação GQM e métricas de Compatibilidade ($TCBN$, $ICR$, $TSIS$) (Issues #03 e #04); escopo e propósito (Issues #05 e #07). | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **Nicole Jovita Fernandes**<br>Matrícula: `241012347` | Analista de Requisitos / Stakeholders, Modelo ISO 25010 e ODS | Justificativa de Compatibilidade cross-browser/mobile (Issue #02); mapeamento de stakeholders (Issue #05); adaptação do modelo ISO 25010 (Issue #06); alinhamento aos ODS 9 (Meta 9.c) e 16 (Meta 16.6) (Issue #08). | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **Davi Ursolino de Oliveira**<br>Matrícula: `241012202` | Analista de Confiabilidade / Especificação GQM e Métricas | Especificação GQM de Confiabilidade (Issue #10); métricas quantitativas ($TDO$, $TCFF$, $DFF$, $TTOA$, $TRTI$, $TMR$) e réguas de pontuação (Issue #11); diagramação Mermaid e fórmulas MathJax (Issues #12 e #13). | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **João Eduardo Pereira Rabelo**<br>Matrícula: `180053299` | Analista de Confiabilidade / Metodologia e Métricas PSM | Fundamentação de Confiabilidade em serviços transacionais (Issue #09); metodologia ISO 25040; métricas PSM/CID de processos e calendário; auditoria de governança e atas. | 12h | R$ 50,00 | R$ 600,00 | **16,66%** |
| **Natan José França**<br>Matrícula: `241011537` | Analista de Usabilidade / Diagrama GQM e Níveis de Julgamento | Justificativa de Usabilidade (Issue #14); modelo GQM e hipóteses nos 4 módulos (Issue #15); escalas de julgamento das métricas $TCAPA$, $IEFO$ e $TPRE$ (Issue #16); diagrama GQM e artigo (Issue #17). | 12h | R$ 50,00 | R$ 600,00 | **16,66%** |
| **Yan Santos Rodrigues**<br>Matrícula: `241025480` | Analista de Usabilidade / Especificação Operacional e Heurísticas | Análise ergonômica e perfil de condutores do DF (Issue #14); procedimentos operacionais para Heurísticas de Nielsen e questionário $SUS$ (Issue #15); métricas quantitativas de usabilidade (Issue #16); documentação MkDocs (Issue #17). | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **TOTAL CONSOLIDADO** | — | **Entregáveis Fases 1 e 2 Consolidados — Ponto de Controle 1** | **72h** | Média: R$ 50,00/h | **R$ 3.600,00** | **100%** |

*Fonte: Elaborado pelos autores conforme diretrizes da disciplina FGA0315 e modelo PSM/CID.*

---

## 4. Estrutura e Roteiro Oficial dos Slides de Apresentação (Ponto de Controle 1)

A apresentação oficial da equipe Kay McNulty para a banca docente foi sintetizada em **10 slides estratégicos**, orientados a evidências de processo, rastreabilidade e métricas de qualidade:

| Slide | Tópico do Slide | Conteúdo Apresentado e Evidências Técnicas |
| :---: | :--- | :--- |
| **Slide 1** | **Capa e Identificação** | Título (*Avaliação da Qualidade do Portal Detran Digital DF — Aplicação das Normas ISO/IEC 25040, ISO/IEC 25010 e Metodologia GQM*), equipe avaliadora completa (Artur Galdino, Davi Ursolino, João Rabelo, Natan França, Nicole Jovita e Yan Santos), disciplina Qualidade de Software 1 e Profa. Dra. Cristiane Soares Ramos. |
| **Slide 2** | **Objeto de Estudo (Módulos Principais)** | Apresentação do Portal Detran Digital DF e delimitação dos quatro módulos prioritários: **Infração** (consulta de débitos, autos e guias DUD/PIX), **Atendimento** (agendamento presencial e escolha de postos), **Protocolo** (recursos administrativos via SEI-GDF) e **Chatbot** (orientação virtual). |
| **Slide 3** | **Fundamentação Teórica** | Alinhamento do arcabouço metodológico: **ISO/IEC 25040** (SQuaRE — ciclo em 5 fases, foco nas Fases 1 e 2), **ISO/IEC 25010:2023** (Modelo de Qualidade de Produto), **GQM** (Desdobramento Objetivo $\rightarrow$ Questão $\rightarrow$ Métrica) e **PSM/CID** (Governança de esforço, progresso e custos da equipe). |
| **Slide 4** | **Requisitos da Avaliação & Partes Interessadas** | Caracterização da auditoria caixa-preta em produção real e mapeamento dos três grupos de partes interessadas: **Cidadãos do DF** (exigência de interfaces responsivas e acessíveis), **Detran-DF e TI** (eficiência, mitigação de filas e integração Gov.br/SEI) e **Equipe UnB** (auditoria empírica reprodutível). |
| **Slide 5** | **GQM: Usabilidade** | Foco na eficiência e na segurança da experiência do usuário. Subcaracterísticas: Aprendibilidade, Operabilidade e Proteção contra Erros. Métricas principais: $TCAPA$ (Conclusão Autônoma no 1º Acesso), $IEFO$ (Eficiência no Fluxo de Cliques), $TPRE$ (Prevenção e Recuperação de Erros de Entrada), Avaliação Heurística de Nielsen e Escala $SUS$. |
| **Slide 6** | **GQM: Compatibilidade** | Avaliação da capacidade de operar em diferentes ambientes e dispositivos. Subcaracterísticas: Coexistência e Interoperabilidade (web e mobile). Métricas principais: $TCBN$ (Compatibilidade Cross-Browser: Chrome, Firefox, Edge, Safari), $ICR$ (Conformidade Responsiva de 360px a 1920px) e $TSIS$ (Taxa de Sucesso em Requisições HTTP com APIs externas). |
| **Slide 7** | **GQM: Confiabilidade** | Foco na estabilidade e na capacidade de recuperação do portal. Subcaracterísticas: Disponibilidade, Ausência de Falhas, Tolerância e Recuperação. Métricas principais: $TDO$ (Disponibilidade Observada via pings), $TCFF$ (Conclusão sem Falhas), $DFF$ (Densidade de Falhas), $TTOA$ (Operações Anômalas), $TRTI$ (Taxa de Recuperação) e $TMR$ (Tempo Médio de Recuperação). |
| **Slide 8** | **Limites do Escopo (Cortes Metodológicos)** | Transparência do que fica de fora da avaliação: sem testes de carga massiva/estresse (prevenção contra indisponibilidade/DoS), sem inspeção interna de código ou bancos de dados (avaliação estritamente caixa-preta), exclusão de navegadores obsoletos e substituição de testes massivos em laboratório UX por amostragem técnica qualificada. |
| **Slide 9** | **Régua de Decisão & Impacto Social (ODS)** | Apresentação da Régua de Avaliação de 4 níveis (Excelente, Bom, Satisfatório e Insuficiente) e conexão com os Objetivos de Desenvolvimento Sustentável da ONU: **ODS 9 (Meta 9.c)** — infraestrutura digital pública inclusiva e acessível; e **ODS 16 (Meta 16.6)** — instituições governamentais eficazes, transparentes e responsáveis. |
| **Slide 10** | **Conclusão e Próximos Passos** | Demonstração do ciclo de vida da ISO/IEC 25040: destaque para as fases concluídas no PC1 (Fase 1: Requisitos de Avaliação; e Fase 2: Especificação GQM/PSM) e encadeamento das próximas etapas (Fase 3: Desenho do Plano e Ambientes de Teste; Fase 4: Execução das Medições em Campo; e Fase 5: Conclusão e Relatório Diagnóstico). |

---
