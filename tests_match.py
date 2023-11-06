import os
from models.match import Match
from models.player import Player


if __name__ == "__main__":
    os.system('cls')
    # cree une instance de tous les joueurs de la liste
    players_list_instance = Player.list_instance()
    print()
    # cree un match avec les deux premiers joueurs de la liste
    # test les differents resultats
    
    match1 = Match([players_list_instance[0], 0], [players_list_instance[1], 0])
    print(f"{match1.result(0)} : {match1}")
    print(f" Match 1 fini : {match1.finished()}")
    match2 = Match([players_list_instance[0], 0], [players_list_instance[1], 0])
    print(f"{match2.result(1)} : {match2}")
    print(f" Match 2 fini : {match2.finished()}")
    match3 = Match([players_list_instance[0], 0], [players_list_instance[1], 0])
    print(f"{match3.result(2)} : {match3}")
    print(f" Match 3 fini : {match3.finished()}")
    match4 = Match([players_list_instance[0], 0], [players_list_instance[1], 0])
    print(f"{match4.result('ffff')} : {match4}")
    print(f" Match 4 fini : {match4.finished()}")
    print()
    print(players_list_instance[0].score, players_list_instance[1].score)
    print()