import json
import os
import random

NATIONAL_ID = 'GB13106'
FOLDER_PLAYERS = 'data/players'
FOLDER_TOURNAMENTS = 'data/tournaments'
FILE_PLAYERS = 'players.json'
FILE_TOURNAMENTS = 'tournaments.json'
FULL_PATH_PLAYERS = os.path.join(FOLDER_PLAYERS, FILE_PLAYERS)
FULL_PATH_TOURNAMENTS = os.path.join(FOLDER_TOURNAMENTS, FILE_TOURNAMENTS)

if not os.path.exists(FOLDER_PLAYERS):
    os.makedirs(FOLDER_PLAYERS)
if not os.path.exists(FOLDER_TOURNAMENTS):
    os.makedirs(FOLDER_TOURNAMENTS)


class Player:
    def __init__(self, first_name, last_name, birthday, score=0):
        self.last_name = last_name.capitalize()
        self.first_name = first_name.capitalize()
        self.birthday = birthday
        self.score = score

    def __str__(self):
        return f"{self.first_name} {self.last_name} née(e) le {self.birthday}"

    def to_json(self):
        # Crée un dictionnaire avec les données du joueur pour enregistrement fichier json
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "score": self.score
        }

    def save_player(self):
        players_list = DataList(FULL_PATH_PLAYERS)
        # Nouveau joueur
        new_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday
        }
        # Vérifie si le joueur est deja dans la liste
        if not any(player == new_player for player in players_list):
            players_list.append(new_player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(FULL_PATH_PLAYERS, "w") as fichier:
                json.dump(players_list, fichier)

            return f"\nLe nouveau joueur a été ajouté à {FILE_PLAYERS}"
        else:
            return "\nLe joueur est deja enregistré !!!"

    def delete_player(self):
        players_list = DataList(FULL_PATH_PLAYERS)
        # joueur
        new_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday
        }
        # Vérifie si le joueur est dans la liste
        if any(player == new_player for player in players_list):
            players_list.remove(new_player)
            # Enregistrez la liste mise à jour dans le fichier JSON
            with open(FULL_PATH_PLAYERS, "w") as fichier:
                json.dump(players_list, fichier)

            return f"\nLe joueur a été supprimé de {FULL_PATH_PLAYERS}"
        else:
            return "\nLe joueur n'est pas dans la liste !!!"


class Match:

    MATCH_WIN = 1
    MATCH_NUL = 0.5

    def __init__(self, player_1, player_2, finished=False):
        self.player_1 = player_1
        self.player_2 = player_2
        self.finished = finished

    def __str__(self):
        return f"{self.player_1} - {self.player_2}"
    
    def to_json(self):
        return {
            'player_1': self.player_1,
            'player_2': self.player_2,
            'finished': self.finished
        }
    
    def result(self, number):
        if number == 1:
            self.player_1[1] = Match.MATCH_WIN
            self.player_1[0]['score'] += Match.MATCH_WIN
            self.player_2[1] = 0
        elif number == 2:
            self.player_1[1] = 0
            self.player_2[1] = Match.MATCH_WIN
            self.player_2[0]['score'] += Match.MATCH_WIN
        else:
            self.player_1[1] = Match.MATCH_NUL
            self.player_1[0]['score'] += Match.MATCH_NUL
            self.player_2[1] = Match.MATCH_NUL
            self.player_2[0]['score'] += Match.MATCH_NUL
        self.finished = True



class Round:
    def __init__(self, number, matchs_list=None, finished=False):
        self.number = number
        self.matchs_list = matchs_list if matchs_list is not None else []
        self.finished = finished

    def __str__(self):
        return f"{self.to_json()}"
    
    def to_json(self):
        return {
            'number': self.number,
            'matchs_list': self.matchs_list,
            'finished': self.finished
        }


class Tournament:
    def __init__(self, name, location, description, nb_rounds=4, players_list=None, rounds_list=None, act_round=1, start_date='', end_date='', finished=False):
        self.national_id = NATIONAL_ID
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
        self.finished = finished

    def __str__(self):
        return f"Tournoi {self.name}.{self.location} du {self.start_date} au {self.end_date}"
    
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
            "status": self.finished
        }

    def save_tournament(self):
        tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
        existing_tournament = next((t for t in tournaments_list if t["name"] == self.name and t["location"] == self.location), None)
        if existing_tournament is not None:
            existing_tournament.update({
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
                "finished": self.finished,
            })
        else:
            tournament = {
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
                "finished": self.finished,
            }
            tournaments_list.append(tournament)
        # Enregistrez la liste mise à jour dans le fichier JSON
        with open(FULL_PATH_TOURNAMENTS, "w") as fichier:
            json.dump(tournaments_list, fichier)
        return "\nLe tournoi a été enregistré avec succes !!!"    

class DataList(list):
    # crée une liste d'apres un fichier json et peut la mélanger
    def __init__(self, full_path):
        self.full_path = full_path
        if os.path.exists(self.full_path):
            with open(self.full_path, "r") as fichier:
                data = json.load(fichier)
        else:
            data = []
        self.extend(data)

    def shuffle(self):
        random.shuffle(self)


if __name__ == "__main__":
    os.system('cls')
    act_round = {'number': 1, 'matchs_list': [{'player_1': [{'last_name': '2', 'first_name': '2', 'birthday': '', 'score': 0}, 0], 'player_2': [{'last_name': '4', 'first_name': '4', 'birthday': '', 'score': 0}, 0], 'finished': False}, {'player_1': [{'last_name': '3', 'first_name': '3', 'birthday': '', 'score': 0}, 0], 'player_2': [{'last_name': '1', 'first_name': '1', 'birthday': '', 'score': 0}, 0], 'finished': False}], 'finished': False}
    round_1 = Round(**act_round)
    print(round_1)
