import os
import secrets
from tinydb import TinyDB, Query

class Tournament:

    NATIONAL_ID = 'GB13106'
    FOLDER_TOURNAMENTS = 'data/tournaments'
    FILE_TOURNAMENTS = 'tournaments.json'
    FULL_PATH_TOURNAMENTS = os.path.join(FOLDER_TOURNAMENTS, FILE_TOURNAMENTS)

    """Creation de la base de donnees des tournois"""
    if not os.path.exists(FOLDER_TOURNAMENTS):
        os.makedirs(FOLDER_TOURNAMENTS)
    db_tournaments = TinyDB(FULL_PATH_TOURNAMENTS)
    db_tournaments = db_tournaments.table('tournaments')
    tournaments_query = Query()
        
    def __init__(self, id= None, name='', location='', description='', nb_rounds=4, players_list=None, rounds_list=None, act_round=0, start_date='', end_date=''):
        self.id = id if id else secrets.token_hex(4)
        self.name = name.lower()
        self.location = location.lower()
        self.description = description
        if not isinstance(nb_rounds, int):
            if nb_rounds.isdigit():
                self.nb_rounds = int(nb_rounds)
            else:
                self.nb_rounds = 4
        else:
            self.nb_rounds = nb_rounds
        self.players_list = players_list if players_list else []
        self.rounds_list = rounds_list if rounds_list else []
        self.act_round = act_round
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"Nom du Tournoi : {self.name}  -  Lieu du Tournoi : {self.location}"

    def to_dict(self):
        return self.__dict__
    
    def save(self):
        result_tournament = self.db_tournaments.search(self.tournaments_query.id == self.id)
        if not result_tournament:
            self.db_tournaments.insert(self.to_dict())
            return f"\nLe tournoi {self.name} de {self.location} a bien été enregistré."
        else:
            self.db_tournaments.update(self.to_dict(), self.tournaments_query.id == self.id)
            return f"\nLe tournoi {self.name} de {self.location} a été mis à jour !!!"


    @staticmethod
    def search(key, query):
        result = Tournament.db_tournaments.search((Tournament.tournaments_query[key] == query))
        if result:
            return result[0]
        return False
    
    @staticmethod
    def list(filter):
        """Retourne la liste de tous les tournois selon un critere de selection
        all : tous les tournois
        finished : les tournois non finis
        """
        if filter == 'all':
            return Tournament.db_tournaments.all()
        elif filter == 'not_finished':
            return Tournament.db_tournaments.search(Tournament.tournaments_query.end_date == '')

    

    
