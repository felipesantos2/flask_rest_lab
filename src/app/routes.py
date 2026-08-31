from flask import Flask

from .controllers.AgreetmentController import AgreetmentController
from .controllers.AgreetmentDetailsController import AgreetmentDetailsController
from .controllers.ContractorsController import ContractorsController
from .controllers.HomeController import HomeController


def web(app: Flask, middleware: list | None = None):
    @app.route("/", methods=["GET"])
    def home():
        ct = HomeController()
        return ct.index()

    @app.route("/agreetments", methods=["GET"])
    def agreetments():
        ct = AgreetmentController()
        return ct.index()

    @app.route("/contrators", methods=["GET"])
    def contractors():
        ct = ContractorsController()
        return ct.index()

    @app.route("/agreetments_details", methods=["GET"])
    def agreetment_details():
        ct = AgreetmentDetailsController()
        return ct.index()


def api(app: Flask, middleware: list | None = None):
    @app.route("/", methods=["GET"])
    def home():
        ct = HomeController()
        return ct.index()

    @app.route("/agreetments", methods=["GET"])
    def agreetments():
        ct = AgreetmentController()
        return ct.index()

    @app.route("/contrators", methods=["GET"])
    def contractors():
        ct = ContractorsController()
        return ct.index()

    @app.route("/agreetments_details", methods=["GET"])
    def agreetment_details():
        ct = AgreetmentDetailsController()
        return ct.index()


if __name__ == "__main__":
    raise SystemExit()
