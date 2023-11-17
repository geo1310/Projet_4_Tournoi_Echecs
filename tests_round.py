import os
from models.round import Round
from models.player import Player


if __name__ == "__main__":
    os.system("cls")
    # cree un round
    round = Round(1)
    print(round)
    print()
    # cree une instance de tous les joueurs de la liste
    players_list_instance = Player.list_instance()
    print()
