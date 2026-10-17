# Configuração

## Arquivo de configuração

Crie um arquivo `config.yml` na raiz do seu projeto:

```yaml title="config.yml"
nome: meu-projeto
modo: producao  # (1)!
opcoes:
  verboso: false
```

1. Valores aceitos: `desenvolvimento` ou `producao`.

## Opções disponíveis

| Opção            | Tipo     | Padrão       | Descrição                         |
| ---------------- | -------- | ------------ | --------------------------------- |
| `nome`           | texto    | —            | Nome identificador do projeto     |
| `modo`           | texto    | `producao`   | Define o ambiente de execução     |
| `opcoes.verboso` | booleano | `false`      | Ativa logs detalhados             |

!!! warning "Atenção"
    Nunca versione credenciais ou chaves secretas. Use variáveis de ambiente.