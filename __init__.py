from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import yaml
from os import path


def create_app():
    app = Flask(__name__)

    config_file = path.join(path.dirname(__file__), "config.yaml")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    # config = yaml.load(open("config.yaml"))
    # app.config["MYSQL_HOST"] = config["mysql_host"]
    # app.config["MYSQL_USER"] = config["mysql_user"]
    # app.config["MYSQL_PASSWORD"] = config["mysql_password"]
    # app.config["MYSQL_DB"] = config["mysql_db"]

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql://{config['mysql_user']}:{config['mysql_password']}@{config['mysql_host']}/{config['mysql_db']}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)
    mysql = MySQL(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
