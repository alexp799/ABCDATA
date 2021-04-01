<<<<<<< HEAD
from flask import Flask,jsonify
=======
from flask import Flask
>>>>>>> ea93205c0d654ed07215b6c6a639f6913685ce31
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

<<<<<<< HEAD
app = Flask(__name__,static_folder=Config.PATH_ABS+"/DATA")
=======
app = Flask(__name__)
>>>>>>> ea93205c0d654ed07215b6c6a639f6913685ce31
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes,models
