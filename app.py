from flask import Flask
from rutas.contacto import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.db import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
#SQLAlchemy(app)
app.register_blueprint(contacts)

