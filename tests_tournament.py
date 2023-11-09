import os
from faker import Faker
from models.player import Player
from models.tournament import Tournament


if __name__ == "__main__":
    os.system('cls')
    
    # cree un tournoi test
    nb_players = 4
    nb_rounds = 3
    fake = Faker('fr_FR')
    tournament_name = fake.word()
    tournament_location = fake.city()
    id = None
    players_list = []
    # avec liste de joueurs au hasard
    for _ in range(nb_players):
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
        birthday_str = birthday.strftime("%d/%m/%Y")
        player = Player(fake.last_name(), fake.first_name(), birthday_str)
        player.create()
        players_list.append(player.to_dict_tournament())
    tournament = Tournament(id , tournament_name, tournament_location, 'tournoi test', nb_rounds)
    tournament.players_list.extend(players_list)
    print()
    print(tournament.save())
    print()
    print(tournament)
    
    
    '''
    # recherche dans la base
    tournament = Tournament.search('id', '7f35229f')
    print(tournament)
    print(tournament.doc_id)
    print()
    
    tournament_instance = Tournament(**tournament)
    print(tournament_instance)
    print(tournament_instance.id)
    tournament_instance.description = 'une toute nouvelle description'
    
    # mettre a jour un tournoi
    Tournament.db_tournaments.update(tournament_instance.to_dict(),Tournament.tournaments_query.id == tournament_instance.id)
    '''
    