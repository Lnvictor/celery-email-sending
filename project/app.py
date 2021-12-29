from flask import Flask

import blueprints


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprints.mail_endpoints)
    return app
