import datetime
from models.base import Player, DataList, Tournament, FULL_PATH_TOURNAMENTS, FULL_PATH_PLAYERS


class Controller:
    def __init__(self, view):
        # models
        self.view = view

    def run(self):
        while True:
            # menu principal
            menu_list = ["Tournois", "Rapports", "Joueurs", "Quitter"]
            title = "Menu Principal"
            choice = self.view.display_menu(title, menu_list)
            if choice == "4":
                self.view.print_something("\nAu revoir!\n")
                break
            elif choice == "1":
                self.tournaments_menu()
            elif choice == "2":
                self.rapports_menu()
            elif choice == "3":
                self.players_menu()
            else:
                self.view.invalid_choice()

    '''
    Gestion des Menus
    
    '''
    def tournaments_menu(self):
        while True:
            # menu tournois
            menu_list = ["Afficher la liste des Tournois", "Créer/Lancer un Tournoi", "Continuer un tournoi en cours", "Retour au menu principal"]
            title = "Menu Tournois"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                self.tournaments_list()
            elif choice == "2":
                self.create_tournament()
            elif choice == "3":
                self.continue_tournament()
            elif choice == '4':
                break
            else:
                self.view.invalid_choice()
    
    def players_menu(self):
        while True:
            # menu joueurs
            menu_list = ["Afficher la liste des joueurs", "Ajouter un joueur", "Supprimer un joueur", "Retour au menu principal"]
            title = "Menu Joueurs"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                self.players_list()
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.del_player()
            elif choice == "4":
                break
            else:
                self.view.invalid_choice()

    def rapports_menu(self):
        while True:
            # menu rapports
            menu_list = ["Afficher la liste des joueurs", "Liste des tournois", "Liste des Joueurs d'un tournoi", "Liste des Tours et matchs d'un tournoi", "Retour au menu principal"]
            title = "Menu Rapports"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                self.players_list()
            elif choice == "2":
                self.tournaments_list()
            elif choice == "3":
                self.players_tournament()
            elif choice == "4":
                self.rounds_matches_tournament()
            elif choice == "5":
                break
            else:
                self.view.invalid_choice()

    '''
    Gestion des Joueurs

    '''
    def players_list(self):
        # affiche la liste des joueurs
        players_list = DataList(FULL_PATH_PLAYERS)
        self.view.print_players_list(players_list)
        self.view.prompt_wait_enter()

    def add_player(self):
        # ajoute un joueur
        player = self.view.create_player("Ajout d'un Joueur dans la base de données ( data/players/players.json)")
        if player[0] != '' and player[1] != '':
            player_instance = Player(player[0], player[1], player[2])
            self.view.print_something(player_instance.save_player())
        self.view.prompt_wait_enter()

    def del_player(self):
        # supprime un joueur
        player = self.view.create_player("Suppression d'un Joueur dans la base de données ( data/players/players.json)")
        player_instance = Player(player[0], player[1], player[2])
        self.view.print_something(player_instance.delete_player())
        self.view.prompt_wait_enter()

    '''
        Gestion des Tournois
   
    '''

    def tournaments_list(self):
        # affiche la liste des tournois
        tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
        self.view.print_tournaments_list(tournaments_list)
        self.view.prompt_wait_enter()

    def create_tournament(self):
        # création d'un tournoi
        tournament = Tournament(*self.view.create_tournament())
        # ajout des joueurs au tournoi
        index = 1
        while True:
            new_player = Player(*self.view.create_player(f"Ajout du joueur {index} au tournoi {tournament.name} de {tournament.location}. "))
            if new_player.last_name == "":
                break
            tournament.players_list.append(new_player.to_json())
            self.view.print_something(new_player.save_player())
            index += 1
        # sauvegarde du tournoi
        self.view.print_something(tournament.save_tournament())
        if self.view.ask_question("Voulez-vous démarrer le tournoi "):
            self.start_tournament(tournament)
    
    def continue_tournament(self):
        # choix d'un tournoi à commencer parmis les tournois non finis
        tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
        tournaments_list_not_finished = []
        for tournament in tournaments_list:
            if not tournament['finished']:
                tournaments_list_not_finished.append(tournament)
        if tournaments_list_not_finished != []:
            self.view.underline_title_and_cls("Liste des Tournois à effectuer :")
            self.view.print_tournaments_list(tournaments_list_not_finished)
            choice = self.view.return_choice("Entrer le Numéro de tournoi que vous souhaiter lancer : ")
            try:
                choice = int(choice)
                new_tournement = tournaments_list_not_finished[choice-1]
                del new_tournement['national_id']
                tournament = Tournament(**new_tournement)
                self.start_tournament(tournament)
            except Exception as e:
                self.view.print_something("\nChoix invalide !!!")
                print(f"{str(e)}")
                self.view.prompt_wait_enter()
        else:
            self.view.print_something("\nAucun Tournoi à continuer !!!")
            self.view.prompt_wait_enter()

    def start_tournament(self, tournament):
        date = datetime.date.today().strftime("%d/%m/%Y")
        # déroulement d'un tournoi
        self.view.underline_title_and_cls(f"{date} - Tournoi : {tournament.name} de {tournament.location} en {tournament.nb_rounds} Rounds")
        self.view.prompt_wait_enter()

    '''
    Gestion des Rapports
    
    '''

    def players_tournament(self):
        print("Liste des Joueurs d'un tournoi")
        self.view.prompt_wait_enter()

    def rounds_matches_tournament(self):
        print("Liste des Tours et matchs d'un tournoi")
        self.view.prompt_wait_enter()