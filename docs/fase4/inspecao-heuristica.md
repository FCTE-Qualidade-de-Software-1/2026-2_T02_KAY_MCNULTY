# Inspeção Heurística de Nielsen (IPH) – Capacidade de Interação

**Responsáveis:** Natan França e Yan  
**Característica:** Capacidade de Interação (ISO/IEC 25010:2023)  
**Métrica:** M4 – Índice de Problemas Heurísticos (IPH)  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 4 (Execução e Julgamento da Avaliação – ISO/IEC 25040)

---

## 1. Como o IPH é calculado

O IPH de um módulo é a soma dos problemas distintos, após a consolidação, com severidade de 1 a 4:

$$IPH_{m} = \sum_{s=1}^{4} N_{s}$$

O total é sempre apresentado junto da distribuição por severidade ($N_1$ a $N_4$). Problemas de severidade 0 não entram na contagem. A especificação não define faixas de julgamento para o IPH, então os valores são lidos pela distribuição e em conjunto com as demais métricas.

| Severidade | Significado | Contabiliza |
| :---: | :--- | :---: |
| 0 | Não é problema | Não |
| 1 | Cosmético: incômodo sem efeito na tarefa | $N_1$ |
| 2 | Menor: o usuário contorna sem esforço relevante | $N_2$ |
| 3 | Maior: o usuário perde tempo, erra ou pode abandonar | $N_3$ |
| 4 | Catastrófico: tarefa impossível ou risco de ação irreversível | $N_4$ |

**Tabela 1 – Escala de severidade.** Fonte: Elaborado pelos autores, com base no guia de severidade da Fase 3.

As heurísticas são indicadas pelo código **NH1** a **NH10**, para não confundir com as hipóteses H1 a H3 da Fase 2.

| Código | Heurística | Código | Heurística |
| :---: | :--- | :---: | :--- |
| NH1 | Visibilidade do estado do sistema | NH6 | Reconhecimento em vez de memorização |
| NH2 | Correspondência com o mundo real | NH7 | Flexibilidade e eficiência de uso |
| NH3 | Controle e liberdade do usuário | NH8 | Estética e design minimalista |
| NH4 | Consistência e padrões | NH9 | Ajudar a reconhecer e corrigir erros |
| NH5 | Prevenção de erros | NH10 | Ajuda e documentação |

**Tabela 2 – Heurísticas de Nielsen.** Fonte: Elaborado pelos autores.

---

## 2. Resultado por módulo

| Módulo | $N_1$ | $N_2$ | $N_3$ | $N_4$ | **IPH** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Infração | 2 | 3 | 2 | 0 | **7** |
| Atendimento | 1 | 4 | 3 | 0 | **8** |
| Protocolo | 1 | 3 | 3 | 1 | **8** |
| Chatbot | 1 | 2 | 2 | 0 | **5** |
| **Total** | 5 | 12 | 10 | 1 | **28** |

**Tabela 3 – IPH por módulo (dados de exemplo).** Fonte: Elaborado pelos autores.

### 2.1 Por dispositivo

Um problema que ocorre nos dois dispositivos (`D+M`) entra nas duas contagens, sem alterar a fórmula.

| Módulo | Desktop ($N_1$/$N_2$/$N_3$/$N_4$) | IPH Desktop | Mobile ($N_1$/$N_2$/$N_3$/$N_4$) | IPH Mobile |
| :--- | :---: | :---: | :---: | :---: |
| Infração | 1 / 3 / 2 / 0 | 6 | 1 / 3 / 2 / 0 | 6 |
| Atendimento | 1 / 3 / 2 / 0 | 6 | 0 / 3 / 3 / 0 | 6 |
| Protocolo | 0 / 3 / 2 / 1 | 6 | 1 / 2 / 3 / 1 | 7 |
| Chatbot | 1 / 1 / 1 / 0 | 3 | 0 / 2 / 2 / 0 | 4 |
| **Total** | 3 / 8 / 7 / 1 | **21** | 2 / 9 / 10 / 1 | **23** |

**Tabela 4 – IPH por módulo e dispositivo (dados de exemplo).** Fonte: Elaborado pelos autores.

---

## 3. Problemas consolidados

Legenda de dispositivo: **D** = Desktop, **M** = Mobile, **D+M** = ambos.

### 3.1 Infração

| ID | Disp. | Tela ou fluxo | Heurística | Problema | Sev. |
| :---: | :---: | :--- | :---: | :--- | :---: |
| CONS-INF-001 | D+M | Histórico de Infrações por Veículo | NH1 | Sem veículo na conta, a tela não lista nada e não mostra mensagem de estado vazio. | 3 |
| CONS-INF-002 | D+M | Menu de veículos | NH4 | O mesmo caminho se chama "Consultar Débitos" no desktop e "Consultar Veículo" no mobile. | 2 |
| CONS-INF-003 | D+M | Página inicial | NH8 | O aviso "É GOLPE!" bloqueia a tela até o clique em "ENTENDI". Registrado com a data da inspeção, pois pode não existir depois. | 2 |
| CONS-INF-004 | D+M | Lista de veículos | NH6 | A lista não indica quais veículos têm débitos, e o usuário precisa abrir um por um. | 2 |
| CONS-INF-005 | D+M | Detalhe do débito | NH2 | Termos como "enquadramento" aparecem sem explicação para o cidadão. | 3 |
| CONS-INF-006 | D | Histórico de Infrações | NH8 | O texto explicativo acima da lista é longo e empurra a lista para fora da primeira tela. | 1 |
| CONS-INF-007 | M | Débitos | NH4 | O botão de voltar fica em posição diferente da usada nas demais telas. | 1 |

**Tabela 5 – Problemas do módulo Infração (dados de exemplo).** Fonte: Elaborado pelos autores.

### 3.2 Atendimento

| ID | Disp. | Tela ou fluxo | Heurística | Problema | Sev. |
| :---: | :---: | :--- | :---: | :--- | :---: |
| CONS-ATE-001 | D+M | Novo Agendamento (Unidade e Data) | NH1 | Ao escolher a unidade e a data, não há sinal visível de que a seleção foi registrada, e o usuário toca de novo. | 3 |
| CONS-ATE-002 | D+M | Formulário de agendamento | NH5 | O botão "Concluir agendamento" aparece sem tela de resumo para conferir os dados antes da ação final. | 3 |
| CONS-ATE-003 | M | Novo Agendamento | NH3 | O botão voltar do navegador sai do fluxo e descarta os campos já preenchidos. | 3 |
| CONS-ATE-004 | D+M | Etapas após a categoria | NH6 | A categoria escolhida não fica visível nas etapas seguintes. | 2 |
| CONS-ATE-005 | D+M | Consentimento | NH2 | O termo de consentimento não explica, em linguagem simples, o que está sendo autorizado. | 2 |
| CONS-ATE-006 | D | Data | NH7 | O calendário não sugere a primeira data disponível, e o usuário percorre os dias manualmente. | 2 |
| CONS-ATE-007 | M | Unidade | NH7 | A lista de unidades é longa e não tem busca nem filtro. | 2 |
| CONS-ATE-008 | D | Etapas do formulário | NH4 | Os botões "Avançar" e "Continuar" são usados com o mesmo sentido em etapas diferentes. | 1 |

**Tabela 6 – Problemas do módulo Atendimento (dados de exemplo).** Fonte: Elaborado pelos autores.

### 3.3 Protocolo

| ID | Disp. | Tela ou fluxo | Heurística | Problema | Sev. |
| :---: | :---: | :--- | :---: | :--- | :---: |
| CONS-PRO-001 | D+M | Assinar Documento | NH5 | A prévia do documento não avisa nem permite editar antes da assinatura com validade legal. | 4 |
| CONS-PRO-002 | D+M | Requerimento Geral | NH2 | O campo "Objeto" não tem exemplo nem explicação do que escrever. | 2 |
| CONS-PRO-003 | D+M | Formulário do requerimento | NH3 | Não há rascunho: sair do formulário descarta tudo o que foi preenchido. | 3 |
| CONS-PRO-004 | M | Nova solicitação | NH1 | Após escolher o tipo de solicitação, a tela não indica em que etapa o usuário está nem quantas faltam. | 3 |
| CONS-PRO-005 | D+M | Formulário do requerimento | NH9 | A mensagem de campo obrigatório é genérica e não aponta qual campo corrigir. | 3 |
| CONS-PRO-006 | D | Nova solicitação | NH10 | Não há orientação sobre qual tipo de solicitação escolher para cada necessidade. | 2 |
| CONS-PRO-007 | D+M | Menu | NH4 | A opção "Protocoloe" aparece repetida em dois níveis seguidos do menu. | 2 |
| CONS-PRO-008 | M | Nova solicitação | NH8 | Os rótulos dos cartões de tipo de solicitação aparecem cortados. | 1 |

**Tabela 7 – Problemas do módulo Protocolo (dados de exemplo).** Fonte: Elaborado pelos autores.

### 3.4 Chatbot

| ID | Disp. | Tela ou fluxo | Heurística | Problema | Sev. |
| :---: | :---: | :--- | :---: | :--- | :---: |
| CONS-BOT-001 | M | Conversa com o assistente | NH1 | O assistente não responde e não informa que houve falha, deixando o usuário sem saber se deve esperar. | 3 |
| CONS-BOT-002 | M | Página inicial em 360 px | NH8 | O avatar do chatbot e o cartão flutuante cobrem o título e parte do conteúdo. Confirmar em aparelho real. | 2 |
| CONS-BOT-003 | D+M | Resposta do assistente | NH10 | As respostas não trazem link para a página oficial, e o conteúdo varia entre desktop e mobile para a mesma pergunta. | 3 |
| CONS-BOT-004 | D+M | Início da conversa | NH6 | Não há sugestões de perguntas, e o usuário precisa formular tudo do zero. | 2 |
| CONS-BOT-005 | D | Ícone do assistente | NH4 | O ícone muda de posição entre páginas do portal. | 1 |

**Tabela 8 – Problemas do módulo Chatbot (dados de exemplo).** Fonte: Elaborado pelos autores.

---

## 4. Leitura dos resultados

* **Protocolo** tem o único problema de severidade 4: a assinatura com validade legal sem aviso nem possibilidade de edição (CONS-PRO-001).
* **Atendimento** e **Infração** concentram problemas de severidade 3 ligados ao retorno ao usuário (NH1) e à ausência de resumo antes da ação final (NH5).
* **Chatbot** tem o menor total, mas dois problemas de severidade 3 que afetam a confiança na resposta.
* O **Mobile** soma mais problemas de severidade 3 e 4 do que o Desktop (11 contra 8), o que combina com a hipótese de que o toque e a tela pequena dificultam a operação.
* O total não deve ser lido isoladamente: um módulo com poucos problemas de severidade 4 pode ser mais crítico do que outro com muitos problemas cosméticos.

---

## 5. Limites da inspeção

* O IPH conta os problemas **encontrados** e **não estima** o total de problemas do portal.
* A inspeção é um julgamento de especialista e não substitui a observação de usuários (M1, M2, M3 e M5).
* Os resultados refletem a versão do portal na data da inspeção.
* A inspeção não equivale a uma auditoria de acessibilidade. Problemas de contraste ou de leitor de tela não são contados no IPH.
* Nenhum dado real foi enviado e nenhuma transação foi concluída durante a inspeção.
