# Plano de Avaliação – Característica: Capacidade de Interação

**Responsáveis:** Natan França e Yan  
**Característica:** Capacidade de Interação (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Aprendibilidade, Operabilidade e Proteção contra Erros de Usuário  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 3 (Projeto da Avaliação – ISO/IEC 25040)

!!! info "Status do Documento (20/11/2026)"
    Os instrumentos da Fase 3 estão definidos e integrados nesta página: catálogo de tarefas e fluxos, cenários de erro, plano do teste com participantes, protocolo de inspeção heurística, matriz de rastreabilidade, responsabilidades e cronograma. O **piloto dos instrumentos** é descrito na [página do piloto](piloto-usabilidade.md), com os limites do que ele valida. A coleta oficial é feita na Fase 4. Esta versão substitui a anterior, que tratava o IEFO por tempo, o SUS como M4 e usava outras faixas de julgamento: **prevalece a [Fase 2](../fase2/usabilidade.md)**.

---

## 1. Método de Avaliação

A avaliação da característica de **Capacidade de Interação** fundamenta-se nas especificações conceituais e métricas operacionais consolidadas na [Fase 2](../fase2/usabilidade.md). A metodologia organiza-se em duas frentes complementares, de abordagem caixa-preta:

1. **Inspeção heurística de interface (M4 – IPH):**
   * Aplicação das 10 heurísticas de **usabilidade** de Jakob Nielsen, por avaliadores independentes, para identificar barreiras cognitivas, falhas de feedback, inconsistências visuais e deficiências no controle do usuário.
2. **Avaliação empírica de desempenho e percepção (M1, M2, M3 e M5):**
   * Tarefas orientadas nos quatro módulos, com participantes em primeiro acesso, para apurar o **TCAPA** (Taxa de Conclusão Autônoma no Primeiro Acesso), o **IEFO** (Índice de Eficiência no Fluxo de Operação, por **passos**) e a **TPRE** (Taxa de Prevenção e Recuperação de Erros).
   * Aplicação do questionário **System Usability Scale (SUS)** para quantificar a percepção de capacidade de interação.

### 1.1 Métricas e instrumentos

As cinco métricas (M1 a M5), seus instrumentos de coleta, as issues de execução e de cálculo e os níveis de julgamento estão na **matriz da Seção 8** (Tabelas 4 e 5), que é a única referência para esses dados nesta página.

### 1.2 Relação com a versão anterior da página

A versão anterior desta página divergia da Fase 2 em cinco pontos: IEFO por tempo (a Fase 2 usa passos), SUS como M4 (a Fase 2 define M4 = IPH e M5 = SUS), questões e hipóteses Q1 a Q4 e H1 a H4 (a Fase 2 define Q1 a Q3 e H1 a H3), faixas "Regular" com limites próprios e faixas de julgamento para o SUS (a Fase 2 não as define para M4 e M5). Todos foram corrigidos nesta página. Se algum texto das Fases 3 e 4 ainda divergir da Fase 2, **vale a Fase 2**.

---

## 2. Roteiro de Tarefas e Inspeção Heurística por Módulo

Os procedimentos cobrem os quatro módulos do escopo. As tarefas são as do catálogo (Seção 6.1); a inspeção heurística percorre todas as telas acessíveis do módulo.

* **Módulo Infração:** consulta de débitos de um veículo, interpretação da lista de infrações e do valor da mais recente.
* **Módulo Atendimento:** agendamento presencial, seleção de categoria, unidade, data e horário, e verificação de resumo, volta e cancelamento antes da ação final.
* **Módulo Protocolo:** preenchimento do Requerimento Geral até a etapa de assinatura, sem concluí-la. Os cenários de anexo inválido não são executados (Seção 6.2).
* **Módulo Chatbot:** consulta ao assistente virtual sobre uma dúvida frequente, clareza das respostas e alternativas quando ele não entende.

---

## 3. Instrumentos de Coleta e Perfil dos Avaliadores

* **Guia de severidade e planilhas da inspeção:** classificação dos problemas em escala de 0 a 4 (0 = não é problema; 1 = cosmético; 2 = menor; 3 = maior; 4 = catastrófico), registrada em `inspecao-heuristica.csv` e consolidada em `inspecao-heuristica-consolidada.csv` (Seção 6.4).
* **Gravação de tela e de áudio:** com consentimento do participante, para conferir a contagem de passos e a decisão de auxílio. Não é versionada e é apagada ao fim da disciplina (Seção 6.3).
* **Avaliadores:** os dois integrantes da dupla, graduandos em Engenharia de Software da UnB, com treinamento no método heurístico. Eles **não participam** do teste com participantes.

---

## 4. Níveis de Pontuação e Matriz

Os níveis de julgamento das métricas M1, M2 e M3 e a matriz de rastreabilidade estão na **Seção 8** (Tabelas 4 e 5). Esta seção foi mantida apenas para preservar a numeração das referências existentes.

---

## 5. Limitações Metodológicas

* **Amostra pequena e de conveniência.** Os resultados valem para os participantes e não se generalizam. Todos os percentuais são acompanhados de numerador e denominador, e as células por módulo e dispositivo são relatadas como contagens.
* **Ambiente de produção.** As tarefas e os cenários de erro não geram efeitos reais (protocolos, agendamentos ou pagamentos) e param nos pontos de parada seguros.
* **Versão do portal.** Os resultados refletem o portal na data da coleta.
* **Infração.** O módulo não tem campo de entrada, então a proteção contra erros dele não é medida por M3. A T1 depende de uma conta com veículo (Seção 6.1).
* **Protocolo.** Os cenários de anexo inválido não são executados, pela assinatura com gov.br.
* **Acessibilidade.** A avaliação não equivale a uma auditoria de acessibilidade. Leitores de tela e contraste ficam fora do escopo.
* **Caixa-preta.** A análise usa só o que é observável na interface, sem acesso ao código-fonte e sem intervenção no portal.
* **Julgamento de especialistas.** O IPH é um julgamento de especialistas e não substitui a observação de usuários. Dois avaliadores são menos que os 3 a 5 recomendados por Nielsen, e o IPH não estima o total de problemas.
* **Conta de teste.** O login gov.br exige conta real. A conta é de terceiro, com consentimento do titular, e seus dados aparecem na tela e na gravação (Seção 6.3).

---

## 6. Instrumentos Integrados

Os arquivos de dados ficam em `docs/dados/capacidade_interacao/`. Esta seção resume o que cada instrumento faz; **o detalhe e as decisões vivem nos arquivos de origem**, para que esta página não fique desatualizada quando eles mudarem. Os arquivos dos PRs #77 e #78 são citados em texto até serem integrados à `main`.

### 6.1 Catálogo de tarefas e fluxos de referência (M1 e M2)

Há uma tarefa por módulo, em desktop e em mobile (8 linhas em [`tarefas-e-fluxos.csv`](../dados/capacidade_interacao/tarefas-e-fluxos.csv); notas em [`tarefas-e-fluxos-notas.md`](../dados/capacidade_interacao/tarefas-e-fluxos-notas.md)). Os enunciados são neutros e não citam nomes de menus ou botões.

| Tarefa | Módulo | P_min (desktop) | P_min (mobile) | Ponto de parada seguro |
| :---: | :--- | :---: | :---: | :--- |
| **T1** | Consultar infrações | 8 | 8 | Lista de infrações, sem pagar, emitir boleto ou recorrer |
| **T2** | Agendar atendimento | 15 | 15 | Formulário preenchido, antes de *Concluir agendamento* |
| **T3** | Abrir protocolo (Requerimento Geral) | 10 | 10 | Etapa de assinatura, sem concluir com gov.br |
| **T4** | Interagir com o chatbot | 3 | 3 | Resposta do assistente exibida |

**Tabela 1 – Tarefas e P_min.** Fonte: Elaborado pelos autores. Valores conciliados entre os dois avaliadores.

**Regra de contagem de passos (vale para todas as sessões).** Cada clique ou toque e cada campo preenchido contam como um passo (Fase 2). Para definir o P_exec, "efetivamente realizados" inclui os desvios que o IEFO mede:

| Ocorrência | Conta em P_exec? |
| :--- | :---: |
| Clique ou toque com efeito | Sim |
| **Clique ou toque sem efeito** (clicou e nada aconteceu) | **Sim** |
| Voltar (do navegador ou do portal) | Sim |
| Recarregar a página | Sim |
| Rolagem e movimento do ponteiro | Não |
| Fechar o aviso temporário da página inicial ("É GOLPE!") | Não; registrar em `observacoes` e como achado de inspeção |
| Passos de **login** | Sim, como no P_min (o login conta no catálogo) |

Se P_exec for menor que P_min, o fluxo de referência é revisado e a ocorrência registrada (Fase 2), para que o IEFO não passe de 100%.

**Conta com veículo (T1).** A T1 só é executável com uma conta gov.br que tenha veículo vinculado. A equipe **vai obter essa conta, com o consentimento do titular, antes do recrutamento** (Seção 10, R1). Se isso não ocorrer até a data de corte, a T1 sai de N_tot de M1 e M2 e é registrada à parte (regra 3 da Seção 4 da Fase 2): N_tot passa de 24 para 18, e a hipótese H1 fica **inconclusiva** para Infração. Essa decisão é tomada na data de corte e registrada nesta seção.

**Login gov.br.** Todas as ações, exceto o assistente virtual, exigem login. T1 a T3 começam sem sessão iniciada, e o login conta no P_min.

### 6.2 Cenários de erro controlados (M3)

Os cenários ficam em [`cenarios-de-erro.csv`](../dados/capacidade_interacao/cenarios-de-erro.csv) e as regras de apuração em [`cenarios-de-erro-regras.md`](../dados/capacidade_interacao/cenarios-de-erro-regras.md). Usam apenas valores sabidamente inválidos e não geram efeitos reais. Nas sessões, são aplicados **depois** que a tarefa chegou ao ponto de parada, em repetição separada, para não contaminar o P_exec (M2) nem o pedido de auxílio (M1).

Classificação do evento:

| Valor | Significado | E_prev | E_tot |
| :--- | :--- | :---: | :---: |
| `prevenido` | A interface impediu o erro | Sim | Sim |
| `corrigido_1a_tentativa` | Mensagem exibida e o participante corrigiu na primeira tentativa | Sim | Sim |
| `nao_recuperado` | Mensagem ausente, genérica ou técnica, ou sem correção na primeira tentativa | Não | Sim |
| `sem_erro` | **A interface aceitou a entrada inválida sem alerta.** É um erro **não prevenido** | Não | Sim |
| `N/A` | Cenário não executado, ou observação sem erro | Não | Não |

`sem_erro` **não** significa "nenhum evento": significa que a interface aceitou o dado inválido, e por isso pertence ao denominador. A execução sem nenhum evento classificável é `N/A`. **Quando E_tot = 0, a M3 é "não aplicável", e nunca 100%.**

| Módulo | Cenários | Situação |
| :--- | :--- | :--- |
| Protocolo | Campo obrigatório vazio, placa incompleta e Renavam curto no Requerimento Geral | Executáveis |
| Chatbot | Entrada vazia, só espaços, texto incoerente, pergunta fora do escopo e símbolos ou emojis | Executáveis |
| Atendimento | Roteiro de observação: resumo antes da ação final, voltar, cancelar | Qualitativo; só entra em M3 se ocorrer erro |
| Infração | Cenários definidos para CPF, placa e RENAVAM | **Não aplicáveis**: a consulta usa o veículo da conta logada e não tem campo de entrada |

**Tabela 2 – Cenários de erro por módulo.** Fonte: Elaborado pelos autores.

**Limitação.** O módulo de Infração não atinge o mínimo de dois cenários executáveis por desenho do portal. Os cenários de anexo inválido do Protocolo não são executados, porque a tela de anexos só vem depois da assinatura com gov.br, que tem validade legal.

### 6.3 Plano do teste com participantes (M1, M2, M3 e M5)

O plano completo, o roteiro do moderador, o termo de consentimento, a regra de auxílio externo, o teto de tempo, a rotação das tarefas e os campos do registro estão em `roteiro-moderador.md` (PR #78). O SUS está em `sus-ptbr.md`. Resumo:

| Item | Definição |
| :--- | :--- |
| Amostra | Mínimo de **6 participantes**, maiores de 18 anos, com 3 em desktop e 3 em mobile e ao menos 1 cidadão de baixo letramento em cada dispositivo |
| Denominador de M1 | N_tot = 24 (6 × 4 tarefas); N_tot = 18 se a T1 sair (Seção 6.1) |
| Tratamento dos dados | **Pseudonimização** por código (P01, P02, ...); termo assinado guardado fora do repositório |
| Conta gov.br | De **terceiro, com consentimento**; nome e dados do titular aparecem na tela e na gravação, e o termo avisa o participante |
| Gravação | Tela **e áudio**, com consentimento; não versionada |
| SUS | Uma vez por participante, ao portal como um todo, **sem considerar o login do gov.br** |

**Tabela 3 – Resumo do plano do teste.** Fonte: Elaborado pelos autores, a partir do `roteiro-moderador.md`.

A amostra é de conveniência e tem finalidade diagnóstica. Os resultados valem para ela e não se generalizam.

### 6.4 Protocolo de inspeção heurística (M4)

O protocolo está em `guia-severidade.md` (PR #77): heurísticas **NH1 a NH10**, guia de severidade com exemplos fictícios, regras de duplicidade e de desempate, `dispositivos_afetados`, calibração, cópias por avaliador (`inspecao-heuristica_N.csv`, `_Y.csv`, `_T.csv`) e o arquivo consolidado. As capturas ficam em `docs/img/usabilidade/`, com o padrão de nomes do `README.md` da pasta.

---

## 7. Ferramentas e Ambiente

| Item | Uso |
| :--- | :--- |
| Navegador em janela anônima | Início de cada tarefa sem sessão anterior |
| Desktop e celular em modo retrato | Contextos de acesso; registrar sistema operacional, navegador e faixa de largura |
| Conta gov.br de terceiro, com consentimento | Login nas tarefas T1 a T3; os dados do titular aparecem na tela e na gravação |
| Gravação de **tela e de áudio** (com consentimento) | Conferência da contagem de passos; não é versionada |
| Planilhas (CSV) | Registro de tarefas, cenários, inspeção e SUS |

Os resultados refletem a versão do portal na data da coleta. Data, navegador, dispositivo e faixa de largura são registrados em cada sessão (o horário exato não é guardado, para reduzir o risco de reidentificação).

---

## 8. Matriz de Rastreabilidade (Fase 2 → Fase 3)

Issues: [#55](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/55) (inspeção), [#56](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/56) (sessões) e [#57](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/57) (cálculo).

| Questão | Hipótese | Métrica | Medidas básicas | Instrumento | Tarefa ou cenário | Execução | Cálculo e julgamento |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| **Q1** Aprendibilidade | H1 | **M1 – TCAPA** | N_aut, N_tot | `registro-tarefas.csv` | T1 a T4 | #56 | #57 |
| **Q2** Operabilidade | H2 | **M2 – IEFO** | P_min, P_exec | `registro-tarefas.csv` e `tarefas-e-fluxos.csv` | T1 a T4 | #56 | #57 |
| **Q3** Proteção contra erros | H3 | **M3 – TPRE** | E_prev, E_tot | `cenarios-de-erro.csv` e `cenarios-de-erro-sessoes.csv` | E-PRO, E-BOT e E-ATE | #56 | #57 |
| **Q2 e Q3** | H2, H3 | **M4 – IPH** | N₁ a N₄ por módulo | `inspecao-heuristica.csv` | Inspeção dos 4 módulos × 2 dispositivos | #55 | #57 |
| **Q1 e Q2** | H1, H2 | **M5 – SUS** | R₁ a R₁₀ | `sus-respostas.csv` | Aplicado após as tarefas | #56 | #57 |

**Tabela 4 – Matriz de rastreabilidade para Capacidade de Interação.** Fonte: Elaborado pelos autores.

**Níveis de pontuação (Fase 2).** Aplicam-se a M1, M2 e M3, separadamente a cada métrica. M4 e M5 não têm faixas e são apresentados diretamente.

| Nível | TCAPA (M1) | IEFO (M2) | TPRE (M3) |
| :---: | :---: | :---: | :---: |
| Excelente | ≥ 90% | ≥ 90% | ≥ 95% |
| Bom | 80% a < 90% | 80% a < 90% | 85% a < 95% |
| Satisfatório | 70% a < 80% | 70% a < 80% | 75% a < 85% |
| Insuficiente | < 70% | < 70% | < 75% |

**Tabela 5 – Níveis de julgamento.** Fonte: Fase 2. Com 3 tarefas por módulo e dispositivo, os percentuais saem em múltiplos de 33%: por célula, relatar **contagens** e aplicar as faixas só ao total da métrica.

**Hipóteses a verificar.** H1: facilidade de aprendizado maior em Infração e Chatbot do que em Protocolo e Atendimento. H2: operabilidade melhor em desktop do que em mobile. H3: fragilidades na proteção contra erros. São expectativas e não resultados constatados. Cada uma será confirmada, refutada ou considerada inconclusiva na Fase 4.

---

## 9. Responsabilidades

| Atividade | Issue | Responsável |
| :--- | :---: | :--- |
| Catálogo de tarefas e fluxos | [#50](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/50) | Natan |
| Cenários de erro | [#51](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/51) | Natan |
| Plano do teste e instrumentos | [#52](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/52) | Natan |
| Protocolo heurístico | [#53](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/53) | Yan |
| Consolidação da Fase 3 e piloto | [#54](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/54) | Natan |
| Inspeção heurística (execução) | [#55](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/55) | Yan e Natan, de forma independente |
| Sessões com participantes (execução) | [#56](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/56) | Yan e Natan, **alternando** os papéis de moderador e observador |
| Cálculo, julgamento e GQM | [#57](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY/issues/57) | Yan |

**Tabela 6 – Responsabilidades da dupla.** Fonte: Elaborado pelos autores, a partir das issues. A divisão das sessões da #56 é uma **proposta para confirmação da dupla**, em especial pela concentração de issues com o Natan.

Nas sessões, quem modera não conta passos, e quem observa não interfere. Os dois alternam os papéis entre participantes.

---

## 10. Cronograma da Coleta

As datas abaixo são uma **proposta**, a confirmar pela dupla e pelo docente. Em 20/11/2026 (sexta-feira, feriado nacional da Consciência Negra) a coleta ainda não começou, e 21 e 22/11 são sábado e domingo; por isso o cronograma usa dias úteis a partir de 23/11. Isso **ultrapassa o encerramento da Fase 4 em 22/11**: o critério "cronograma termina antes de 22/11" se refere à **coleta**, e não pode ser cumprido com as datas reais. É preciso **confirmar com o docente o novo prazo** antes de seguir.

| Rodada | Período | Atividade | Métricas | Issue |
| :---: | :---: | :--- | :---: | :---: |
| **R0** | 20/11 | Piloto dos instrumentos ([página do piloto](piloto-usabilidade.md)) | M1 a M5 | #54 |
| **R1** | 20/11 a 24/11 (**corte em 24/11**) | Recrutamento; obter a conta com veículo; confirmar a questão do comitê de ética com o docente | – | #54 |
| **R2** | 23/11 a 25/11 | Inspeção heurística **independente**, com calibração antes; cada avaliador entrega a lista individual **antes de moderar qualquer sessão** | M4 | #55 |
| **R3** | 25/11 (P00) e 26/11 a 27/11 (sessões); **30/11 reserva** | Sessão P00 fora da amostra, sessões com os participantes e SUS | M1, M2, M3, M5 | #56 |
| **R4** | 30/11 | Consolidação das listas heurísticas e conferência dos registros | M4 | #55 |
| **R5** | 30/11 a 01/12 | Cálculo das métricas, julgamento e respostas GQM | M1 a M5 | #57 |
| **R6** | A partir de 01/12 | Oportunidades, protótipo e validação (Fase 4) | – | #58, #59 e #60 |

**Tabela 7 – Cronograma de coleta (proposta).** Fonte: Elaborado pelos autores.

- **A mesma dupla** faz a inspeção (R2) e modera as sessões (R3). Por isso a inspeção termina **antes** das sessões: ver os participantes antes de fechar a lista comprometeria a independência.
- **Data de corte do recrutamento: 24/11.** Se até lá houver menos de 6 participantes: com **4 ou 5** (ao menos 2 por dispositivo), a coleta segue com N_tot reduzido e a limitação registrada; com **menos de 4**, a dupla pede ao docente prorrogação ou a coleta é registrada como inconclusiva para M1 a M3.
- A decisão sobre a T1 (Seção 6.1) também é tomada na data de corte.
- Os participantes da validação do protótipo (#60) devem ser, preferencialmente, outros, porque quem fez o teste deixa de estar em primeiro acesso.

---

## 11. Piloto dos Instrumentos

O piloto é descrito em [piloto-usabilidade.md](piloto-usabilidade.md), com resultados, achados e capturas. Resumo do que ele **valida e não valida**:

| Instrumento | Situação |
| :--- | :--- |
| Catálogo de tarefas (T1 a T4) | Conciliado pelos dois avaliadores (consenso nos 8 casos) |
| Cenários de erro (M3) | Executados pelos avaliadores em Protocolo e Chatbot; Infração não aplicável |
| Percurso de T1 a T4 e contagem de passos | Percorrido com assistente de navegador (T1 a T3 em desktop; T4 em desktop e em mobile **emulado**); valida o caminho, as telas e a regra de contagem, **não** o comportamento de um participante. Os passos de login e a T1 com conta com veículo estão pendentes |
| Roteiro do moderador, regra de auxílio, tempo de sessão | **Pendentes**: dependem de uma sessão com pessoa real (P00, Seção 10) |
| `sus-respostas.csv` | Cálculo conferido em script com os valores-limite 100, 0 e 50 e o exemplo de 85; a conferência **na planilha** está pendente |
| `inspecao-heuristica.csv` | Pendente: calibração e consolidação com os dois avaliadores (R2) |

**Tabela 8 – Situação do piloto.** O piloto **não é critério de aceitação deste PR**: o que depende de pessoas é executado na rodada R0/R3 e acompanhado na issue #54. Os dados do piloto **não entram** nos resultados da avaliação.
