# Evidências da inspeção heurística (IPH, M4)

Esta pasta guarda as capturas de tela da inspeção heurística de Capacidade de Interação no Portal Detran Digital DF. Ela ainda não contém capturas: elas são geradas na execução da inspeção (issue de execução da Fase 4).

O protocolo completo está em `docs/dados/capacidade_interacao/guia-severidade.md`. Os registros ficam em `docs/dados/capacidade_interacao/inspecao-heuristica.csv`.

## Padrão de nomes

`{id_problema}_{AAAA-MM-DD}.png`

O `id_problema` segue `IPH-{MOD}-{D|M}-{A}-{NNN}`:

| Parte | Valores |
|---|---|
| `MOD` | `INF` (Infração), `ATE` (Atendimento), `PRO` (Protocolo), `BOT` (Chatbot) |
| `D` ou `M` | Desktop ou Mobile |
| `A` | Inicial do avaliador (`N` para Natan, `Y` para Yan, `T` para um terceiro) |
| `NNN` | Sequência de três dígitos por avaliador, módulo e dispositivo |

Exemplo: `IPH-PRO-M-Y-003_2026-11-18.png`.

O nome da captura deve ser igual ao valor da coluna `evidencia` do CSV.

## O que cada captura deve mostrar

- A tela inteira em que o problema ocorre, com a largura visível.
- O elemento do problema à vista. Se precisar de destaque, use uma marcação (caixa ou seta) em uma cópia, e mantenha o original.
- Uma descrição do cenário no campo `descricao` do CSV, pois a imagem sozinha não reproduz o problema.

## Privacidade e segurança

- Use só conta de teste e valores sabidamente fictícios.
- Cubra qualquer dado pessoal real (CPF, placa, RENAVAM, nome, e-mail) antes de salvar. Os arquivos versionados devem estar anonimizados.
- Não registre capturas de transações concluídas: a inspeção para nos pontos de parada seguros.

## Formato

PNG, uma imagem por problema. Sem subpastas: o módulo e o dispositivo já constam no nome.
