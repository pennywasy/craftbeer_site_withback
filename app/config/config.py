import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__, static_folder="../static/", template_folder="../html/")
app.secret_key = 'VERYSECRET'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///craftbeer.db'
db = SQLAlchemy(app)

