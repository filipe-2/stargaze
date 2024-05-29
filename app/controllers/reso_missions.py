from flask import jsonify, request
from flask_restful import Resource, reqparse
from app.models.missions import Missions
from datetime import datetime

# formatador personalizado para datas
def parse_date(x):
    return datetime.strptime(x, '%Y-%m-%d').date()

# formata Missoes para JSON
def parse_mission(mission):
    mission = mission.__dict__
    del mission['_sa_instance_state'] # remove instância inconvertível do banco de dados
    mission['cost'] = float(mission['cost'])
    mission['duration'] = f'{mission["duration"].days} days'
    mission['date_launch'] = mission['date_launch'].strftime('%Y-%m-%d')
    return mission

def parse_mission_resume(mission):
    mission = parse_mission(mission)
    return {
        'id': mission['id'], 'name': mission['name'], 'date_launch': mission['date_launch'],
        'destiny': mission['destiny'], 'status': mission['status']
    }

# Adicionando missões
parser = reqparse.RequestParser()# Definição de argumentos
parser.add_argument('name', required=True, help="Type mission name")
parser.add_argument('date_launch', required=True, help="Type mission date launch", type=parse_date)
parser.add_argument('date_return', required=True, help="Type mission date return", type=parse_date) # a data de retorno é requerida para calcular a duração da missão
parser.add_argument('destiny', required=True, help="Type a destiny", type=str)
parser.add_argument('status', required=True, help="Type mission state", type=str)
parser.add_argument('crew', required=True, help="Type mission crew", type=str)
parser.add_argument('load', required=True, help="Type mission load", type=str)
parser.add_argument('cost', required=True, help="Type mission cost", type=float)
parser.add_argument('status_details', required=True, help="Type mission status", type=str)

class MissionsCreate(Resource):
    def post(self): 
        
            datab = parser.parse_args() 
            datab['duration'] = datab['date_return'] - datab['date_launch'] # cálculo da duração da missão
            Missions.save_mission(
                self, datab['name'], datab['date_launch'], datab['destiny'], datab['status'],
                datab['crew'], datab['load'], datab['duration'], datab['cost'], datab['status_details']
            )
            return {"message": 'Mission added!'}, 200    
        

class MissionsUpdate(Resource):
    def put(self, id):
        try:
            datab = parser.parse_args() 
            datab['duration'] = datab['date_return'] - datab['date_launch'] # cálculo da duração da missão
            Missions.update_mission(
                self, id, datab['name'], datab['date_launch'], datab['destiny'], datab['status'],
                datab['crew'], datab['load'], datab['duration'], datab['cost'], datab['status_details']
            )
            return {"message": 'Mission Updated!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsDelete(Resource):
    def delete(self, id):
        try:
            Missions.delete_mission(self, id)
            return {"message": 'Mission Deleted!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsGet(Resource):
    def get(self, id):
        try:
            mission = Missions.get_mission(self, id)
            return parse_mission(mission), 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionsGetAll(Resource):
    def get(self):
        try:
            start_date = request.args.get('start_date')
            end_date = request.args.get('end_date')
            missions = Missions.get_all_missions(self, start_date, end_date)
            return [parse_mission_resume(mission) for mission in missions], 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
