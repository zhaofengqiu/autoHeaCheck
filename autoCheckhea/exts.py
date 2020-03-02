from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    return app
app = create_app()
def create_db(app):
    db = SQLAlchemy(app)
    return db
db = create_db(app)
