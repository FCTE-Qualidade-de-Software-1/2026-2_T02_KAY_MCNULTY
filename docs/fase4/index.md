# Execução, Julgamento e Ações de Melhoria (Fase 4 – ISO/IEC 25040)

**Disciplina:** Qualidade de Software 1 (FGA0315) – Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 02)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Norma Base:** ABNT NBR ISO/IEC 25040:2011 (Processo de Avaliação de Produto de Software, Seção 6.4 – *Execute the evaluation* e Seção 6.5 – *Conclude the evaluation*)  
**Marcos de Referência:** Marco M5 (*Resultados Empíricos, Julgamento e Propostas de Melhoria*)

---

## 1. Visão Geral da Fase de Execução e Julgamento

A Fase 4 da norma ISO/IEC 25040 consolida a materialização prática do processo de avaliação da qualidade de software. Neste estágio, a equipe executa integralmente os planos e roteiros operacionais projetados na [Fase 3](../fase3/index.md), coleta e audita os dados brutos empíricos observados em produção, calcula as medidas derivadas e aplica as réguas de pontuação e critérios de julgamento estabelecidos na [Fase 2](../fase2/index.md).

Adicionalmente, em consonância com as boas práticas de engenharia de software e os requisitos da disciplina, a Fase 4 abrange o desenvolvimento e a validação de **Ações Práticas de Melhoria Técnica**, intervindo pontualmente sobre os problemas diagnósticos mais severos identificados nas características avaliadas.

---

## 2. Estrutura da Documentação e Atribuições

Os resultados empíricos, análises diagnósticas e intervenções práticas organizam-se nas seguintes seções:

| Dimensão da Avaliação | Subcaracterísticas e Escopo | Responsáveis Técnicos | Página de Resultados |
| :--- | :--- | :--- | :---: |
| **Compatibilidade** | Resultados empíricos de Coexistência (Cross-Browser e Responsividade) e Interoperabilidade | Artur Fernandes Galdino e Nicole Jovita Fernandes | [Acessar Resultados](../fase4/compatibilidade.md) |
| **Capacidade de Interação** | Resultados da Inspeção Heurística, Desempenho Operacional e Escore SUS | Natan França e Yan | [Acessar Resultados](../fase4/usabilidade.md) |
| **Confiabilidade** | Resultados da Janela de Disponibilidade, Falhas em Fluxos e Tolerância a Anomalias | Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo | [Acessar Resultados](../fase4/confiabilidade.md) |
| **Ações de Melhoria** | Especificação, implementação e verificação da ação técnica de melhoria obrigatória | Toda a Equipe Kay McNulty | [Acessar Ações de Melhoria](../fase4/melhorias.md) |

**Tabela 1 – Organização da documentação da Fase 4.** Fonte: Elaborado pelos autores.

---

## 3. Fluxo de Agregação e Julgamento Final

Para produzir o parecer conclusivo sobre a qualidade do Portal Detran Digital DF, os resultados brutos percorrem o seguinte pipeline analítico:

1. **Compilação e Auditoria dos Dados Brutos:** Registro em tabelas e arquivos rastreáveis das observações de campo, gravações de ensaios e medições automatizadas.
2. **Cálculo das Medidas Derivadas:** Aplicação estrita das equações matemáticas definidas na Fase 2 para cada métrica operacional.
3. **Classificação pelos Níveis de Pontuação:** Enquadramento de cada indicador nos limiares formais (Excelente, Bom, Regular/Satisfatório ou Insuficiente).
4. **Resposta às Questões GQM e Confronto de Hipóteses:** Análise técnica qualitativa e quantitativa que confirma ou refuta as hipóteses formuladas no planejamento.
5. **Síntese de Conformidade Global:** Agregação ponderada dos resultados das características para direcionamento do relatório técnico conclusivo e do artigo científico.
