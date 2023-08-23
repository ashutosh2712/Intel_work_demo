from flask import Flask
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import yaml
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    config_file = path.join(path.dirname(__file__), "config.yaml")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{config['mysql_user']}:{config['mysql_password']}@{config['mysql_host']}/{config['mysql_db']}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    mysql = MySQL(app)

    migrate = Migrate(app, db)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import Workload

    # create Datebase Object
    with app.app_context():
        db.create_all()

    return app
