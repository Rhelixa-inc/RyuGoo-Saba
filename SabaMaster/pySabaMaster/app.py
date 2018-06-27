#!/usr/bin/python3
# coding: utf-8
from flask import Flask
import ssl

from pySabaMaster import config
from pySabaMaster import root_dir
from pySabaMaster.apis import api
from pySabaMaster.models import db


def initialize_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = \
        config.SQLALCHEMY_TRACK_MODIFICATIONS
    api.init_app(app)
    db.init_app(app)
    db.create_all(app=app)

    return app


def main():
    app = initialize_app()
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(str(root_dir.joinpath("ssl_certification").joinpath("ca.crt")),
                            str(root_dir.joinpath("ssl_certification").joinpath("ca.key")))
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG, ssl_context=context, threaded=True)


if __name__ == "__main__":
    main()
