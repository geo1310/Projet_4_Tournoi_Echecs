import json
import os
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

    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
            "score": self.score
        }

    def save_player(self):
        fichier_json = "data/players/players.json"
        players_list = DataList('players/players.json')
        # Nouveau joueur
        new_player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday
        }
        # Vérifie si le joueur est deja dans la liste
        if not any(player == new_player for player in players_list):
            players_list.append(new_player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(fichier_json, "w") as fichier:
                json.dump(players_list, fichier)

            print("\nLe nouveau joueur a été ajouté à", fichier_json)
        else:
            print("\nLe joueur est deja enregistré !!!")

    def delete_player(self):
        fichier_json = "data/players/players.json"
        players_list = DataList('players/players.json')
        # joueur
        new_player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday
        }
        # Vérifie si le joueur est dans la liste
        if any(player == new_player for player in players_list):
            players_list.remove(new_player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(fichier_json, "w") as fichier:
                json.dump(players_list, fichier)

            print("\nLe joueur a été supprimé de", fichier_json)
        else:
            print("\nLe joueur n'est pas dans la liste !!!")


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
    def __init__(self, name, location, description, nb_rounds=4, players_list=None, rounds_list=None, act_round=1, start_date='', end_date='', status='new'):
        self.national_id = NATIONAL_ID
        self.name = name
        self.location = location
        self.description = description
        self.nb_rounds = nb_rounds
        self.players_list = players_list if players_list is not None else []
        self.rounds_list = rounds_list if rounds_list is not None else []
        self.act_round = act_round
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"Tournoi {self.name} du {self.start_date} au {self.end_date}"
    
    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "national_id": self.national_id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "nb_rounds": self.nb_rounds,
            "players_list": self.players_list,
            "rounds_list": self.rounds_list,
            "act_round": self.act_round,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status
        }

    def save_tournament(self):
        fichier_json = "data/tournaments/tournaments.json"
        tournaments_list = DataList('tournaments/tournaments.json')
        existing_tournament = next((t for t in tournaments_list if t["name"] == self.name and t["location"] == self.location), None)
        if existing_tournament is not None:
            existing_tournament.update({
                "national_id": self.national_id,
                "name": self.name,
                "location": self.location,
                "description": self.description,
                "nb_rounds": self.nb_rounds,
                "rounds_list": self.rounds_list,
                "players_list": self.players_list,
                "act_round": self.act_round,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "status": self.status,
            })
        else:
            tournament = {
                "national_id": self.national_id,
                "name": self.name,
                "location": self.location,
                "description": self.description,
                "nb_rounds": self.nb_rounds,
                "rounds_list": self.rounds_list,
                "players_list": self.players_list,
                "act_round": self.act_round,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "status": self.status,
            }
            tournaments_list.append(tournament)
        # Enregistrez la liste mise à jour dans le fichier JSON
        with open(fichier_json, "w") as fichier:
            json.dump(tournaments_list, fichier)
        print("\nLe tournoi a été enregistré avec succes !!!")    

class DataList(list):
    # crée une liste d'apres un fichier json et peut la mélanger
    def __init__(self, data_file_list):
        self.data_file_list = data_file_list
        full_path = os.path.join("./data/", data_file_list)
        if os.path.exists(full_path):
            with open(full_path, "r") as fichier:
                data = json.load(fichier)
        else:
            data = []
        self.extend(data)

    def shuffle(self):
        random.shuffle(self)


if __name__ == "__main__":
    player = Player('test', 'test', 'test')
    player.save_player()
