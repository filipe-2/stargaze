from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missions import Missions
from datetime import datetime

# formatador personalizado para datas
def parse_date(x):
    return datetime.strptime(x, '%Y-%m-%d').date()

# Adicionando missões
parser = reqparse.RequestParser()# Definição de argumentos
parser.add_argument('name', required=True, help="Type mission name")
parser.add_argument('date_launch', required=True, help="Type mission date launch", type=parse_date)
parser.add_argument('destiny', required=True, help="Type a destiny", type=str)
parser.add_argument('status', required=True, help="Type mission state", type=str)
parser.add_argument('crew', required=True, help="Type mission crew", type=str)
parser.add_argument('load', required=True, help="Type mission load", type=str)
parser.add_argument('cost', required=True, help="Type mission cost", type=float)
parser.add_argument('status_details', required=True, help="Type mission status", type=str)

class Index(Resource):
    def get(self):
        return jsonify('Bem-vindo a stargaze!')
    
class MissionsCreate(Resource):
    def post(self): 
            datab = parser.parse_args()
            Missions.save_mission(
                self, datab['name'], datab['date_launch'], datab['destiny'], 
                datab['status'], datab['crew'], datab['load'], datab['cost'], datab['status_details']
            )
            return jsonify({"message": 'Mission added!'}), 200

class MissionsUpdate(Resource):
    def put(self, id):
        try:
            datab = parser.parse_args() 
            Missions.update_mission(
                self, id, datab['name'], datab['date_launch'], datab['destiny'], 
                datab['status'], datab['crew'], datab['load'], datab['cost'], datab['status_details']
            )
            return {"message": 'Mission Updated!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsDelete(Resource):
    def delete(self, id):
        try:
            Missions.delete_mission(self,id)
            return {"message": 'Mission Deleted!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500