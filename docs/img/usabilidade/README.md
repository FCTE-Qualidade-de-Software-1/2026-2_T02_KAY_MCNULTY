# Evidências da inspeção heurística (IPH, M4)

Esta pasta guarda as capturas de tela da inspeção heurística de Capacidade de Interação no Portal Detran Digital DF. As capturas da inspeção são geradas na execução da inspeção (issue de execução da Fase 4).

O protocolo completo está em `docs/dados/capacidade_interacao/guia-severidade.md`. Os registros ficam em `docs/dados/capacidade_interacao/` (`inspecao-heuristica.csv` e `inspecao-heuristica-consolidada.csv`).

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

## Exceção: capturas do piloto

As capturas do **piloto dos instrumentos** ficam na subpasta `piloto/` e seguem outro padrão, porque não são problemas da inspeção e não entram no IPH:

`PILOTO-{etapa}_{dispositivo}_{AAAA-MM-DD}.png`

Elas não têm `id_problema` e não são referenciadas pelos CSV da inspeção.

## O que cada captura deve mostrar

- A tela inteira em que o problema ocorre, com a largura visível.
- O elemento do problema à vista. Se precisar de destaque, use uma marcação (caixa ou seta) em uma cópia, e mantenha o original fora do repositório.
- Uma descrição do cenário no campo `descricao` do CSV, pois a imagem sozinha não reproduz o problema.

## Privacidade e segurança

O login gov.br exige conta real. A conta usada é de **terceiro, com consentimento do titular**, então a área autenticada mostra dados pessoais dessa pessoa.

- Cubra qualquer dado pessoal (nome, CPF, e-mail, placa, RENAVAM, dados do perfil) antes de salvar.
- Cubra também a barra do navegador: avatar, e-mail da conta e URL com parâmetros.
- A cobertura deve ser **gravada na imagem** (tarja aplicada ao arquivo salvo), nunca em camada separada.
- Os arquivos versionados não podem conter dados pessoais legíveis.
- Não registre capturas de transações concluídas: a inspeção para nos pontos de parada seguros.

## Formato

PNG, uma imagem por problema. Sem subpastas, exceto `piloto/`: o módulo e o dispositivo já constam no nome.
