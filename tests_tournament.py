import os
from faker import Faker
from models.round import Round
from models.match import Match
from models.player import Player
from models.tournament import Tournament


if __name__ == "__main__":
    os.system('cls')
    # cree un tournoi test
    nb_players = 4
    fake = Faker('fr_FR')
    tournament_name = fake.word()
    tournament_location = fake.city()
    players_list = []
    for _ in range(nb_players):
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65)
        birthday_str = birthday.strftime("%d/%m/%Y")
        player = Player(fake.last_name(), fake.first_name(), birthday_str)
        players_list.append(player.create())

    print()
    print(players_list)
    print()
    
    tournament = Tournament(tournament_name, tournament_location, 'tournoi test', 2, players_list )
    print(tournament.create())
    print()
    print(tournament)
    