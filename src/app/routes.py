from flask import Flask, jsonify, request


def routes(app: Flask, middleware: list | None = None):
    @app.route("/", methods=["GET"])
    def home():
        return jsonify(
            [
                {
                    "name": "felipesantos2",
                    "idade": 23,
                    "profissao": "desenvolvedor backend",
                },
                {
                    "name": "felipesantos2",
                    "idade": 23,
                    "profissao": "desenvolvedor backend",
                },
            ]
        )

    # lista todos os contratos
    # Número
    # Ano
    # Valor
    # Período
    # Partes
    @app.route("/agreetments", methods=["GET"])
    def agreetments():
        print(request.headers)
        return request.base_url

    # lista contratadores
    # Nome
    # Serviço
    # Pagamentos Previstos
    @app.route("/contrators", methods=["GET"])
    def contractors():
        print(request.headers)
        return request.base_url

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
    @app.route("/agreetments_details", methods=["GET"])
    def agreetment_details():
        print(request.headers)
        return request.base_url


if __name__ == "__main__":
    raise SystemExit()
