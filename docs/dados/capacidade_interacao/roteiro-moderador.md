# Plano do teste com participantes e roteiro do moderador

Rascunho de apoio aos arquivos `registro-tarefas.csv`, `sus-ptbr.md` e `sus-respostas.csv`. Base: métricas M1 (TCAPA), M2 (IEFO), M3 (TPRE) e M5 (SUS) e Seções 4 e 6 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

Este plano depende do catálogo de tarefas e fluxos (`tarefas-e-fluxos.csv`, issue #50) e dos cenários de erro (`cenarios-de-erro.csv`, issue #51). Os enunciados, os pontos de parada seguros e o P_min vêm desses arquivos e não são repetidos aqui.

## 1. Perfil e amostra

**Perfis.** O teste usa dois grupos, para cobrir diferentes níveis de familiaridade com o portal:

| Grupo | Perfil | Objetivo |
|---|---|---|
| Cidadãos | Pessoas com diferentes faixas etárias e níveis de letramento digital, que usariam o portal como cidadãos | Representar o público do serviço |
| Engenheiros avaliadores | Estudantes ou profissionais de engenharia, sem participação na inspeção heurística | Complementar com um olhar técnico |

Quem inspecionou o portal na inspeção heurística (Natan e Yan) não participa do teste, pois já conhece os fluxos e não está em primeiro acesso.

**Tamanho mínimo: 6 participantes**, com pelo menos 2 cidadãos de baixo letramento digital e pelo menos 1 engenheiro. A sugestão de partida da issue era de 5; o número 6 permite dividir a amostra de forma equilibrada entre os dois dispositivos.

**Distribuição por dispositivo.** Cada participante usa **um único dispositivo** durante a sessão, para que o aprendizado de uma execução não contamine a outra:

| Dispositivo | Participantes |
|---|---|
| Desktop | 3 |
| Mobile | 3 |

**Justificativa.** A amostra é de conveniência, com finalidade diagnóstica: serve para identificar dificuldades recorrentes, não para estimar proporções da população. Pequenas amostras já revelam a maior parte dos problemas graves de interface, mas os percentuais calculados sobre poucos participantes têm incerteza grande. Por isso, os resultados devem ser apresentados com numerador e denominador, por módulo e por dispositivo, e **não podem ser generalizados além da amostra** (Seção 6 de `docs/fase2/usabilidade.md`).

Com 6 participantes e 4 tarefas, o denominador de M1 é N_tot = 24 tarefas (12 por dispositivo). Se algum participante não completar todas as tarefas por motivo alheio ao portal, registre e ajuste o denominador.

**Critério de primeiro acesso.** O participante nunca executou a tarefa no portal e não recebe demonstração prévia. Ter usado o portal para outro fim não o exclui, mas deve ser registrado (campo `ja_usou_portal` do registro). Se o participante já executou **a mesma tarefa** antes, ele não está em primeiro acesso para ela: a execução é registrada, mas não entra em N_tot de M1.

**Participantes da validação do protótipo.** O teste rápido da validação do protótipo (Fase 4) deve, preferencialmente, usar participantes diferentes dos deste teste, porque quem já fez as tarefas no portal atual deixa de estar em primeiro acesso.

## 2. Preparação da sessão

- Conta de teste do portal e valores fictícios para os campos, preparados antes. O participante nunca usa conta ou documento pessoal.
- Navegador em janela anônima, na página inicial do portal, conforme o estado inicial de cada tarefa em `tarefas-e-fluxos.csv`.
- Desktop: registrar a resolução. Mobile: celular em modo retrato.
- Gravação de tela habilitada, quando o participante consentir, sem capturar dados pessoais.
- Cronômetro **não** é necessário para M2: o IEFO usa passos, não tempo.
- Cópia em branco de `registro-tarefas.csv` e do formulário do SUS.
- Definir quem modera e quem observa. O observador conta os passos e preenche o registro; o moderador não interfere.
- Sessão estimada em 30 a 40 minutos, para 4 tarefas, os cenários de erro e o SUS.

## 3. Termo de consentimento e tratamento dos dados

### 3.1 Texto do termo (para leitura e assinatura)

> **Termo de consentimento – Avaliação de usabilidade do Portal Detran Digital DF**
>
> Você está sendo convidado(a) a participar de um teste acadêmico da disciplina Qualidade de Software 1 (UnB/FCTE). O objetivo é avaliar o **portal**, não você. Não existem respostas certas ou erradas.
>
> Você fará algumas tarefas no portal, usando uma conta de teste e dados fictícios, e depois responderá a um questionário curto. A sessão dura cerca de 40 minutos. Nenhuma tarefa gera protocolo, agendamento ou pagamento reais.
>
> - A participação é voluntária. Você pode parar a qualquer momento, sem consequências.
> - Registraremos suas ações e comentários por código (por exemplo, P01), e não pelo seu nome.
> - Não pediremos nem registraremos dados pessoais seus (nome, CPF, e-mail, telefone). Se a tela mostrar algum dado seu por engano, avise e não o leia em voz alta.
> - A gravação de tela, se você permitir, será usada apenas para conferir a contagem de passos e será apagada ao fim do trabalho.
> - Os resultados serão publicados apenas de forma agregada e anonimizada.
>
> Declaro que li e entendi este termo e aceito participar.
>
> Participante (código): ______  Data: ____/____/______
> Assinatura ou aceite verbal registrado pelo moderador: ______

O termo é preenchido pelo **código** do participante. O nome nunca é registrado nos arquivos do repositório.

### 3.2 Anonimização (LGPD)

1. Cada participante recebe um código sequencial (`P01`, `P02`, …) no início da sessão.
2. O código é a **única** identificação nos arquivos versionados (`registro-tarefas.csv`, `sus-respostas.csv`, capturas e notas).
3. Nenhuma tabela liga o código ao nome. Se for preciso manter a correspondência para agendamento, ela fica fora do repositório e é destruída ao fim da coleta.
4. O perfil é registrado por categorias amplas (faixa etária e nível de letramento digital), nunca por idade exata, profissão específica ou local de moradia, para evitar a reidentificação em amostra pequena.
5. As gravações de tela não são versionadas. As capturas versionadas não podem conter dado pessoal real.

## 4. Roteiro do moderador

### 4.1 Princípios

- **Fala neutra.** O moderador não indica menus, botões nem o caminho. Os enunciados são lidos exatamente como estão em `tarefas-e-fluxos.csv`.
- **Primeiro acesso.** Nenhuma demonstração antes da tarefa.
- **Pensar em voz alta.** Peça ao participante para dizer o que está tentando fazer, sem forçar.
- **Sem dicas, sem julgamento.** Não confirme nem corrija o que o participante faz. Respostas neutras, como "Faça como faria normalmente", são permitidas.
- **Parada segura.** Interrompa a tarefa no ponto de parada seguro definido no catálogo. Se o participante tentar concluir uma ação real (pagar, agendar, assinar), interrompa de forma neutra e registre.

### 4.2 Sequência da sessão

1. **Boas-vindas e termo** (3 min). Explique o objetivo ("avaliamos o portal, não você"), leia o termo e registre o consentimento e o código do participante.
2. **Perfil** (2 min). Registre a faixa etária, o nível de letramento digital (baixo, médio ou alto) e se já usou o portal. Não registre dados pessoais.
3. **Tarefas T1 a T4** (20 min). Leia o enunciado, deixe o participante executar e anote no registro. A ordem das tarefas é a do catálogo, com a rotação indicada na Seção 4.4. O login gov.br usa a conta de teste.
4. **Cenários de erro** (5 min). Aplique os cenários de `cenarios-de-erro.csv` marcados como `núcleo`, no momento em que a tarefa chega ao campo correspondente. Os valores inválidos são fornecidos pelo moderador, que explica apenas "digite este valor".
5. **SUS** (3 min). Aplique o questionário (`sus-ptbr.md`) **logo após a última tarefa e antes de qualquer discussão**. Não comente o resultado.
6. **Encerramento** (2 min). Pergunte livremente sobre dificuldades e agradeça. Esse momento é qualitativo e fica depois do SUS.

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
- Pedir o valor fictício de um campo (a conta de teste, os dados de teste).
- Lembrar o participante de falar em voz alta ou perguntar "o que você está pensando?".
- Usar a **ajuda interna do próprio portal** (texto de ajuda, assistente virtual quando não é a tarefa). Registre o uso nas observações.
- Questões técnicas alheias ao portal (internet caiu, tela travou). Repita a tarefa e registre.

**Regras de registro:**
- A tarefa é **autônoma** quando `concluiu = sim` e `pediu_ajuda = nao`.
- Registre o tipo da ajuda (`tipo_ajuda`) quando houver.
- Se o participante desistir ou atingir 2 vezes o tempo razoável sem avançar, o moderador encerra a tarefa. Ela é registrada como **não concluída**.
- A decisão sobre o que é auxílio é do **observador**, anotada no momento. Em dúvida, registre como auxílio e justifique em `observacoes`.

### 4.4 Ordem e viés de aprendizado

Para reduzir o efeito de aprendizado entre tarefas, alterne a ordem das tarefas T1 a T4 entre os participantes (por exemplo, rotação circular: P01 faz T1-T2-T3-T4, P02 faz T2-T3-T4-T1, e assim por diante). Registre a ordem de cada participante. A T4 (chatbot) pode vir em qualquer posição.

### 4.5 Escopo do SUS

O SUS é aplicado **uma vez por participante, referindo-se ao Portal Detran Digital DF como um todo**, considerando as tarefas realizadas na sessão. A razão é prática e metodológica: o SUS mede a percepção geral do sistema e perde validade se for aplicado a trechos curtos. A aplicação por módulo, após cada tarefa, geraria quatro questionários por pessoa e respostas muito influenciadas pelo cansaço.

Consequência: o SUS é apresentado por participante e como média, e **não por módulo**. A comparação entre módulos fica a cargo de M1, M2, M3 e M4 (IPH). O registro anota quais tarefas o participante executou e o dispositivo, para que o SUS possa ser lido por dispositivo.

## 5. Dados a registrar e ligação com as métricas

`registro-tarefas.csv` tem uma linha por participante e tarefa. Os campos permitem reproduzir numeradores e denominadores:

| Métrica | Numerador | Denominador | Campos de origem |
|---|---|---|---|
| M1 – TCAPA | N_aut: linhas com `concluiu = sim` e `pediu_ajuda = nao` e `primeiro_acesso = sim` | N_tot: linhas com `primeiro_acesso = sim` | `concluiu`, `pediu_ajuda`, `primeiro_acesso` |
| M2 – IEFO | P_min (campo `p_min`) | P_exec (`passos_executados`), só se `concluiu = sim` e P_exec > 0 | `p_min`, `passos_executados`, `concluiu` |
| M3 – TPRE | E_prev (eventos prevenidos ou corrigidos na 1ª tentativa) | E_tot (todos os eventos de erro) | `cenarios-de-erro.csv` (classificação do evento) |
| M5 – SUS | Pontuação de cada participante (0 a 100) | – | `sus-respostas.csv` |

Regras:
- O IEFO é calculado **por execução** e depois resumido. Se `passos_executados` < `p_min`, o fluxo de referência é revisado e a ocorrência é registrada em `observacoes`, de modo que o IEFO não passe de 100%.
- Tarefa não concluída: IEFO **não** é calculado e a não conclusão é registrada separadamente.
- Os eventos de erro de M3 são registrados em `cenarios-de-erro.csv`, que é a fonte de E_prev e E_tot. O `registro-tarefas.csv` guarda apenas os erros espontâneos (`erros_espontaneos`), como apoio qualitativo, e eles só entram em M3 se forem classificados naquele arquivo.
- Resultados por módulo e por dispositivo, sem misturar tarefas diferentes sem identificação.

## 6. Limites

- Amostra de conveniência e pequena: resultados válidos apenas para ela, sem generalização.
- O portal exige login gov.br: as tarefas T1 a T3 usam uma conta de teste, e o login conta no P_min.
- Nenhum teste gera efeito real. Os resultados refletem a versão do portal na data da coleta.
- Participantes com deficiência não são recrutados como grupo específico; a avaliação não equivale a uma auditoria de acessibilidade.
