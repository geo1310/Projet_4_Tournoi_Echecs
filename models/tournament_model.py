import os
from tinydb import TinyDB, Query

NATIONAL_ID = 'GB13106'
FOLDER_TOURNAMENTS = 'data/tournaments'
FILE_TOURNAMENTS = 'tournaments.json'
FULL_PATH_TOURNAMENTS = os.path.join(FOLDER_TOURNAMENTS, FILE_TOURNAMENTS)


def db_tournaments_create():
    """Creation de la base de donnees des tournois"""
    if not os.path.exists(FOLDER_TOURNAMENTS):
        os.makedirs(FOLDER_TOURNAMENTS)
    db_tournaments = TinyDB(FULL_PATH_TOURNAMENTS)
    db_tournaments = db_tournaments.table(NATIONAL_ID)
    tournaments_query = Query()
    return db_tournaments, tournaments_query


class Tournament:

    db_tournaments, tournaments_query = db_tournaments_create()

    def __init__(self, name, location, description='', nb_rounds=4, players_list=None, rounds_list=None, act_round=0, start_date='', end_date=''):
        self.name = name.capitalize()
        self.location = location.capitalize()
        self.description = description
        if not isinstance(nb_rounds, int):
            if nb_rounds.isdigit():
                self.nb_rounds = int(nb_rounds)
            else:
                self.nb_rounds = 4
        else:
            self.nb_rounds = nb_rounds
        self.players_list = players_list if players_list is not None else []
        self.rounds_list = rounds_list if rounds_list is not None else []
        self.act_round = act_round
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.name} de {self.location}"
    
    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "nb_rounds": self.nb_rounds,
            "players_list": self.players_list,
            "rounds_list": self.rounds_list,
            "act_round": self.act_round,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    def save(self):
        if not self.db_tournaments.search((self.tournaments_query.name == self.name) & (self.tournaments_query.location == self.location)):
            self.db_tournaments.insert(self.to_json())
            return f"\nLe tournoi {self.name} de {self.location} a bien été enregistré."
        else:
            self.db_tournaments.update(self.to_json())
            return f"\nLe tournoi {self.name} de {self.location} a été mis à jour !!!"

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


if __name__ == "__main__":
    os.system('cls')
    print(Tournament.verify_round(1))
