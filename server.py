from flask import Flask

from src.app import routes

app = Flask(__name__, instance_relative_config=True)

# rotas da aplicação
routes.routes(app, [])

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
