from flask import Flask
from myapp.models import db


def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    app.config.from_pyfile(filename='config.py')

    db.init_app(app)

    from .admin.routes import admin
    from .main.routes import main
    from .api.routes import api

    app.register_blueprint(admin)
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
