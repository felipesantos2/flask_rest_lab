# API REST COM FLASK

Um estudo prático do padrão de arquitetura REST, APIs REST.

Stack inicial:
- Python
- Flask
- Python Dotenv
- Rich CLI
- MySQL Connector

Setup:

Essas duas variáveis definidas no `.env` permite utilizarmos a cli do flask de uma forma facilitada.

```env 
FLASK_APP=server.py
FLASK_RUN_PORT=8000
```

Sincronizando as dependências e ativando o ambiente virtual:

```bash
uv sync
```

Subindo a aplicação:

```bash
flask run
uv run flask run
```

É possível também startar o APP pelo arquivo de entrada, nosso front controller do PHP `index.php`. Aqui é o `server.py`

```bash
uv run server.py
```

Se sua versão do Python for compatível é possível execurar o app diretamente: `python3 server.py`. Prefiro sempre executar com o `UV`

**Python Version** do Projeto: [3.12](.python-version)

---

Vamos trocar uma ideia no LinkedIn:

[LinkedIn](https://www.linkedin.com/in/felipepinheiro2/)

---

#### *ACESSO RÁPIDO DAS PRINCIPAIS DOCS*

[https://flask.palletsprojects.com/en/stable](https://flask.palletsprojects.com/en/stable)

[https://docs.astral.sh/uv](https://docs.astral.sh/uv)

[https://github.com/textualize/rich-cli](https://github.com/textualize/rich-cli)
