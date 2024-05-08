from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='views', static_folder='public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

from app.models.missions import Missions
with app.app_context():
    db.create_all()

@app.route('/') # Migrar para a pasta 'routes'
def index():
    return render_template('index.html')