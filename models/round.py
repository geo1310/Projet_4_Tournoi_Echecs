import random
from models.match import Match


class Round:
    def __init__(self, number, matchs_list=None, start_date="", end_date=""):
        self.number = number
        self.matchs_list = matchs_list if matchs_list else []
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.__dict__}"

    def to_dict(self):
        return self.__dict__

    def matchs_list(self, filter):
        """retourne la liste des matchs selon un filtre ( all ou not_finished)"""
        if filter == "all":
            return self.matchs_list
        elif filter == "not_finished":
            matchs_list_not_finished = []
            for match in self.matchs_list:
                if not match.finished():
                    matchs_list_not_finished.append(match)
            return matchs_list_not_finished

    def create_matchs_list(self, players_list):
        if self.number == 1:
            # creation de la liste des matchs ( joueurs choisis au hasard pour lre round 1)
            random.shuffle(players_list)

        # liste des joueurs ayant deja joués
        players_played = set()

        for i in range(len(players_list)):
            player_1 = players_list[i]
            if player_1["id"] in players_played:
                continue
            for j in range(i + 1, len(players_list)):
                player_2 = players_list[j]
                if player_2["id"] in players_played:
                    continue

                # Vérifie si les joueurs n'ont pas déjà joué ensemble
                if player_2["id"] not in player_1["opponents"]:
                    # Crée un match et l ajoute à la liste des matchs
                    match = Match([player_1, 0], [player_2, 0])
                    self.matchs_list.append(match.to_dict())

                    # Mise à jour de la liste des adversaires des joueurs
                    player_1["opponents"].append(player_2["id"])
                    player_2["opponents"].append(player_1["id"])
                    # Mise à jour de la liste des joueurs ayant deja joués
                    players_played.add(player_1["id"])
                    players_played.add(player_2["id"])
                    break
