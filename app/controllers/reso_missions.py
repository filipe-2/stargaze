from flask import jsonify
from flask_restful import Resource
from app.models.missions import Missions

class Index(Resource):
    def get(self):
        return jsonify('Bem-vindo!')

# Retorna erro para o cliente caso a missão não seja encontrada
class GetMission(Resource):
    def get(self, id):
        mission = Missions.get_mission(self, id)
        if(mission == None):
            return {'message': 'Missão não cadastrada!'}, 404
        return jsonify(mission)
