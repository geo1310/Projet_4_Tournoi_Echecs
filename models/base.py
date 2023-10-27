import json
import os
import random

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
