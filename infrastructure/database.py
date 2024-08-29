from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@database-flask-ddd:3306/library_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
