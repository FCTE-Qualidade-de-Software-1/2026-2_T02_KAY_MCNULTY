# Plano de Avaliação – Característica: Capacidade de Interação

**Responsáveis:** Natan França e Yan  
**Característica:** Capacidade de Interação (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Aprendibilidade, Operabilidade e Proteção contra Erros de Usuário  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 3 (Projeto da Avaliação – ISO/IEC 25040)

!!! note "Status do Documento"
    Página placeholder estruturada pela equipe Kay McNulty para a Fase 3 da ISO/IEC 25040. Os roteiros detalhados de inspeção heurística, tarefas de usuário e formulários do System Usability Scale (SUS) estão em desenvolvimento ativo pela dupla responsável (Natan França e Yan).

---

## 1. Método de Avaliação

A avaliação da característica de **Capacidade de Interação** fundamenta-se nas especificações conceituais e métricas operacionais consolidadas na [Fase 2](../fase2/usabilidade.md). A metodologia organiza-se em duas frentes complementares de inspeção diagnóstica caixa-preta:

1. **Inspeção Heurística de Interface:**
   * Aplicação das 10 Heurísticas de Capacidade de Interação de Jacob Nielsen para identificar barreiras cognitivas, falhas de feedback, inconsistências visuais e deficiências no controle do usuário sobre as ações.
2. **Avaliação Empírica de Desempenho e Satisfação:**
   * Condução de ensaios com tarefas operacionais simuladas nos quatro módulos para apuração das métricas **TCAPA** ($Taxa\ de\ Conclusão\ Autônoma\ no\ Primeiro\ Acesso$), **IEFO** ($Índice\ de\ Eficiência\ no\ Fluxo\ Operacional$) e **TPRE** ($Taxa\ de\ Prevenção\ e\ Recuperação\ de\ Erros$).
   * Aplicação do instrumento padronizado **System Usability Scale (SUS)** para quantificação do escore percebido de capacidade de interação.

### 1.1 Visão Geral das Métricas Operacionais

| Métrica | Questão GQM | O que é medido | Instrumento de Coleta | Procedimento de Apuração |
| :--- | :---: | :--- | :--- | :--- |
| **M1 – TCAPA** | Q1 | Taxa de conclusão de tarefas sem solicitação de auxílio externo no primeiro contato | Roteiro de tarefas orientadas | Razão entre tarefas concluídas autonomamente e o total planejado |
| **M2 – IEFO** | Q2 | Relação entre o tempo ideal previsto para a tarefa e o tempo real despendido | Cronometragem sobre gravações de tela | Divisão entre o tempo de referência e a média do tempo cronometrado |
| **M3 – TPRE** | Q3 | Capacidade da interface de prevenir entradas errôneas e auxiliar o usuário na correção imediata | Roteiro de simulação de erros induzidos | Proporção de erros bloqueados ou com mensagens instrutivas claras |
| **M4 – SUS** | Q4 | Escore padronizado de capacidade de interação percebida (escala de 0 a 100) | Questionário SUS de 10 perguntas | Cálculo ponderado conforme fórmula oficial de John Brooke |

**Tabela 1 – Métricas operacionais para Capacidade de Interação.** Fonte: Elaborado pelos autores.

---

## 2. Roteiro de Tarefas e Inspeção Heurística por Módulo

Os procedimentos práticos cobrem os quatro módulos prioritários definidos no escopo do projeto:

* **Módulo Infração:** Tarefa de busca de débitos veiculares, interpretação dos campos e visualização dos detalhes de auto de infração sem ambiguidade visual.
* **Módulo Atendimento:** Tarefa de agendamento presencial, compreensão dos fluxos de seleção de unidade, verificação de clareza dos calendários e cancelamento de etapas.
* **Módulo Protocolo:** Tarefa de envio de documentação digital, validação de limites de tamanho/formato de arquivos e transparência no status do protocolo.
* **Módulo Chatbot:** Tarefa de resolução de dúvidas frequentes, clareza das mensagens automáticas e facilidade de alternância para atendimento humano.

---

## 3. Instrumentos de Coleta e Perfil dos Avaliadores

* **Planilha de Severidade Heurística:** Instrumento para classificação dos problemas detectados em escala de 0 a 4 (0 = Não é problema; 1 = Apenas cosmético; 2 = Problema menor; 3 = Problema maior; 4 = Catástrofe de capacidade de interação).
* **Gravação de Telas e Áudio:** Registro visual das sessões de teste para auditoria temporal precisa e identificação exata dos pontos de hesitação ou falha.
* **Avaliadores Técnicos:** Membros da equipe com treinamento no método heurístico e graduandos em Engenharia de Software da UnB.

---

## 4. Matriz de Rastreabilidade (Fase 2 para Fase 3)

| Métrica Formal (Fase 2) | Questão e Hipótese | Medidas Básicas | Roteiro Operacional (Fase 3) | Instrumento de Registro | Níveis de Pontuação (Fase 2) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **M1 – TCAPA** | Q1, H1 | $T_{aut}$, $T_{tot}$ | Tarefas guiadas nos 4 módulos | Formulário de registro de execução | Excelente: ≥ 90%<br>Bom: 80% a 89%<br>Regular: 65% a 79%<br>Insuficiente: < 65% |
| **M2 – IEFO** | Q2, H2 | $t_{ideal}$, $t_{real}$ | Cronometragem dos fluxos | Tabela de tempos cronometrados | Excelente: ≥ 85%<br>Bom: 70% a 84%<br>Regular: 50% a 69%<br>Insuficiente: < 50% |
| **M3 – TPRE** | Q3, H3 | $E_{prev}$, $E_{tot}$ | Simulação de entradas inválidas | Checklist de prevenção de erros | Excelente: ≥ 90%<br>Bom: 75% a 89%<br>Regular: 60% a 74%<br>Insuficiente: < 60% |
| **M4 – SUS** | Q4, H4 | Respostas Q1 a Q10 | Questionário padronizado | Planilha de consolidação SUS | Excelente: ≥ 80,3<br>Bom: 68,0 a 80,2<br>Regular: 51,0 a 67,9<br>Insuficiente: < 51,0 |

**Tabela 2 – Matriz de rastreabilidade entre Fase 2 e Fase 3 para Capacidade de Interação.** Fonte: Elaborado pelos autores.

---

## 5. Limitações Metodológicas

* **Tamanho Amostral de Participantes:** Por se tratar de auditoria acadêmica diagnóstica, os ensaios laboratoriais com usuários utilizam amostragem de conveniência especializada, complementada pela análise heurística exaustiva dos avaliadores.
* **Simulação de Pagamentos e Envios Oficiais:** Para evitar geração indevida de dados no banco do Detran-DF, as tarefas terminam antes da confirmação final do protocolo ou quitação bancária de guias.
