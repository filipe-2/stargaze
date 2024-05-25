from datetime import date
from dataclasses import dataclass

from app import db

@dataclass
class Missions(db.Model):
    # tanto o decorator 'dataclass' quanto a tipagem dos atributos são importantes, para a serialização do objeto em JSON
    id: int
    name: str
    date_launch: date
    # sempre que for adicionar uma nova field ao model, atribua a tipagem como feito acima, ou o 'jsonify' não funcionará corretamente

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

    # Obter missão pelo ID
    def get_mission(self, id):
        try:
            mission = db.session.query(Missions).get(id)
            print('Missão obtida com sucesso.')
            return mission
        except Exception as e:
            print('Ocorreu um erro ao obter a missão: ', e)
