import os
import json
import random

NATIONAL_ID = 'GB13106'


class Player:
    def __init__(self, first_name, last_name, birthday='00/00/0000', score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.score = score

    def __str__(self):
        return f"{self.first_name} {self.last_name} née(e) le {self.birthday}"

    def is_player_in_list(self, new_player, players_list):
        for player in players_list:
            if player["nom"] == new_player["nom"] and player["prenom"] == new_player["prenom"] and player["date_de_naissance"] == new_player["date_de_naissance"]:
                return True
        return False

    def save_player(self):
        fichier_json = "data/players/players.json"
        players_list = PlayersList('players.json')
        # Nouveau joueur
        new_player = {
            "nom": self.last_name,
            "prenom": self.first_name,
            "date_de_naissance": self.birthday
        }
        # Vérifie si le joueur est deja dans la liste
        if not self.is_player_in_list(new_player, players_list):
            players_list.append(new_player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(fichier_json, "w") as fichier:
                json.dump(players_list, fichier)

            print("\nLe nouveau joueur a été ajouté à", fichier_json)
        else:
            print("\nLe joueur est deja enregistré !!!")

    def delete_player(self):
        fichier_json = "data/players/players.json"
        players_list = PlayersList('players.json')
        # joueur
        player = {
            "nom": self.last_name,
            "prenom": self.first_name,
            "date_de_naissance": self.birthday
        }
        # Vérifie si le joueur est dans la liste
        if self.is_player_in_list(player, players_list):
            players_list.remove(player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(fichier_json, "w") as fichier:
                json.dump(players_list, fichier)

            print("\nLe joueur a été supprimé de", fichier_json)
        else:
            print("\nLe joueur n'est pas dans la liste !!!")


class PlayersList(list):
    # crée la liste des joueurs depuis un fichier json et peut la mélanger
    def __init__(self, players_file_list):
        self.players_file_list = players_file_list
        full_path = os.path.join("./data/players/", players_file_list)
        if os.path.exists(full_path):
            with open(full_path, "r") as fichier:
                players = json.load(fichier)
        else:
            players = []
        self.extend(players)

    def shuffle(self):
        random.shuffle(self)


class Match:
    def __init__(self, player_score1, player_score2):
        self.player_score1 = player_score1
        self.player_score2 = player_score2

    def __str__(self):
        return f"{self.player_score1} - {self.player_score2}"


class Round:
    def __init__(self, number, player_score1, player_score2):
        self.number = number
        self.player_score1 = player_score1
        self.player_score2 = player_score2

    def __str__(self):
        return f"{self.player_score1} - {self.player_score2}"


class Tournament:
    def __init__(self, name, location, description, rounds_list, players_list, nb_rounds=4, round=1,start_date='', end_date=''):
        self.national_id = NATIONAL_ID
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.round = round
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description

    def __str__(self):
        return f"Tournoi {self.name} du {self.start_date} au {self.end_date}"


if __name__ == "__main__":
    player = Player('test', 'test', 'test')
    player.save_player()
