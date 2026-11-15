# Resultados Empíricos e Julgamento – Característica: Compatibilidade

**Responsáveis:** Artur Fernandes Galdino e Nicole Jovita Fernandes  
**Característica:** Compatibilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Coexistência e Interoperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 4 (Execução e Julgamento da Avaliação – ISO/IEC 25040)

!!! note "Status do Documento"
    Página placeholder estruturada para consolidação dos resultados empíricos, medidas derivadas e parecer de julgamento da característica de Compatibilidade. Os dados brutos e evidências de execução da bateria de testes em produção serão inseridos pela dupla responsável (Artur Fernandes Galdino e Nicole Jovita Fernandes) após a conclusão das coletas.

---

## 1. Sumário dos Dados Brutos Coletados

Nesta seção serão compilados os registros das baterias de testes executadas em ambiente de produção:

* **Resultados dos Ensaios Cross-Browser (TCBN):** Matriz de aprovação/reprovação dos fluxos nos navegadores Google Chrome, Mozilla Firefox, Microsoft Edge e Apple Safari.
* **Resultados da Inspeção de Responsividade (ICR):** Relatório de inspeção visual nas cinco viewports padrão (360px, 414px, 768px, 1366px e 1920px) nos 4 módulos.
* **Resultados de Interoperabilidade e Tráfego de Rede (TSIS):** Amostragem de chamadas aos serviços externos (Gov.br, SEI-GDF, emissão bancária e motor do Chatbot).

---

## 2. Medidas Básicas e Cálculo das Métricas

Aplicação formal das equações estabelecidas na especificação da Fase 2:

### 2.1 Taxa de Compatibilidade Entre Navegadores (TCBN)

Fórmula da medida derivada:
$$TCBN = \left(\frac{N_{ap}}{N_{tot}}\right) \times 100$$

* $N_{ap}$: Número de fluxos executados com pleno sucesso em todos os navegadores.
* $N_{tot}$: Total de fluxos planejados nos 4 módulos.

### 2.2 Índice de Conformidade Responsiva (ICR)

Fórmula da medida derivada:
$$ICR = \left(\frac{N_{cp}}{N_{res}}\right) \times 100$$

* $N_{cp}$: Total de verificações responsivas sem quebra de layout, sobreposição ou overflow horizontal.
* $N_{res}$: Total de verificações planejadas (4 módulos × 5 viewports = 20 verificações).

### 2.3 Taxa de Sucesso de Integração de Serviços (TSIS)

Fórmula da medida derivada:
$$TSIS = \left(\frac{R_{suc}}{R_{tot}}\right) \times 100$$

* $R_{suc}$: Quantidade de requisições a serviços externos finalizadas com status HTTP 2xx ou 3xx.
* $R_{tot}$: Total de requisições de integração monitoradas.

---

## 3. Aplicação dos Níveis de Pontuação e Julgamento

| Métrica | Valor Apurado | Nível de Pontuação Obtido | Situação de Conformidade |
| :--- | :---: | :---: | :---: |
| **M1 – TCBN (Cross-Browser)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M2 – ICR (Responsividade)** | *Aguardando dados* | *A definir* | *Pendente de medição* |
| **M3 – TSIS (Interoperabilidade)** | *Aguardando dados* | *A definir* | *Pendente de medição* |

**Tabela 1 – Julgamento das métricas de Compatibilidade.** Fonte: Elaborado pelos autores.

---

## 4. Respostas às Questões e Validação de Hipóteses GQM

* **Questão Q1 (Cross-Browser):** Parecer analítico confrontando os dados da TCBN com a Hipótese H1.
* **Questão Q2 (Responsividade):** Parecer analítico confrontando os dados do ICR com a Hipótese H2.
* **Questão Q3 (Interoperabilidade):** Parecer analítico confrontando os dados da TSIS com a Hipótese H3.

---

## 5. Registro de Não-Conformidades e Evidências

Catálogo de problemas visuais, comportamentais e de comunicação detectados, acompanhados de evidências auditáveis (capturas de tela, dumps de rede e passos de reprodução).
