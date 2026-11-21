# Catálogo de tarefas e fluxos de referência (P_min): notas

Rascunho de apoio ao arquivo `tarefas-e-fluxos.csv`. Base: regra 1 da Seção 4 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

## Escopo
Uma tarefa principal por módulo do Portal Detran Digital DF, em desktop e mobile (8 linhas): consultar infrações (T1), agendar atendimento (T2), abrir protocolo (T3) e interagir com o chatbot (T4). Os enunciados são neutros: não citam nomes de menus ou botões.

## Regra de contagem do P_min
- Cada clique ou toque é 1 passo.
- O preenchimento de um campo também é 1 passo.
- Os dois avaliadores (Natan e Yan) percorreram os fluxos de forma independente e conciliaram a contagem.

## P_min por tarefa
| Tarefa | Módulo | Desktop | Mobile |
|---|---|---|---|
| T1 | Consultar infrações | 5 | 3 |
| T2 | Agendar atendimento | 12 | 12 |
| T3 | Abrir protocolo (Requerimento Geral) | 7 | 7 |
| T4 | Chatbot | 4 | 4 |

## Login gov.br
Todas as ações do portal, exceto o assistente virtual, exigem login gov.br. Decisão: as tarefas T1 a T3 começam com sessão iniciada e **o login não conta no P_min**. A T4 não exige login. Os participantes usam apenas conta de teste; nunca dados de terceiros.

## Pontos de parada seguros (Seção 6)
Nenhuma tarefa gera protocolo, agendamento ou pagamento reais.
- **T1:** na tela com a lista de infrações e valores, sem pagar, emitir boleto, recorrer ou indicar condutor.
- **T2:** no formulário preenchido (categoria, consentimento, unidade, data e hora), antes de clicar em Concluir agendamento. O portal não tem tela de resumo antes da ação final.
- **T3:** no fluxo do Requerimento Geral, ao chegar à etapa de assinatura do documento gerado pelo portal, sem concluir a assinatura com gov.br. O P_min da T3 inclui o passo "Assinar Documento", conforme a conciliação dos avaliadores.
- **T4:** quando a resposta do assistente sobre o prazo de recurso aparece.

## Decisões de escopo
- **T3 usa o Requerimento Geral.** O tipo "Acesso a processos" exige o número de um processo existente, o que não pode ser garantido igual para todos os participantes.
- **T4 mantém a pergunta sobre prazo de recurso.** A resposta do assistente varia entre execuções; por isso a condição de conclusão é "uma resposta sobre o prazo, indicando onde ele consta e como é contado", e não um valor em dias.
