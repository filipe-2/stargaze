from app import db
    
class Missions(db.Model):
    
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_launch = db.Column(db.Date)
    destiny = db.Column(db.String(255)) 
    state = db.Column(db.String(255)) 
    crew = db.Column(db.String(255))
    load = db.Column(db.String(255))
    duration = db.Column(db.Interval)
    cost = db.Column(db.DECIMAL)
    status = db.Column(db.String(255))
    
    def __init__(self, id, name, date_launch, destiny, state, crew, load, duration, cost, status):
        self.name = name
        self.date_launch = date_launch
        self.id = id
        self.destiny = destiny 
        self.state = state 
        self.crew = crew 
        self.load = load# carga útil
        self.duration = duration# duração
        self.cost = cost# custo
        self.status = status# status

    # Salvar missões
    def save_mission(self, id, name, date_launch, destiny, state, crew, load, duration, cost, status):
        try:
            add_to_db = Missions(id, name, date_launch, destiny, state, crew, load, duration, cost, status)
            print(add_to_db)
            db.session.add(add_to_db) 
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão salva com sucesso.')
        except Exception as e: 
            print('Ocorreu um erro ao salvar a missão: ', e)

    # Atualizar missões
    def update_mission(self, id, name, date_launch, destiny, state, crew, load, duration, cost, status):
        try:
            db.session.query(Missions).filter(Missions.id==id).update({
                'name':name, 'date_launch': date_launch, 'destiny':destiny, 'state':state,
                'crew':crew, 'load':load, 'duration':duration, 'cost': cost, 'status':status
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
    
    # Get
    def get_mission(self, id):
        try:
            mission = db.session.query(Missions).get(id)
            print('Missão obtida com sucesso.')
            return mission
        except Exception as e:
            print('Ocorreu um erro ao obter a missão: ', e)