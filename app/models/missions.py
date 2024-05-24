from app import db

class Missions(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_launch = db.Column(db.Date)

    # Inicializador
    def __init__(self, name, date_launch):
        self.name = name
        self.data_lancamento = date_launch
    # Salvar missões
    def save_missions(self, name, date_launch):
        try:
            add_to_db = Missions(name, date_launch)
            print(add_to_db)
            db.session.add(add_to_db)
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão salva com sucesso.')
        except Exception as e:
            print('Ocorreu um erro ao salvar a missão: ', e)

    # Atualizar missões
    def update_missions(self, id, name, date_launch):
        try:
            db.session.query(Missions).filter(Missions.id==id).update({'name':name, 'date_launch': date_launch})
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão atualizada com sucesso.')
        except Exception as e:
            print('Ocorreu um erro ao atualizar a missão: ', e)

    # Remover missões
    def delete_missions(self, id):
        try:
            db.session.query(Missions).filter(Missions.id==id).delete()
            db.session.commit() # Confirmar e salvar as alterações no banco de dados
            print('Missão removida com sucesso.')
        except Exception as e:
            print('Ocorreu um erro ao remover a missão: ', e)