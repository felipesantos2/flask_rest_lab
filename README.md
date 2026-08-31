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

`FLASK_APP=server.py`

`FLASK_RUN_PORT=8000`

Subindo a aplicação:

`flask run`

ou

`uv run flask run`

É possível também startar o APP pelo arquivo de entrada, nosso front controller do PHP `index.php`. Aqui é o `server.py`

`uv run server.py`

Se sua versão do Python for compatível é possível execurar o app diretamente: `python3 server.py`. Prefiro sempre executar com o `UV`

Versão do Projeto: [3.12](.python-version)

Problema:

Notas: