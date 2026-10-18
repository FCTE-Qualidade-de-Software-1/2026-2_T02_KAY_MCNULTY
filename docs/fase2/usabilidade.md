# GQM – Característica: Usabilidade

**Responsáveis:** Natan França e Yan Santos

A avaliação da característica de **Usabilidade** fundamenta-se na ISO/IEC 25010:2023 e considera o uso do Portal Detran Digital DF por cidadãos com diferentes faixas etárias, níveis de letramento digital e pessoas com deficiência. O objetivo é identificar barreiras que dificultem a compreensão, a navegação e a conclusão autônoma dos serviços nos módulos de Infração, Atendimento, Protocolo e Chatbot.

Nesta especificação, o foco quantitativo está nas subcaracterísticas **Aprendibilidade**, **Operabilidade** e **Proteção contra Erros de Usuário**, conforme delimitado para a avaliação. A Estética da Interface do Usuário e a Acessibilidade fazem parte do contexto conceitual de Usabilidade, mas não recebem métricas próprias nesta modelagem. Uma auditoria exaustiva de acessibilidade, incluindo testes completos com leitores de tela e avaliação especializada de contraste, está fora do escopo desta etapa.

---

## 1. Objetivo de Medição (Nível Conceitual)

| Elemento GQM | Descrição Estruturada |
| :--- | :--- |
| **Analisar** | Os módulos de Infração, Atendimento, Protocolo e Chatbot do Portal Detran Digital DF |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Usabilidade, com foco em Aprendibilidade, Operabilidade e Proteção contra Erros de Usuário (ISO/IEC 25010:2023) |
| **Do ponto de vista do** | Cidadão usuário e dos engenheiros de software avaliadores |
| **No contexto de** | Acessos ao portal em ambiente web e mobile no Distrito Federal |

A avaliação busca verificar se o cidadão consegue compreender os fluxos, realizar as operações necessárias com esforço adequado e prevenir ou recuperar-se de erros sem depender de suporte externo.

---

## 2. Questões Operacionais e Hipóteses (Nível Operacional)

### Questão Q1 – Aprendibilidade

**Pergunta:** O tempo e o esforço necessários para que um cidadão em seu primeiro acesso compreenda e conclua as tarefas principais dos quatro módulos — consultar infrações, agendar atendimento, abrir um protocolo e interagir com o chatbot — são reduzidos e dispensam suporte técnico, tutoriais ou ajuda externa?

**Hipótese H1:** Espera-se maior facilidade de aprendizado nos módulos de Infração e Chatbot, por envolverem fluxos de consulta e conversação mais diretos. Nos módulos de Protocolo e Atendimento, prevê-se uma curva de aprendizado mais acentuada devido à terminologia técnica, à quantidade de campos dos formulários e à possível ausência de ajuda contextual.

### Questão Q2 – Operabilidade

**Pergunta:** Os quatro módulos oferecem controles de navegação claros, interface consistente, baixo esforço operacional — medido pela quantidade de passos ou cliques — e retorno adequado ao cidadão durante o uso em ambiente web e mobile?

**Hipótese H2:** A operabilidade tende a ser mais satisfatória em computadores desktop. Em dispositivos móveis, podem ocorrer dificuldades como áreas de toque reduzidas na seleção de datas do módulo de Atendimento, demora ou dificuldade de acompanhamento das respostas do Chatbot e excesso de passos ou redirecionamentos no envio de documentos do módulo de Protocolo.

### Questão Q3 – Proteção contra Erros de Usuário

**Pergunta:** O portal previne erros de preenchimento por meio de máscaras, validações e confirmações de ações, e apresenta mensagens claras que permitam ao cidadão compreender o problema e recuperar-se dele?

**Hipótese H3:** A proteção contra erros pode apresentar fragilidades, como validação insuficiente de campos críticos (CPF, placa e RENAVAM) no módulo de Infração, ausência de confirmação resumida antes da conclusão do agendamento e mensagens genéricas ou técnicas no módulo de Protocolo. Essas situações podem dificultar a correção autônoma pelo cidadão. No Chatbot, também deve ser observado se entradas vazias, incoerentes ou não reconhecidas recebem orientação útil e alternativas de recuperação.

---

## 3. Definição Formal das Métricas (Nível Quantitativo)

As métricas abaixo relacionam cada questão operacional a medidas básicas observáveis e a uma medida derivada, seguindo a abordagem GQM e os princípios de medição do Practical Software Measurement (PSM).

### Métrica M1 – Taxa de Conclusão Autônoma no Primeiro Acesso (TCAPA)

**Questão associada:** Q1 – Aprendibilidade.

Avalia a proporção de tarefas concluídas com sucesso por cidadãos em seu primeiro contato com os módulos, sem solicitação de auxílio externo.

**Medidas básicas:**

- **N_aut:** número de tarefas concluídas com sucesso e sem solicitação de auxílio externo no primeiro acesso.
- **N_tot:** número total de tarefas de primeiro acesso executadas pelos participantes nos quatro módulos.

**Fórmula:**

\[
TCAPA = \frac{N_{aut}}{N_{tot}} \times 100\%
\]

**Procedimento de coleta:** realizar testes observacionais com participantes em primeiro acesso, utilizando tarefas previamente definidas para os quatro módulos. Registrar a conclusão ou não conclusão de cada tarefa, a solicitação de ajuda e as dificuldades observadas em uma planilha ou registro de teste.

**Critério de interpretação:** quanto maior o percentual, maior a proporção de tarefas que podem ser concluídas autonomamente. O resultado deve ser interpretado junto às observações qualitativas, sem generalizar além da amostra utilizada.

### Métrica M2 – Índice de Eficiência no Fluxo de Operação (IEFO)

**Questão associada:** Q2 – Operabilidade.

Compara a quantidade mínima de passos ou cliques prevista para a tarefa com a quantidade efetivamente realizada pelo participante.

**Medidas básicas:**

- **P_min:** número mínimo de passos ou cliques necessários para concluir a tarefa, conforme o fluxo de referência definido pelos avaliadores.
- **P_exec:** número de passos ou cliques efetivamente realizados pelo participante até concluir a tarefa.

**Fórmula:**

\[
IEFO = \frac{P_{min}}{P_{exec}} \times 100\%
\]

**Procedimento de coleta:** definir previamente o fluxo de referência de cada tarefa; observar ou registrar a navegação dos participantes em desktop e mobile; contabilizar os passos efetivamente realizados. O valor de \(P_{exec}\) deve ser maior que zero para que a métrica seja calculada. Se a tarefa não for concluída, registrar a não conclusão separadamente e não atribuir artificialmente um valor de eficiência.

**Critério de interpretação:** um valor de 100% representa execução pelo número mínimo de passos definido como referência. Valores menores indicam passos adicionais ou desvios em relação ao fluxo de referência. O indicador não deve ser interpretado isoladamente, pois uma tarefa pode exigir mais passos por razões legítimas de segurança ou confirmação.

### Métrica M3 – Taxa de Prevenção e Recuperação de Erros (TPRE)

**Questão associada:** Q3 – Proteção contra Erros de Usuário.

Mensura a proporção de eventos de erro em que a interface impede o erro ou oferece orientação suficientemente clara para que o usuário consiga corrigi-lo na primeira tentativa após o alerta.

**Medidas básicas:**

- **E_prev:** número de eventos de erro impedidos pela validação da interface ou corrigidos pelo usuário na primeira tentativa após receber uma mensagem clara.
- **E_tot:** número total de eventos de erro ou invalidação observados durante as tarefas nos quatro módulos.

**Fórmula:**

\[
TPRE = \frac{E_{prev}}{E_{tot}} \times 100\%
\]

**Procedimento de coleta:** executar cenários controlados com dados inválidos ou incompletos nos campos de Infração, anexos inválidos no Protocolo e entradas vazias ou incoerentes no Chatbot. No Atendimento, observar a existência e a clareza de confirmações antes de ações finais. Registrar a resposta da interface, a mensagem exibida e se o usuário conseguiu corrigir o problema na primeira tentativa.

**Critério de interpretação:** quanto mais próximo de 100%, maior a proporção de eventos prevenidos ou recuperados conforme a definição da métrica. Quando nenhum evento de erro for observado (\(E_{tot}=0\)), a métrica é **não aplicável** para aquela execução, e não deve ser registrada como 100%.

---

## 4. Níveis de Pontuação e Critérios de Julgamento

Os resultados percentuais devem ser classificados conforme as faixas estabelecidas para esta especificação. Os limites são aplicados separadamente a cada métrica.

| Nível de julgamento | TCAPA (M1) | IEFO (M2) | TPRE (M3) | Interpretação técnica |
| :---: | :---: | :---: | :---: | :--- |
| **Excelente** | ≥ 90% | ≥ 90% | ≥ 95% | Usabilidade exemplar: tarefas realizadas com autonomia, fluxo eficiente e elevada prevenção ou recuperação de erros. |
| **Bom** | 80% a < 90% | 80% a < 90% | 85% a < 95% | Usabilidade adequada: podem ocorrer dúvidas ou desvios pontuais, sem impedir a conclusão da tarefa. |
| **Satisfatório** | 70% a < 80% | 70% a < 80% | 75% a < 85% | Usabilidade limítrofe: o cidadão pode precisar de esforço adicional, repetir ações ou consultar ajuda ocasionalmente. |
| **Insuficiente** | < 70% | < 70% | < 75% | Usabilidade crítica: há indícios de abandono, navegação confusa ou erros sem orientação suficiente para correção. |

**Regras de aplicação e registro:**

1. Registrar numeradores e denominadores junto aos percentuais, permitindo reproduzir os cálculos.
2. Registrar separadamente tarefas não concluídas, eventos não observados e situações em que a métrica não puder ser calculada.
3. Interpretar resultados por módulo e por contexto de acesso sempre que a amostra permitir, sem misturar observações de tarefas diferentes sem identificá-las.
4. Documentar evidências observáveis — por exemplo, capturas de tela, registros de observação e descrição do cenário — para fundamentar o julgamento.
5. As hipóteses H1, H2 e H3 são expectativas a serem verificadas durante a execução; não representam resultados já constatados.

---

## 5. Diagrama Hierárquico GQM

O diagrama abaixo explicita a rastreabilidade entre o objetivo de medição, as questões operacionais e as métricas quantitativas.

```mermaid
flowchart TD
    G["Objetivo G: Avaliar a usabilidade dos módulos de Infração, Atendimento, Protocolo e Chatbot do Detran Digital DF, do ponto de vista do cidadão e dos avaliadores, em acessos web e mobile"]

    Q1["Q1 — Aprendibilidade: o cidadão consegue concluir tarefas no primeiro acesso sem ajuda externa?"]
    Q2["Q2 — Operabilidade: os fluxos são claros e exigem quantidade adequada de passos/cliques?"]
    Q3["Q3 — Proteção contra erros: a interface previne erros e orienta a recuperação?"]

    M1["M1 — TCAPA: (N_aut / N_tot) × 100%"]
    M2["M2 — IEFO: (P_min / P_exec) × 100%"]
    M3["M3 — TPRE: (E_prev / E_tot) × 100%"]

    G --> Q1
    G --> Q2
    G --> Q3
    Q1 --> M1
    Q2 --> M2
    Q3 --> M3
```

---

## 6. Limites da Avaliação de Usabilidade

A avaliação será realizada por inspeção da interface e testes de tarefas guiadas com amostragem técnica reduzida de cidadãos e engenheiros avaliadores. Não contempla testes presenciais em laboratório UX com centenas de participantes, nem intervenção ou alteração direta no portal de produção.

Embora a inclusão de pessoas com deficiência seja relevante para a avaliação de um serviço público, esta especificação não equivale a uma auditoria completa de acessibilidade. Testes exaustivos com leitores de tela, avaliação especializada de contraste e demais verificações avançadas ficam reservados a um estudo específico. Os resultados deverão explicitar essa limitação.

A análise utiliza somente comportamentos observáveis na interface e nos fluxos acessíveis ao avaliador. Não pressupõe acesso ao código-fonte ou aos sistemas internos do Detran-DF.
