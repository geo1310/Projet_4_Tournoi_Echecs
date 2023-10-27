import os
from tinydb import TinyDB, Query

NATIONAL_ID = 'GB13106'
FOLDER_PLAYERS = 'data/players'
FILE_PLAYERS = 'players.json'
FULL_PATH_PLAYERS = os.path.join(FOLDER_PLAYERS, FILE_PLAYERS)


def db_players_create():
    if not os.path.exists(FOLDER_PLAYERS):
        os.makedirs(FOLDER_PLAYERS)
    db_players = TinyDB(FULL_PATH_PLAYERS)
    db_players = db_players.table(NATIONAL_ID)
    player_query = Query()
    return db_players, player_query


class Player:
    
    db_players, player_query = db_players_create()

    def __init__(self, last_name, first_name, birthday=''):
        self.last_name = last_name.capitalize()
        self.first_name = first_name.capitalize()
        self.birthday = birthday

    def __repr__(self):
        return f"{self.last_name} {self.first_name} née(e) le {self.birthday}"

    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
        }

    def save(self):
        """Sauvegarde un joueur de la base players.json"""
        if not self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name)):
            self.db_players.insert(self.to_json())
            return f"\nLe joueur {self.first_name} {self.last_name} a bien été enregistré."
        else:
            return f"\nLe joueur {self.first_name} {self.last_name} est deja dans la liste !!!"

    def delete(self):
        """Supprime un joueur de la base players.json"""
        if self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name)):
            self.db_players.remove((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name))
            return f"\nLe joueur {self.first_name} {self.last_name} a bien été suppimé."
        else:
            return f"\nLe joueur {self.first_name} {self.last_name} n'est pas dans la liste !!!"

    @staticmethod
    def list():
        """Retourne la liste de tous les joueurs"""
        return Player.db_players.all()
    
    @staticmethod
    def del_all_db():
        """vide players.json"""
        Player.db_players.truncate()

    @staticmethod
    def bootstrap_db():
        """Ajoute 10 joueurs à players.json"""
        players = [
            {
                'last_name': 'Smith',
                'first_name': 'John',
                'birthday': '15/03/1990'
            },
            {
                'last_name': 'Johnson',
                'first_name': 'Alice',
                'birthday': '22/07/1985'
            },
            {
                'last_name': 'Brown',
                'first_name': 'David',
                'birthday': '10/01/1995'
            },
            {
                'last_name': 'Wilson',
                'first_name': 'Emily',
                'birthday': '30/09/1998'
            },
            {
                'last_name': 'Martinez',
                'first_name': 'Daniel',
                'birthday': '08/05/1992'
            },
            {
                'last_name': 'Lee',
                'first_name': 'Sophia',
                'birthday': '19/11/1989'
            },
            {
                'last_name': 'Garcia',
                'first_name': 'Liam',
                'birthday': '25/12/1997'
            },
            {
                'last_name': 'Taylor',
                'first_name': 'Olivia',
                'birthday': '03/08/1994'
            },
            {
                'last_name': 'Harris',
                'first_name': 'Michael',
                'birthday': '12/04/1996'
            },
            {
                'last_name': 'Clark',
                'first_name': 'Ella',
                'birthday': '28/06/1991'
            }
        ]
        
        for player in players:
            
            if not Player.db_players.search((Player.player_query.first_name == player['first_name']) & (Player.player_query.last_name == player['last_name'])):
                Player.db_players.insert(player)
                print(f"Le joueur {player['last_name']} - {player['first_name']} a bien été enregistré.")
            else:
                print(f"Le joueur {player['last_name']} - {player['first_name']} est deja dans la liste !!!")

    def reboot_db():
        pass


if __name__ == "__main__":
    os.system('cls')
    Player.bootstrap_db()   
    print(Player.list())
    #Player.del_all_db()
   
