from sqlalchemy import desc
from app import db
    
class Missions(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_launch = db.Column(db.Date)
    destiny = db.Column(db.String(255)) 
    status = db.Column(db.String(255)) 
    crew = db.Column(db.String(255))
    load = db.Column(db.String(255))
    duration = db.Column(db.Interval)
    cost = db.Column(db.DECIMAL)
    status_details = db.Column(db.String(255))
    
    def __init__(self, id, name, date_launch, destiny, status, crew, load, duration, cost, status_details):
        self.name = name
        self.date_launch = date_launch
        self.id = id
        self.destiny = destiny 
        self.status = status 
        self.crew = crew 
        self.load = load# carga útil
        self.duration = duration# duração
        self.cost = cost# custo
        self.status_details = status_details# status

    # Salvar missões
    def save_mission(self, name, date_launch, destiny, status, crew, load, duration, cost, status_details):
        try:
            add_to_db = Missions(None, name, date_launch, destiny, status, crew, load, duration, cost, status_details)
            print(add_to_db)
            db.session.add(add_to_db) 
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão salva com sucesso.')
        except Exception as e: 
            print('Ocorreu um erro ao salvar a missão: ', e)

    # Atualizar missões
    def update_mission(self, id, name, date_launch, destiny, status, crew, load, duration, cost, status_details):
        try:
            db.session.query(Missions).filter(Missions.id==id).update({
                'name':name, 'date_launch': date_launch, 'destiny':destiny, 'status':status,
                'crew':crew, 'load':load, 'duration':duration, 'cost': cost, 'status_details':status_details
            })
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão atualizada com sucesso.')
        except Exception as e:
            print('Ocorreu um erro ao atualizar a missão: ', e)

    # Remover missões
    def delete_mission(self, id):
        try:
            db.session.query(Missions).filter(Missions.id==id).delete()
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão removida com sucesso.')
        except Exception as e:
            print('Ocorreu um erro ao remover a missão: ', e)
    
    # Obter missão específica
    def get_mission(self, id):
        try:
            mission = db.session.query(Missions).get(id)
            print('Missão obtida com sucesso.')
            return mission
        except Exception as e:
            print('Ocorreu um erro ao obter a missão: ', e)

    # Obter todas as missões ordenadas pela data de lançamento em ordem descrescente entre as datas (se passadas)
    def get_all_missions(self, start_date, end_date):
        try:
            query = db.session.query(Missions)
            if start_date and end_date:
                query = query.filter(Missions.date_launch.between(start_date, end_date))
            missions = query.order_by(desc(Missions.date_launch)).all()
            print('Todas as missões obtidas com sucesso.')
            return missions
        except Exception as e:
            print('Ocorreu um erro ao obter todas as missões: ', e)
