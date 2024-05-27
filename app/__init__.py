from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='views', static_folder='public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from app.models.missions import Missions
with app.app_context():
    db.create_all()   
     
@app.route('/') # Migrar para a pasta 'routes'
@cross_origin()
def index():
    return render_template('index.html')