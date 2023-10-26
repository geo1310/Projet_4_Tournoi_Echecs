import os
from db_create import db_players_create


class Player:
    
    db_players, player_query = db_players_create()

    def __init__(self, first_name, last_name, birthday=''):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birthday = birthday

    def __repr__(self):
        return f"{self.first_name} {self.last_name} née(e) le {self.birthday}"

    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
        }

    def save(self):
        """Sauvegarde un joueur de la base players.json"""
        if not self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name)):
            self.db_players.insert(self.to_json())
            print(f"Le joueur {self.first_name} {self.last_name} a bien été enregistré.")
        else:
            print(f"Le joueur {self.first_name} {self.last_name} est deja dans la liste !!!")

    def delete(self):
        """Supprime un joueur de la base players.json"""
        if self.db_players.search((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name)):
            self.db_players.remove((self.player_query.first_name == self.first_name) & (self.player_query.last_name == self.last_name))
            print(f"Le joueur {self.first_name} {self.last_name} a bien été suppimé.")
        else:
            print(f"Le joueur {self.first_name} {self.last_name} n'est pas dans la liste !!!")

    def del_all_db(self):
        """vide players.json"""
        self.db_players.truncate()

    def bootstrap_db(self):
        """Ajoute 10 joueurs à players.json"""
        players = [
            {
                'nom': 'Smith',
                'prenom': 'John',
                'date_de_naissance': '15/03/1990',
                'score': 0
            },
            {
                'nom': 'Johnson',
                'prenom': 'Alice',
                'date_de_naissance': '22/07/1985',
                'score': 0
            },
            {
                'nom': 'Brown',
                'prenom': 'David',
                'date_de_naissance': '10/01/1995',
                'score': 0
            },
            {
                'nom': 'Wilson',
                'prenom': 'Emily',
                'date_de_naissance': '30/09/1998',
                'score': 0
            },
            {
                'nom': 'Martinez',
                'prenom': 'Daniel',
                'date_de_naissance': '08/05/1992',
                'score': 0
            },
            {
                'nom': 'Lee',
                'prenom': 'Sophia',
                'date_de_naissance': '19/11/1989',
                'score': 0
            },
            {
                'nom': 'Garcia',
                'prenom': 'Liam',
                'date_de_naissance': '25/12/1997',
                'score': 0
            },
            {
                'nom': 'Taylor',
                'prenom': 'Olivia',
                'date_de_naissance': '03/08/1994',
                'score': 0
            },
            {
                'nom': 'Harris',
                'prenom': 'Michael',
                'date_de_naissance': '12/04/1996',
                'score': 0
            },
            {
                'nom': 'Clark',
                'prenom': 'Ella',
                'date_de_naissance': '28/06/1991',
                'score': 0
            }
        ]
        
        for player in players:
            
            if not self.db_players.search((self.player_query.first_name == player['prenom']) & (self.player_query.last_name == player['nom'])):
                self.db_players.insert(player)
                print(f"Le joueur {player['nom']} - {player['prenom']} a bien été enregistré.")
            else:
                print(f"Le joueur {player['nom']} - {player['prenom']} est deja dans la liste !!!")

    def reboot_db():
        pass


if __name__ == "__main__":
    os.system('cls')   
    player = Player('sue ellen', 'cousin', '25/11/1982')

    print(player)
    player.save()
    player.del_all_db()
    player.bootstrap_db()
