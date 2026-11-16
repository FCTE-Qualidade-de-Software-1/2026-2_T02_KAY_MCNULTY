# Relatório de Planejamento e Acompanhamento — Ponto de Controle 2 (Entrega 2)

**Disciplina:** Qualidade de Software 1 (FGA0315) — Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 02)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Normas Base:** ISO/IEC 25010:2023 (Modelo de Qualidade) e ISO/IEC 25040:2011 (Processo de Avaliação)  
**Frameworks de Apoio:** GQM (*Goal-Question-Metric*) e PSM/CID (*Practical Software Measurement*)  
**Data do Ponto de Controle 2:** 16/11/2026

---

## 1. Linha do Tempo e Ponto Atual do Projeto (Calendário e Progresso — PSM/CID)

Este relatório formaliza o progresso cronológico e técnico da equipe Kay McNulty na transição entre o primeiro ciclo avaliativo e o **Ponto de Controle 2 (PC2)**, cobrindo o encadeamento dos marcos operacionais da ISO/IEC 25040 e a governança via métricas PSM.

### Tabela 1 — Matriz de Marcos, Fases Normativas e Status de Execução

| Marco (Milestone) | Etapa Relativa | Fase da ISO/IEC 25040 | Descrição das Atividades da Equipe | Status Atual |
| :--- | :--- | :--- | :--- | :--- |
| **M0: Setup Inicial e Governança** | Etapa 1 | Concepção e Governança | Definição do grupo, escolha do Portal Detran Digital DF, repositório Git, configuração do MkDocs Material, templates de issues e governança de branches. | **CONCLUÍDO (12/10)** |
| **M1: Requisitos da Avaliação** | Etapa 2 | **Fase 1 (ISO/IEC 25040)** | Propósito da avaliação, mapeamento de stakeholders, delimitação arquitetural dos 4 módulos (Infração, Atendimento, Protocolo, Chatbot), modelo ISO 25010 e alinhamento aos ODS 9 e 16. | **CONCLUÍDO (18/10)** |
| **M2: Especificação da Avaliação** | Etapa 3 | **Fase 2 (ISO/IEC 25040)** | Construção das árvores formais GQM para Compatibilidade, Capacidade de Interação e Confiabilidade, formulação de hipóteses, métricas quantitativas e escalas de pontuação. | **CONCLUÍDO (21/10)** |
| **M3: Consolidação e Release E1** | Etapa 4 | **Entrega 1 (PC1)** | Fechamento da 1ª versão do artigo científico (Fases 1 e 2), auditoria editorial de rubricas, apresentação e publicação da tag `v1.0.0-pc1`. | **CONCLUÍDO (26/10)** |
| **M4: Projeto da Avaliação** | Etapa 5 | **Fase 3 (ISO/IEC 25040)** | Elaboração dos planos operacionais e roteiros reproduzíveis de teste para Compatibilidade, Capacidade de Interação e Confiabilidade, definição do ferramental e setup de ambientes. | **CONCLUÍDO / EM VALIDAÇÃO (15/11)** |
| **M5: Execução, Julgamento e Melhorias** | Etapa Final | **Fase 4 (PC2 / Release Final)** | Execução empírica das coletas em produção, compilação de dados brutos, cálculo das métricas, validação de hipóteses, ação prática de melhoria e versão final do artigo. | **EM ANDAMENTO (16/11 a 22/11)** |

*Fonte: Elaborado pelos autores conforme metodologia da disciplina FGA0315.*

---

## 2. Síntese do Progresso por Característica de Qualidade

### 2.1 Compatibilidade (Coexistência e Interoperabilidade)
* **Responsáveis:** Artur Fernandes Galdino e Nicole Jovita Fernandes.
* **Avanço na Fase 3:** Elaboração do plano detalhado contemplando a matriz de testes *cross-browser* (Chrome, Firefox, Edge, Safari), a verificação responsiva nas 5 viewports críticas (360px a 1920px) e os pontos de verificação de cabeçalhos e payloads HTTP nos fluxos de integração com Gov.br, SEI-GDF e emissão de DUD bancário.
* **Avanço na Fase 4:** Estruturação dos modelos de dados para tabulação dos índices $TCBN$, $ICR$ e $TSIS$.

### 2.2 Capacidade de Interação (Aprendibilidade, Operabilidade e Proteção contra Erros)
* **Responsáveis:** Natan França e Yan.
* **Avanço na Fase 3:** Especificação do roteiro de tarefas guiadas nos 4 módulos do portal, definição da matriz de severidade das 10 Heurísticas de Nielsen e planejamento da coleta do formulário *System Usability Scale* (SUS).
* **Avanço na Fase 4:** Modelagem dos templates de consolidação de dados para cálculo de $TCAPA$, $IEFO$, $TPRE$ e escore global SUS.

### 2.3 Confiabilidade (Disponibilidade, Tolerância e Recuperabilidade)
* **Responsáveis:** Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo.
* **Avanço na Fase 3:** Plano de avaliação homologado com piloto do script de monitoramento automatizado da métrica $TDO$ (verificações a cada 15 min), catálogo de 10 cenários anômalos ($TTOA$) e cenários de interrupção forçada ($TRTI$/$TMR$).
* **Avanço na Fase 4:** Coleta de dados brutos iniciada na janela de observação em produção e preparação dos scripts de consolidação analítica.

---

## 3. Gestão de Recursos, Esforço e Custos (PSM/CID)

Mantendo a coerência com a metodologia estabelecida na Entrega 1, os custos são estimados a partir da taxa horária de **R$ 87,55/h** (calculada com base no custo médio anual por estudante universitário federal de R$ 52.533,00 para uma carga de 600h anuais).

### Tabela 2 — Alocação de Recursos, Esforço e Custos para a Entrega 2

| Integrante | Papel Principal | Foco de Atuação no Ponto de Controle 2 | Horas Estimadas (h) | Taxa Horária (R$) | Custo Total Estimado (R$) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Artur Fernandes Galdino** | Analista de Compatibilidade / Arquitetura MkDocs | Reorganização da arquitetura do MkDocs, roteiro de testes de Compatibilidade e execução cross-browser/responsividade. | 8,0h | R$ 87,55 | R$ 700,40 |
| **Nicole Jovita Fernandes** | Analista de Compatibilidade / Rastreabilidade | Rastreabilidade Fase 2 para Fase 3, testes de interoperabilidade HTTP/APIs e consolidação de evidências. | 7,0h | R$ 87,55 | R$ 612,85 |
| **Davi Ursolino de Oliveira** | Analista de Confiabilidade / Automação | Execução dos ensaios de anomalias/recuperação, suporte ao monitoramento e ação prática de melhoria. | 7,5h | R$ 87,55 | R$ 656,63 |
| **João Eduardo Pereira Rabelo** | Analista de Confiabilidade / PSM e Governança | Operação do monitor de disponibilidade (M1), métricas de processos PSM, governança de branches e atas. | 7,0h | R$ 87,55 | R$ 612,85 |
| **Natan França** | Analista de Capacidade de Interação / Avaliação Heurística | Roteiro de tarefas, condução das inspeções de capacidade de interação e consolidação de violações heurísticas. | 7,0h | R$ 87,55 | R$ 612,85 |
| **Yan** | Analista de Capacidade de Interação / Métricas de Desempenho | Tabulação dos tempos de tarefa (IEFO), apuração de erros de usuário e processamento do escore SUS. | 7,0h | R$ 87,55 | R$ 612,85 |
| **Total Consolidado** | **Equipe Kay McNulty** | **Planejamento, Execução e Preparação do PC2** | **43,5h** | **R$ 87,55** | **R$ 3.808,43** |

*Fonte: Elaborado pelos autores.*

---

## 4. Rastreabilidade com as Issues e Commits do Repositório

Todas as tarefas do Marco M4 e do início do Marco M5 estão vinculadas a issues no GitHub, com branches específicas e mensagens de commit padronizadas segundo a especificação *Conventional Commits*:

* **Issue de Arquitetura e Estruturação de Páginas:** Criação dos diretórios `docs/fase3/`, `docs/fase4/` e `docs/entregas/entrega2.md`, organização da navegação hierárquica no `mkdocs.yml` e validação do build sem quebras de link.
* **Issues de Roteiros e Execução Técnica:** Acompanhamento independente por cada dupla com rastreabilidade direta nas atas de reunião e no painel PSM.

---

## 5. Verificação de Conformidade Editorial e Metodológica

* [x] **Zero Emojis e Ícones:** Textos, títulos e tabelas utilizam exclusivamente tipografia padrão e notação técnica, sem emojis ou caracteres pictográficos informais.
* [x] **Títulos Sem Nomenclatura Avaliativa:** Todas as seções adotam títulos conceituais de engenharia de software e da norma ISO/IEC 25040, sem transcrever códigos de critérios de avaliação nos cabeçalhos.
* [x] **Declaração de Uso de Ferramentas de IA:** Conforme a política da disciplina, ferramentas de assistência foram empregadas exclusivamente para revisão estilística, estruturação sintática de tabelas e automação de scripts de métricas, com conferência manual integral pelos autores.
* [x] **Integridade Estrutural do MkDocs:** Todos os links internos foram validados e o site compila sem qualquer aviso de referência órfã ou quebrada.
