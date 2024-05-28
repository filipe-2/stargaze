from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missions import Missions
from datetime import datetime

# formatador personalizado para datas
def parse_date(x):
    return datetime.strptime(x, '%Y-%m-%d').date()

# Adicionando missões
parser = reqparse.RequestParser()# Definição de argumentos
parser.add_argument('id', required=True, help="Digite o ID", type=int)
parser.add_argument('name', required=True, help="Digite o nome")
parser.add_argument('date_launch', required=True, help="Digite a data", type=parse_date)

# Atualizar missões date_launch = datetime.strptime(args['date_launch'], '%Y-%m-%d') isso aqui, a gente tem q implementar isso
parser_update = reqparse.RequestParser() 
parser_update.add_argument('id', required=True, help="Digite o ID", type=int)
parser_update.add_argument('name', required=True, help="Digite o nome")
parser_update.add_argument('date_launch', required=True, help="Digite a data", type=parse_date)
#Deletar missões
parser_delete = reqparse.RequestParser()
parser_delete.add_argument('id', required= True, help="Digite o ID", type=int)

class Index(Resource):
    def get(self):
        return jsonify('Bem-vindo a stargaze!')
    
class MissionsCreate(Resource):
    def post(self): 
        try:
            datab = parser.parse_args()
            Missions.save_mission(self, datab['id'], datab['name'], datab['date_launch'])
            return {"message": 'Mission added!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsUpdate(Resource):
    def put(self):
        try:
            datab = parser_update.parse_args() 
            Missions.update_mission(self, datab['id'], datab['name'], datab['date_launch'])
            return {"message": 'Mission Updated!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsDelete(Resource):
    def delete(self):
        try:
            datab = parser_delete.parse_args()
            Missions.delete_mission(self,datab['id'])
            return {"message": 'Mission Deleted!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500