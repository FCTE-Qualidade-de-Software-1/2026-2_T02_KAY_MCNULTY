# Resultados Empíricos e Julgamento – Característica: Confiabilidade

**Responsáveis:** Davi Ursulino de Oliveira e João Eduardo Pereira Rabelo  
**Característica:** Confiabilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Disponibilidade, Ausência de Falhas, Tolerância a Falhas e Recuperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 4 (Execução e Julgamento da Avaliação – ISO/IEC 25040)

!!! note "Status dos Dados"
    Resultados **parciais**. A coleta manual cobriu 9 das 30 execuções de fluxo previstas, 9 dos 10 cenários anômalos e 3 dos 8 cenários de interrupção. A série da M1 está calculada sobre os dados disponíveis em 20/11/2026 e deve ser recalculada no corte das 18h. Todas as fórmulas usam as quantidades efetivamente executadas, e as diferenças em relação ao plano da [Fase 3](../fase3/confiabilidade.md) estão na seção 6.

---

## 1. Sumário dos Dados Brutos Coletados

### 1.1 Disponibilidade (M1 – TDO)

O workflow do GitHub Actions verificou os alvos públicos do portal, e o resultado de cada verificação está em [`m1/disponibilidade_actions_parcial_20261120.csv`](../dados/confiabilidade/m1/disponibilidade_actions_parcial_20261120.csv). Foram obtidos **15 ciclos** entre 15/11 às 20h42 e 20/11 às 05h58 (horário de Brasília), de cerca de 422 previstos para esse intervalo, porque o agendador do GitHub pulou a maior parte das execuções de 15 minutos. O controle C01 (example.com) respondeu em todos os ciclos, então nenhum ciclo foi excluído como falha local.

| Alvo | Verificações | Sucessos | Taxa | Erros registrados |
| :--- | :---: | :---: | :---: | :--- |
| **A01** – Portal (página inicial) | 15 | 0 | 0,0% | 9 estouros de tempo na conexão TLS; 6 respostas HTTP 200 sem o texto esperado |
| **A02** – Script do widget do Chatbot | 15 | 15 | 100,0% | Nenhum |
| **A04** – Login | 15 | 0 | 0,0% | 5 estouros de tempo na conexão TLS; 10 respostas HTTP 200 sem o texto esperado |
| **A05** – Balcão Virtual | 15 | 0 | 0,0% | 11 estouros de tempo na conexão TLS; 4 respostas HTTP 200 sem o texto esperado |
| **C01** – Controle (não entra no TDO) | 15 | 15 | 100,0% | Nenhum |

*Tabela 1 – Verificações da M1 por alvo (workflow do Actions). Fonte: dados coletados pelos autores.*

O alvo A03 (widget montado na página), verificado pelo Playwright em outra máquina, não está neste conjunto e entra no cálculo final.

### 1.2 Execução dos Fluxos (M2 – TCFF e M3 – DFF)

Os registros estão em [`m2-m3/fluxos.csv`](../dados/confiabilidade/m2-m3/fluxos.csv).

| Fluxo | Módulo | Execuções | Sem falha | Com falha |
| :--- | :--- | :---: | :---: | :---: |
| **INF-01** – Consulta de débitos do veículo | Infração | 3 | 1 | 2 |
| **INF-02** – Detalhe de auto de infração | Infração | 0 | – | – |
| **INF-03** – Emissão da guia | Infração | 0 | – | – |
| **ATE-01** – Agendamento presencial | Atendimento | 2 | 2 | 0 |
| **PRO-01** – Requerimento Geral até a assinatura | Protocolo | 2 | 2 | 0 |
| **CHA-01** – Conversa com o chatbot | Chatbot | 2 | 2 | 0 |
| **Total** | | **9** | **7** | **2** |

*Tabela 2 – Execuções dos fluxos. Fonte: dados coletados pelos autores.*

### 1.3 Operações Anômalas (M4 – TTOA)

Os registros estão em [`m4/anomalias.csv`](../dados/confiabilidade/m4/anomalias.csv).

| Cenário | Módulo | Operação anômala | Resultado | Tolerado |
| :---: | :--- | :--- | :--- | :---: |
| **A1** | Infração | Placa e Renavam inválidos | Alerta "Veículo não encontrado" e formulário operante | Sim |
| **A2** | Infração | Renavam inválido | Mesmo alerta (o formulário não pede CPF) | Sim |
| **A3** | Infração | Campos vazios | Botão Consultar desabilitado, sem mensagem de campo obrigatório | Sim |
| **A4** | Infração | Duplo clique em Consultar | Duas requisições `debitos`, uma 200 e uma 503, sem mensagem de erro | Não |
| **A5** | Atendimento | Horário indisponível | Portal lista só datas e horários com vaga | Sim |
| **A6** | Atendimento | Botão voltar do navegador | Página funciona, mas o formulário volta vazio | Não |
| **A7** | Protocolo | Arquivo fora do padrão | Não executado: o campo de anexo só aparece depois de Avançar com dados reais | – |
| **A8** | Protocolo | Duplo clique em Avançar | Uma única requisição (201) e uma única tela de assinatura | Sim |
| **A9** | Chatbot | Mensagem vazia | Chat ignora, sem erro e sem aviso | Sim |
| **A10** | Chatbot | Mensagem longa com caracteres especiais | Resposta padrão; a tag de script aparece como texto, sem executar | Sim |

*Tabela 3 – Cenários anômalos. Fonte: dados coletados pelos autores.*

### 1.4 Interrupção e Retomada (M5 – TRTI e M6 – TMR)

Os registros estão em [`m5-m6/interrupcoes.csv`](../dados/confiabilidade/m5-m6/interrupcoes.csv). O tempo Tᵢ foi medido sobre a gravação de tela de cada cenário, do fim do restabelecimento (página recarregada ou sessão limpa) até voltar ao mesmo ponto da tarefa.

| Cenário | Módulo | Interrupção | Resultado | Recuperado | Tᵢ (s) |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **B3** | Atendimento | Sessão limpa durante o agendamento | Portal volta à página inicial deslogado; foi preciso entrar de novo e refazer o formulário | Não | 48 |
| **B4** | Atendimento | Recarga com o agendamento preenchido | Formulário volta vazio | Não | 33 |
| **B5** | Protocolo | Recarga com o Requerimento Geral preenchido | Portal volta à tela inicial do Protocolo e o texto se perde | Não | 3 |
| **B1, B2, B7, B8** | Infração e Chatbot | Recarga e perda de conexão | Não executados | – | – |
| **B6** | Protocolo | Perda de conexão no upload | Não executável: não há campo de anexo antes do envio | – | – |

*Tabela 4 – Cenários de interrupção. Fonte: dados coletados pelos autores.*

---

## 2. Medidas Básicas e Cálculo das Métricas

As fórmulas são as da [Fase 2](../fase2/confiabilidade.md) e do plano da [Fase 3](../fase3/confiabilidade.md).

### 2.1 Taxa de Disponibilidade Observada (M1 – TDO)

* **Cₒₖ (verificações com HTTP 2xx/3xx e elemento esperado):** `15`
* **Cₜₒₜ (verificações válidas dos alvos A01, A02, A04 e A05):** `60` (nenhum ciclo foi excluído pelo controle C01)

$$TDO = \left(\frac{C_{ok}}{C_{tot}}\right) \times 100 = \left(\frac{15}{60}\right) \times 100 = 25{,}00\%$$

Esse valor foi calculado conforme o plano, e a seção 4.1 explica por que ele não representa a disponibilidade percebida pelo cidadão.

### 2.2 Taxa de Conclusão de Fluxos sem Falha (M2 – TCFF)

* **Fₒₖ (execuções concluídas sem falha):** `7`
* **Fₑₓₑ (execuções válidas realizadas):** `9`

$$TCFF = \left(\frac{F_{ok}}{F_{exe}}\right) \times 100 = \left(\frac{7}{9}\right) \times 100 = 77{,}78\%$$

### 2.3 Densidade de Falhas por Fluxo (M3 – DFF)

* **Fd (falhas com causas distintas):** `1` (HTTP 503 no endpoint de débitos, que ocorreu nas execuções 1 e 2 do INF-01)
* **Flₜₒₜ (fluxos distintos testados):** `4` (INF-01, ATE-01, PRO-01 e CHA-01)

$$DFF = \frac{F_d}{Fl_{tot}} = \frac{1}{4} = 0{,}25$$

Com os 6 fluxos do plano no denominador, o valor seria 0,17, e o nível é o mesmo. Se o travamento de mais de 20 s com resposta 504, que ocorreu na nova tentativa da execução 1, fosse contado como uma segunda causa, o valor seria 0,50, ainda no mesmo nível.

### 2.4 Taxa de Tolerância a Operações Anômalas (M4 – TTOA)

* **Sₜₒₗ (cenários tolerados):** `7` (A1, A2, A3, A5, A8, A9 e A10)
* **Sₜₒₜ (cenários executados):** `9`

$$TTOA = \left(\frac{S_{tol}}{S_{tot}}\right) \times 100 = \left(\frac{7}{9}\right) \times 100 = 77{,}78\%$$

Se o A7 fosse contado como não tolerado, o valor seria 70,00%, e como tolerado, 80,00%. Nos dois casos o nível é o mesmo.

### 2.5 Taxa de Recuperação após Interrupção (M5 – TRTI)

* **Rₒₖ (cenários retomados sem perda de dados):** `0`
* **Rₜₒₜ (cenários de interrupção executados):** `3`

$$TRTI = \left(\frac{R_{ok}}{R_{tot}}\right) \times 100 = \left(\frac{0}{3}\right) \times 100 = 0{,}00\%$$

### 2.6 Tempo Médio de Retomada (M6 – TMR)

* **Tᵢ (s):** `48`, `33` e `3`
* **Rᵣₑₜ (cenários em que houve retomada):** `3`

$$TMR = \frac{\sum T_i}{R_{ret}} = \frac{48 + 33 + 3}{3} = 28{,}0 \text{ s}$$

O tempo conta a retomada mesmo quando houve perda de dados, porque o avaliador refez a tarefa até voltar ao mesmo ponto. A perda de dados já é penalizada na M5.

---

## 3. Aplicação dos Níveis de Pontuação e Julgamento

| Métrica | Valor Apurado | Faixa de Enquadramento | Nível | Nota |
| :--- | :---: | :---: | :---: | :---: |
| **M1 – TDO** | 25,00% | < 95% | Insuficiente | 1 |
| **M2 – TCFF** | 77,78% | 70% a < 85% | Satisfatório | 2 |
| **M3 – DFF** | 0,25 | > 0 a ≤ 0,5 | Bom | 3 |
| **M4 – TTOA** | 77,78% | 70% a < 85% | Satisfatório | 2 |
| **M5 – TRTI** | 0,00% | < 60% | Insuficiente | 1 |
| **M6 – TMR** | 28,0 s | ≤ 30 s | Excelente | 4 |

*Tabela 5 – Julgamento das métricas de Confiabilidade. Fonte: elaboração dos autores com base nas réguas da Fase 2.*

### 3.1 Agregação por Questão e Objetivo

| Questão | Composição | Nota | Nível |
| :--- | :--- | :---: | :---: |
| **Q1** – Disponibilidade | M1 | 1,0 | Insuficiente |
| **Q2** – Ausência de Falhas | Média de M2 e M3 = (2 + 3) / 2 | 2,5 | Bom |
| **Q3** – Tolerância a Falhas | M4 | 2,0 | Satisfatório |
| **Q4** – Recuperabilidade | Média de M5 e M6 = (1 + 4) / 2 | 2,5 | Bom |
| **G1** – Confiabilidade | Média das quatro questões = (1 + 2,5 + 2 + 2,5) / 4 | 2,0 | Satisfatório, com ressalva |

*Tabela 6 – Notas por questão e objetivo. Fonte: elaboração dos autores com base na regra de agregação da Fase 2.*

Como a Q1 recebeu nota 1, a regra da Fase 2 exige que o julgamento de G1 seja registrado com **ressalva**. A ressalva é reforçada por dois motivos: a nota da Q1 é afetada por limitação de medição (seção 4.1) e a nota da Q4 resulta da média de duas métricas que apontam em direções opostas (seção 4.4).

---

## 4. Respostas às Questões e Validação de Hipóteses GQM

### 4.1 Questão Q1 (Disponibilidade)

* **Pergunta:** Os módulos estão acessíveis e respondendo corretamente nos momentos em que o cidadão precisa utilizá-los, inclusive em horários de maior demanda?
* **Resposta técnica:** **Inconclusiva (TDO = 25,00% pela regra do plano).** O resultado é dominado por três dos quatro alvos (portal, login e Balcão Virtual) terem falhado em todas as 15 verificações do Actions, com estouro de tempo na conexão TLS ou com uma resposta HTTP 200 sem o texto esperado. O controle C01 respondeu sempre, então a regra do plano não classifica esses ciclos como falha local. Ao mesmo tempo, o portal respondeu normalmente às execuções manuais dos dias 16, 17 e 20 a partir da conexão do avaliador no DF, e o chatbot (A02) respondeu 100% das vezes. Isso indica que o servidor do GitHub, fora do DF, é rejeitado ou atrasado pela infraestrutura do portal. Há também rejeições em acessos manuais: em 18/11 às 10h31 e em 19/11 às 08h17, a conexão do avaliador no DF recebeu a página "Request Rejected", que é típica de firewall de aplicação web. Os dois fatos juntos mostram que o portal rejeita requisições em alguns momentos, e os dados desta janela não permitem dizer com que frequência isso atinge o cidadão comum.
* **Confronto com a Hipótese H1** (disponibilidade acima de 98%, com degradação em horários de pico e dependência do Gov.br): **não confirmada pelo número, mas sem base para ser refutada com segurança.** A série cobre 15 ciclos, e não se pode separar horário de pico de outros horários. O Gov.br não é monitorado pela M1, e o login por ele funcionou em todas as sessões manuais, exceto por uma queda de sessão com tela de login em repetição em 17/11, das 17h11 às 17h13, de causa não identificada.

### 4.2 Questão Q2 (Ausência de Falhas)

* **Pergunta:** Os fluxos principais dos quatro módulos são concluídos sem falhas, em condições normais de uso?
* **Resposta técnica:** **Em grande parte (TCFF = 77,78%, DFF = 0,25).** ATE-01, PRO-01 e CHA-01 foram concluídos nas 2 execuções de cada um. As duas únicas falhas ocorreram no INF-01, ambas com a mesma causa: HTTP 503 no endpoint de débitos do veículo, com a tela de carregamento sem resultado. Na execução 1, a nova tentativa travou por mais de 20 s e terminou em 504. A terceira execução do INF-01, à noite, foi concluída. No CHA-01, as imagens das respostas do chat não carregaram na execução 2, sem impedir a conversa.
* **Confronto com a Hipótese H2** (acima de 95% em Infração, menos e mais falhas em Atendimento e Protocolo, falha intermitente do Chatbot): **refutada na distribuição.** A falha concentrou-se na Infração (1 sucesso em 3 execuções), e Atendimento e Protocolo concluíram todas as execuções. O Chatbot apresentou falha parcial intermitente (imagens), não de resposta. A amostra é pequena (9 execuções, 4 fluxos), e INF-02 e INF-03 não puderam ser executados porque a conta usada não tem débitos nem autos de infração.

### 4.3 Questão Q3 (Tolerância a Falhas)

* **Pergunta:** O portal permanece estável diante de operações anômalas do cidadão?
* **Resposta técnica:** **Em parte (TTOA = 77,78%).** As entradas inválidas simples foram bloqueadas (A1, A2 e A3), embora o A3 não mostre mensagem de campo obrigatório e o A9 ignore a mensagem vazia sem aviso. O duplo clique no envio do Requerimento Geral (A8) não duplicou a requisição. Dois cenários não foram tolerados: no A4, um duplo clique em Consultar gerou duas requisições, com um 503 sem mensagem de erro (a causa do 503 pode ser instabilidade do serviço, e não do duplo clique), e no A6 o botão voltar do navegador fez o formulário de agendamento voltar vazio.
* **Confronto com a Hipótese H3** (entradas inválidas bloqueadas, mas ações repetidas e anexos fora do padrão geram erro técnico): **parcialmente confirmada.** As entradas inválidas foram bloqueadas, como previsto. A ação repetida gerou erro apenas na Infração (A4), e o Protocolo (A8) tolerou o duplo clique. Os anexos fora do padrão (A7) não puderam ser testados.

### 4.4 Questão Q4 (Recuperabilidade)

* **Pergunta:** Após uma interrupção, o cidadão retoma a tarefa sem perda de dados e rapidamente?
* **Resposta técnica:** **Não (TRTI = 0,00%, TMR = 28,0 s).** Nos três cenários executados, o portal perdeu o que o cidadão tinha preenchido: o agendamento voltou vazio após a recarga (B4), o Requerimento Geral voltou à tela inicial do Protocolo (B5) e a sessão limpa levou o cidadão à página inicial deslogado (B3). O TMR baixo não indica boa recuperação, e sim que o refazer manual foi rápido para formulários curtos (3 s no B5, que tem um campo). Por isso a média das notas da M5 (1) e da M6 (4) dá 2,5, no limite entre Satisfatório e Bom, e a leitura qualitativa da questão continua sendo de recuperação insuficiente.
* **Confronto com a Hipótese H4** (perda de dados no Protocolo ao recarregar, reinício do agendamento após sessão expirada, tempo curto em Infração e longo nos demais): **confirmada na perda de dados** (B3, B4 e B5), e **não confirmada no tempo longo para o Protocolo** (3 s). Os cenários de Infração e do Chatbot (B1, B2, B7 e B8) não foram executados.

### 4.5 Objetivo G1 e Julgamento Final

* **Resultado:** nota 2,0, nível **Satisfatório, com ressalva** pela nota 1 da Q1.
* **Relação com o Propósito da Fase 1:** o propósito da avaliação é fundamentar um diagnóstico técnico independente das fragilidades de resiliência e integração do portal. Os dados mostram que os fluxos de Atendimento, Protocolo e Chatbot concluem em condições normais, mas que a **resiliência é o ponto fraco**: o portal não preserva o estado do formulário diante de recarga, sessão limpa ou botão voltar, e a consulta de débitos depende de um endpoint que respondeu 503 em duas de três execuções. Para o cidadão, que precisa cumprir prazos legais (defesa prévia, recurso, vencimento de guia), isso significa refazer o preenchimento e, em alguns casos, repetir a consulta. Para a equipe de TI do Detran-DF, os registros fornecem o endpoint, o horário e as evidências de cada falha.

### 4.6 Visualização Gráfica dos Resultados

```mermaid
xychart-beta
    title "Notas por métrica de Confiabilidade (1 a 4)"
    x-axis ["M1 TDO", "M2 TCFF", "M3 DFF", "M4 TTOA", "M5 TRTI", "M6 TMR"]
    y-axis "Nota" 0 --> 4
    bar [1, 2, 3, 2, 1, 4]
```

```mermaid
flowchart TD
    G1["G1 Confiabilidade: 2,0 Satisfatório, com ressalva"]
    G1 --> Q1["Q1 Disponibilidade: 1,0"]:::ruim
    G1 --> Q2["Q2 Ausência de Falhas: 2,5"]:::medio
    G1 --> Q3["Q3 Tolerância a Falhas: 2,0"]:::medio
    G1 --> Q4["Q4 Recuperabilidade: 2,5"]:::medio
    Q1 --> M1["M1 TDO 25,00%"]:::ruim
    Q2 --> M2["M2 TCFF 77,78%"]:::medio
    Q2 --> M3["M3 DFF 0,25"]:::bom
    Q3 --> M4["M4 TTOA 77,78%"]:::medio
    Q4 --> M5["M5 TRTI 0,00%"]:::ruim
    Q4 --> M6["M6 TMR 28 s"]:::bom

    classDef bom fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;
    classDef medio fill:#fff3cd,stroke:#d39e00,stroke-width:2px,color:#533f03;
    classDef ruim fill:#f8d7da,stroke:#dc3545,stroke-width:2px,color:#721c24;
```

---

## 5. Catálogo de Falhas e Anomalias Identificadas

| ID | Descrição observável | Origem | Ocorrências | Onde |
| :---: | :--- | :--- | :--- | :--- |
| **C-01** | HTTP 503 no endpoint de débitos do veículo, com tela de carregamento sem resultado | Portal | INF-01 execuções 1 e 2; A4 | Infração |
| **C-02** | Nova tentativa da consulta de débitos travou por mais de 20 s e terminou em 504 | Portal | INF-01 execução 1 | Infração |
| **C-03** | Imagens das respostas do chat não carregaram (conversa concluída) | Chatbot (InBot) | CHA-01 execução 2 | Chatbot |
| **C-04** | Mensagem de erro `inbot.language` não carregou, registrada no console | Chatbot (InBot) | 17/11 | Chatbot |
| **C-05** | Página "Request Rejected" (firewall) em acesso manual, e estouro de tempo TLS ou resposta sem o texto esperado no monitor | Portal | 18/11 às 10h31 e 19/11 às 08h17; monitor do Actions | Todos os alvos públicos |
| **C-06** | Retorno à tela de login após o login no Gov.br, com carregamento preso, resolvido em nova tentativa | Portal ou Gov.br (não identificado) | 17/11, 17h11 a 17h13 | Autenticação |
| **C-07** | Perda do que foi preenchido ao recarregar, voltar pelo navegador ou limpar a sessão | Portal | A6, B3, B4 e B5 | Atendimento e Protocolo |

*Tabela 7 – Catálogo de falhas e anomalias. Fonte: dados coletados pelos autores.*

Observação sem classificação como falha: a abertura do Requerimento Geral cria um protocolo em rascunho antes da assinatura (a requisição `requerimento-geral` retorna 201). Nada foi assinado nem enviado em nenhuma execução.

### 5.1 Oportunidades de Melhoria

1. **Preservar o estado do formulário.** Guardar o preenchimento (no navegador ou como rascunho no servidor) e restaurá-lo após recarga, botão voltar ou novo login. Atende a C-07 e é a oportunidade com maior efeito sobre a Q4.
2. **Tratar o erro da consulta de débitos.** Mostrar mensagem clara e opção de tentar de novo quando o endpoint de débitos falhar, em vez de manter a tela de carregamento. Atende a C-01 e C-02.
3. **Proteger a consulta contra duplo clique.** Desabilitar o botão enquanto a requisição está em andamento (A4).
4. **Dar retorno ao cidadão em entradas vazias.** Mensagem de campo obrigatório no A3 e aviso ao enviar mensagem vazia no chatbot (A9).
5. **Revisar a rejeição de requisições.** Trocar a página "Request Rejected" por uma mensagem compreensível e verificar se as regras do firewall estão rejeitando tráfego legítimo (C-05).

A ação escolhida entre essas oportunidades será registrada em [Ações de Melhoria](melhorias.md).

---

## 6. Limitações e Desvios do Plano

* **Amostras reduzidas.** M2 teve 9 das 30 execuções, M4 teve 9 dos 10 cenários e M5 teve 3 dos 8. Um único resultado muda o nível das métricas de contagem, e os resultados descrevem só estas execuções.
* **Fluxos não executados.** INF-02 e INF-03 não têm dados porque a conta usada não possui débitos nem autos de infração. As execuções de pico e fora do pico previstas para vários fluxos não foram completadas.
* **A7 e B6.** O campo de anexo só aparece depois do Avançar com placa e auto de infração reais, e nenhum protocolo é enviado nesta avaliação.
* **Coleta fora do prazo.** O plano previa a coleta manual de 16/11 a 19/11. Os cenários B3, B4 e B5 foram executados em 20/11, porque o portal rejeitou o acesso nos dias 18 e 19 de manhã.
* **Evidência por capturas de tela.** A maior parte das execuções de M2 e M4 tem capturas, e não gravação. Os cenários de M5 têm gravação de tela, e a gravação da PRO-01 de 16/11 também.
* **Origem das verificações da M1.** O monitor roda em servidores do GitHub fora do DF, e a série ficou com 15 dos cerca de 422 ciclos previstos. O TDO desta janela mede principalmente o acesso desse monitor ao portal.
* **Dados pessoais.** As capturas e gravações foram versionadas com nome, CPF, placa, endereço e telefone cobertos.

---

## 7. Galeria de Evidências

Todos os arquivos estão em `docs/dados/confiabilidade/`, com o nome no formato `{métrica}_{fluxo ou cenário}_{execução}_{data}_{hora}`.

### 7.1 Fluxos (M2 e M3)

#### INF-01 – Consulta de débitos (1 sucesso, 2 falhas)

![INF-01 execução 1, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e1_20261117_1703_1.png)
![INF-01 execução 1, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e1_20261117_1704_2.png)
![INF-01 execução 1, passo 3](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e1_20261117_1704_3.png)
![INF-01 execução 1, passo 4](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e1_20261117_1708_4.png)
![INF-01 execução 1, passo 5](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e1_20261117_1710_5.png)
![INF-01 execução 2, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e2_20261117_1723_1.png)
![INF-01 execução 2, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e2_20261117_1724_2.png)
![INF-01 execução 3, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e3_20261117_2050_1.png)
![INF-01 execução 3, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_e3_20261117_2050_2.png)

Tentativa pelo histórico de infrações por veículo, que retornou lista vazia e não conta como execução:

![INF-01 pelo histórico, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_desvio-historico_20261117_1659_1.png)
![INF-01 pelo histórico, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_desvio-historico_20261117_1700_2.png)
![INF-01 pelo histórico, passo 3](../dados/confiabilidade/m2-m3/evidencias/M2_INF-01_desvio-historico_20261117_1701_3.png)

#### ATE-01 – Agendamento (2 sucessos)

![ATE-01 execução 1, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_ATE-01_e1_20261117_1714_1.png)
![ATE-01 execução 1, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_ATE-01_e1_20261117_1715_2.png)
![ATE-01 execução 1, passo 3](../dados/confiabilidade/m2-m3/evidencias/M2_ATE-01_e1_20261117_1715_3.png)
![ATE-01 execução 2, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_ATE-01_e2_20261117_2049_1.png)
![ATE-01 execução 2, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_ATE-01_e2_20261117_2049_2.png)

#### PRO-01 – Requerimento Geral (2 sucessos)

Execução 1, gravação de tela de 16/11:

<video controls width="100%" src="../dados/confiabilidade/m2-m3/evidencias/M2_PRO-01_e1_20261116_2000.mp4"></video>

Execução 2:

![PRO-01 execução 2, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_PRO-01_e2_20261117_1716_1.png)
![PRO-01 execução 2, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_PRO-01_e2_20261117_1716_2.png)
![PRO-01 execução 2, passo 3](../dados/confiabilidade/m2-m3/evidencias/M2_PRO-01_e2_20261117_1716_3.png)

#### CHA-01 – Chatbot (2 sucessos)

![CHA-01 execução 1, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e1_20261117_1717_1.png)
![CHA-01 execução 1, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e1_20261117_1717_2.png)
![CHA-01 execução 1, passo 3](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e1_20261117_1717_3.png)
![CHA-01 execução 2, passo 1](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e2_20261117_2047_1.png)
![CHA-01 execução 2, passo 2](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e2_20261117_2047_2.png)
![CHA-01 execução 2, passo 3, imagens do chat sem carregar](../dados/confiabilidade/m2-m3/evidencias/M2_CHA-01_e2_20261117_2048_3.png)

#### Observações de acesso

Página "Request Rejected" em acesso manual:

![Acesso rejeitado em 18/11 às 10h31](../dados/confiabilidade/m2-m3/evidencias/OBS_acesso-rejeitado_20261118_1031_1.png)
![Controle em 18/11 às 10h32](../dados/confiabilidade/m2-m3/evidencias/OBS_acesso-rejeitado_20261118_1032_controle.png)
![Acesso rejeitado em 18/11 às 10h35](../dados/confiabilidade/m2-m3/evidencias/OBS_acesso-rejeitado_20261118_1035_2.png)
![Acesso rejeitado em 19/11 às 08h17](../dados/confiabilidade/m2-m3/evidencias/OBS_acesso-rejeitado_20261119_0817_1.png)

Retorno à tela de login em 17/11:

![Login em repetição, passo 1](../dados/confiabilidade/m2-m3/evidencias/OBS_login-loop_20261117_1711_1.png)
![Login em repetição, passo 2](../dados/confiabilidade/m2-m3/evidencias/OBS_login-loop_20261117_1711_2.png)
![Login em repetição, passo 3](../dados/confiabilidade/m2-m3/evidencias/OBS_login-loop_20261117_1713_3.png)
![Console durante o login em repetição](../dados/confiabilidade/m2-m3/evidencias/OBS_login-loop_20261117_1713_4_console.png)

### 7.2 Operações anômalas (M4)

| Cenário | Evidência |
| :---: | :--- |
| **A1** | ![A1, passo 1](../dados/confiabilidade/m4/evidencias/M4_A1_20261117_2117_1.png) ![A1, passo 2](../dados/confiabilidade/m4/evidencias/M4_A1_20261117_2117_2.png) |
| **A2** | ![A2](../dados/confiabilidade/m4/evidencias/M4_A2_20261117_2118_1.png) |
| **A3** | ![A3](../dados/confiabilidade/m4/evidencias/M4_A3_20261117_2119_1.png) |
| **A4** | ![A4](../dados/confiabilidade/m4/evidencias/M4_A4_20261117_2119_1.png) |
| **A5** | ![A5, horários](../dados/confiabilidade/m4/evidencias/M4_A5_20261116_2008_1.png) ![A5, datas](../dados/confiabilidade/m4/evidencias/M4_A5_20261116_2008_2.png) |
| **A6** | ![A6, depois de voltar](../dados/confiabilidade/m4/evidencias/M4_A6_20261116_2009_1.png) ![A6, formulário vazio](../dados/confiabilidade/m4/evidencias/M4_A6_20261116_2009_2.png) |
| **A7** | ![A7, aviso do Recurso JARI](../dados/confiabilidade/m4/evidencias/M4_A7_20261116_2005_1.png) ![A7, formulário do Recurso JARI](../dados/confiabilidade/m4/evidencias/M4_A7_20261116_2005_2.png) |
| **A8** | ![A8, campo vazio](../dados/confiabilidade/m4/evidencias/M4_A8_20261117_1720_1.png) ![A8, duplo clique](../dados/confiabilidade/m4/evidencias/M4_A8_20261117_1730_2.png) |
| **A9** | ![A9](../dados/confiabilidade/m4/evidencias/M4_A9_20261117_1718_1.png) |
| **A10** | ![A10](../dados/confiabilidade/m4/evidencias/M4_A10_20261117_1719_1.png) |

*Tabela 8 – Evidências dos cenários anômalos.*

### 7.3 Interrupção e retomada (M5 e M6)

#### B3 – Sessão limpa durante o agendamento (48 s)

<video controls width="100%" src="../dados/confiabilidade/m5-m6/evidencias/M5_B3_20261120_1159.mp4"></video>

#### B4 – Recarga com o agendamento preenchido (33 s)

<video controls width="100%" src="../dados/confiabilidade/m5-m6/evidencias/M5_B4_20261120_1142.mp4"></video>

#### B5 – Recarga com o Requerimento Geral preenchido (3 s)

<video controls width="100%" src="../dados/confiabilidade/m5-m6/evidencias/M5_B5_20261120_1149.mp4"></video>
