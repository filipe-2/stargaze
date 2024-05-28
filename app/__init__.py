from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_restful import Api

app = Flask(__name__, template_folder='views', static_folder='public')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from app.models.missions import Missions
with app.app_context():
    db.create_all()   

from app.controllers.reso_missions import Index, MissionsCreate,MissionsUpdate, MissionsDelete
api.add_resource(Index, '/get') 
api.add_resource(MissionsCreate, '/create')
api.add_resource(MissionsUpdate, '/update/<int:id>')#digitar Id da missão após /
api.add_resource(MissionsDelete, '/delete/<int:id>')

@app.route('/',  methods=['GET', 'POST','DELETE','PUT']) # Mover para a pasta 'routes' e declarando métodos
@cross_origin()

def Index():
    return render_template('index.html')