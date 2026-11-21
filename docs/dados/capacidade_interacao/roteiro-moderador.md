# Plano do teste com participantes e roteiro do moderador

Rascunho de apoio aos arquivos `registro-tarefas.csv`, `cenarios-de-erro-sessoes.csv`, `sus-ptbr.md` e `sus-respostas.csv`. Base: métricas M1 (TCAPA), M2 (IEFO), M3 (TPRE) e M5 (SUS) e Seções 4 e 6 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

Este plano usa o catálogo de tarefas e fluxos ([`tarefas-e-fluxos.csv`](tarefas-e-fluxos.csv), issue #50) e os cenários de erro ([`cenarios-de-erro.csv`](cenarios-de-erro.csv) e [`cenarios-de-erro-regras.md`](cenarios-de-erro-regras.md), issue #51), ambos já na pasta `docs/dados/capacidade_interacao/`. Os enunciados, os pontos de parada seguros e o P_min vêm desses arquivos e não são repetidos aqui.

## 1. Perfil e amostra

**Idade mínima: 18 anos.** Menores de idade não participam (LGPD, art. 14).

**Perfis.** O teste usa dois grupos (`grupo`: `cidadao` ou `engenheiro`):

| Grupo | Perfil | Objetivo |
|---|---|---|
| Cidadãos | Pessoas com diferentes faixas etárias e níveis de letramento digital, que usariam o portal como cidadãos | Representar o público do serviço |
| Engenheiros avaliadores | Estudantes ou profissionais de engenharia, sem participação na inspeção heurística | Complementar com um olhar técnico |

Quem fez a inspeção heurística (Natan e Yan) não participa do teste, pois já conhece os fluxos e não está em primeiro acesso.

**Faixas etárias** (`faixa_etaria`): `18-29`, `30-44`, `45-59`, `60+`. A amostra deve cobrir **pelo menos 3** faixas diferentes.

**Nível de letramento digital** (`letramento_digital`). Classificado na triagem, com três perguntas de sim ou não:

1. Você costuma resolver serviços online sozinho(a) (banco, governo, compras)?
2. Você já preencheu formulários longos online sem ajuda?
3. Você usa aplicativos no celular ou programas no computador sem pedir ajuda de outra pessoa?

Três "sim" = `alto`; dois = `medio`; zero ou um = `baixo`. A classificação é feita **antes** da sessão e não é informada ao participante.

**Tamanho mínimo: 6 participantes.** Cada um usa **um único dispositivo**, para que o aprendizado de uma execução não contamine a outra. A distribuição entre dispositivos deve respeitar:

| Dispositivo | Participantes | Composição mínima |
|---|---|---|
| Desktop | 3 | pelo menos 1 cidadão de baixo letramento |
| Mobile | 3 | pelo menos 1 cidadão de baixo letramento |

Pelo menos 1 engenheiro na amostra, **sem concentrar todos os engenheiros no mesmo dispositivo**. Se a composição mínima não for atingida até a data de corte (Seção 10 de `docs/fase3/usabilidade.md`), registre a limitação e o que ficou sem cobertura.

**Participantes com deficiência.** Podem participar, como qualquer outra pessoa que atenda aos critérios, mas **não são recrutados como grupo específico**. Se usarem tecnologia assistiva, registre em `observacoes`, pois isso muda o contexto de acesso. A avaliação não equivale a uma auditoria de acessibilidade.

**Justificativa e limites da amostra.** A amostra é de conveniência, com finalidade diagnóstica: serve para identificar dificuldades recorrentes, não para estimar proporções da população. A literatura indica que poucos participantes já revelam boa parte dos problemas de interface (VIRZI, 1992; NIELSEN; LANDAUER, 1993), mas esse resultado vale para grupos **homogêneos**, e esta amostra tem dois grupos, dois dispositivos e três participantes por dispositivo. Por isso:

- os percentuais por módulo e por dispositivo têm 3 tarefas por célula e saem em múltiplos de 33%. **Não aplique as faixas da Seção 4 da Fase 2 a essas células**; reporte **contagens** (ex.: "2 de 3");
- as faixas de julgamento podem ser aplicadas ao total de cada métrica, sempre com numerador, denominador e a ressalva de amostra pequena;
- os resultados **não podem ser generalizados** além da amostra (Seção 6 da Fase 2).

**Denominador de M1.** Com 6 participantes e 4 tarefas, N_tot = 24 tarefas (12 por dispositivo). A T1 depende de uma conta com veículo (Seção 2): **se ela não for obtida antes do recrutamento**, a T1 sai de N_tot e é registrada à parte, como prevê a regra 3 da Seção 4 da Fase 2. Nesse caso, N_tot = 18 (9 por dispositivo) e a hipótese H1 fica inconclusiva para o módulo de Infração. Se algum participante deixar de fazer uma tarefa por motivo alheio ao portal, registre e ajuste o denominador.

**Critério de primeiro acesso.** O participante nunca executou a tarefa no portal e não recebe demonstração prévia. Ter usado o portal para outro fim não o exclui, mas deve ser registrado (`ja_usou_portal`). A triagem pergunta, **para cada tarefa**, se o participante já a executou antes (`ja_executou_tarefa`): se sim, a execução é registrada, mas **não entra em N_tot** de M1.

**Falha técnica e repetição.** Se uma falha alheia ao portal interromper a tarefa (internet, travamento), registre a tentativa 1 com `motivo_nao_conclusao = falha_tecnica_externa`. A repetição (`tentativa = 2`) **entra em N_tot no lugar da primeira**, desde que o participante **não tenha chegado ao ponto de parada seguro** na tentativa 1. Se já tinha chegado, ele deixou de estar em primeiro acesso e a tarefa é excluída de N_tot, com o motivo registrado.

**Participantes da validação do protótipo.** O teste rápido da validação do protótipo (Fase 4) deve, preferencialmente, usar participantes diferentes dos deste teste, porque quem já fez as tarefas no portal atual deixa de estar em primeiro acesso.

## 2. Preparação da sessão

- **Conta de teste gov.br.** O portal só aceita conta gov.br real. A conta usada é de **terceiro, com o consentimento do titular**, e deve ter **veículo vinculado** (necessário para a T1). Nome e dados do titular aparecem na tela e na gravação, e o termo avisa o participante (Seção 3). O titular não é identificado nos arquivos do repositório.
- **Login.** O login conta como o passo `Login` do catálogo, no P_min e no P_exec, e é igual para todos. A senha e o código do segundo fator são digitados pelo **moderador**, com o titular fornecendo o código; essa digitação **não é auxílio externo**. O participante executa o clique de entrada.
- **Dados.** Valores fictícios para os campos, preparados antes. O participante nunca usa conta ou documento pessoal.
- Navegador em janela anônima, na página inicial do portal, conforme o estado inicial de cada tarefa em `tarefas-e-fluxos.csv`.
- Desktop: registrar a faixa de largura. Mobile: celular em modo retrato.
- **Gravação de tela e de áudio** habilitada, quando o participante consentir. A tela autenticada mostra dados do titular da conta, e a voz é dado pessoal (Seção 3).
- **Cronômetro.** Não é usado para M2, que mede passos. É usado só para o **teto de tempo por tarefa** (Seção 4.3).
- Cópia em branco de `registro-tarefas.csv`, de `cenarios-de-erro-sessoes.csv` e do formulário do SUS, **em papel**.
- Definir quem modera e quem observa. O observador conta os passos e preenche o registro; o moderador não interfere.
- **Sessão P00 (piloto, fora da amostra).** Antes das sessões oficiais, uma sessão com alguém que não entra na amostra valida a duração, a contagem de passos e a regra de auxílio. Seus dados não entram nos resultados.
- Duração estimada: **45 a 60 minutos** (Seção 4.2).

## 3. Termo de consentimento e tratamento dos dados

### 3.1 Texto do termo (para leitura e assinatura)

> **Termo de consentimento – Avaliação de usabilidade do Portal Detran Digital DF**
>
> Você está sendo convidado(a) a participar de um teste acadêmico da disciplina Qualidade de Software 1 (UnB/FCTE). O objetivo é avaliar o **portal**, não você. Não existem respostas certas ou erradas. É preciso ter **18 anos ou mais**.
>
> Você fará algumas tarefas no portal e depois responderá a um questionário curto. A sessão dura de 45 a 60 minutos. Nenhuma tarefa gera protocolo, agendamento ou pagamento reais.
>
> - A participação é voluntária. Você pode parar a qualquer momento e **retirar seu consentimento**, inclusive depois da sessão, pedindo a **exclusão dos seus dados** ao responsável abaixo.
> - Seus dados serão identificados por um **código** (por exemplo, P01), e não pelo seu nome. Isso é **pseudonimização**: a equipe guarda, fora do repositório, o termo assinado que liga o código a você.
> - Não pediremos nem registraremos dados pessoais seus (nome, CPF, e-mail, telefone) nos arquivos de resultado. Registramos apenas faixa etária, nível de familiaridade com tecnologia e o tipo de aparelho.
> - **Conta de teste.** O portal exige login do gov.br, e usaremos a conta de **outra pessoa, que consentiu**. **Nome e dados dessa pessoa podem aparecer na tela e na gravação.** Não os leia em voz alta nem os anote.
> - **Gravação.** Com a sua permissão, gravaremos a **tela e o áudio** (você pensando em voz alta). A gravação será usada só para conferir a contagem de passos e **não será publicada**. Será apagada em [DATA A CONFIRMAR COM O DOCENTE, ao fim da disciplina].
> - Os resultados serão publicados em tabelas **identificadas apenas pelo código**, sem nome, e sem a gravação.
> - Responsável e contato para dúvidas, retirada do consentimento e exclusão de dados: [NOME E CONTATO DO RESPONSÁVEL, A PREENCHER ANTES DA COLETA].
>
> Declaro que li e entendi este termo e aceito participar.
>
> Participante (código): ______  Data: ____/____/______
> Assinatura ou aceite verbal registrado pelo moderador: ______
> Autorizo a gravação de tela e áudio:  ( ) sim  ( ) não

### 3.2 Pseudonimização e guarda dos dados (LGPD)

1. Cada participante recebe um código sequencial (`P01`, `P02`, …) no início da sessão.
2. O código é a **única** identificação nos arquivos versionados (`registro-tarefas.csv`, `cenarios-de-erro-sessoes.csv`, `sus-respostas.csv`, capturas e notas). Isso é **pseudonimização**, e não anonimização: os dados por participante continuam ligados a um código que pode ser relacionado a uma pessoa pelo termo assinado.
3. **Termo assinado.** Fica **fora do repositório**, em pasta de acesso restrito aos dois integrantes da dupla (Natan e Yan), e é destruído ao fim da disciplina, na data confirmada com o docente. Qualquer tabela código ↔ nome segue a mesma regra.
4. O perfil é registrado por categorias amplas (faixa etária e nível de letramento digital), nunca por idade exata, profissão específica ou local de moradia.
5. **Quase-identificadores.** Em uma amostra de 6 pessoas conhecidas da equipe, o horário exato, a versão do navegador e a largura exata da tela podem reidentificar. Por isso o registro guarda só a **data** (sem horário), o **nome do navegador** (sem versão), o **sistema operacional** e uma **faixa de largura**.
6. As gravações **não são versionadas**. As capturas versionadas não podem conter dado pessoal legível, inclusive o do titular da conta.

## 4. Roteiro do moderador

### 4.1 Princípios

- **Fala neutra.** O moderador não indica menus, botões nem o caminho. Os enunciados são lidos exatamente como estão em `tarefas-e-fluxos.csv`.
- **Primeiro acesso.** Nenhuma demonstração antes da tarefa.
- **Pensar em voz alta.** Peça ao participante para dizer o que está tentando fazer, sem forçar.
- **Sem dicas, sem julgamento.** Não confirme nem corrija o que o participante faz. Respostas neutras, como "Faça como faria normalmente", são permitidas.
- **Parada segura.** Interrompa a tarefa no ponto de parada seguro definido no catálogo. Se o participante tentar concluir uma ação real (pagar, agendar, assinar), interrompa de forma neutra e registre com `motivo_nao_conclusao = acao_real`.

### 4.2 Sequência da sessão

1. **Boas-vindas e termo** (5 min). Explique o objetivo ("avaliamos o portal, não você"), leia o termo, registre o consentimento, a autorização de gravação e o código.
2. **Perfil** (3 min). Faça as três perguntas de letramento, registre a faixa etária e pergunte se já usou o portal e **se já executou cada uma das tarefas**.
3. **Tarefas T1 a T3, em ordem rotacionada, e depois T4** (até 35 min). Leia o enunciado, deixe o participante executar e anote no registro. A ordem segue a Seção 4.4. O login é o da Seção 2.
4. **Cenários de erro** (até 8 min). Aplicados **depois** das tarefas, em repetição separada (Seção 4.5).
5. **SUS** (3 min). Aplique o questionário (`sus-ptbr.md`) **logo após os cenários de erro e antes de qualquer discussão**. Não comente o resultado.
6. **Encerramento** (2 min). Pergunte livremente sobre dificuldades e agradeça. Esse momento é qualitativo e fica depois do SUS.

Tempo típico: cerca de 45 min; máximo, cerca de 60 min.

### 4.3 O que conta como solicitação de auxílio externo

A solicitação de auxílio é o que decide se a tarefa conta em N_aut (M1). A regra vale para todos os moderadores.

**Conta como auxílio externo** (a tarefa deixa de ser autônoma, mesmo se concluída):
- O participante pede ao moderador uma instrução, uma dica ou a confirmação de que está no caminho certo.
- O participante pergunta "onde fica…", "como faço…" ou "está certo?".
- O moderador dá qualquer informação que oriente o caminho, mesmo sem ser pedida.
- O participante consulta outra pessoa, tutorial ou buscador para saber como realizar a tarefa.
- O participante pede para desistir ou para ver a resposta.

**Não conta como auxílio externo:**
- Esclarecer o **enunciado** (o que a tarefa pede), sem mencionar o portal.
- Pedir o valor fictício de um campo.
- A digitação de senha e código do gov.br pelo moderador (Seção 2).
- Lembrar o participante de falar em voz alta ou perguntar "o que você está pensando?".
- Usar a **ajuda interna do próprio portal** (texto de ajuda, assistente virtual quando não é a tarefa). Registre o uso em `usou_ajuda_do_portal` e em `observacoes`.
- Questões técnicas alheias ao portal (Seção 1, "Falha técnica e repetição").

**Regras de registro:**
- A tarefa é **autônoma** quando `concluiu = sim` e `pediu_ajuda = nao`.
- `concluiu = sim` significa que o participante **alcançou o ponto de parada seguro** do catálogo e cumpriu a condição de conclusão da tarefa.
- Registre o tipo da ajuda em `tipo_ajuda` (valores na Seção 5.1).
- **Teto de tempo por tarefa:** 10 minutos para T1 a T3 e 5 minutos para T4, contados pelo observador a partir da leitura do enunciado. Ao atingir o teto, ou se o participante desistir, o moderador encerra a tarefa, que é registrada como **não concluída** (`motivo_nao_conclusao = teto_de_tempo` ou `desistencia`). O teto serve só para padronizar o encerramento; o tempo não é métrica.
- A decisão sobre o que é auxílio é do **observador**, anotada no momento. **Em dúvida, registre como auxílio** e justifique em `observacoes`. Essa é uma **escolha consciente**, que tende a deslocar o TCAPA para baixo, e deve ser declarada nos resultados.
- **Conferência.** Em pelo menos 2 sessões, uma segunda pessoa confere a contagem de passos e a decisão de auxílio pela gravação, e as diferenças são registradas.

### 4.4 Ordem das tarefas e viés de aprendizado

A **T4 (chatbot) é sempre a última**, porque o assistente pode ensinar o caminho de T1 a T3 e quebrar o primeiro acesso. As tarefas T1 a T3 são rotacionadas em **quadrado latino**, em que cada tarefa aparece uma vez em cada posição dentro de cada dispositivo:

| Participante | Dispositivo | Ordem |
|---|---|---|
| P01 | Desktop | T1 – T2 – T3 – T4 |
| P02 | Desktop | T2 – T3 – T1 – T4 |
| P03 | Desktop | T3 – T1 – T2 – T4 |
| P04 | Mobile | T1 – T3 – T2 – T4 |
| P05 | Mobile | T3 – T2 – T1 – T4 |
| P06 | Mobile | T2 – T1 – T3 – T4 |

Mesmo assim, T2 e T3 têm trechos parecidos de formulário, então a rotação **reduz, mas não elimina**, o efeito de ordem. Registre a ordem de cada participante em `ordem_sessao`.

### 4.5 Cenários de erro (M3)

Os cenários de `cenarios-de-erro.csv` marcados com `prioridade_na_sessao = núcleo` são aplicados **depois que a tarefa chegou ao ponto de parada**, em uma **repetição separada**. Assim, os passos de reentrada e correção **não entram em P_exec** (que seria penalizado, já que o P_min não os inclui) e a dificuldade do erro induzido **não vira pedido de ajuda em M1**.

- O moderador fornece o valor inválido e diz apenas "digite este valor".
- Os eventos são registrados em `cenarios-de-erro-sessoes.csv`, com a classificação de `cenarios-de-erro-regras.md`.
- **Quando E_tot = 0, a M3 é "não aplicável" e nunca 100%.**
- Os cenários E-INF-01 a E-INF-12 são não aplicáveis por desenho do portal (consulta pela conta logada) e não são executados.

### 4.6 Escopo do SUS

O SUS é aplicado **uma vez por participante, referindo-se ao Portal Detran Digital DF como um todo**, considerando as tarefas realizadas na sessão. A razão é prática e metodológica: o SUS mede a percepção geral do sistema e perde validade se aplicado a trechos curtos, e a aplicação por módulo geraria quatro questionários por pessoa.

Como o login do gov.br não é parte do portal, a instrução pede que **o participante não considere o login** (ver `sus-ptbr.md`). O SUS é apresentado por participante e como média, e **não por módulo**. A comparação entre módulos fica a cargo de M1, M2, M3 e M4 (IPH). O formulário é **em papel**, para não coletar e-mail nem IP.

## 5. Dados a registrar e ligação com as métricas

### 5.1 Campos e valores fixos

`registro-tarefas.csv` tem uma linha por participante, tarefa e tentativa. Valores aceitos:

| Campo | Valores |
|---|---|
| `grupo` | `cidadao`, `engenheiro` |
| `faixa_etaria` | `18-29`, `30-44`, `45-59`, `60+` |
| `letramento_digital` | `baixo`, `medio`, `alto` |
| `dispositivo` | `Desktop`, `Mobile` |
| `sistema_operacional` | Nome do sistema (ex.: `Android`, `iOS`, `Windows`, `Linux`) |
| `navegador` | Nome do navegador, sem versão |
| `faixa_largura` | `ate_480`, `481_1024`, `acima_1024` |
| `ja_usou_portal`, `ja_executou_tarefa`, `primeiro_acesso`, `concluiu`, `pediu_ajuda`, `usou_ajuda_do_portal` | `sim`, `nao` |
| `tentativa` | `1` ou `2` (Seção 1) |
| `tipo_ajuda` | `instrucao_moderador`, `confirmacao_caminho`, `consulta_externa`, `pedido_desistir`, `outro` (vazio se não houve ajuda) |
| `motivo_nao_conclusao` | `desistencia`, `teto_de_tempo`, `falha_tecnica_externa`, `acao_real` (vazio se concluiu) |
| `data` | AAAA-MM-DD, sem horário |
| `moderador`, `observador` | Inicial do integrante (`N` ou `Y`) |

`primeiro_acesso = sim` quando `ja_executou_tarefa = nao` e a tentativa vale como primeira (Seção 1).

### 5.2 Ligação com as métricas

| Métrica | Numerador | Denominador | Campos de origem |
|---|---|---|---|
| M1 – TCAPA | N_aut: linhas com `concluiu = sim`, `pediu_ajuda = nao` e `primeiro_acesso = sim` | N_tot: linhas com `primeiro_acesso = sim` (uma por participante e tarefa) | `registro-tarefas.csv` |
| M2 – IEFO | P_min | P_exec (`passos_executados`), só se `concluiu = sim` e P_exec > 0 | `p_min`, `passos_executados`, `concluiu` |
| M3 – TPRE | E_prev (prevenidos ou corrigidos na 1ª tentativa) | E_tot (todos os eventos classificados, exceto `N/A`) | `cenarios-de-erro-sessoes.csv` |
| M5 – SUS | Pontuação de cada participante (0 a 100) | – | `sus-respostas.csv` |

Regras:
- O IEFO é calculado **por execução** e depois resumido. Se `passos_executados` < `p_min`, o fluxo de referência é revisado e a ocorrência é registrada em `observacoes`, de modo que o IEFO não passe de 100%.
- **Execuções concluídas com ajuda:** os passos guiados inflam o P_exec. O IEFO é calculado **só para execuções concluídas sem ajuda**; as concluídas com ajuda são relatadas à parte.
- Tarefa não concluída: IEFO **não** é calculado e a não conclusão é registrada separadamente, com o motivo.
- Resultados por módulo e por dispositivo, sem misturar tarefas diferentes sem identificação, e **como contagens** nas células pequenas (Seção 1).
- Os erros espontâneos (`erros_espontaneos`) são apoio qualitativo e só entram em M3 se forem classificados em `cenarios-de-erro-sessoes.csv`.

### 5.3 `cenarios-de-erro-sessoes.csv`

O arquivo `cenarios-de-erro.csv` é o **catálogo** (um cenário por linha, sem participante). A execução com participantes é registrada em `cenarios-de-erro-sessoes.csv`, com `id_participante`, `dispositivo`, `tarefa`, `id_cenario`, `prioridade_na_sessao` (`núcleo` ou `opcional`), `mensagem_exibida`, `orientacao_oferecida`, `corrigiu_na_primeira_tentativa`, `classificacao_do_evento` (valores de `cenarios-de-erro-regras.md`) e `observacoes`.

## 6. Limites

- Amostra de conveniência e pequena: resultados válidos apenas para ela, sem generalização.
- O portal exige login gov.br: as tarefas T1 a T3 usam a conta de terceiro da Seção 2, e o login conta no P_min.
- A T1 só entra em N_tot se a conta com veículo for obtida antes do recrutamento (Seção 1).
- Nenhum teste gera efeito real. Os resultados refletem a versão do portal na data da coleta.
- A avaliação não equivale a uma auditoria de acessibilidade.

## Referências

- NIELSEN, J.; LANDAUER, T. K. A mathematical model of the finding of usability problems. In: *Proceedings of INTERCHI '93*. ACM, 1993. p. 206-213.
- VIRZI, R. A. Refining the test phase of usability evaluation: how many subjects is enough? *Human Factors*, v. 34, n. 4, p. 457-468, 1992.
