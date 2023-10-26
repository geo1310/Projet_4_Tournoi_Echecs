import os
from tinydb import TinyDB, Query


NATIONAL_ID = 'GB13106'
FOLDER_PLAYERS = 'data/players'
FOLDER_TOURNAMENTS = 'data/tournaments'
FILE_PLAYERS = 'players.json'
FILE_TOURNAMENTS = 'tournaments.json'
FULL_PATH_PLAYERS = os.path.join(FOLDER_PLAYERS, FILE_PLAYERS)
FULL_PATH_TOURNAMENTS = os.path.join(FOLDER_TOURNAMENTS, FILE_TOURNAMENTS)


def db_players_create():
    if not os.path.exists(FOLDER_PLAYERS):
        os.makedirs(FOLDER_PLAYERS)
    db_players = TinyDB(FULL_PATH_PLAYERS)
    db_players = db_players.table(NATIONAL_ID)
    player_query = Query()
    return db_players, player_query


def db_tournaments_create():
    if not os.path.exists(FOLDER_TOURNAMENTS):
        os.makedirs(FOLDER_TOURNAMENTS)
    db_tournaments = TinyDB(FULL_PATH_PLAYERS)
    return db_tournaments

    
if __name__ == "__main__":
    os.system('cls')
    db = db_players_create()

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
        Joueur = Query()
        if not db.search((Joueur.nom == player['nom']) & (Joueur.prenom == player['prenom'])):
            db.insert(player)
            print(f"Le joueur {player['nom']} - {player['prenom']} a bien été enregistré.")
        else:
            print(f"Le joueur {player['nom']} - {player['prenom']} est deja dans la liste !!!")

    joueur = db.get(doc_id=2)
    print(joueur)
