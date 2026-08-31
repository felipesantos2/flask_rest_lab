from flask import jsonify


# lista contratadores
# Nome
# Serviço
# Pagamentos Previstos
class ContractorsController:
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
