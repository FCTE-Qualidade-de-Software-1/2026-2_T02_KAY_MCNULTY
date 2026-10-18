# GQM – Característica: Confiabilidade

**Responsáveis:** João e Davi

A avaliação da característica de **Confiabilidade** fundamenta-se na norma **ISO/IEC 25010:2023**, sendo desdobrada em suas quatro subcaracterísticas:

* **Ausência de Falhas (*Faultlessness*):** Capacidade de o sistema executar suas funções sem falhas em operação normal. Na versão 2023 da norma, esta subcaracterística substitui a antiga *Maturidade*.

* **Disponibilidade (*Availability*):** Capacidade de o sistema estar operacional e acessível quando o cidadão precisa utilizá-lo.

* **Tolerância a Falhas (*Fault Tolerance*):** Capacidade de o sistema manter o nível de desempenho esperado diante de falhas ou de uso fora do fluxo ideal.

* **Recuperabilidade (*Recoverability*):** Capacidade de o sistema retomar o estado desejado e restaurar os dados afetados após uma interrupção ou falha.

Como a auditoria é externa e em ambiente de produção (caixa-preta), a Confiabilidade é observada **somente a partir da camada do cliente**: comportamento da interface, códigos de status HTTP e respostas do servidor. Falhas internas de infraestrutura só são inferidas pelo seu efeito visível ao cidadão.

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

### Questão Q1 (Ausência de Falhas / Execução dos Fluxos Principais)

* **Pergunta:** Os fluxos principais dos quatro módulos (consulta de débitos, emissão de guia, agendamento, abertura de protocolo e atendimento pelo Chatbot) são concluídos sem falha, em condições normais de uso?
* **Hipótese H1:** Espera-se taxa de execução sem falha superior a 95% no módulo de Infração, por ser majoritariamente consulta. Espera-se taxa inferior nos módulos de Atendimento e Protocolo, que dependem de integrações externas (Gov.br e SEI-GDF) e de upload de arquivos, com falhas intermitentes e erros HTTP 5xx. No Chatbot, espera-se falha intermitente de resposta (timeout ou mensagem de erro genérica).

---

### Questão Q2 (Disponibilidade)

* **Pergunta:** O portal e seus módulos estão acessíveis e respondem corretamente nos momentos em que o cidadão precisa utilizá-los, inclusive em horários de maior demanda?
* **Hipótese H2:** Espera-se disponibilidade geral acima de 98%, com degradação concentrada em horários comerciais de pico (manhã e início da tarde de dias úteis) e em janelas de manutenção não anunciadas. Espera-se que a dependência do Gov.br seja a principal causa de indisponibilidade parcial.

---

### Questão Q3 (Tolerância a Falhas e Recuperabilidade)

* **Pergunta:** Quando ocorre uma interrupção comum do lado do cidadão (queda de conexão, recarregamento da página, uso do botão voltar ou expiração de sessão) no meio de um fluxo, o portal permite retomar a tarefa sem perda de dados e com orientação clara?
* **Hipótese H3:** Espera-se baixa tolerância nos fluxos longos. Prevê-se perda dos dados preenchidos no Protocolo ao recarregar a página, reinício completo do agendamento (módulo de Atendimento) após expiração de sessão e mensagens de erro genéricas ou técnicas que não orientam a retomada. Espera-se melhor recuperação no módulo de Infração, que tem fluxo curto.

---

## 3. Definição Formal das Métricas (Nível Quantitativo)

As métricas foram estruturadas conectando o GQM com o modelo de informação do **Practical Software Measurement (PSM)**, detalhando medidas básicas, derivadas, procedimentos de coleta e interpretação.

### Fluxos-alvo de medição

Os mesmos fluxos servem de base para as métricas M1 e M3. Os cenários detalhados serão refinados na Fase 3 (Projeto da Avaliação).

| Fluxo | Módulo | Descrição do fluxo |
| :---: | :--- | :--- |
| **F1** | Infração | Consultar débitos e infrações de um veículo |
| **F2** | Infração | Gerar guia de pagamento (DUD / PIX) |
| **F3** | Atendimento | Percorrer o agendamento até a tela de confirmação |
| **F4** | Protocolo | Preencher o formulário e anexar documento até a tela de revisão |
| **F5** | Chatbot | Realizar uma conversa de três perguntas frequentes |

!!! warning "Restrições éticas e de segurança da coleta"
    A coleta ocorre em produção. Por isso: (i) fluxos que criariam registro real (agendamento e protocolo) **não são confirmados**, ou são cancelados imediatamente quando houver opção de cancelamento; (ii) não se realiza teste de carga, e a frequência de requisições é baixa (ver M2); (iii) nenhuma credencial ou dado pessoal real de terceiros é utilizado.

**Definição de falha (usada em M1 e M2):** considera-se falha qualquer das ocorrências a seguir durante a execução: resposta HTTP 5xx; *timeout* superior a 30 segundos; tela em branco ou mensagem de erro exibida ao usuário; resultado incorreto ou incompleto; ou travamento que exija recarregar a página para prosseguir.

---

### Métrica M1: Taxa de Fluxos Sem Falha (TFSF) – Associada a Q1
Avalia a proporção de execuções dos fluxos principais concluídas sem nenhuma falha, em condições normais de uso.

* **Medidas Básicas (PSM):**
  * **E_ok:** Número de execuções dos fluxos F1 a F5 concluídas sem falha.
  * **E_tot:** Número total de execuções realizadas dos fluxos F1 a F5 (mínimo de 10 repetições por fluxo, distribuídas em dias e turnos diferentes: manhã, tarde e noite).
* **Medida Derivada (Fórmula):**
  > **TFSF = (E_ok / E_tot) × 100%**
* **Procedimento de Coleta:** Execução manual dos fluxos em navegador desktop e em smartphone real, registrando em planilha a data, o horário, o fluxo, o resultado e o tipo de falha. Os códigos HTTP e erros de script são verificados no `DevTools` (abas *Network* e *Console*). Cada falha recebe captura de tela como evidência.
* **Critério de Interpretação:** Quanto maior a porcentagem, maior a ausência de falhas em operação normal. O resultado também é calculado por módulo para localizar onde as falhas se concentram.

---

### Métrica M2: Taxa de Disponibilidade Observada (TDO) – Associada a Q2
Avalia a proporção de verificações em que o portal e seus módulos estiveram acessíveis e respondendo corretamente durante a janela de observação.

* **Medidas Básicas (PSM):**
  * **V_ok:** Número de verificações em que o endereço monitorado respondeu com status HTTP 2xx ou 3xx, em até 10 segundos, com conteúdo esperado na página (e sem tela de manutenção).
  * **V_tot:** Número total de verificações realizadas na janela de observação.
* **Medida Derivada (Fórmula):**
  > **TDO = (V_ok / V_tot) × 100%**
* **Procedimento de Coleta:** Monitoramento externo de baixa frequência: uma requisição `GET` a cada 15 minutos por endereço monitorado (página inicial e entrada de cada um dos 4 módulos) durante 7 dias consecutivos, com *script* automatizado que registra data, horário, status HTTP e tempo de resposta. A frequência é deliberadamente baixa para não caracterizar carga sobre a infraestrutura pública. O resultado é analisado também por faixa de horário.
* **Critério de Interpretação:** Quanto maior a porcentagem, maior a disponibilidade percebida pelo cidadão. Como a medição é externa, quedas de rede do próprio avaliador são descartadas por verificação cruzada (acesso simultâneo a um serviço de referência).

---

### Métrica M3: Taxa de Recuperação após Falha (TRF) – Associada a Q3
Mede a capacidade do portal de tolerar interrupções comuns do lado do cidadão e permitir a retomada da tarefa sem perda de dados.

* **Medidas Básicas (PSM):**
  * **C_rec:** Número de cenários de interrupção em que o fluxo foi retomado sem perda de dados e sem necessidade de recomeçar do início, com mensagem ou estado que oriente o usuário.
  * **C_tot:** Número total de cenários de interrupção induzidos.
* **Medida Derivada (Fórmula):**
  > **TRF = (C_rec / C_tot) × 100%**
* **Procedimento de Coleta:** Indução controlada, no meio dos fluxos F2 a F5, dos cenários: (a) perda de conexão seguida de restabelecimento (modo offline do `DevTools`); (b) recarregamento da página (`F5`) com formulário parcialmente preenchido; (c) uso do botão voltar do navegador; (d) expiração de sessão (aguardar o limite de inatividade). Cada cenário é classificado como recuperado ou não recuperado, com registro da mensagem exibida.
* **Critério de Interpretação:** Quanto maior a porcentagem, maior a tolerância a falhas e a recuperabilidade. Valores baixos indicam perda de dados ou reinício forçado, com risco de o cidadão perder prazos legais.

---

## 4. Níveis de Pontuação e Critérios de Julgamento

A interpretação técnica dos resultados consolidados da característica de Confiabilidade segue a seguinte matriz de decisão:

| Nível de Julgamento | Faixa TFSF (M1) | Faixa TDO (M2) | Faixa TRF (M3) | Parecer Técnico e Ação Recomendada |
| :---: | :---: | :---: | :---: | :--- |
| **Excelente** | ≥ 98% | ≥ 99,5% | ≥ 90% | Confiabilidade exemplar. O portal opera sem falhas perceptíveis, está sempre disponível e permite retomar tarefas interrompidas. Manter boas práticas. |
| **Bom** | 90% a 97,99% | 98% a 99,49% | 75% a 89,99% | Confiabilidade adequada. Falhas raras e pontuais, sem impedimento de conclusão do serviço pelo cidadão. |
| **Satisfatório** | 80% a 89,99% | 95% a 97,99% | 60% a 74,99% | Confiabilidade limítrofe. O cidadão precisa repetir a operação ou recomeçar o fluxo. Priorizar correções nos módulos mais críticos. |
| **Insuficiente** | < 80% | < 95% | < 60% | Confiabilidade crítica e reprovada. Falhas frequentes, indisponibilidade ou perda de dados que podem fazer o cidadão perder prazos legais. Ação de melhoria obrigatória. |

!!! note "Regra de consolidação"
    O nível final da característica é o **menor nível obtido entre as três métricas**, pois uma falha grave em qualquer dimensão (por exemplo, indisponibilidade) compromete o serviço independentemente das demais. Os resultados também são apresentados por módulo.

---

## 5. Diagrama Hierárquico GQM

<!-- Espaço reservado para o diagrama GQM de Confiabilidade -->
