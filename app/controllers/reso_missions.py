from flask import jsonify
from flask_restful import Resource
from app.models.missions import Missions

class Index(Resource):
    def get(self):
        return jsonify('Bem-vindo!')