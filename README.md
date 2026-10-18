# Avaliação da Qualidade do Portal Detran Digital DF

Documentação da avaliação de qualidade de produto de software desenvolvida na disciplina **Qualidade de Software 1 (FGA0315)** da Universidade de Brasília (UnB), ministrada pela Profa. Dra. Cristiane Soares Ramos.

O site publicado está disponível em: [Kay Mcnulty](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_KAY_MCNULTY/)

---

## Informações do Projeto

- **Produto avaliado:** [Portal Detran Digital DF](https://portal.detran.df.gov.br/#/home)
- **Equipe:** Kay McNulty (Turma 01)
- **Repositório:** [GitHub](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY)

### Integrantes

| <img src="https://avatars.githubusercontent.com/u/188686795?v=4" width="100" alt="Foto de Nicole Jovita"> | <img src="https://avatars.githubusercontent.com/u/187340217?v=4" width="100" alt="Foto de Artur Fernandes"> | <img src="https://avatars.githubusercontent.com/u/187406144?v=4" width="100" alt="Foto de Davi Ursolino"> | <img src="https://avatars.githubusercontent.com/u/78875892?v=4" width="100" alt="Foto de João Eduardo"> | <img src="https://avatars.githubusercontent.com/u/93289005?v=4" width="100" alt="Foto de Natan França"> | <img src="https://avatars.githubusercontent.com/u/159590199?v=4" width="100" alt="Foto de Yan Santos"> |
|:---:|:---:|:---:|:---:|:---:|:---:|
| [Nicole Jovita](https://github.com/nicolejovita) | [Artur Fernandes](https://github.com/ArturFGaldino) | [Davi Ursolino](https://github.com/DaviUrsulino) | [João Eduardo](https://github.com/JoaoEduardoP) | [Natan França](https://github.com/Natan8643) | [Yan Santos](https://github.com/yanrdgs-dev) |

---

## Executando o site localmente

O site é gerado com [MkDocs](https://www.mkdocs.org/) e o tema [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Siga os passos abaixo para visualizar a documentação em sua máquina antes de contribuir.

### Pré-requisitos

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/) 3.9 ou superior (com `pip`)

### Passo a passo

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAY_MCNULTY.git
   cd 2026-2_T02_KAY_MCNULTY
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv

   # Linux e macOS
   source .venv/bin/activate

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # Windows (cmd)
   .venv\Scripts\activate.bat
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor local:

   ```bash
   mkdocs serve
   ```

5. Acesse <http://127.0.0.1:8000> no navegador. O site é recarregado automaticamente a cada arquivo salvo. Para encerrar o servidor, use `Ctrl + C`.

### Validar antes de enviar

O deploy executa o build em modo estrito, no qual qualquer aviso (link quebrado, página fora do menu) interrompe a publicação. Rode o mesmo comando localmente antes do push:

```bash
mkdocs build --strict
```

---

## Como contribuir

1. Atualize a branch principal: `git pull origin main`.
2. Crie uma branch para a sua alteração: `git checkout -b nome-da-alteracao`.
3. Edite ou adicione os arquivos Markdown dentro da pasta `docs/`.
4. Se criar uma página nova, adicione-a à seção `nav` do arquivo `mkdocs.yml`.
5. Valide com `mkdocs build --strict`.
6. Faça o commit e envie a branch: `git push origin nome-da-alteracao`.
7. Abra um Pull Request descrevendo a mudança.

### Estrutura do repositório

```
.
├── .github/workflows/pages.yml   # build e deploy automático no GitHub Pages
├── docs/                         # conteúdo do site (Markdown)
│   ├── fase1/
│   ├── fase2/
│   ├── gestao/
│   ├── entregas/
│   ├── img/
│   ├── stylesheets/
│   └── index.md
├── mkdocs.yml                    # configuração do site e do menu
├── requirements.txt              # dependências Python
└── README.md
```

---

## Publicação

A publicação é automática. A cada push na branch `main`, o workflow definido em `.github/workflows/pages.yml` gera o site e o publica no GitHub Pages.