# Questionário SUS em português e cálculo da pontuação (M5)

Rascunho de apoio ao arquivo `sus-respostas.csv`. Base: métrica M5 de `docs/fase2/usabilidade.md`. O texto final será integrado a `docs/fase3/usabilidade.md` pela issue de consolidação da Fase 3.

## 1. Escopo e aplicação

- **Escopo:** o questionário se refere ao **Portal Detran Digital DF como um todo**, considerando as tarefas que o participante executou na sessão. A justificativa está na Seção 4.5 de `roteiro-moderador.md`.
- **Quando aplicar:** individualmente, **logo após a última tarefa e antes de qualquer discussão** sobre o resultado.
- **Quem preenche:** o próprio participante, sem interferência do moderador. O moderador só esclarece o significado de uma palavra, se perguntado, sem explicar como responder.
- **Registro:** além das 10 respostas, anote o código do participante, o dispositivo, o escopo e as tarefas executadas.

## 2. Instrução ao participante

> Para cada afirmação abaixo, marque o quanto você concorda, **pensando no Portal Detran Digital DF, considerando as tarefas que acabou de fazer**. Responda com a sua primeira impressão, sem pensar muito. Não existem respostas certas ou erradas. Se uma afirmação não parecer se aplicar, marque 3.

Escala: **1** = discordo totalmente · **2** · **3** · **4** · **5** = concordo totalmente.

## 3. Os 10 itens

Versão em português do System Usability Scale (Brooke, 1996), com os 10 itens originais, na tradução e adaptação transcultural para o português do Brasil (Martins et al., 2015).

| Item | Afirmação | Polaridade |
|:---:|---|:---:|
| 1 | Eu acho que gostaria de usar este sistema com frequência. | Positiva |
| 2 | Eu achei o sistema desnecessariamente complexo. | Negativa |
| 3 | Eu achei o sistema fácil de usar. | Positiva |
| 4 | Eu acho que precisaria de ajuda de uma pessoa com conhecimentos técnicos para usar o sistema. | Negativa |
| 5 | Eu achei que as várias funções do sistema estão muito bem integradas. | Positiva |
| 6 | Eu achei que o sistema apresenta muita inconsistência. | Negativa |
| 7 | Eu imagino que as pessoas aprenderão como usar esse sistema rapidamente. | Positiva |
| 8 | Eu achei o sistema atrapalhado de usar. | Negativa |
| 9 | Eu me senti confiante ao usar o sistema. | Positiva |
| 10 | Eu precisei aprender várias coisas novas antes de conseguir usar o sistema. | Negativa |

Itens ímpares são positivos e itens pares são negativos. Antes de usar com os participantes, a redação final deve ser conferida contra a publicação de Martins et al. (2015), e qualquer ajuste de redação deve ser registrado.

## 4. Cálculo da pontuação

Fórmula da Seção 3 de `docs/fase2/usabilidade.md`:

```
SUS = 2,5 × [ Σ (R_i − 1) para i ímpar + Σ (5 − R_i) para i par ]
```

Passo a passo:
1. Para cada item **ímpar** (1, 3, 5, 7, 9), subtraia 1 da resposta.
2. Para cada item **par** (2, 4, 6, 8, 10), subtraia a resposta de 5.
3. Some as 10 contribuições. Cada uma vale de 0 a 4, então a soma vai de 0 a 40.
4. Multiplique a soma por 2,5. O resultado vai de 0 a 100.

O resultado **não é um percentual**. A literatura cita 68 como média de referência, mas a especificação não define faixas de julgamento para o SUS: apresente a média **junto das pontuações individuais**, sem classificar em níveis.

### Fórmula para planilha

Com `r01` a `r10` nas colunas F a O do arquivo `sus-respostas.csv` (linha 2 como exemplo), a coluna `pontuacao_sus` (P):

```
=2,5*((F2-1)+(5-G2)+(H2-1)+(5-I2)+(J2-1)+(5-K2)+(L2-1)+(5-M2)+(N2-1)+(5-O2))
```

Em planilha configurada em inglês, use ponto decimal: `=2.5*(...)`. A coluna deve ser calculada somente se as 10 respostas estiverem preenchidas.

### Exemplo conferido

Respostas de um participante fictício: R1=4, R2=2, R3=5, R4=1, R5=4, R6=2, R7=5, R8=2, R9=4, R10=1.

| Item | Resposta | Contribuição |
|:---:|:---:|:---:|
| 1 | 4 | 4 − 1 = 3 |
| 2 | 2 | 5 − 2 = 3 |
| 3 | 5 | 5 − 1 = 4 |
| 4 | 1 | 5 − 1 = 4 |
| 5 | 4 | 4 − 1 = 3 |
| 6 | 2 | 5 − 2 = 3 |
| 7 | 5 | 5 − 1 = 4 |
| 8 | 2 | 5 − 2 = 3 |
| 9 | 4 | 4 − 1 = 3 |
| 10 | 1 | 5 − 1 = 4 |
| **Soma** | | **34** |

SUS = 2,5 × 34 = **85**. Este exemplo é só para conferir a fórmula e não representa dado da avaliação.

Valores-limite para teste da planilha: todas as respostas "melhores" (ímpares 5, pares 1) dão 100; todas as "piores" (ímpares 1, pares 5) dão 0; todas iguais a 3 dão 50.

## 5. Tratamento das respostas

- Respostas em branco: o questionário daquele participante é registrado como **incompleto** e não entra na média. Não imputar valores.
- Valores fora de 1 a 5 são inválidos e devem ser reconferidos com o participante no momento.
- Apresentar: número de participantes, média, menor e maior pontuação, e a lista das pontuações individuais. Se possível, separar por dispositivo, informando o número de cada grupo.
- Interpretar junto de M1, M2, M3 e das observações qualitativas, sem generalizar além da amostra. O SUS indica a percepção geral, mas não identifica a causa das dificuldades.

## Referências

- BROOKE, J. SUS: a "quick and dirty" usability scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. London: Taylor & Francis, 1996. p. 189-194.
- MARTINS, A. I. et al. Brazilian Portuguese translation and cross-cultural adaptation of the System Usability Scale (SUS). *Anais do CIAIQ*, 2015.
