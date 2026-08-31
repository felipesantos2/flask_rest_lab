from flask import jsonify

# lista todos os contratos
# Número
# Ano
# Valor
# Período
# Partes


class AgreetmentController:
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
