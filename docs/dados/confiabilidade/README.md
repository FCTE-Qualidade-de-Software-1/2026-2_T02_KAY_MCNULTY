# Dados brutos – Confiabilidade

| Métrica | Arquivo | Conteúdo | Evidências | Período |
|---|---|---|---|---|
| M1 (TDO) | `m1/disponibilidade_actions.csv` | Verificações a cada 15 min (workflow do Actions), copiado no corte | Não se aplica | 15/11 a 21/11/2026 |
| M1 (TDO), cópia parcial | `m1/disponibilidade_actions_parcial_20261120.csv` | Verificações do Actions de 15/11 20h42 a 20/11 05h58 (horário de Brasília) | Não se aplica | 15/11 a 20/11/2026 |
| M2 e M3 | `m2-m3/fluxos.csv` | Execuções dos fluxos INF-01 a CHA-01 | `m2-m3/evidencias/` | 16/11 a 17/11/2026 |
| M4 | `m4/anomalias.csv` | Cenários A1 a A10 | `m4/evidencias/` | 16/11 a 17/11/2026 |
| M5 e M6 | `m5-m6/interrupcoes.csv` | Cenários B1 a B8 e tempos de recuperação | `m5-m6/evidencias/` | 20/11/2026 |

Convenção dos nomes das evidências: `{ID}_exec{n}_{AAAA-MM-DD}_{hhmm}.{ext}`.
O CSV da M1 é gerado na branch `monitoramento-m1` e copiado para esta pasta ao fim da janela.