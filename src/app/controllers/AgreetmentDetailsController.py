from flask import jsonify

# informações sobre um contrato
# Partes
# Serviço
# Contrato
# Detalhes
#   - Valores
#   - Arquivos
#   - Pagamentos Feitos
#   - Pagamentos Pendentes
# Link para Download ou para gerar o documento


class AgreetmentDetailsController:
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
