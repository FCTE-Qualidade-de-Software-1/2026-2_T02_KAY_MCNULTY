# Protocolo de inspeção heurística de Nielsen (IPH, M4)

Rascunho de apoio ao arquivo `inspecao-heuristica.csv`. Base: métrica M4 e Seção 6 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

O objetivo é padronizar a inspeção para que o IPH seja comparável entre avaliadores, módulos e dispositivos. A inspeção é um julgamento de especialistas e não substitui a observação de usuários.

## 1. Arquivos e campos de registro

`inspecao-heuristica.csv` é o modelo em branco. Cada avaliador usa uma cópia própria durante a inspeção independente.

| Campo | Conteúdo |
|---|---|
| `id_problema` | Identificador no padrão da Seção 5 (ex.: `IPH-PRO-D-N-001`) |
| `avaliador` | `Natan`, `Yan` ou o terceiro avaliador, se houver |
| `modulo` | `Infração`, `Atendimento`, `Protocolo` ou `Chatbot` |
| `dispositivo` | `Desktop` ou `Mobile` |
| `tela_ou_fluxo` | Tela ou etapa em que o problema ocorre |
| `heuristica_violada` | Código `H1` a `H10` (Seção 2) |
| `descricao` | O que ocorre, em uma ou duas frases, e o cenário que o reproduz |
| `severidade` | 0 a 4 (Seção 3) |
| `evidencia` | Nome do arquivo da captura (Seção 5) |
| `data_hora` | Data e hora da inspeção (AAAA-MM-DD hh:mm) |
| `navegador_versao` | Navegador e versão |
| `largura_tela_px` | Largura da janela ou da tela em pixels |
| `observacoes` | Dúvidas, ligação com outros registros |

Cada linha é uma ocorrência. Um mesmo problema visto em desktop e em mobile gera duas linhas na inspeção individual e é tratado na consolidação (Seção 4).

O arquivo consolidado (`inspecao-heuristica-consolidada.csv`, issue de execução da Fase 4) mantém esses campos e acrescenta `id_consolidado`, `severidade_avaliador_1`, `severidade_avaliador_2` e `severidade_final`.

## 2. As 10 heurísticas de Nielsen

| Código | Heurística | O que verificar |
|---|---|---|
| H1 | Visibilidade do estado do sistema | O portal informa o que está acontecendo, em que etapa o usuário está e se a ação foi concluída |
| H2 | Correspondência entre o sistema e o mundo real | Linguagem, termos e ordem das informações são compreensíveis para o cidadão, sem jargão técnico ou legal sem explicação |
| H3 | Controle e liberdade do usuário | É possível voltar, cancelar, desfazer ou sair de um fluxo sem perder o que foi preenchido |
| H4 | Consistência e padrões | Mesmos nomes, ícones, posições e comportamentos para as mesmas ações, dentro do portal e em relação às convenções da web |
| H5 | Prevenção de erros | A interface impede o erro antes de ele ocorrer (máscaras, limites, confirmação antes de ações finais) |
| H6 | Reconhecimento em vez de memorização | Opções, instruções e dados necessários estão visíveis, sem exigir que o usuário lembre de telas anteriores |
| H7 | Flexibilidade e eficiência de uso | Atalhos, valores padrão e caminhos curtos atendem tanto o iniciante quanto o usuário frequente |
| H8 | Estética e design minimalista | A tela mostra o necessário, sem informação irrelevante, sobreposições ou elementos que competem pela atenção |
| H9 | Ajudar a reconhecer, diagnosticar e corrigir erros | As mensagens de erro usam linguagem simples, apontam o campo e sugerem a correção |
| H10 | Ajuda e documentação | Há ajuda contextual, exemplos e orientação sobre como concluir a tarefa, fácil de achar e curta |

Cada problema recebe **uma** heurística principal, a que melhor explica a falha. Se mais de uma se aplicar, registre a principal em `heuristica_violada` e cite as demais em `observacoes`.

## 3. Guia de severidade

A severidade combina três fatores: frequência (ocorre sempre ou só em casos raros), impacto (o usuário consegue contornar) e persistência (o usuário supera o problema uma vez ou volta a ser afetado).

| Nível | Significado | Critério de decisão | Contabiliza no IPH |
|---|---|---|---|
| 0 | Não é problema | O avaliador não considera a ocorrência um problema de usabilidade | Não |
| 1 | Cosmético | Incomodo visual ou de redação, sem efeito na tarefa; corrigir só se sobrar tempo | Sim (N₁) |
| 2 | Menor | O usuário percebe e contorna sem esforço relevante; baixa prioridade | Sim (N₂) |
| 3 | Maior | O usuário perde tempo, erra ou precisa tentar de novo; pode ocorrer abandono; alta prioridade | Sim (N₃) |
| 4 | Catastrófico | A tarefa não pode ser concluída ou há risco de ação irreversível ou de efeito indevido; deve ser corrigido antes de qualquer outro | Sim (N₄) |

### Exemplos por nível, aplicados aos módulos

Os exemplos são **ilustrativos**, para calibrar os avaliadores. Não são resultados da avaliação: a severidade de cada problema real é definida na inspeção e na consolidação.

| Nível | Módulo | Exemplo | Heurística |
|---|---|---|---|
| 0 | Chatbot | Resposta diferente a cada execução para a mesma pergunta, desde que o conteúdo seja correto: variação esperada de um assistente de IA, não é problema de interface | – |
| 1 | Infração | Rótulo de coluna em caixa alta, destoando do restante do portal | H4 |
| 2 | Chatbot | O assistente, ao não entender, responde sem sugerir exemplos de pergunta, mas o usuário pode reformular | H9 |
| 3 | Protocolo | O formulário avança para a etapa de assinatura com campo obrigatório vazio, sem aviso | H5 |
| 3 | Atendimento | Não há tela de resumo antes de concluir o agendamento | H1, H5 |
| 4 | Atendimento | Um erro no meio do fluxo apaga todo o formulário e não há como retomar | H3 |

Em caso de dúvida entre dois níveis, discuta na consolidação. Não use a média: registre cada avaliador e defina o valor final por consenso.

## 4. Rotina de inspeção e consolidação

1. **Preparar.** Cada avaliador abre uma cópia do `inspecao-heuristica.csv` e o checklist de cobertura (Seção 6). O ambiente de cada sessão (data, hora, navegador, largura) é preenchido nas colunas de contexto.
2. **Inspecionar de forma independente.** Cada avaliador percorre os quatro módulos, em desktop e em mobile, sem consultar o outro. Em cada tela, passa pelas 10 heurísticas e registra um problema por linha, com severidade e evidência.
3. **Parar nos pontos seguros.** Siga os pontos de parada seguros do catálogo de tarefas e fluxos. Não envie dados reais e não conclua protocolo, agendamento nem pagamento.
4. **Entregar as listas.** Quando os dois terminam, as listas são reunidas. Nenhum avaliador altera a lista do outro.
5. **Eliminar duplicidades.** Dois registros são o mesmo problema quando descrevem a mesma falha, na mesma tela ou fluxo, com a mesma causa. Um problema visto em desktop e em mobile conta uma vez se a causa for a mesma. Se a causa difere, são dois problemas.
6. **Definir a severidade final.** Para cada problema consolidado, os avaliadores comparam as severidades individuais e chegam a um valor por consenso. Divergências e a justificativa ficam registradas.
7. **Calcular o IPH.** Para cada módulo, conte os problemas consolidados por severidade (N₁ a N₄). IPH do módulo = N₁ + N₂ + N₃ + N₄. Apresente sempre a distribuição junto do total. Problemas de severidade 0 não entram na contagem.
8. **Terceiro avaliador (opcional).** Um terceiro integrante da equipe pode inspecionar de forma independente e entra na consolidação do mesmo modo. Registre quantos avaliadores participaram.

## 5. Evidências e padrão de nomes

As capturas ficam em `docs/img/usabilidade/` e são nomeadas como o problema:

`{id_problema}_{AAAA-MM-DD}.png`

O `id_problema` tem o formato `IPH-{MOD}-{D|M}-{A}-{NNN}`:

| Parte | Valores |
|---|---|
| `MOD` | `INF` (Infração), `ATE` (Atendimento), `PRO` (Protocolo), `BOT` (Chatbot) |
| `D` ou `M` | Desktop ou Mobile |
| `A` | Inicial do avaliador (`N` para Natan, `Y` para Yan, `T` para o terceiro) |
| `NNN` | Sequência de três dígitos por avaliador, módulo e dispositivo |

Exemplo: `IPH-PRO-M-Y-003_2026-11-18.png`.

Cada captura mostra a tela inteira, com a largura visível, e deve ser acompanhada de uma descrição do cenário no campo `descricao`. Capturas não podem expor dados pessoais: use apenas conta de teste e valores sabidamente fictícios, e cubra qualquer dado real antes de salvar.

## 6. Checklist de cobertura

Marque cada célula quando o avaliador terminar. A cobertura está completa quando as 8 células de cada avaliador estiverem marcadas.

| Módulo | Desktop (Natan) | Mobile (Natan) | Desktop (Yan) | Mobile (Yan) |
|---|:---:|:---:|:---:|:---:|
| Infração | [ ] | [ ] | [ ] | [ ] |
| Atendimento | [ ] | [ ] | [ ] | [ ] |
| Protocolo | [ ] | [ ] | [ ] | [ ] |
| Chatbot | [ ] | [ ] | [ ] | [ ] |

## 7. Limites de segurança e de escopo

- A inspeção não envia dados reais nem conclui transações (Seção 6 de `docs/fase2/usabilidade.md`).
- Os resultados refletem a versão do portal na data da inspeção. Registre data, horário, navegador, dispositivo e largura de tela.
- A inspeção não equivale a uma auditoria de acessibilidade. Contraste e leitores de tela ficam fora do escopo.
- A análise usa só o que é observável na interface, sem acesso ao código-fonte.
- O IPH não tem faixas de julgamento na especificação. Os valores são apresentados por módulo com a distribuição por severidade e interpretados junto das demais métricas.
