# Oportunidades de Melhoria e Decisão da Ação – Capacidade de Interação

**Responsável:** Natan França  
**Característica:** Capacidade de Interação (ISO/IEC 25010:2023)  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 4 (Execução e Julgamento da Avaliação – ISO/IEC 25040)  
**Depende de:** [#57](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/57) (cálculo das métricas e resultados em [Resultados de Capacidade de Interação](usabilidade.md))

!!! note "Status do Documento (22/11/2026)"
    A lista, a matriz e a decisão abaixo usam apenas **evidências reais**: M1, M2, M3 e M5 (`resultados-consolidados.csv`), as observações do piloto e do catálogo de falhas da [Confiabilidade](confiabilidade.md). A **M4 (IPH) não tem dados reais**: `inspecao-heuristica.csv` e `inspecao-heuristica-consolidada.csv` estão sem linhas (issue #55), e as Tabelas 7 a 13 da página de resultados são **dados de exemplo**. Por isso **nenhuma oportunidade ou pontuação depende de um problema do IPH**; os itens de severidade 3 e 4 do exemplo aparecem só no [Apêndice A](#apendice-a-itens-de-severidade-3-e-4-do-exemplo), com a evidência real que os corrobora, quando existe. A decisão é uma **proposta pendente de validação da equipe**.

---

## 1. Base de Evidências

Cada oportunidade da Seção 2 cita um ou mais destes identificadores. Os valores vêm de `docs/dados/capacidade_interacao/resultados-consolidados.csv`, de `cenarios-de-erro-piloto.csv`, do [piloto](../fase3/piloto-usabilidade.md) e das páginas de [resultados](usabilidade.md) e de [Confiabilidade](confiabilidade.md).

| ID | Evidência | Fonte |
| :---: | :--- | :--- |
| **EV-01** | TCAPA total: 13 de 22 (59,1%), nível Insuficiente | M1, `resultados-consolidados.csv` |
| **EV-02** | TCAPA do Protocolo (T3): 2 de 6 (0 de 3 no desktop, 2 de 3 no mobile). Das 4 execuções não autônomas: P01 desistiu, P06 atingiu o teto de tempo, P02 e P03 concluíram com auxílio | M1 e registro à parte |
| **EV-03** | TCAPA do Atendimento (T2): 4 de 6; P02 (desktop) e P05 (mobile) concluíram com auxílio | M1 e registro à parte |
| **EV-04** | TCAPA do Chatbot (T4): 2 de 5; P02, P03 e P06 concluíram com auxílio; a T4 de P04 ficou fora de N_tot por falha técnica externa (o chatbot não respondeu) | M1 e registro à parte |
| **EV-05** | TCAPA da Infração (T1): 5 de 5 | M1 |
| **EV-06** | IEFO por dispositivo: desktop 63,6% (6 execuções) e mobile 86,1% (8); Infração 56,1% contra 91,7% e Atendimento 56,6% contra 89,0%; Protocolo sem execução válida no desktop. Pela razão agregada (91 ÷ 141), o total cai de 76,4% (Satisfatório) para 64,5% (Insuficiente) | M2 |
| **EV-07** | TPRE do Protocolo: 0 de 3. Objeto vazio (E-PRO-01), placa incompleta (E-PRO-08) e Renavam curto (E-PRO-09) avançaram até a assinatura **sem nenhum alerta** (`sem_erro`) | M3, `cenarios-de-erro-piloto.csv` |
| **EV-08** | Chatbot, TPRE 5 de 5, mas: entrada vazia e só espaços (E-BOT-01 e 02) têm só feedback visual, sem texto; texto incoerente (E-BOT-03) e fora do escopo (E-BOT-04) recebem orientação parcial, **sem atendimento humano** | M3, `cenarios-de-erro-piloto.csv` |
| **EV-09** | Atendimento, observações qualitativas: sem tela de resumo antes da ação final (E-ATE-01), sem voltar sem perder dados (E-ATE-02), sem cancelar o fluxo (E-ATE-03) e sem informação de como cancelar ou reagendar depois de concluído (E-ATE-04) | `cenarios-de-erro-piloto.csv` |
| **EV-10** | SUS médio 53,3 (mediana 53,75; mínimo 45; máximo 62,5); os 6 participantes ficaram abaixo da referência de 68 | M5 |
| **EV-11** | Piloto da T3: a prévia do documento não traz aviso nem opção de editar antes da etapa de assinatura. **A confirmar na inspeção** | Piloto, Tabela 2 |
| **EV-12** | Piloto da T1: com a conta de teste sem veículo, a tela não lista nada e não mostra estado vazio. **A confirmar com conta com veículo** | Piloto, Tabela 2 |
| **EV-13** | Piloto da T2: 2 cliques sem efeito (Unidade e Data), com P_exec de 14 passos | Piloto, Tabela 1 |
| **EV-14** | Perda do que foi preenchido ao recarregar ou voltar pelo navegador (A6, B3, B4, B5) em Atendimento e Protocolo, catalogada como C-07 | Confiabilidade |
| **EV-15** | A8: no Requerimento Geral, um envio com **campo vazio** retornou 409 e mensagem clara. **Diverge de EV-07** para o campo vazio | `anomalias.csv` (Confiabilidade) |

**Tabela 1 – Base de evidências.** Fonte: Elaborado pelos autores.

**M4 (IPH).** Sem registros consolidados. Esta página será atualizada quando a issue #55 for fechada (Seção 3).

---

## 2. Lista de Oportunidades

| ID | Módulo | Oportunidade | Métrica afetada | Evidências |
| :---: | :--- | :--- | :---: | :--- |
| **O1** | Protocolo | Validar os campos do Requerimento Geral antes de avançar e mostrar a mensagem junto do campo (hoje, placa e Renavam inválidos avançam sem alerta) | M3 | EV-07 (com a ressalva de EV-15) |
| **O2** | Protocolo | Tornar a T3 concluível sem ajuda: 4 de 6 execuções não foram autônomas, e o desktop teve 0 de 3 | M1, M2 | EV-02, EV-06 |
| **O3** | Protocolo | Avisar e permitir rever os dados antes da etapa de assinatura | M3 | EV-11, EV-07 |
| **O4** | Atendimento | Incluir resumo antes de concluir, opção de cancelar, volta sem perda de dados e orientação de cancelamento ou reagendamento | M3 (qualitativo), M1 | EV-09, EV-03, EV-14 |
| **O5** | Infração e Atendimento | Entender e reduzir os passos extras no desktop (IEFO menor que o do mobile; cliques sem efeito) | M2 | EV-06, EV-13 |
| **O6** | Chatbot | Dar saída ao cidadão quando o assistente não resolve (exemplos de pergunta, atendimento humano) e texto na entrada vazia | M1, M3 | EV-04, EV-08 |
| **O7** | Infração | Mostrar estado vazio quando não há veículo | M1 | EV-12 |
| **O8** | Portal inteiro | Elevar a percepção geral de usabilidade (SUS abaixo de 68 nos 6 participantes) | M5 | EV-10, EV-01 |

**Tabela 2 – Oportunidades derivadas de M1, M2, M3 e M5.** Fonte: Elaborado pelos autores. A perda de estado do formulário (EV-14) já é atacada pela ação da Confiabilidade ([Melhoria da Confiabilidade](melhoria-confiabilidade.md)) e **não é repetida** como oportunidade própria.

---

## 3. Problemas de Severidade 3 e 4 (M4)

O IPH é o instrumento que classifica problemas de 0 a 4, mas **não há classificação real** no repositório. Por isso:

* os problemas de severidade 3 e 4 **não** foram usados para criar oportunidades nem para pontuar a matriz;
* as Tabelas 10 a 13 da página de resultados (11 itens de severidade 3 ou 4) são exemplo, e o Apêndice A mostra qual evidência real cada um tem;
* para a severidade da matriz (Seção 4) foi usado um **critério provisório de impacto observado na tarefa**, que não é a escala de 0 a 4 do guia de severidade;
* quando o IPH consolidado existir, cada problema de severidade 3 ou 4 deve ser ligado a uma das oportunidades acima ou virar uma nova, e a Tabela 4 deve ser recalculada.

---

## 4. Priorização

### 4.1 Critérios

Cada critério vai de 1 a 3, e a nota da oportunidade é a **soma** (4 a 12). Em caso de empate, vale a maior solidez, depois a maior viabilidade e depois a maior severidade.

| Critério | 3 | 2 | 1 |
| :--- | :--- | :--- | :--- |
| **Severidade** (impacto observado na tarefa; critério provisório) | Tarefa não concluída sem ajuda por parte relevante dos participantes, ou entrada inválida aceita sem alerta em fluxo com efeito legal | Perda de eficiência ou ausência de salvaguarda, sem falha observada | Incômodo sem efeito observado |
| **Módulos afetados** | 3 ou mais | 2 | 1 |
| **Solidez da evidência** | Mais de um instrumento ou fonte independente concordam | Um instrumento, observação direta e reprodutível | Só piloto, exemplo, causa não documentada, fontes divergentes ou resultado que muda com a escolha de cálculo |
| **Viabilidade no prazo** | Cabe em protótipo de um fluxo, sem depender de dado novo | Cabe com escopo reduzido ou depende de uma conferência | Depende do portal, do Detran ou de nova coleta |

**Tabela 3 – Critérios de priorização.** Fonte: Elaborado pelos autores. Prazo restante: a Fase 4 encerra em 22/11/2026 ([Fase 3](../fase3/usabilidade.md), Seção 10).

### 4.2 Aplicação

| Pos. | ID | Severidade | Módulos | Solidez | Viabilidade | **Nota** | Justificativa das notas |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | **O1** | 3 | 1 | 2 | 3 | **9** | Entrada inválida aceita em fluxo com efeito legal; 3 eventos reprodutíveis; solidez 2 por causa da divergência EV-15 no campo vazio |
| 2 | **O4** | 2 | 1 | 2 | 3 | **8** | Sem falha observada, mas 4 ausências reproduzíveis; resumo cabe em protótipo |
| 3 | **O2** | 3 | 1 | 2 | 2 | **8** | Desistência, teto de tempo e 2 auxílios; a causa não está documentada nos dados disponíveis |
| 4 | **O8** | 2 | 3 | 2 | 1 | **8** | 6 de 6 abaixo de 68, mas não aponta o que mudar |
| 5 | **O3** | 3 | 1 | 1 | 3 | **8** | Risco potencial alto, mas só observado no piloto e "a confirmar" |
| 6 | **O6** | 2 | 1 | 2 | 2 | **7** | Limitações reprodutíveis; o M3 do chatbot é 5 de 5 e a causa dos auxílios na T4 não está documentada |
| 7 | **O7** | 2 | 1 | 1 | 3 | **7** | Só piloto com conta sem veículo; a Infração teve 5 de 5 |
| 8 | **O5** | 2 | 2 | 1 | 1 | **6** | n pequeno, P_min diverge do catálogo, a faixa muda com a agregação e a causa é desconhecida |

**Tabela 4 – Matriz de priorização.** Fonte: Elaborado pelos autores, com base na Tabela 1.

**Robustez.** O1 fica em primeiro lugar com o dobro de peso na severidade (12 pontos), na solidez (11) ou na viabilidade (12), e com pesos iguais (9). A segunda posição **não é estável**: O4, O2, O8 e O3 empatam com 8 e trocam de ordem conforme o peso. A matriz sustenta O1 como prioridade, mas não distingue com folga as demais.

**Leitura.** O1, O2 e O3 pertencem ao **mesmo fluxo** (Requerimento Geral, Protocolo), e juntos descrevem uma sequência: o formulário aceita dados inválidos (EV-07), o cidadão chega à assinatura sem revisão nem aviso (EV-11) e, no desktop, nenhuma das 3 execuções terminou sem auxílio (EV-02). O Protocolo é também o único módulo em que a medição com participantes (M1) e a execução dos cenários de erro pelos avaliadores (M3) apontam fragilidade.

---

## 5. Análise das Modalidades de Ação

| Modalidade | Aplicável? | Evidência e escopo | Decisão |
| :--- | :---: | :--- | :---: |
| **Protótipo de alta fidelidade** | Sim | As oportunidades de maior nota (O1, O4, O2, O3) são de interface e de fluxo: validação, resumo, aviso e etapas. Um protótipo permite testar a correção sem tocar no portal | **Escolhida** |
| **Modificação de código** | Não | A avaliação é caixa-preta: sem acesso ao código-fonte e sem intervenção no portal em produção ([Fase 2](../fase2/usabilidade.md), Seção 6; [Fase 3](../fase3/usabilidade.md), Seção 5). Nenhuma oportunidade pode ser entregue como alteração do portal | **Descartada** |
| **Templates técnicos** | Em parte | Só há evidência de ajuda e documentação frágil no Chatbot (EV-08) e no cancelamento do Atendimento (EV-09), vinda da execução dos avaliadores. O IPH (heurística de ajuda e documentação) não tem dados, e a causa dos auxílios na T4 não está documentada | Não escolhida; recomendada como complemento (O6) |
| **Proposição de processo** | Não sustentada | A falta de salvaguardas aparece em Protocolo e Atendimento, mas as evidências são sobre a interface. Nada foi observado do processo de desenvolvimento ou de validação do Detran-DF, então não há como atribuir os problemas a um vício de processo | Não escolhida |

**Tabela 5 – Modalidades de ação frente às evidências e ao escopo.** Fonte: Elaborado pelos autores. O protótipo da Confiabilidade segue o mesmo princípio: é validado fora do portal, e seus resultados não são medidas feitas em produção.

---

## 6. Decisão

!!! info "Ação proposta: protótipo de alta fidelidade do Requerimento Geral"
    Protótipo do fluxo **Requerimento Geral** do módulo **Protocolo**, com validação por campo, revisão com aviso antes da etapa de assinatura e, como hipótese a testar, indicação de etapa.

### 6.1 Problema atacado, módulo e métrica

| Item | Definição |
| :--- | :--- |
| **Módulo e fluxo** | Protocolo, Requerimento Geral (tarefa T3), do formulário até a etapa de assinatura |
| **Problemas atacados** | O1 (campos inválidos aceitos sem alerta) e O3 (assinatura sem revisão nem aviso); O2 (T3 sem autonomia) como efeito esperado, a verificar |
| **Métricas afetadas** | **M3** (TPRE do Protocolo, 0 de 3) e **M1** (TCAPA da T3, 2 de 6, com 0 de 3 no desktop); **M2** (IEFO do Protocolo, 77,8% em 2 execuções, só mobile) como acompanhamento |
| **Linha de base** | EV-02, EV-07 e EV-11 |

**Tabela 6 – Alvo da ação.** Fonte: Elaborado pelos autores.

### 6.2 Justificativa rastreável

* **Maior nota da matriz** (O1, 9 pontos), mantida em primeiro lugar em todas as variações de peso (Seção 4.2).
* **Maior concentração de problemas no mesmo fluxo:** O1, O2 e O3 estão no Requerimento Geral. Com 4 de 6 execuções não autônomas (EV-02), o Protocolo é o pior módulo em M1, e o único com TPRE de 0 de 3 (EV-07).
* **O efeito do problema é o mais grave:** dados inválidos chegam à etapa de assinatura com validade legal (Fase 3, Seção 6.2), sem aviso nem revisão (EV-11).
* **Não repete a ação da Confiabilidade:** a perda de estado (EV-14) já tem protótipo próprio. O protótipo desta ação **não reimplementa o rascunho**.
* **Cabe no prazo:** um fluxo de poucas telas, sem dado novo e sem depender do portal.
* **Por que não o Atendimento (O4, 2º lugar):** sua perda de estado já é coberta pela Confiabilidade, e o prazo comporta um fluxo. O padrão de revisão antes da ação final é o mesmo e fica como extensão (Seção 6.4).

### 6.3 Escopo do protótipo

| Elemento | Responde a | Base |
| :--- | :--- | :---: |
| Validação por campo (Objeto, placa, Renavam), com mensagem junto do campo e sem avançar com valor inválido | O1 | EV-07 |
| Tela de revisão com os dados informados, aviso do que a assinatura implica e botão para voltar e editar | O3 | EV-11 |
| Indicação da etapa atual e do total de etapas | O2 | **Hipótese**, sem dado real que a sustente |
| Exemplo no campo Objeto | O2 | **Hipótese**, sem dado real que a sustente |

**Tabela 7 – Elementos do protótipo.** Fonte: Elaborado pelos autores. As duas últimas linhas vêm de itens do exemplo do IPH. Entram **como hipóteses a testar** na validação, e o resultado não deve ser atribuído a elas sem teste separado.

**Fora do escopo:** rascunho (Confiabilidade), assinatura real com gov.br, anexos, Atendimento, Chatbot e Infração.

### 6.4 Condições antes de construir

1. **Reexecutar o E-PRO-01 (Objeto vazio).** A Confiabilidade (A8) registrou 409 e mensagem clara para campo vazio, e o M3 registrou avanço sem alerta (EV-07 e EV-15). Se a mensagem existir, o elemento de validação do Objeto muda de "criar" para "tornar visível junto do campo". A placa e o Renavam (E-PRO-08 e 09) não são contrariados por A8.
2. **Ler a coluna `observacoes` das sessões da T3** (P01, P02, P03 e P06) para registrar a causa da falta de autonomia. Os registros por participante não estão nos arquivos desta issue (`registro-tarefas.csv` está vazio e `registro-tarefas-preenchido.csv` não consta em `docs/dados/capacidade_interacao/`), então a causa de O2 ainda não é conhecida.
3. **Confirmar EV-11** (aviso e edição antes da assinatura) na inspeção heurística (#55).

### 6.5 Verificação proposta (para a issue de validação)

* **M3 no protótipo:** repetir E-PRO-01, 08 e 09. Critério proposto: os 3 classificados como `prevenido` ou `corrigido_1a_tentativa`, contra 0 de 3 hoje.
* **M1 e M2 no protótipo:** executar a T3 com participantes que **não** participaram das sessões, e comparar o N_aut com 2 de 6.
* **Declarar o limite:** o resultado vale para o protótipo, não para o portal em produção.

Os critérios são proposta, e a dupla confirma antes da execução.

---

## 7. Limitações

* **Sem IPH real.** A severidade da matriz é um critério provisório de impacto observado, e a Tabela 4 deve ser recalculada com o IPH consolidado.
* **Amostra pequena:** 6 participantes e até 3 execuções por célula de módulo e dispositivo; os resultados valem para a amostra.
* **M3 sem participantes:** a TPRE vem da execução dos avaliadores, em Protocolo e Chatbot, sem separação por dispositivo.
* **IEFO frágil:** o P_min usado não inclui o login (difere do catálogo da Fase 3), só entram execuções sem auxílio, e a razão agregada muda a faixa do total (EV-06). Por isso O5 tem solidez 1.
* **Causas não documentadas:** os dados disponíveis mostram onde houve falha ou auxílio, não por quê.
* **Divergência entre fontes** no campo vazio do Requerimento Geral (EV-07 e EV-15), a resolver antes da construção.
* **Sem acessibilidade e sem código-fonte:** a avaliação não é uma auditoria de acessibilidade e não inspeciona o código do portal.
* **Matriz com margem curta:** a segunda posição não é estável (Seção 4.2).

---

## Apêndice A. Itens de Severidade 3 e 4 do Exemplo

Os itens abaixo são os de severidade 3 ou 4 das Tabelas 10 a 13 da [página de resultados](usabilidade.md), que são **dados de exemplo**. A coluna de correspondência indica só a evidência **real** que toca no mesmo assunto, e não confirma o item.

| ID (exemplo) | Sev. | Assunto | Correspondência real | Situação |
| :---: | :---: | :--- | :---: | :--- |
| CONS-PRO-001 | 4 | Assinatura sem aviso nem edição | EV-11 | Parcial: observação do piloto, a confirmar |
| CONS-PRO-003 | 3 | Sem rascunho no formulário | EV-14 | Real e atacada pela Confiabilidade |
| CONS-PRO-005 | 3 | Mensagem de campo obrigatório genérica | EV-07, EV-15 | **Diverge:** EV-07 registra ausência de alerta e EV-15 registra mensagem clara |
| CONS-PRO-004 | 3 | Sem indicação de etapa (mobile) | Nenhuma | Só exemplo |
| CONS-ATE-001 | 3 | Sem sinal de seleção de unidade e data | EV-13 | Parcial: 2 cliques sem efeito no piloto |
| CONS-ATE-002 | 3 | Sem resumo antes de concluir | EV-09 (E-ATE-01) | Corroborado |
| CONS-ATE-003 | 3 | Voltar descarta os campos | EV-09 (E-ATE-02), EV-14 | Corroborado |
| CONS-INF-001 | 3 | Sem estado vazio sem veículo | EV-12 | Parcial: piloto, a confirmar |
| CONS-INF-005 | 3 | Termo "enquadramento" sem explicação | Nenhuma | Só exemplo |
| CONS-BOT-001 | 3 | Assistente sem resposta e sem aviso (mobile) | EV-04 | Parcial: falha técnica externa de P04 na T4 |
| CONS-BOT-003 | 3 | Sem link oficial; resposta varia entre dispositivos | Piloto da T4 (variação) | Parcial: a variação foi observada, o link não |

**Tabela A1 – Correspondência entre o exemplo do IPH e a evidência real.** Fonte: Elaborado pelos autores.

Ao fechar a issue #55, substituir esta tabela pelos problemas consolidados de severidade 3 e 4, cada um ligado a uma oportunidade da Tabela 2.
