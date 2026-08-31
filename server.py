from flask import Flask

from src.app import routes

# WSGI server
app = Flask(__name__, instance_relative_config=True)

# rotas da aplicação
routes.web(app, [])
routes.api(app, [])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
