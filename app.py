import flask
from flask_cors import CORS
import myfilter.routes as routes


def add_cors(app: flask.Flask):
    CORS(
        app,
        supports_credentials=True,
        resources={
            r"*": {"origins": "*"},
        },
    )


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    app.register_blueprint(routes.bp)
    add_cors(app)

    return app
