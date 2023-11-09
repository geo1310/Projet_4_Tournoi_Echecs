import os
import secrets
import random
from tinydb import TinyDB, Query

class Player:

    NATIONAL_ID = 'GB13106'
    FOLDER_PLAYERS = 'data/players'
    FILE_PLAYERS = 'players.json'
    FULL_PATH_PLAYERS = os.path.join(FOLDER_PLAYERS, FILE_PLAYERS)
    
    """Creation de la base de donnees des joueurs"""
    if not os.path.exists(FOLDER_PLAYERS):
        os.makedirs(FOLDER_PLAYERS)
    db_players = TinyDB(FULL_PATH_PLAYERS)
    player_query = Query()

    def __init__(self, last_name , first_name , birthday='', score=0, opponents=None, id=None):
        
        self.last_name = last_name.lower()
        self.first_name = first_name.lower()
        self.birthday = birthday
        self.score = score
        self.opponents = opponents if opponents else []
        self.id = id

    def __repr__(self):
        return f"{self.last_name} {self.first_name} née(e) le {self.birthday}"

    def to_dict(self):
        """ Crée un dictionnaire avec les données du joueur pour enregistrement players.json """
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
        }
    
    def to_dict_tournament(self):
        """ Crée un dict. pour la players_list des tournois """
        return {
            "id": self.id,
            "score": self.score,
            "opponents": self.opponents
        }

    def create(self):
        """Sauvegarde un joueur dans la base players.json"""
        search_result = self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name))
        if not search_result:
            self.id = secrets.token_hex(4)
            self.db_players.insert(self.to_dict())
            return True
        else:
            self.id = search_result[0]['id']
            return False

    def delete(self):
        """Supprime un joueur dans la base players.json"""
        if self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name)):
            self.db_players.remove((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name))
            return f"\nLe joueur {self.first_name} {self.last_name} a bien été suppimé.\n"
        else:
            return f"\nLe joueur {self.first_name} {self.last_name} n'est pas dans la liste !!!\n"

    @staticmethod
    def search(key, query):
        result = Player.db_players.search((Player.player_query[key] == query))
        if result:
            return result[0]
        return False
    
    @staticmethod
    def list():
        """Retourne la liste de tous les joueurs"""
        return Player.db_players.all()
    
    @staticmethod
    def list_instance():
        """Retourne la liste d'instances de tous les joueurs"""
        return [Player(**data) for data in Player.db_players.all()]
        




