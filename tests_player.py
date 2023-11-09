import os
from faker import Faker
from datetime import datetime
from  models.player import Player


def del_all_db():
    """vide players.json"""
    Player.db_players.truncate()

def bootstrap_db(nb_players):
    """ crée une liste de joueurs au hasard """
    players = []
    fake = Faker('fr_FR')
    for _ in range(nb_players):
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
        birthday_str = birthday.strftime("%d/%m/%Y")
        player = {
            'last_name': fake.last_name(),
            'first_name': fake.first_name(),
            'birthday': birthday_str
        }
        print(player)
        players.append(player)
        
    for player_test in players:
        player = Player(**player_test)
        print(player.create())


if __name__ == "__main__":
    os.system('cls')
    
    # efface tous les joueurs de la base
    #del_all_db()
    
    # cree une liste de joueurs
    bootstrap_db(8)
    
    # cree une instance de joueur avec son id
    #id_search = '533e313d'
    #player = Player.from_id(id_search)
    #print(f"\nJoueur avec l'id {id_search} : {player}\n")
    
    # cree une instance de joueur
    #player = Player('laroche', 'jean', '13/10/1969')
    
    # sauvegarde un joueur
    #print(player.create())
    
    # efface un joueur
    #print(player.delete())
    
    # affiche la liste des joueurs
    #print("\nListe des joueurs : \n")
    #print(Player.list())
    #print()

    # cree une instance de tous les joueurs de la liste
    #print("Liste des instances de joueurs : \n")
    #print(Player.list_instance())
    #print()
    
    # rechercher dans la base players
    #print(Player.search('id', '33e002ea'))
    #print(Player.search('last_name', 'laroche'))


    

