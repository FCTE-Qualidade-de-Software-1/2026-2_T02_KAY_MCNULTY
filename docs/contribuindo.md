# Contribuindo

Contribuições são muito bem-vindas.

## Fluxo

1. Faça um fork do repositório.
2. Crie uma branch: `git checkout -b minha-melhoria`.
3. Faça suas alterações e commits.
4. Abra um Pull Request descrevendo a mudança.

## Rodando a documentação localmente

```bash
python -m venv .venv
source .venv/bin/activate   # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

O site ficará disponível em `http://127.0.0.1:8000`, com recarga automática.