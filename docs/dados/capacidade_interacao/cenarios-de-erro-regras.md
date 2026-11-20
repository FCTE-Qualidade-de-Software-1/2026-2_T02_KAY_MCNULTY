# Cenários de erro e regras de apuração da TPRE (M3)

Rascunho de apoio ao arquivo `cenarios-de-erro.csv`. A fonte das definições é `docs/fase2/usabilidade.md` (métrica M3). O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

## Arquivos
- `cenarios-de-erro.csv`: modelo com os cenários e as colunas de registro em branco, usado nas sessões com participantes.
- `cenarios-de-erro-piloto.csv`: execução-piloto dos avaliadores, com os resultados registrados. Serve de evidência e de base para a conciliação entre avaliadores; não entra nos dados dos participantes.

## Fórmula e regra de não aplicabilidade
- **TPRE = E_prev ÷ E_tot × 100%**
- **E_prev:** eventos de erro impedidos pela interface ou corrigidos pelo participante na primeira tentativa, após mensagem clara.
- **E_tot:** total de eventos de erro ou invalidação observados nas tarefas.
- **Quando E_tot = 0, a métrica é registrada como não aplicável (N/A) para a execução. Nunca como 100%.**

## Classificação dos eventos (coluna `classificacao_do_evento`)
| Valor | Significado | Conta em E_prev | Conta em E_tot |
|---|---|---|---|
| `prevenido` | A interface impediu o erro (bloqueio, máscara, feedback que impede o envio) | sim | sim |
| `corrigido_1a_tentativa` | Mensagem exibida e o participante corrigiu na primeira tentativa | sim | sim |
| `nao_recuperado` | Mensagem ausente, genérica ou técnica, ou o participante não corrigiu na primeira tentativa | não | sim |
| `sem_erro` | Entrada inválida aceita sem alerta | não | sim |
| `N/A` | Cenário não executado ou observação sem erro | não | não |

## Atendimento
A observação de resumo antes da ação final e da possibilidade de voltar ou cancelar é qualitativa. Só entra em E_prev e E_tot se ocorrer um evento de erro durante o agendamento (cenário E-ATE-05).

## Limites de segurança
- Apenas valores sabidamente inválidos; nenhum CPF, placa ou RENAVAM de terceiros.
- Nenhum cenário gera protocolo, agendamento ou pagamento reais (Seção 6 de `usabilidade.md`).
- Sem testes destrutivos, de estresse ou tentativas de burlar validações.

## Limitações registradas
1. **Infração sem campos de entrada.** O portal exige login gov.br e a consulta de débitos usa o veículo da conta logada, sem digitação de CPF, placa ou RENAVAM. Os cenários E-INF-01 a E-INF-12 foram definidos, mas marcados como não aplicáveis por desenho do portal. Por isso o módulo não atinge o mínimo de 2 cenários executáveis previsto nos critérios de aceitação da issue; a justificativa deve constar no texto final.
2. **Anexos no Protocolo.** O documento do Requerimento Geral é gerado pelo próprio portal e a tela de anexos só aparece depois da assinatura com gov.br. Como a assinatura tem validade legal e a Seção 6 proíbe efeitos reais, os cenários de anexo inválido não foram executados. O módulo é coberto pelos cenários de campos do formulário (E-PRO-01, E-PRO-08 e E-PRO-09).
3. **Login.** Todas as ações, exceto o assistente virtual, exigem login gov.br. As tarefas dos módulos Infração, Atendimento e Protocolo começam com a sessão já iniciada na conta de teste de um avaliador.

## Achados qualitativos do piloto
- **Protocolo:** o Requerimento Geral avançou até a tela de assinatura sem validar objeto vazio, placa incompleta ou Renavam curto (`sem_erro`).
- **Chatbot:** entrada vazia e só espaços foram prevenidas com feedback visual (a caixa treme, sem texto); texto incoerente, pergunta fora do escopo e símbolos receberam resposta com orientação e foram corrigidos na primeira tentativa. O conteúdo da resposta a uma mesma pergunta variou entre execuções.
- **Atendimento:** não há tela de resumo antes da ação final, não há opção de cancelar o fluxo, não é possível voltar sem perder o que foi preenchido e o portal não informa como cancelar ou reagendar depois de concluído.

Esses números e achados vêm do piloto dos avaliadores e não substituem a apuração com participantes.
