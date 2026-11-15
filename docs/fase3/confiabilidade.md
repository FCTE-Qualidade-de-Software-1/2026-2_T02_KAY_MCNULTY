# Plano de Avaliação – Característica: Confiabilidade

Este plano é a Fase 3 (Projeto da Avaliação) do processo ISO/IEC 25040 para a característica de **Confiabilidade**. Ele define como as métricas M1 a M6, especificadas na [Fase 2](../fase2/confiabilidade.md), serão obtidas no Portal Detran Digital DF, com quais recursos, em que ambiente e em que prazo. A profundidade em cada módulo e os limites do escopo seguem a [seção 4 do escopo da Fase 1](../fase1/escopo-limites.md).

A avaliação é uma auditoria externa em produção. Tudo o que é medido é o comportamento observável no cliente, e nenhuma medição pode prejudicar cidadãos nem o serviço.

---

## 1. Método de Avaliação

### 1.1 Visão geral

| Métrica | Questão | O que é medido | Forma de coleta | Rodadas |
| :--- | :---: | :--- | :--- | :--- |
| M1 – TDO | Q1 | Disponibilidade das páginas públicas e do widget do Chatbot | Monitoramento automatizado | Verificação a cada 15 min durante a janela de observação |
| M2 – TCFF | Q2 | Conclusão dos fluxos principais sem falha | Execução manual dos fluxos | 5 execuções por fluxo |
| M3 – DFF | Q2 | Falhas distintas por fluxo | Classificação sobre os registros da M2 | Mesmas execuções da M2 |
| M4 – TTOA | Q3 | Tolerância a operações anômalas | Execução manual de cenários anômalos | 1 execução por cenário |
| M5 – TRTI | Q4 | Retomada da tarefa após interrupção | Execução manual de cenários de interrupção | 1 execução por cenário |
| M6 – TMR | Q4 | Tempo de retomada | Cronometragem sobre as gravações da M5 | Mesmos cenários da M5 |

**Tabela 1 – Visão geral dos métodos de coleta.** Fonte: elaboração da equipe.

### 1.2 Fluxos, cenários anômalos e cenários de interrupção

Os conjuntos abaixo definem os totais das medidas básicas Fₑₓₑ, Sₜₒₜ e Rₜₒₜ da Fase 2.

| Fluxo | Módulo | Descrição | Limite da execução |
| :---: | :--- | :--- | :--- |
| F1 | Infração | Consulta de débitos por placa e RENAVAM | Consulta, sem pagamento |
| F2 | Infração | Detalhamento de um auto de infração | Visualização |
| F3 | Infração | Emissão da guia (DUD ou PIX) | Emissão, sem pagamento |
| F4 | Atendimento | Agendamento de serviço presencial | Até a etapa anterior à confirmação definitiva |
| F5 | Protocolo | Preenchimento e anexação de documentos | Até a etapa anterior ao envio definitivo |
| F6 | Chatbot | Diálogo de perguntas frequentes | Conversa completa |

**Tabela 2 – Fluxos da M2 e da M3.** Fₑₓₑ = 6 fluxos × 5 execuções = 30 execuções. Fonte: elaboração da equipe.

| Cenário | Módulo | Operação anômala |
| :---: | :--- | :--- |
| A1 | Infração | Placa inválida |
| A2 | Infração | CPF ou RENAVAM inválido |
| A3 | Infração | Campo obrigatório vazio |
| A4 | Infração | Envio duplicado (duplo clique) |
| A5 | Atendimento | Horário indisponível |
| A6 | Atendimento | Uso do botão voltar durante o agendamento |
| A7 | Protocolo | Arquivo fora do padrão (formato ou tamanho) |
| A8 | Protocolo | Envio duplicado |
| A9 | Chatbot | Mensagem vazia |
| A10 | Chatbot | Mensagem extensa e com caracteres especiais |

**Tabela 3 – Cenários anômalos da M4.** Sₜₒₜ = 10 cenários. Fonte: elaboração da equipe.

| Cenário | Módulo | Interrupção |
| :---: | :--- | :--- |
| B1 | Infração | Recarga da página no meio da consulta |
| B2 | Infração | Perda de conexão (modo offline) durante a emissão da guia |
| B3 | Atendimento | Sessão invalidada durante o agendamento |
| B4 | Atendimento | Recarga da página antes da confirmação |
| B5 | Protocolo | Recarga da página com o formulário preenchido |
| B6 | Protocolo | Perda de conexão durante o upload do anexo |
| B7 | Chatbot | Recarga da página no meio da conversa |
| B8 | Chatbot | Perda de conexão durante a conversa |

**Tabela 4 – Cenários de interrupção da M5 e da M6.** Rₜₒₜ = 8 cenários. Fonte: elaboração da equipe.

### 1.3 Instruções de coleta

**M1 – Taxa de Disponibilidade Observada (TDO)**

1. Configurar o monitor com a lista de endereços públicos monitorados: página inicial, páginas públicas de cada um dos módulos e o widget do Chatbot.
2. A cada 15 minutos, carregar cada endereço em um navegador automatizado e registrar uma linha no CSV: data e hora, endereço, código HTTP, indicador de elemento esperado renderizado (sim ou não) e tempo de carga.
3. Contar como verificação com sucesso (Cₒₖ) a que retornou HTTP 2xx ou 3xx e renderizou o elemento esperado. Contar todas as verificações em Cₜₒₜ.
4. Registrar à parte qualquer manutenção anunciada pelo órgão e calcular a TDO com e sem exclusão dessas janelas.
5. Ao fim da janela, calcular TDO = Cₒₖ / Cₜₒₜ × 100%.

Como o portal é uma aplicação de página única, um código HTTP 200 não prova que a página funciona. Por isso a verificação exige que um elemento visível da página seja renderizado.

**M2 e M3 – Conclusão de fluxos e densidade de falhas**

1. Executar cada fluxo da Tabela 2 cinco vezes, em dias e horários diferentes: duas em horário de pico (manhã ou início da tarde de dia útil), duas fora do pico e uma à noite.
2. Gravar a tela durante a execução e guardar a aba de rede do navegador quando houver erro.
3. Registrar cada execução na planilha: fluxo, data e hora, resultado (concluída sem falha ou com falha), descrição da falha e nome do arquivo de evidência.
4. Contar em Fₒₖ as execuções concluídas sem falha e calcular TCFF = Fₒₖ / Fₑₓₑ × 100%.
5. Classificar cada falha pela causa observável. Falhas com a mesma causa contam uma vez (Fd). Calcular DFF = Fd / 6.

**M4 – Taxa de Tolerância a Operações Anômalas (TTOA)**

1. Executar cada cenário da Tabela 3 uma vez, na etapa do fluxo indicada.
2. Registrar o comportamento do portal e o código HTTP das respostas.
3. Contar o cenário como tolerado (Sₜₒₗ) quando o portal continua operante e consistente e mostra uma mensagem compreensível. Não é tolerado: erro 5xx, tela em branco, travamento ou perda de estado.
4. Calcular TTOA = Sₜₒₗ / 10 × 100%.

**M5 e M6 – Recuperação após interrupção e tempo de recuperação**

1. Para cada cenário da Tabela 4, iniciar a gravação de tela, avançar o fluxo até o ponto indicado e provocar a interrupção (recarga, modo offline pelo navegador ou limpeza da sessão).
2. Restabelecer as condições normais e tentar retomar a tarefa de onde parou.
3. Contar o cenário como recuperado (Rₒₖ) quando a tarefa é retomada sem perda de dados. Calcular TRTI = Rₒₖ / 8 × 100%.
4. Na gravação, cronometrar o intervalo entre o restabelecimento das condições normais e a retomada da tarefa (Tᵢ), em segundos. Calcular TMR = Σ Tᵢ / Rᵣₑₜ, considerando só os cenários com retomada.

### 1.4 Repetibilidade

Cada passo acima usa só ferramentas públicas e registra a evidência em arquivo, de modo que outra pessoa consiga repetir a medição e comparar os resultados. Qualquer desvio em relação a este plano deve ser registrado na planilha de coleta, com data e motivo.

---

## 2. Recursos e Ambiente de Avaliação

### 2.1 Ambiente de referência

| Item | Configuração adotada |
| :--- | :--- |
| Navegador | Google Chrome, versão estável mais recente, sem extensões |
| Dispositivo | Computador pessoal (desktop) com resolução de 1366 por 768 |
| Rede | Conexão residencial de banda larga no Distrito Federal |
| Perfil do navegador | Perfil limpo (sem cache e sem cookies) no início de cada execução |
| Monitoramento (M1) | Navegador automatizado em máquina ligada de forma contínua durante a janela |

**Tabela 5 – Ambiente de referência.** A variação entre navegadores e resoluções é objeto da Compatibilidade e não é avaliada aqui. Fonte: elaboração da equipe.

### 2.2 Ferramentas

| Ferramenta | Uso |
| :--- | :--- |
| Playwright (navegador automatizado) | Verificação da M1 e checagem do elemento renderizado |
| Ferramentas do desenvolvedor do navegador (aba de rede) | Registro de códigos HTTP, simulação de modo offline e limpeza de sessão |
| Gravador de tela | Evidência das execuções da M2, M4 e M5 e base da cronometragem da M6 |
| Cronômetro sobre a gravação | Medida Tᵢ da M6 |
| Planilha (CSV) | Registro das execuções, com o modelo da seção 2.4 |
| Git e GitHub | Versionamento dos dados brutos e das evidências |

**Tabela 6 – Ferramentas.** Fonte: elaboração da equipe.

### 2.3 Dados de teste e cuidados éticos

* Consultas válidas usam a placa e o CPF do próprio avaliador, com consentimento dele. Não se consultam dados de terceiros.
* Os dados de entrada inválidos (placas, CPF e RENAVAM) são fictícios e criados só para o teste.
* Os fluxos autenticados pelo Gov.br usam a conta pessoal de um integrante, executados manualmente. As credenciais nunca vão para o repositório.
* Nenhum dado pessoal aparece nas evidências versionadas: capturas e gravações devem ter CPF, nome e placa ocultados.
* Não se realiza pagamento, nenhum processo é protocolado no SEI-GDF e nenhum agendamento é mantido. Se um agendamento precisar chegar à confirmação, é cancelado em seguida.
* Não há teste de carga, estresse ou injeção de falhas. O monitoramento da M1 faz uma verificação a cada 15 minutos por endereço, volume que não afeta o serviço.

### 2.4 Modelos de registro

| Arquivo | Conteúdo | Métricas |
| :--- | :--- | :--- |
| `disponibilidade.csv` | data_hora, endereço, codigo_http, elemento_renderizado, tempo_carga_ms, manutencao_anunciada | M1 |
| `fluxos.csv` | fluxo, execucao, data_hora, resultado, causa_da_falha, evidencia | M2 e M3 |
| `anomalias.csv` | cenario, data_hora, comportamento, codigo_http, tolerado, evidencia | M4 |
| `interrupcoes.csv` | cenario, data_hora, recuperado, tempo_recuperacao_s, evidencia | M5 e M6 |

**Tabela 7 – Arquivos de dados brutos.** Os arquivos ficam em `docs/dados/confiabilidade/`, e as evidências em subpastas por métrica. Gravações muito grandes são guardadas fora do repositório, com o link registrado no `fluxos.csv`, `anomalias.csv` ou `interrupcoes.csv`. Fonte: elaboração da equipe.

### 2.5 Conhecimento exigido do avaliador

Familiaridade básica com o navegador e suas ferramentas do desenvolvedor, e leitura dos roteiros da seção 1.3. A configuração do monitor da M1 exige conhecimento de Playwright, e quem a executar deve ser o integrante que a configurou.

---

## 3. Cronograma Operacional

O cronograma segue o [calendário oficial da disciplina](../gestao/metricas-psm.md#linha-do-tempo-ate-a-entrega-final): Ponto de Controle 2 em 16/11 ou 18/11 e entrega final em 22/11.

| Período | Atividade | Issue |
| :--- | :--- | :---: |
| 15/11 | Plano de avaliação pronto e piloto do monitor da M1. Início do monitoramento | #46 |
| 15/11 a 21/11 | Janela de observação da M1 | #47 |
| 16/11 a 19/11 | Execução manual da M2, M3, M4, M5 e M6 e registro dos dados brutos | #47 |
| 20/11 | Cálculo das métricas, julgamento e respostas ao GQM | #48 |
| 20/11 a 21/11 | Ação técnica de melhoria | #49 |
| 20/11 a 21/11 | Artigo v2 e atualização do GitPage | #45 |
| 22/11 | Entrega final | |

**Tabela 8 – Cronograma operacional da Confiabilidade.** Fonte: elaboração da equipe.

### 3.1 Desvio em relação à Fase 2

A Fase 2 especifica que o monitoramento da M1 dura 14 dias. Com a entrega final em 22/11 e a Fase 3 concluída em 15/11, só cabem 7 dias de observação, de 15/11 a 21/11. Com uma verificação a cada 15 minutos, isso dá 672 verificações por endereço, em vez das 1.344 previstas.

A decisão é manter o intervalo de 15 minutos e reduzir a janela. As consequências são registradas no julgamento da Fase 4: a TDO representa só esses 7 dias e não deve ser lida como disponibilidade média do portal, e o desvio será citado no artigo. Os níveis de pontuação da Fase 2 não mudam.

---

## 4. Matriz de Rastreabilidade (Fase 2 para Fase 3)

A matriz mostra que cada elemento da especificação da Fase 2 tem um método e um recurso correspondente na Fase 3.

| Métrica | Questão e hipótese | Medidas básicas (Fase 2) | Método (Fase 3) | Recurso e evidência | Níveis de pontuação (Fase 2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| M1 – TDO | Q1, H1 | Cₒₖ, Cₜₒₜ | Seção 1.3, M1 | Playwright e `disponibilidade.csv` | Excelente ≥ 99,5%; Bom 98% a < 99,5%; Satisfatório 95% a < 98%; Insuficiente < 95% |
| M2 – TCFF | Q2, H2 | Fₒₖ, Fₑₓₑ | Seção 1.3, M2 e M3 | Tabela 2, gravação de tela e `fluxos.csv` | Excelente ≥ 95%; Bom 85% a < 95%; Satisfatório 70% a < 85%; Insuficiente < 70% |
| M3 – DFF | Q2, H2 | Fd, Flₜₒₜ | Seção 1.3, M2 e M3 | Tabela 2 e `fluxos.csv` | Excelente 0; Bom > 0 a ≤ 0,5; Satisfatório > 0,5 a ≤ 1,0; Insuficiente > 1,0 |
| M4 – TTOA | Q3, H3 | Sₜₒₗ, Sₜₒₜ | Seção 1.3, M4 | Tabela 3, aba de rede e `anomalias.csv` | Excelente ≥ 95%; Bom 85% a < 95%; Satisfatório 70% a < 85%; Insuficiente < 70% |
| M5 – TRTI | Q4, H4 | Rₒₖ, Rₜₒₜ | Seção 1.3, M5 e M6 | Tabela 4, gravação de tela e `interrupcoes.csv` | Excelente ≥ 90%; Bom 75% a < 90%; Satisfatório 60% a < 75%; Insuficiente < 60% |
| M6 – TMR | Q4, H4 | Tᵢ, Rᵣₑₜ | Seção 1.3, M5 e M6 | Cronometragem sobre a gravação e `interrupcoes.csv` | Excelente ≤ 30 s; Bom > 30 a ≤ 60 s; Satisfatório > 60 a ≤ 120 s; Insuficiente > 120 s |

**Tabela 9 – Rastreabilidade entre a Fase 2 e a Fase 3.** Fonte: elaboração da equipe, com base na [Fase 2](../fase2/confiabilidade.md).

A agregação das notas (Q1 = M1; Q2 = média de M2 e M3; Q3 = M4; Q4 = média de M5 e M6; G1 = média das quatro questões) e a regra de ressalva quando uma questão recebe nota 1 permanecem como definidas na Fase 2 e serão aplicadas na Fase 4.
