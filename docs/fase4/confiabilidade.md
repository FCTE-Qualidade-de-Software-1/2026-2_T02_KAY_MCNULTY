# Resultados Empíricos e Julgamento – Característica: Confiabilidade

**Responsáveis:** Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo  
**Característica:** Confiabilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Disponibilidade, Ausência de Falhas, Tolerância a Falhas e Recuperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 4 (Execução e Julgamento da Avaliação – ISO/IEC 25040)

!!! note "Status do Documento"
    Página placeholder estruturada pela equipe Kay McNulty para a consolidação dos resultados empíricos da avaliação de Confiabilidade. Os dados coletados pelo monitor de disponibilidade automatizado e pelas baterias manuais de ensaios em produção serão consolidados pela dupla responsável (Davi Ursolino de Oliveira e João Eduardo Pereira Rabelo).

---

## 1. Compilação dos Registros de Monitoramento e Ensaios

Nesta seção serão compilados os conjuntos de dados empíricos brutos:

* **Série Temporal de Disponibilidade (M1 – TDO):** Logs das verificações periódicas executadas a cada 15 minutos ao longo da janela de observação.
* **Execuções dos Fluxos Principais (M2 – TCFF e M3 – DFF):** Registro das 30 execuções manuais (6 fluxos × 5 rodadas) com anotação de falhas e travamentos.
* **Ensaios de Operações Anômalas (M4 – TTOA):** Respostas do sistema aos 10 cenários de estresse de dados e entradas fora de padrão.
* **Ensaios de Interrupção e Retomada (M5 – TRTI e M6 – TMR):** Gravações e cronometragens dos cenários de perda de conexão e recarga de página.

---

## 2. Cálculo das Medidas Derivadas

Aplicação formal das equações especificadas na Fase 2 e no plano da Fase 3:

* **Taxa de Disponibilidade Observada (TDO):**
  $$TDO = \left(\frac{C_{ok}}{C_{tot}}\right) \times 100$$
* **Taxa de Conclusão de Fluxos sem Falha (TCFF):**
  $$TCFF = \left(\frac{F_{ok}}{F_{exe}}\right) \times 100$$
* **Densidade de Falhas por Fluxo (DFF):**
  $$DFF = \frac{F_d}{Fl_{tot}}$$
* **Taxa de Tolerância a Operações Anômalas (TTOA):**
  $$TTOA = \left(\frac{S_{tol}}{S_{tot}}\right) \times 100$$
* **Taxa de Retomada de Tarefas Interrompidas (TRTI):**
  $$TRTI = \left(\frac{R_{ok}}{R_{tot}}\right) \times 100$$
* **Tempo Médio de Retomada (TMR):**
  $$TMR = \frac{1}{R_{ret}} \sum_{i=1}^{R_{ret}} T_i$$

---

## 3. Aplicação das Réguas de Pontuação e Julgamento

| Métrica | Valor Apurado | Nível de Pontuação Obtido | Situação de Conformidade |
| :--- | :---: | :---: | :---: |
| **M1 – TDO (Disponibilidade)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M2 – TCFF (Execução Nominal)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M3 – DFF (Densidade de Falhas)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M4 – TTOA (Tolerância a Anomalias)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M5 – TRTI (Taxa de Retomada)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M6 – TMR (Tempo de Retomada)** | *Aguardando dados* | *A definir* | *Pendente de medição* |

**Tabela 1 – Julgamento das métricas de Confiabilidade.** Fonte: Elaborado pelos autores.

---

## 4. Respostas às Questões e Validação de Hipóteses GQM

* **Questão Q1 (Disponibilidade):** Parecer técnico confrontando o TDO apurado com a Hipótese H1.
* **Questão Q2 (Ausência de Falhas):** Análise da conclusão nominal e densidade de falhas frente à Hipótese H2.
* **Questão Q3 (Tolerância a Anomalias):** Análise da contenção de erros frente à Hipótese H3.
* **Questão Q4 (Recuperabilidade):** Avaliação da capacidade e tempo de restauração do estado frente à Hipótese H4.

---

## 5. Catálogo de Falhas e Anomalias Identificadas

Registro detalhado das falhas observadas, categorizando eventos originados no portal e falhas causadas por dependências externas (Gov.br, SEI-GDF e serviço terceirizado do Chatbot).
