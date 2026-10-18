# Instalação

## Requisitos

- Sistema operacional: Linux, macOS ou Windows
- Versão mínima da linguagem/runtime: `X.Y`

## Instalar

=== "pip"

    ```bash
    pip install nome-do-projeto
    ```

=== "A partir do código-fonte"

    ```bash
    git clone https://github.com/SEU-USUARIO/NOME-DO-REPO.git
    cd NOME-DO-REPO
    pip install -e .
    ```

## Verificar a instalação

```bash
nome-do-projeto --version
```

!!! tip "Dica"
    Use um ambiente virtual (`python -m venv .venv`) para manter as dependências isoladas.

Próximo passo: [Configuração](configuracao.md).