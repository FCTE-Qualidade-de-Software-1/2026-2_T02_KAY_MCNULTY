# Avaliação da Qualidade do Portal Detran Digital DF

[![Norma ISO/IEC 25010](https://img.shields.io/badge/Norma-ISO%2FIEC%2025010-blue.svg)](https://www.iso.org/standard/78176.html)
[![Norma ISO/IEC 25040](https://img.shields.io/badge/Processo-ISO%2FIEC%2025040-green.svg)](https://www.iso.org/standard/83642.html)
[![Metodologia GQM](https://img.shields.io/badge/Metodologia-GQM%20v2.0-orange.svg)](fase2/index.md)
[![Gestão PSM/CID](https://img.shields.io/badge/Gestão-PSM%2FCID-purple.svg)](gestao/metricas-psm.md)
[![Status da Release](https://img.shields.io/badge/Release-E1%20(v1.0.0--pc1)-brightgreen.svg)](entregas/entrega1.md)

Documentação oficial da avaliação de qualidade de produto de software desenvolvida na disciplina **Qualidade de Software 1 (FGA0315)** da Universidade de Brasília (UnB / FCTE), ministrada pela Profa. Dra. Cristiane Soares Ramos.

O projeto tem por objetivo conduzir uma auditoria diagnóstica e independente sobre o [Portal Detran Digital DF](https://portal.detran.df.gov.br/#/home), fundamentada na família de normas **ISO/IEC 25000 (SQuaRE)**, no método **GQM (Goal-Question-Metric)** e no modelo **PSM/CID (Practical Software Measurement / Cost, Income, Duration)**.

---

## 1. Identificação da Equipe e Gestão de Recursos (PSM/CID — Critério AG-C5)

A Tabela 1 consolida os membros da equipe avaliadora, suas matrículas acadêmicas na Universidade de Brasília, identificação no GitHub, e-mail institucional/de contato, papel técnico principal na avaliação, horas dedicadas no Ponto de Controle 1, valor/hora profissional de referência, custo total apurado e percentual relativo de esforço (totalizando rigorosamente 100%).

### Tabela 1 — Identificação da Equipe, Alocação de Papéis, Esforço e Custos (Ponto de Controle 1)

| Integrante | Matrícula UnB | Usuário GitHub | E-mail de Contato | Papel Principal na Avaliação | Horas (h) | Valor / Hora (R$) | Custo Total (R$) | % Esforço (AG-C5) |
| :--- | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **Artur Fernandes Galdino** | `241010923` | `@ArturFGaldino` | `fernandesartur4@gmail.com` | Analista de Compatibilidade / Mapeamento de Arquitetura e Escopo | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **Nicole Jovita Fernandes** | `241012347` | `@nicolejovita` | `nicolejovitafernandes@gmail.com` | Analista de Requisitos / Stakeholders, Modelo ISO 25010 e ODS | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **Davi Ursolino de Oliveira** | `241012202` | `@DaviUrsulino` | `daviursulinodeoliveira@gmail.com` | Analista de Confiabilidade / Especificação GQM e Métricas | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **João Eduardo Pereira Rabelo** | `180053299` | `@JoaoEduardoP` | `180053299@aluno.unb.br` | Analista de Confiabilidade / Metodologia e Métricas PSM | 12h | R$ 50,00 | R$ 600,00 | **16,66%** |
| **Natan José França** | `241011537` | `@Natan8643` | `natan.j.franca@gmail.com` | Analista de Usabilidade / Diagrama GQM e Níveis de Julgamento | 12h | R$ 50,00 | R$ 600,00 | **16,66%** |
| **Yan Santos Rodrigues** | `241025480` | `@yanrdgs-dev` | `yansantosrodrigues.dev@gmail.com` | Analista de Usabilidade / Especificação Operacional e Heurísticas | 12h | R$ 50,00 | R$ 600,00 | **16,67%** |
| **TOTAL CONSOLIDADO** | — | — | — | **Esforço Acumulado — Ponto de Controle 1** | **72h** | Média: R$ 50,00/h | **R$ 3.600,00** | **100%** |

*Fonte: Elaborado pelos autores conforme diretrizes da disciplina FGA0315 e modelo PSM/CID.*

*Nota explicativa: O esforço planejado e executado para o Ponto de Controle 1 foi distribuído igualmente entre os 6 membros da equipe (12 horas por integrante, totalizando 72 horas). Os centésimos foram ajustados matematicamente (quatro membros com 16,67% e dois com 16,66%) para assegurar a soma exata de 100,00%, em estrita observância ao Critério de Avaliação AG-C5.*

---

## 2. Objeto de Avaliação e Escopo Tecnológico

O software auditado é o **Portal Detran Digital DF** ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home)), plataforma governamental voltada à prestação de serviços públicos de trânsito aos cidadãos e condutores do Distrito Federal.

A avaliação concentra-se transversalmente nos **quatro módulos funcionais principais**:

1. **Módulo de Infração:** Consulta de débitos, autos de infração e emissão de guias de pagamento DUD/PIX.
2. **Módulo de Atendimento:** Agendamento de serviços presenciais e escolha orientada de postos e vagas.
3. **Módulo de Protocolo:** Abertura de recursos administrativos e envio digital integrado via barramento SEI-GDF.
4. **Módulo de Chatbot:** Assistente virtual inteligente para orientação e autoatendimento do cidadão.

---

## 3. Fundamentação Normativa e Metodológica

A avaliação adota o rigor de normas e modelos consolidados da Engenharia de Software:

* **ISO/IEC 25010 (Product Quality Model):** Recorte analítico focado em três características de alta criticidade para o serviço público estadual:
    * **Usabilidade (Capacidade de Interação):** Aprendibilidade, operabilidade e proteção contra erros de entrada, avaliadas pelas métricas $TCAPA$, $IEFO$, $TPRE$, inspeção por heurísticas de Nielsen e questionário $SUS$.
    * **Compatibilidade:** Coexistência e interoperabilidade (web e mobile), avaliadas por taxa de compatibilidade cross-browser ($TCBN$), índice de conformidade responsiva ($ICR$) e sucesso de integrações externas ($TSIS$).
    * **Confiabilidade:** Disponibilidade, ausência de falhas, tolerância e recuperação, medidas por taxa de disponibilidade observada ($TDO$), conclusão sem falhas ($TCFF$), densidade de falhas ($DFF$), operações anômalas ($TTOA$), taxa ($TRTI$) e tempo médio de recuperação ($TMR$).
* **ISO/IEC 25040 (Processo de Avaliação de Produto):** Condução do trabalho em 5 fases sequenciais (Requisitos, Especificação, Projeto da Avaliação, Execução e Julgamento).
* **GQM (Goal-Question-Metric):** Desdobramento estruturado dos objetivos estratégicos em questões analíticas e métricas operacionais com critérios objetivos de julgamento.
* **PSM/CID (Practical Software Measurement):** Acompanhamento gerencial do projeto em Desempenho dos Processos, Calendário e Progresso, e Recursos e Custos.
* **Alinhamento aos ODS da ONU:** Conexão direta com o **ODS 9** (Meta 9.c — Infraestrutura digital pública inclusiva e acessível) e **ODS 16** (Meta 16.6 — Instituições governamentais eficazes, transparentes e responsáveis).

---

## 4. Mapa da Documentação do Projeto

| Seção Documental | Caminho | Descrição do Conteúdo |
| :--- | :--- | :--- |
| **Requisitos da Avaliação (Fase 1)** | [`fase1/`](fase1/proposito-stakeholders.md) | Propósito, partes interessadas, mapeamento dos 4 módulos (Infração, Atendimento, Protocolo e Chatbot), modelo ISO 25010, limites de escopo e ODS 9 e 16. |
| **Especificação GQM (Fase 2)** | [`fase2/`](fase2/index.md) | Árvores GQM completas, fórmulas, procedimentos de coleta e limiares de decisão para Compatibilidade, Usabilidade e Confiabilidade. |
| **Gestão do Projeto (PSM/CID)** | [`gestao/`](gestao/metricas-psm.md) | Indicadores de processo, estrutura de Marcos M0 a M5, alocação de custos, atas e catálogo atômico das 17 issues fechadas. |
| **Ponto de Controle 1 (Entrega 1)** | [`entregas/entrega1.md`](entregas/entrega1.md) | Linha do tempo "Onde Estamos", matriz de entregáveis, consolidação de esforço e roteiro detalhado dos 10 slides da apresentação. |

---

## 5. Governança e Declaração de Uso de Ferramentas de IA (Critério AG-C3)

Em estrito cumprimento ao **Critério AG-C3** das diretrizes da disciplina Qualidade de Software 1:

* **Ferramentas Utilizadas:** Foram empregados assistentes de inteligência artificial generativa como suporte pontual para:
    1. Revisão ortográfica, sintática e adequação ao padrão formal acadêmico em língua portuguesa;
    2. Apoio na formatação e validação de código Mermaid para renderização de diagramas;
    3. Estruturação tabular de métricas e alinhamento de esquemas de documentação MkDocs.
* **Procedimento de Validação e Responsabilidade Humana:** Todos os textos, formulações de métricas, delimitações de escopo técnico sobre o Portal Detran Digital DF, diagramas conceituais e tabelas de custos foram minuciosamente concebidos, revisados, recalculados e validados pelos seis membros da equipe Kay McNulty. A equipe assume integral responsabilidade técnica e acadêmica pelo conteúdo apresentado.
* **Padronização Visual:** O relatório e as páginas de documentação foram revisados para assegurar a total ausência de emojis, ícones decorativos ou caracteres informais no corpo do texto e títulos, em conformidade com as rubricas de avaliação institucional.
