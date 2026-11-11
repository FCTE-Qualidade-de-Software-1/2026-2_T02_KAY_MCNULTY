# Atas de Reunião da Equipe Kay McNulty

**Disciplina:** Qualidade de Software 1 (FGA0315) — UnB / FCTE  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 01)  
**Objeto de Avaliação:** Portal Detran Digital DF  
**Referência Normativa:** ISO/IEC 25040 e ISO/IEC 25010  

Registro cronológico e formal das reuniões deliberativas e técnicas da equipe Kay McNulty, documentando decisões de arquitetura, governança, divisão de esforço e marcos do processo de avaliação em estrita observância à Premissa 4 das diretrizes institucionais. Todas as reuniões da equipe são realizadas presencialmente no Campus UnB Gama (FCTE), imediatamente após o término da aula presencial da disciplina (segundas e quartas-feiras, das 10h às 12h).

---

## Reunião 1 — Concepção do Projeto, Escolha do Objeto e Formação das Duplas

* **Data e Horário:** 07/10/2026 (Quarta-feira), 12h00 – 13h00
* **Local:** Presencial — Campus UnB Gama (FCTE), Sala de aula (logo após a aula de Qualidade de Software 1, 10h – 12h)
* **Participantes Presentes:**
    * Artur Fernandes Galdino
    * Nicole Jovita Fernandes
    * Davi Ursolino de Oliveira
    * João Eduardo Pereira Rabelo
    * Natan José França
    * Yan Santos Rodrigues
* **Pauta:**
    1. Definição do software público objeto de avaliação da disciplina.
    2. Estruturação do modelo de governança e divisão de trabalho em regime de duplas técnicas.
    3. Escolha das características preliminares de qualidade da norma ISO/IEC 25010.
* **Decisões Registradas:**
    * **Objeto de Avaliação Aprovado por Unanimidade:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home)), em função de sua relevância social e abrangência para cidadãos e condutores do DF.
    * **Divisão de Duplas por Características Técnicas:**
        * **Dupla 1 (Compatibilidade e Arquitetura):** Artur Fernandes Galdino e Nicole Jovita Fernandes.
        * **Dupla 2 (Confiabilidade e Governança PSM):** Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo.
        * **Dupla 3 (Usabilidade e Interação Humano-Computador):** Natan José França e Yan Santos Rodrigues.
    * **Infraestrutura:** Adoção de repositório Git sob a organização oficial da disciplina, documentação estática via MkDocs Material e automação contínua via GitHub Actions.
* **Ações e Próximos Passos:**
    * Configuração inicial do repositório Git, `mkdocs.yml` e fluxo de branches (Issue #01).
    * Levantamento arquitetural preliminar dos módulos do Detran Digital.

---

## Reunião 2 — Delimitação de Escopo (Fase 1) e Alinhamento aos ODS

* **Data e Horário:** 14/10/2026 (Quarta-feira), 12h00 – 13h15
* **Local:** Presencial — Campus UnB Gama (FCTE), Sala de aula (logo após a aula de Qualidade de Software 1, 10h – 12h)
* **Participantes Presentes:**
    * Artur Fernandes Galdino
    * Nicole Jovita Fernandes
    * Davi Ursolino de Oliveira
    * João Eduardo Pereira Rabelo
    * Natan José França
    * Yan Santos Rodrigues
* **Pauta:**
    1. Delimitação dos 4 módulos funcionais centrais a serem avaliados.
    2. Mapeamento formal de partes interessadas (stakeholders).
    3. Fixação dos cortes metodológicos e limites éticos da avaliação em caixa-preta.
    4. Conexão com os Objetivos de Desenvolvimento Sustentável (ODS) da ONU.
* **Decisões Registradas:**
    * **Módulos Delimitados:** Infração (consulta/emissão), Atendimento (agendamento), Protocolo (recursos via SEI) e Chatbot (orientação virtual).
    * **Cortes Metodológicos:** Foco exclusivo em auditoria de caixa-preta externa em produção, sem testes destrutivos de estresse/DoS e sem acesso ao backend proprietário ou bases relacionais.
    * **Alinhamento ODS:** Adoção do ODS 9 (Meta 9.c — universalização do acesso a TIC de qualidade) e ODS 16 (Meta 16.6 — desenvolvimento de instituições eficazes, responsáveis e transparentes).
    * **Características Selecionadas:** Três características da ISO/IEC 25010: Usabilidade (ênfase em inclusão e proteção contra erros), Compatibilidade (cross-browser e responsividade) e Confiabilidade (disponibilidade e tolerância a falhas).
* **Ações e Próximos Passos:**
    * Redação dos arquivos da Fase 1 (`fase1/`): `proposito-stakeholders.md`, `arquitetura-modulos.md`, `modelo-qualidade.md`, `escopo-limites.md` e `ods.md`.

---

## Reunião 3 — Especificação Formal GQM e Governança PSM/CID (Fase 2)

* **Data e Horário:** 19/10/2026 (Segunda-feira), 12h00 – 13h20
* **Local:** Presencial — Campus UnB Gama (FCTE), Sala de aula (logo após a aula de Qualidade de Software 1, 10h – 12h)
* **Participantes Presentes:**
    * Artur Fernandes Galdino
    * Nicole Jovita Fernandes
    * Davi Ursolino de Oliveira
    * João Eduardo Pereira Rabelo
    * Natan José França
    * Yan Santos Rodrigues
* **Pauta:**
    1. Estruturação das árvores de decisão GQM (Goal-Question-Metric) por característica.
    2. Validação matemática das fórmulas de medição e definição das escalas de julgamento de 4 níveis.
    3. Implantação do modelo PSM/CID de governança de esforço e custos.
* **Decisões Registradas:**
    * **Árvores GQM Homologadas:**
        * Compatibilidade: foco em coexistência cross-browser/mobile ($TCBN$, $ICR$) e interoperabilidade de serviços ($TSIS$).
        * Usabilidade: foco em aprendibilidade e prevenção de erros ($TCAPA$, $IEFO$, $TPRE$), inspeção heurística de Nielsen e escala SUS.
        * Confiabilidade: foco em disponibilidade de serviço e tolerância ($TDO$, $TCFF$, $DFF$, $TTOA$, $TRTI$, $TMR$).
    * **Régua de Avaliação Padronizada:** Adoção da escala homogênea de quatro níveis (Excelente, Bom, Satisfatório e Insuficiente) para todas as métricas.
    * **Governança PSM/CID:** Fixação do valor profissional de referência em R$ 50,00/h e acompanhamento das três dimensões (Processos, Calendário e Recursos) com catálogo rastreável de issues.
* **Ações e Próximos Passos:**
    * Documentação da Fase 2 (`fase2/`): `compatibilidade.md`, `usabilidade.md`, `confiabilidade.md` e diagramas Mermaid.
    * Criação do script de automação de métricas `update_metrics.py`.

---

## Reunião 4 — Consolidação da Entrega 1, Artigo v1 e Validação de Rubricas

* **Data e Horário:** 26/10/2026 (Segunda-feira), 12h00 – 13h10
* **Local:** Presencial — Campus UnB Gama (FCTE), Sala de aula (logo após a aula de Qualidade de Software 1, 10h – 12h)
* **Participantes Presentes:**
    * Artur Fernandes Galdino
    * Nicole Jovita Fernandes
    * Davi Ursolino de Oliveira
    * João Eduardo Pereira Rabelo
    * Natan José França
    * Yan Santos Rodrigues
* **Pauta:**
    1. Revisão final da 1ª versão do artigo científico em LaTeX.
    2. Auditoria de conformidade das rubricas editoriais institucionais (AG-C1 a AG-C5).
    3. Fechamento dos slides de apresentação do Ponto de Controle 1.
    4. Homologação da Release E1 (`v1.0.0-pc1`).
* **Decisões Registradas:**
    * **Artigo Científico v1:** Texto final aprovado com 7 páginas, contendo introdução, fundamentação, metodologia, Fases 1 e 2, apêndice com Tabela de Contribuição de 100% de esforço e declaração explícita de uso de IA.
    * **Auditoria de Rubricas:** Verificação de rigor estilístico: zero emojis no corpo do texto, figuras e tabelas com legendas e fontes, e sumário funcional.
    * **Slides da Apresentação:** Estruturação em 10 slides estratégicos conforme detalhado na página de Entrega 1.
* **Ações e Próximos Passos:**
    * Submissão do PDF do artigo no ambiente Moodle (26/10/2026).
    * Apresentação do Ponto de Controle 1 perante a banca docente.

---

## Reunião 5 — Retrospectiva do PC1 e Planejamento da Entrega 2 (Fases 3 e 4)

* **Data e Horário:** 04/11/2026 (Quarta-feira), 12h00 – 13h15
* **Local:** Presencial — Campus UnB Gama (FCTE), Sala de Aula (logo após a aula de Qualidade de Software 1, 10h – 12h)
* **Participantes Presentes:**
    * Artur Fernandes Galdino
    * Nicole Jovita Fernandes
    * Davi Ursolino de Oliveira
    * João Eduardo Pereira Rabelo
    * Natan José França
    * Yan Santos Rodrigues
* **Pauta:**
    1. Retrospectiva dos feedbacks recebidos no Ponto de Controle 1.
    2. Planejamento da Fase 3 (Projeto da Avaliação) e especificação dos ambientes de teste.
    3. Cronograma para a apresentação das métricas PSM (11/11) e Ponto de Controle 2 (16/11 ou 18/11).
    4. Identificação preliminar de oportunidades para a ação técnica de melhoria obrigatória da Fase 4.
* **Decisões Registradas:**
    * **Planejamento de Testes (Fase 3):** Roteiros de coleta por amostragem em navegadores modernos, testes de viewports responsivas (360px a 1920px) e monitoramento de disponibilidade de endpoints públicos.
    * **Ação de Melhoria Técnica (Fase 4):** A equipe avaliará, a partir dos dados coletados, se a intervenção será um protótipo de alta fidelidade para correção de problemas de navegação/usabilidade ou proposição técnica de templates/processos.
    * **Governança de Issues:** Padronização das issues da Entrega 2 com campos obrigatórios de esforço e critérios de aceitação.
* **Ações e Próximos Passos:**
    * Elaboração dos roteiros operacionais de teste da Fase 3.
    * Atualização do painel e cronograma do PSM.
