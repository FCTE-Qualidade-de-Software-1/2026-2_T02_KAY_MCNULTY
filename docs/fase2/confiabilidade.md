# GQM – Característica: Confiabilidade

A avaliação da característica de **Confiabilidade** fundamenta-se na norma **ISO/IEC 25010:2023**, sendo desdobrada em suas quatro subcaracterísticas:

* **Ausência de Falhas (*Faultlessness*):** Capacidade de o sistema executar suas funções sem falhas em operação normal. Na versão 2023 da norma, esta subcaracterística substitui a antiga *Maturidade*.

* **Disponibilidade (*Availability*):** Capacidade de o sistema estar operacional e acessível quando o cidadão precisa utilizá-lo.

* **Tolerância a Falhas (*Fault Tolerance*):** Capacidade de o sistema manter o nível de desempenho esperado diante de falhas ou de uso fora do fluxo ideal.

* **Recuperabilidade (*Recoverability*):** Capacidade de o sistema retomar o estado desejado e restaurar os dados afetados após uma interrupção ou falha.

A profundidade da avaliação em cada módulo e os limites do escopo estão definidos em [Escopo e Limites da Avaliação](../fase1/escopo-limites.md), seção 4.

---

## 1. Objetivo de Medição (Nível Conceitual)

O objetivo de medição foi estruturado seguindo rigorosamente o template formal da abordagem Goal-Question-Metric (GQM):

| Elemento GQM | Descrição Estruturada |
| :--- | :--- |
| **Analisar** | Os módulos de Infração, Atendimento, Protocolo e Chatbot do Portal Detran Digital DF |
| **Para o propósito de** | Avaliar |
| **Com respeito a** | Confiabilidade (Ausência de Falhas, Disponibilidade, Tolerância a Falhas e Recuperabilidade - ISO/IEC 25010:2023) |
| **Do ponto de vista do** | Cidadão usuário e dos Engenheiros de Software avaliadores |
| **No contexto de** | Acessos em ambiente web e mobile no Distrito Federal, em serviços transacionais com prazos legais (defesa prévia, recursos e vencimento de guias) |

---

## 2. Questões Operacionais e Hipóteses (Nível Operacional)

### Questão Q1 (Disponibilidade)

* **Pergunta:** Os módulos estão acessíveis e respondendo corretamente nos momentos em que o cidadão precisa utilizá-los, inclusive em horários de maior demanda?
* **Hipótese H1:** Espera-se disponibilidade geral acima de 98%, com degradação concentrada em horários comerciais de pico (manhã e início da tarde de dias úteis) e em janelas de manutenção não anunciadas. Espera-se que a dependência do Gov.br seja a principal causa de indisponibilidade parcial.

---

### Questão Q2 (Ausência de Falhas)

* **Pergunta:** Os fluxos principais dos quatro módulos (consulta de débitos, emissão de guia, agendamento, abertura de protocolo e atendimento pelo Chatbot) são concluídos sem falhas, em condições normais de uso?
* **Hipótese H2:** Espera-se taxa de conclusão sem falha superior a 95% no módulo de Infração, por ser majoritariamente consulta. Espera-se taxa inferior e maior densidade de falhas nos módulos de Atendimento e Protocolo, que dependem de integrações externas (Gov.br e SEI-GDF) e de upload de arquivos, com erros HTTP 5xx intermitentes. No Chatbot, espera-se falha intermitente de resposta (*timeout* ou mensagem de erro genérica).

---

### Questão Q3 (Tolerância a Falhas)

* **Pergunta:** O portal permanece estável diante de operações anômalas do cidadão, como dados inválidos, ações repetidas, uso do botão voltar e anexos fora do padrão?
* **Hipótese H3:** Espera-se que entradas inválidas simples sejam bloqueadas, mas que ações repetidas (clique duplo em envio) e anexos fora do padrão gerem erros genéricos ou técnicos (por exemplo, "Erro 500") ou travamento da tela, sobretudo em Protocolo e Atendimento.

---

### Questão Q4 (Recuperabilidade)

* **Pergunta:** Após uma interrupção (queda de conexão, recarregamento da página ou expiração de sessão), o cidadão retoma a tarefa sem perda de dados e rapidamente?
* **Hipótese H4:** Espera-se baixa recuperação nos fluxos longos, com perda dos dados preenchidos no Protocolo ao recarregar a página e reinício completo do agendamento (módulo de Atendimento) após expiração de sessão. Espera-se tempo de recuperação curto em Infração, que tem fluxo curto, e longo nos demais módulos, por exigir novo login e novo preenchimento.

---

## 3. Definição Formal das Métricas (Nível Quantitativo)

As métricas conectam o GQM ao modelo de informação do **Practical Software Measurement (PSM)**. Os termos usados nas medições são:

* **Fluxo:** sequência de passos de um serviço, do acesso à conclusão ou à última etapa reversível.
* **Falha:** comportamento que impede a conclusão do fluxo ou compromete seu resultado (erro HTTP não previsto, tela em branco, travamento, redirecionamento indevido, perda de dados).
* **Operação anômala:** entrada inválida ou ação atípica (envio duplicado, campo vazio, arquivo inválido, botão voltar).
* **Interrupção:** perda temporária das condições normais (recarga, perda de conexão, sessão invalidada).

### Métrica M1 – Taxa de Disponibilidade Observada (TDO) – Associada a Q1

* **Medidas básicas (PSM):** Cₒₖ = verificações com HTTP 2xx/3xx e elemento esperado renderizado; Cₜₒₜ = verificações realizadas.
* **Medida derivada:** **TDO = (Cₒₖ / Cₜₒₜ) × 100%**
* **Coleta:** monitoramento automatizado das páginas públicas e do widget do Chatbot, a cada 15 min por 14 dias, em CSV no repositório. Manutenções oficiais são apresentadas com e sem exclusão.
* **Interpretação:** quanto maior, melhor.

### Métrica M2 – Taxa de Conclusão de Fluxos sem Falha (TCFF) – Associada a Q2

* **Medidas básicas (PSM):** Fₒₖ = execuções concluídas sem falha; Fₑₓₑ = execuções realizadas nos quatro módulos.
* **Medida derivada:** **TCFF = (Fₒₖ / Fₑₓₑ) × 100%**
* **Coleta:** execução manual e repetida dos fluxos principais, com evidências (captura, gravação de tela, aba de rede) em planilha.
* **Interpretação:** quanto maior, melhor.

### Métrica M3 – Densidade de Falhas por Fluxo (DFF) – Associada a Q2

* **Medidas básicas (PSM):** Fd = falhas distintas (uma por causa observável); Flₜₒₜ = fluxos distintos testados.
* **Medida derivada:** **DFF = Fd / Flₜₒₜ**
* **Coleta:** mesma planilha da M2, com classificação e eliminação de duplicidades.
* **Interpretação:** quanto menor, melhor; zero indica ausência de falhas.

### Métrica M4 – Taxa de Tolerância a Operações Anômalas (TTOA) – Associada a Q3

* **Medidas básicas (PSM):** Sₜₒₗ = cenários anômalos em que o portal permaneceu operante e consistente; Sₜₒₜ = cenários executados.
* **Medida derivada:** **TTOA = (Sₜₒₗ / Sₜₒₜ) × 100%**
* **Coleta:** cenários anômalos predefinidos em cada módulo, com registro do comportamento e das respostas HTTP.
* **Interpretação:** quanto maior, melhor. Não se tolera erro 5xx, tela em branco, travamento ou perda de estado.

### Métrica M5 – Taxa de Recuperação de Tarefas após Interrupção (TRTI) – Associada a Q4

* **Medidas básicas (PSM):** Rₒₖ = cenários retomados sem perda de dados; Rₜₒₜ = cenários de interrupção executados.
* **Medida derivada:** **TRTI = (Rₒₖ / Rₜₒₜ) × 100%**
* **Coleta:** simulação de recarga, modo offline e sessão invalidada durante os fluxos, com gravação de tela e planilha.
* **Interpretação:** quanto maior, melhor.

### Métrica M6 – Tempo Médio de Recuperação (TMR) – Associada a Q4

* **Medidas básicas (PSM):** Tᵢ = segundos entre o restabelecimento das condições normais e a retomada da tarefa no cenário i; Rᵣₑₜ = cenários com retomada.
* **Medida derivada:** **TMR = (Σ Tᵢ) / Rᵣₑₜ**
* **Coleta:** cronometragem sobre as gravações da M5. Cenários sem recuperação já são penalizados na M5.
* **Interpretação:** quanto menor, melhor.

---

## 4. Níveis de Pontuação e Critérios de Julgamento

A interpretação dos resultados quantitativos é balizada pela matriz de julgamento da Tabela 1. A cada nível corresponde uma nota, utilizada na agregação descrita adiante.

**Tabela 1 – Níveis de pontuação das métricas de confiabilidade.**

| Métrica | Excelente (4) | Bom (3) | Satisfatório (2) | Insuficiente (1) |
| :--- | :---: | :---: | :---: | :---: |
| TDO (M1) | ≥ 99,5% | 98% a < 99,5% | 95% a < 98% | < 95% |
| TCFF (M2) | ≥ 95% | 85% a < 95% | 70% a < 85% | < 70% |
| DFF (M3) | 0 | > 0 a ≤ 0,5 | > 0,5 a ≤ 1,0 | > 1,0 |
| TTOA (M4) | ≥ 95% | 85% a < 95% | 70% a < 85% | < 70% |
| TRTI (M5) | ≥ 90% | 75% a < 90% | 60% a < 75% | < 60% |
| TMR (M6) | ≤ 30 s | > 30 a ≤ 60 s | > 60 a ≤ 120 s | > 120 s |

A interpretação qualitativa de cada nível é apresentada na Tabela 2.

**Tabela 2 – Interpretação e julgamento técnico por nível.**

| Nível | Interpretação e julgamento técnico |
| :--- | :--- |
| **Excelente** | Confiabilidade exemplar. Portal acessível, sem falhas, tolerante a anomalias e com recuperação rápida. |
| **Bom** | Confiabilidade adequada. Falhas pontuais ou recuperações mais lentas, sem impedir o serviço. |
| **Satisfatório** | Confiabilidade limítrofe. O cidadão precisa repetir etapas, recarregar ou tentar mais tarde. |
| **Insuficiente** | Confiabilidade crítica e reprovada. Indisponibilidade relevante, falhas recorrentes, instabilidade e perda de dados em interrupções. |

**Regra de agregação.** A nota de cada questão é a média das notas de suas métricas: Q1 = M1; Q2 = média de M2 e M3; Q3 = M4; Q4 = média de M5 e M6. A nota de G1 é a média simples das quatro questões, pois a Fase 1 não priorizou subcaracterísticas.

Escala: < 1,5 Insuficiente; 1,5 a < 2,5 Satisfatório; 2,5 a < 3,5 Bom; ≥ 3,5 Excelente.

Se alguma questão receber nota 1, o julgamento de G1 é registrado com ressalva. Os resultados também são comparados às hipóteses das questões.

---

## 5. Diagrama Hierárquico GQM
 
O diagrama da Figura 1 mostra o desdobramento do objetivo em questões e métricas, com os três níveis identificados. As questões Q2 e Q4 são respondidas por duas métricas cada.
 
![Diagrama Confiabilidade](../img/Confiabilidade.png)
 
*Figura 1 – Hierarquia GQM da característica Confiabilidade. Fonte: elaboração da equipe.*
 
---