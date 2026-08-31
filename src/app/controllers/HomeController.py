from flask import jsonify


class HomeController:
    def __init__(self):
        pass

    def index(self):
        return jsonify(
            [
                {
                    "name": "felipesantos2",
                    "idade": 23,
                    "profissao": "desenvolvedor backend",
                }
            ]
        )
