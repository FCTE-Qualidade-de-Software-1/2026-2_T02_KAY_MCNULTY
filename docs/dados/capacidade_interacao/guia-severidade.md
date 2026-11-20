# Protocolo de inspeção heurística de Nielsen (IPH, M4)

Rascunho de apoio aos arquivos `inspecao-heuristica.csv` e `inspecao-heuristica-consolidada.csv`. Base: métrica M4 e Seção 6 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

O objetivo é padronizar a inspeção para que o IPH seja comparável entre avaliadores, módulos e dispositivos. A inspeção é um julgamento de especialistas e não substitui a observação de usuários.

**Pastas.** Os dados ficam em `docs/dados/capacidade_interacao/`, a mesma pasta já usada por `tarefas-e-fluxos.csv` e `cenarios-de-erro.csv`. As capturas ficam em `docs/img/usabilidade/`. Foi mantida `docs/img/usabilidade/` para as capturas, em vez das subpastas por métrica de `docs/assets/evidencias/`, porque as páginas da Fase 3 já referenciam essa pasta (piloto). O módulo e o dispositivo constam no nome do arquivo (Seção 5), o que dispensa subpastas.

## 1. Arquivos e campos de registro

| Arquivo | Uso |
|---|---|
| `inspecao-heuristica.csv` | Modelo em branco. Cada avaliador copia para `inspecao-heuristica_N.csv` (Natan), `inspecao-heuristica_Y.csv` (Yan) ou `inspecao-heuristica_T.csv` (terceiro avaliador, se houver) |
| `inspecao-heuristica-consolidada.csv` | Modelo em branco do arquivo consolidado (Seção 4) |

### 1.1 Campos da lista individual

| Campo | Conteúdo |
|---|---|
| `id_problema` | Identificador no padrão da Seção 5 (ex.: `IPH-PRO-D-N-001`) |
| `avaliador` | `Natan`, `Yan` ou o terceiro avaliador, se houver |
| `modulo` | `Infracao`, `Atendimento`, `Protocolo` ou `Chatbot` |
| `dispositivo` | `Desktop` ou `Mobile` |
| `tela_ou_fluxo` | Tela ou etapa em que o problema ocorre |
| `heuristica_violada` | Código `NH1` a `NH10` (Seção 2) |
| `descricao` | O que ocorre, em uma ou duas frases, e o cenário que o reproduz |
| `severidade` | 0 a 4 (Seção 3) |
| `evidencia` | Nome do arquivo da captura (Seção 5) |
| `data_hora` | Data e hora da inspeção (AAAA-MM-DD hh:mm) |
| `navegador_versao` | Navegador e versão |
| `largura_tela_px` | Largura da janela ou da tela em pixels |
| `dispositivo_modelo_so` | Em Mobile: modelo e sistema operacional do aparelho, ou `emulado` se a inspeção foi feita no DevTools. Em Desktop: sistema operacional |
| `observacoes` | Dúvidas, ligação com outros registros, heurísticas secundárias e observações fora do IPH (Seção 7) |

Valores sem acento nos campos de categoria (`Infracao`), como nos demais CSV do repositório, para não atrapalhar filtros e junções.

Cada linha é uma ocorrência. Um mesmo problema visto em desktop e em mobile gera duas linhas na lista individual e é tratado na consolidação (Seção 4).

### 1.2 O que é "Mobile"

A inspeção em Mobile deve ser feita, sempre que possível, em **aparelho real**. A emulação do DevTools é aceita, mas deve ser registrada como `emulado` em `dispositivo_modelo_so`. A emulação reproduz mal a área de toque e o comportamento do teclado virtual, que são centrais para a hipótese H2 da Fase 2; por isso, achados sobre toque feitos em emulação devem ser marcados em `observacoes` como "a confirmar em aparelho real". Largura de referência: até 480 px, em modo retrato.

## 2. As 10 heurísticas de Nielsen

Para não confundir com as hipóteses H1 a H3 da Fase 2 (GQM), as heurísticas usam o prefixo **NH** (Nielsen, heurística).

| Código | Heurística | O que verificar |
|---|---|---|
| NH1 | Visibilidade do estado do sistema | O portal informa o que está acontecendo, em que etapa o usuário está e se a ação foi concluída |
| NH2 | Correspondência entre o sistema e o mundo real | Linguagem, termos e ordem das informações são compreensíveis para o cidadão, sem jargão técnico ou legal sem explicação |
| NH3 | Controle e liberdade do usuário | É possível voltar, cancelar, desfazer ou sair de um fluxo sem perder o que foi preenchido |
| NH4 | Consistência e padrões | Mesmos nomes, ícones, posições e comportamentos para as mesmas ações, dentro do portal e em relação às convenções da web |
| NH5 | Prevenção de erros | A interface impede o erro antes de ele ocorrer (máscaras, limites, confirmação antes de ações finais) |
| NH6 | Reconhecimento em vez de memorização | Opções, instruções e dados necessários estão visíveis, sem exigir que o usuário lembre de telas anteriores |
| NH7 | Flexibilidade e eficiência de uso | Atalhos, valores padrão e caminhos curtos atendem tanto o iniciante quanto o usuário frequente |
| NH8 | Estética e design minimalista | A tela mostra o necessário, sem informação irrelevante, sobreposições ou elementos que competem pela atenção, nem elementos que bloqueiam a tarefa |
| NH9 | Ajudar a reconhecer, diagnosticar e corrigir erros | As mensagens de erro usam linguagem simples, apontam o campo e sugerem a correção |
| NH10 | Ajuda e documentação | Há ajuda contextual, exemplos e orientação sobre como concluir a tarefa, fácil de achar e curta |

Cada problema recebe **uma** heurística principal, a que melhor explica a falha. Se mais de uma se aplicar, registre a principal em `heuristica_violada` e cite as demais em `observacoes`.

## 3. Guia de severidade

A severidade combina três fatores: frequência (ocorre sempre ou só em casos raros), impacto (o usuário consegue contornar) e persistência (o usuário supera o problema uma vez ou volta a ser afetado).

| Nível | Significado | Critério de decisão | Contabiliza no IPH |
|---|---|---|---|
| 0 | Não é problema | O avaliador não considera a ocorrência um problema de usabilidade | Não |
| 1 | Cosmético | Incômodo visual ou de redação, sem efeito na tarefa; corrigir só se sobrar tempo | Sim (N₁) |
| 2 | Menor | O usuário percebe e contorna sem esforço relevante; baixa prioridade | Sim (N₂) |
| 3 | Maior | O usuário perde tempo, erra ou precisa tentar de novo; pode ocorrer abandono; alta prioridade | Sim (N₃) |
| 4 | Catastrófico | A tarefa não pode ser concluída (beco sem saída) ou há risco de ação irreversível ou de efeito indevido; deve ser corrigido antes de qualquer outro | Sim (N₄) |

### Exemplos por nível

Os exemplos são **ilustrativos** e vêm de **sistemas fictícios, de outros domínios**, para calibrar os avaliadores sem sugerir o que procurar no Detran Digital DF. Não são resultados da avaliação: a severidade de cada problema real é definida na inspeção e na consolidação.

| Nível | Sistema fictício | Exemplo | Heurística principal |
|---|---|---|---|
| 0 | Site de notícias | Cor de destaque diferente da que o avaliador preferiria, sem prejuízo à leitura: preferência pessoal, não problema | – |
| 1 | Aplicativo de biblioteca | Rótulo de coluna em caixa alta, destoando do restante do aplicativo | NH4 |
| 2 | Aplicativo de biblioteca | Ícone de ajuda sem rótulo; o usuário descobre o que ele faz ao tocar | NH6 |
| 3 | Aplicativo bancário | O botão "Voltar" do navegador sai do fluxo de transferência e descarta o que foi digitado, obrigando a refazer a etapa | NH3 |
| 4 | Loja virtual | O botão "Finalizar compra" cobra o cartão sem tela de confirmação e sem cancelamento | NH5 |
| 4 | Sistema de matrícula | Uma tela de erro sem botão de voltar nem de recomeçar impede o aluno de concluir a matrícula | NH3 |

Em caso de dúvida entre dois níveis, discuta na consolidação (Seção 4, passo 6). Não use a média.

## 4. Rotina de inspeção e consolidação

1. **Calibrar.** Antes da inspeção, os avaliadores percorrem juntos **um** fluxo à escolha, severidades incluídas, e anotam onde divergiram. Esse fluxo não entra na contagem. Os desencontros viram regras neste guia.
2. **Preparar.** Cada avaliador copia o `inspecao-heuristica.csv` com o nome da Seção 1. O ambiente de cada sessão (data, hora, navegador, largura, modelo ou `emulado`) é preenchido nas colunas de contexto.
3. **Inspecionar de forma independente.** Cada avaliador percorre os quatro módulos, em desktop e em mobile, sem consultar o outro. Em cada tela, passa pelas 10 heurísticas e registra um problema por linha, com severidade e evidência. O catálogo `tarefas-e-fluxos.csv` cobre **uma** tarefa principal por módulo, mas a inspeção percorre **todas** as telas acessíveis do módulo.
4. **Parar antes de ações finais.** Siga os pontos de parada seguros de `tarefas-e-fluxos.csv`. Para as telas fora das tarefas do catálogo, a regra geral é: **pare antes de qualquer botão de confirmação final** (enviar, concluir, pagar, assinar, agendar). Não envie dados reais.
5. **Entregar as listas.** Quando os dois terminam, as listas são reunidas em `inspecao-heuristica-consolidada.csv`. Nenhum avaliador altera a lista do outro.
6. **Eliminar duplicidades.** Dois registros são o **mesmo problema** quando descrevem a mesma **causa observável**: o mesmo componente ou o mesmo comportamento da interface (por exemplo, "a lista suspensa de unidades sobrepõe o texto"), mesmo que apareçam em telas diferentes do mesmo módulo. A análise é caixa-preta, então a causa é definida pelo que se vê, não pelo que se supõe do código. Regras:
    - Mesma causa em desktop e em mobile: **um** problema, com `dispositivos_afetados = D+M`.
    - Mesma causa em telas diferentes do mesmo módulo: **um** problema, e as telas ficam em `tela_ou_fluxo`.
    - Mesma causa em **módulos diferentes**: um problema **em cada módulo**, pois o IPH é por módulo.
    - Mesma causa com severidades diferentes por dispositivo (por exemplo, grave só em mobile): **dois** problemas, um por dispositivo.
    - Uma linha que reúne várias falhas distintas é **desdobrada** em uma linha por falha antes da comparação.
    - Se a causa difere, são problemas distintos, mesmo na mesma tela.
7. **Definir heurística e severidade finais.** Para cada problema consolidado, os avaliadores comparam as classificações individuais e definem `heuristica_final` e `severidade_final` por consenso. As severidades de cada avaliador permanecem nas colunas `severidade_N`, `severidade_Y` e `severidade_T`. **Sem consenso**, aplica-se, nesta ordem:
    1. Com terceiro avaliador, vale a **mediana** das três severidades.
    2. Sem terceiro avaliador, vale a **severidade mais alta** (decisão conservadora, para não subestimar risco).
    3. A divergência e a justificativa são registradas em `observacoes_consolidacao`.
8. **Calcular o IPH.** Para cada módulo, conte os problemas consolidados por severidade (N₁ a N₄). IPH do módulo = N₁ + N₂ + N₃ + N₄. Apresente sempre a distribuição junto do total. Problemas de severidade 0 não entram. Para o IPH **por dispositivo**, conte os problemas cujo `dispositivos_afetados` inclui o dispositivo (D ou M); um problema `D+M` entra nos dois cálculos, sem mudar a fórmula.
9. **Terceiro avaliador (opcional).** Um terceiro integrante pode inspecionar de forma independente e entra na consolidação do mesmo modo. Registre quantos avaliadores participaram.

### 4.1 Campos do consolidado

`inspecao-heuristica-consolidada.csv` mantém os campos da Seção 1.1, sem `avaliador` e sem `severidade`, e acrescenta:

| Campo | Conteúdo |
|---|---|
| `id_consolidado` | Formato `CONS-{MOD}-{NNN}` (ex.: `CONS-PRO-007`), sequência por módulo |
| `ids_origem` | `id_problema` das linhas individuais reunidas |
| `dispositivos_afetados` | `D`, `M` ou `D+M` |
| `heuristica_final` | Código `NH1` a `NH10` acordado |
| `severidade_N`, `severidade_Y`, `severidade_T` | Severidade de cada avaliador (vazio se não houve o avaliador ou se ele não registrou o problema) |
| `severidade_final` | Severidade definida na consolidação (0 a 4) |
| `observacoes_consolidacao` | Divergências, justificativa e regra de desempate usada |

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

Cada captura mostra a tela inteira, com a largura visível, e deve ser acompanhada de uma descrição do cenário no campo `descricao`. Problemas de severidade 0 **não exigem** captura; registre-os apenas se ajudarem a calibrar.

**Privacidade.** O login gov.br exige uma conta real, e a conta usada nos testes é de **terceiro, com consentimento do titular** (conforme `roteiro-moderador.md`). Por isso, a área autenticada mostra nome e outros dados dessa pessoa. Antes de salvar qualquer captura:

- cubra nome, CPF, e-mail, placa, RENAVAM e demais dados pessoais da área autenticada;
- cubra também a **barra do navegador** (avatar, e-mail da conta, URL com parâmetros);
- grave a cobertura **na própria imagem** (tarja aplicada ao arquivo salvo), nunca em camada separada que possa ser removida;
- mantenha o original sem cobertura fora do repositório, apenas se for indispensável, e apague-o ao fim do trabalho.

## 6. Critério de cobertura

A cobertura está completa quando cada avaliador tiver inspecionado os 4 módulos em Desktop e em Mobile (8 combinações por avaliador). O acompanhamento do andamento fica na issue de execução da inspeção (#55) ou em uma cópia pessoal do avaliador, e **não** neste arquivo, para não misturar protocolo com andamento nem gerar conflito de merge.

## 7. Limites de segurança e de escopo

- A inspeção não envia dados reais nem conclui transações (Seção 6 de `docs/fase2/usabilidade.md`).
- Os resultados refletem a versão do portal na data da inspeção. Registre data, horário, navegador, dispositivo e largura de tela.
- A inspeção não equivale a uma auditoria de acessibilidade. Se o avaliador notar problema de contraste ou de leitor de tela, **registre em `observacoes`**, sem atribuir severidade e **sem contar no IPH**.
- Elementos que bloqueiam a tela até uma ação do usuário (por exemplo, avisos modais de campanha) devem ser registrados como achado de NH8, com a data da inspeção, pois podem não existir na data da coleta de outras métricas.
- A análise usa só o que é observável na interface, sem acesso ao código-fonte.
- O IPH não tem faixas de julgamento na especificação. Os valores são apresentados por módulo com a distribuição por severidade e interpretados junto das demais métricas.
- **Número de avaliadores.** Nielsen recomenda de 3 a 5 avaliadores para a inspeção heurística; com dois, a cobertura dos problemas existentes é menor. O IPH conta os problemas **encontrados** pela equipe e **não estima** o total de problemas do portal.
- **Calibração.** A concordância entre avaliadores antes do consenso (Seção 4, passo 1) é registrada para dar transparência à comparação, mas não a torna estatisticamente validada.
