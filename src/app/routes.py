import sys

from flask import Flask, make_response, request


def routes(app: Flask, middleware: list | None = None):
    @app.route("/", methods=["GET"])
    async def home():
        return request.base_url

    # lista todos os contratos
    # Número
    # Ano
    # Valor
    # Período
    # Partes
    @app.route("/agreetments", methods=["GET"])
    async def agreetments():
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
    async def agreetment_details():
        print(request.headers)
        return request.base_url


if __name__ == "__main__":
    raise SystemExit()
