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
| INF-01 | Infração | Consulta de débitos por placa e RENAVAM | Consulta, sem pagamento |
| INF-02 | Infração | Detalhamento de um auto de infração | Visualização |
| INF-03 | Infração | Emissão da guia (DUD ou PIX) | Emissão, sem pagamento |
| ATE-01 | Atendimento | Agendamento de serviço presencial | Até a etapa anterior à confirmação definitiva |
| PRO-01 | Protocolo | Preenchimento e anexação de documentos | Até a etapa anterior ao envio definitivo |
| CHA-01 | Chatbot | Diálogo de perguntas frequentes | Conversa completa |

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
| A8 | Protocolo | Duplo clique em avançar ou anexar, na etapa anterior ao envio definitivo |
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

1. Configurar o monitor com os alvos da Tabela 5, todos acessíveis sem login, e com o elemento esperado de cada um. O monitor principal é um navegador automatizado (Playwright), em máquina ligada de forma contínua durante a janela.
2. A cada 15 minutos, carregar cada alvo e registrar uma linha no CSV: data e hora, endereço, código HTTP, indicador de elemento esperado renderizado (sim ou não), tempo de carga e resultado do alvo de controle no mesmo ciclo. O tempo limite é de 20 s por alvo, sem nova tentativa: uma verificação que falha é registrada como falha.
3. Contar como verificação com sucesso (Cₒₖ) a que retornou HTTP 2xx ou 3xx e renderizou o elemento esperado. Contar todas as verificações válidas em Cₜₒₜ.
4. Se o alvo de controle (C01) também falhar no mesmo ciclo, marcar o ciclo como falha local (computador ou rede do monitor) e excluí-lo de Cₜₒₜ. Ciclos perdidos e lacunas no CSV são registrados e reportados junto com o TDO.
5. Registrar à parte qualquer manutenção anunciada pelo órgão e calcular a TDO com e sem exclusão dessas janelas.
6. Ao corte dos dados (Tabela 9), calcular TDO = Cₒₖ / Cₜₒₜ × 100%.
7. Como segunda fonte independente, um workflow agendado do GitHub Actions executa o script `.github/scripts/monitor_m1.py` com os mesmos alvos e grava o resultado na branch `monitoramento-m1`. A segunda fonte serve para comparação e não substitui o monitor principal.
8. O CSV do monitor principal é versionado no repositório ao fim de cada dia de coleta, em `docs/dados/confiabilidade/`.

| ID | Alvo | Endereço | Elemento esperado |
| :---: | :--- | :--- | :--- |
| A01 | Portal (página inicial) | `https://portal.detran.df.gov.br/` | Elemento `app-header` renderizado (Playwright); texto `Detran Digital` no HTML (workflow) |
| A02 | Widget do Chatbot (script) | `https://bot-server.s3.amazonaws.com/api/inbot.gz.js?bot_id=1010&bot_token=45lyi7gjii&bot_server_type=production` | Texto `inbot.js-loaded` |
| A03 | Widget do Chatbot (montado na página) | Página inicial (A01) | Elemento `#divtoincludechat` com conteúdo renderizado (somente Playwright) |
| A04 | Endpoints públicos do portal | **A DEFINIR** (identificados pela aba de rede, sem login) | **A DEFINIR** |
| C01 | Controle (fora do portal) | `https://example.com/` | Texto `Example Domain` |

**Tabela 5 – Alvos do monitoramento (M1).** O alvo C01 não faz parte do cálculo do TDO e serve apenas para identificar falhas locais do monitor. Fonte: elaboração da equipe.

Como o portal é uma aplicação de página única, um código HTTP 200 não prova que a página funciona. Por isso a verificação exige que um elemento visível da página seja renderizado.

Os módulos de Infração e Protocolo exigem login e, em conformidade com a definição da M1 na Fase 2, não são monitorados automaticamente. A acessibilidade deles é observada nas execuções manuais da M2: o primeiro passo de cada fluxo é o acesso ao módulo, e uma falha nele é registrada como falha do fluxo.

**M2 e M3 – Conclusão de fluxos e densidade de falhas**

1. Executar cada fluxo da Tabela 2 cinco vezes, em dias e horários diferentes: duas em horário de pico (dias úteis, das 8h às 12h ou das 13h às 15h), duas fora do pico (dias úteis, das 15h às 19h) e uma à noite (das 20h às 23h).
2. Gravar a tela durante a execução e guardar a aba de rede do navegador quando houver erro.
3. Registrar cada execução na planilha: fluxo, data e hora, resultado (concluída sem falha ou com falha), descrição da falha, origem da falha (seção 1.4) e nome do arquivo de evidência.
4. Contar em Fₒₖ as execuções concluídas sem falha e calcular TCFF = Fₒₖ / Fₑₓₑ × 100%.
5. Classificar cada falha pela causa observável. Falhas com a mesma causa contam uma vez (Fd). Calcular DFF = Fd / 6.

**M4 – Taxa de Tolerância a Operações Anômalas (TTOA)**

1. Executar cada cenário da Tabela 3 uma vez, na etapa do fluxo indicada.
2. Registrar o comportamento do portal, o código HTTP das respostas e a origem de qualquer falha (seção 1.4).
3. Contar o cenário como tolerado (Sₜₒₗ) quando o portal continua operante e consistente e mostra uma mensagem compreensível. Não é tolerado: erro 5xx, tela em branco, travamento ou perda de estado.
4. Calcular TTOA = Sₜₒₗ / 10 × 100%.

**M5 e M6 – Recuperação após interrupção e tempo de recuperação**

1. Para cada cenário da Tabela 4, iniciar a gravação de tela, avançar o fluxo até o ponto indicado e provocar a interrupção (recarga, modo offline pelo navegador ou limpeza da sessão).
2. Restabelecer as condições normais e tentar retomar a tarefa de onde parou.
3. Contar o cenário como recuperado (Rₒₖ) quando a tarefa é retomada sem perda de dados. Nos cenários do Chatbot (B7 e B8), a recarga que reinicia a conversa sem o histórico anterior conta como perda de dados. Calcular TRTI = Rₒₖ / 8 × 100%.
4. Na gravação, cronometrar o intervalo entre o restabelecimento das condições normais e a retomada da tarefa (Tᵢ), em segundos. O restabelecimento é o instante em que a página termina de recarregar (recarga), em que o modo offline é desativado (perda de conexão) ou em que a sessão é limpa (sessão invalidada). A retomada é o instante em que o avaliador consegue continuar do ponto em que parou, ou, quando a tarefa precisa recomeçar, em que ele volta ao mesmo ponto. No cenário B3, o novo login faz parte do tempo. Calcular TMR = Σ Tᵢ / Rᵣₑₜ, considerando só os cenários com retomada.

### 1.4 Definições operacionais

* **Fluxo:** sequência de passos de um serviço, do acesso à conclusão ou à última etapa reversível.
* **Falha:** comportamento que impede a conclusão do fluxo ou compromete seu resultado (erro HTTP não previsto, tela em branco, travamento, redirecionamento indevido ou perda de dados). Considera-se travamento a tela sem resposta visível por mais de 20 s.
* **Operação anômala:** entrada inválida ou ação atípica (envio duplicado, campo vazio, arquivo inválido, botão voltar).
* **Interrupção:** perda temporária das condições normais (recarga, perda de conexão ou sessão invalidada).
* **Origem da falha:** portal, Gov.br, SEI-GDF ou chatbot de terceiro (serviço InBot). A falha em integração durante o fluxo conta como falha do módulo avaliado, porque o cidadão não distingue a origem. A origem é registrada para analisar as hipóteses H1 e H2 da Fase 2.
* **Falha local:** problema no computador, na rede ou na conta do avaliador, comprovado por teste com um site de controle. Não conta como falha do portal, e a execução é repetida.
* **Acesso indisponível:** indisponibilidade da tela de login do Gov.br antes do início do fluxo. A execução é registrada com origem Gov.br, repetida em outro horário e não entra em Fₑₓₑ. A quantidade desses registros é reportada junto com os resultados.

### 1.5 Repetibilidade

Cada passo acima usa só ferramentas públicas e registra a evidência em arquivo, de modo que outra pessoa consiga repetir a medição e comparar os resultados. Qualquer desvio em relação a este plano deve ser registrado na planilha de coleta, com data e motivo.

---

## 2. Recursos e Ambiente de Avaliação

### 2.1 Ambiente de referência

| Item | Configuração adotada |
| :--- | :--- |
| Navegador | Google Chrome, versão estável mais recente, sem extensões |
| Dispositivo | Computador pessoal (desktop) com resolução de 1366 por 768 |
| Rede | Conexão residencial de banda larga no Distrito Federal |
| Perfil do navegador | Perfil limpo (sem cache e sem cookies) no início de cada sessão de teste. A sessão autenticada é mantida entre os fluxos da mesma sessão, exceto no cenário B3 |
| Monitoramento (M1) | Navegador automatizado em máquina ligada de forma contínua durante a janela, mais o workflow do GitHub Actions como segunda fonte |

**Tabela 6 – Ambiente de referência.** A variação entre navegadores e resoluções é objeto da Compatibilidade e não é avaliada aqui. Fonte: elaboração da equipe.

### 2.2 Ferramentas

| Ferramenta | Uso |
| :--- | :--- |
| Playwright (navegador automatizado) | Verificação da M1 e checagem do elemento renderizado |
| Python e GitHub Actions | Segunda fonte da M1 (`monitor_m1.py`, dados na branch `monitoramento-m1`) |
| Ferramentas do desenvolvedor do navegador (aba de rede) | Registro de códigos HTTP, simulação de modo offline e limpeza de sessão |
| Gravador de tela | Evidência das execuções da M2, M4 e M5 e base da cronometragem da M6 |
| Cronômetro sobre a gravação | Medida Tᵢ da M6 |
| Planilha (CSV) | Registro das execuções, com o modelo da seção 2.4 |
| Git e GitHub | Versionamento dos dados brutos e das evidências |

**Tabela 7 – Ferramentas.** Fonte: elaboração da equipe.

### 2.3 Dados de teste e cuidados éticos

* Consultas válidas usam a placa e o CPF do próprio avaliador, com consentimento dele. Não se consultam dados de terceiros.
* Os dados de entrada inválidos (placas, CPF e RENAVAM) são fictícios e criados só para o teste. Os arquivos de anexo do cenário A7 também são fictícios.
* Os fluxos autenticados pelo Gov.br usam a conta pessoal de um integrante, executados manualmente. As credenciais nunca vão para o repositório.
* Capturas de tela versionadas devem ter CPF, nome e placa ocultados. Gravações de tela que exibam dados pessoais não são versionadas no repositório público: ficam em armazenamento de acesso restrito, com o link registrado no CSV e acesso concedido à professora.
* Não se realiza pagamento, nenhum processo é protocolado no SEI-GDF e nenhum agendamento é confirmado. Os fluxos de agendamento e de protocolo param na etapa anterior à confirmação definitiva.
* Não há teste de carga, estresse ou injeção de falhas. O monitoramento da M1 faz uma verificação a cada 15 minutos por endereço, volume que não afeta o serviço.

### 2.4 Modelos de registro

| Arquivo | Conteúdo | Métricas |
| :--- | :--- | :--- |
| `disponibilidade.csv` | data_hora, endereço, codigo_http, elemento_renderizado, tempo_carga_ms, controle_ok, manutencao_anunciada | M1 |
| `disponibilidade_actions.csv` | timestamp_utc, timestamp_brasilia, alvo_id, modulo, url, http_status, tempo_ms, elemento_ok, ok, erro | M1 (segunda fonte) |
| `fluxos.csv` | fluxo, execucao, data_hora, resultado, causa_da_falha, origem_falha, evidencia | M2 e M3 |
| `anomalias.csv` | cenario, data_hora, comportamento, codigo_http, tolerado, origem_falha, evidencia | M4 |
| `interrupcoes.csv` | cenario, data_hora, recuperado, tempo_recuperacao_s, origem_falha, evidencia | M5 e M6 |

**Tabela 8 – Arquivos de dados brutos.** Os arquivos ficam em `docs/dados/confiabilidade/`, e as evidências em subpastas por métrica. O arquivo `disponibilidade_actions.csv` é gerado na branch `monitoramento-m1` e copiado para essa pasta ao fim da janela. Gravações que exibam dados pessoais seguem a regra da seção 2.3, com o link registrado no `fluxos.csv`, `anomalias.csv` ou `interrupcoes.csv`. Fonte: elaboração da equipe.

### 2.5 Conhecimento exigido do avaliador

Familiaridade básica com o navegador e suas ferramentas do desenvolvedor, e leitura dos roteiros da seção 1.3. A configuração do monitor da M1 exige conhecimento de Playwright, e quem a executar deve ser o integrante que a configurou.

---

## 3. Cronograma Operacional

O cronograma segue o [calendário oficial da disciplina](../gestao/metricas-psm.md#linha-do-tempo-ate-a-entrega-final): Ponto de Controle 2 em 16/11 ou 18/11 e entrega final em 22/11.

| Período | Atividade | Responsável | Issue |
| :--- | :--- | :--- | :---: |
| 15/11 | Plano de avaliação pronto e piloto do monitor da M1. Início do monitoramento | João Eduardo e Davi Ursolino | #46 |
| 15/11 a 20/11 (corte às 18h) | Janela de observação da M1 | João Eduardo e Davi Ursolino | #47 |
| 16/11 ou 18/11 | Ponto de Controle 2, com dados parciais da M1 | Equipe | |
| 16/11 a 19/11 | Execução manual da M2, M3, M4, M5 e M6 e registro dos dados brutos | João Eduardo e Davi Ursolino | #47 |
| 20/11 (após o corte) a 21/11 | Cálculo das métricas, julgamento e respostas ao GQM | João Eduardo e Davi Ursolino | #48 |
| 20/11 a 21/11 | Ação técnica de melhoria | Davi Ursolino | #49 |
| 20/11 a 21/11 | Artigo v2 e atualização do GitPage | João Eduardo e Davi Ursolino | #45 |
| 22/11 | Entrega final | Equipe | |

**Tabela 9 – Cronograma operacional da Confiabilidade.** Fonte: elaboração da equipe.

### 3.1 Desvio em relação à Fase 2

A Fase 2 especifica que o monitoramento da M1 dura 14 dias. Com a entrega final em 22/11 e a Fase 3 concluída em 15/11, a janela de observação vai de 15/11 até o corte dos dados em 20/11 às 18h, cerca de 5 dias e 18 horas. Com uma verificação a cada 15 minutos, isso dá até 552 verificações por endereço, em vez das 1.344 previstas.

A decisão é manter o intervalo de 15 minutos e reduzir a janela. As consequências são registradas no julgamento da Fase 4: a TDO representa só esse período e não deve ser lida como disponibilidade média do portal, e o desvio será citado no artigo. Os níveis de pontuação da Fase 2 não mudam.

O TDO usado no artigo é calculado com os dados até o corte. Verificações descartadas por falha local (seção 1.3, passo 4) ficam fora de Cₜₒₜ, e a quantidade delas é reportada junto com o resultado.

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

**Tabela 10 – Rastreabilidade entre a Fase 2 e a Fase 3.** Fonte: elaboração da equipe, com base na [Fase 2](../fase2/confiabilidade.md).

A agregação das notas (Q1 = M1; Q2 = média de M2 e M3; Q3 = M4; Q4 = média de M5 e M6; G1 = média das quatro questões) e a regra de ressalva quando uma questão recebe nota 1 permanecem como definidas na Fase 2 e serão aplicadas na Fase 4.

---

## 5. Limitações do Plano

* **Janela da M1:** a observação cobre menos dias que o previsto na Fase 2 (seção 3.1), e o resultado descreve apenas esse período.
* **Amostras pequenas:** M4 e M5 usam uma execução por cenário, e M2 usa cinco por fluxo. Nessas amostras, um único resultado muda o nível: na M4, 9 de 10 cenários toleram (Bom) e 8 de 10 (Satisfatório). A amostra é pequena e não aleatória, e os resultados não permitem estimar o comportamento geral do portal.
* **Falhas intermitentes:** a Fase 2 prevê erros intermitentes (H2), e eles podem não aparecer nas execuções manuais.
* **Módulos autenticados:** Infração e Protocolo não entram no monitoramento automático da M1. Sua acessibilidade é observada apenas nas execuções manuais, e a nota da Q1 reflete só os alvos públicos.
* **Origem das verificações:** o monitor principal roda de uma conexão residencial no Distrito Federal, e a segunda fonte roda em servidores do GitHub fora do DF. Diferenças entre as duas fontes podem refletir o caminho de rede, e não o portal.
* **Aplicação de página única:** a verificação depende de elementos renderizados no navegador, e a segunda fonte, que lê o HTML bruto, só confirma que o servidor entrega a página.
* **Terceiros:** o Gov.br, o SEI-GDF e o serviço do chatbot (InBot, na Amazon) não estão sob controle do portal, e suas falhas contam como falhas do módulo avaliado (seção 1.4), registradas com a origem.