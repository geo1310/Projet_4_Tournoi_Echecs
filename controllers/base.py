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
                print("\nAu revoir!\n")
                break
            elif choice == "1":
                self.tournaments_menu()
            elif choice == "2":
                self.rapports_menu()
            elif choice == "3":
                self.players_menu()
            else:
                self.view.invalid_choice()

    def tournaments_menu(self):
        while True:
            # menu tournois
            menu_list = ["Créer/Lancer un Tournoi", "Continuer un tournoi en cours", "Retour au menu principal"]
            title = "Menu Tournois"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                # continuer un tournoi deja commencé
                self.continue_tournament()
            elif choice == "3":
                break
            else:
                self.view.invalid_choice()
    
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
            new_player.save_player()
            index += 1
        # sauvegarde du tournoi
        tournament.save_tournament()
        if self.view.ask_question("Voulez-vous démarrer le tournoi "):
            self.start_tournament(tournament)
    
    def continue_tournament(self):
        pass

    def start_tournament(self, tournament):
        # déroulement d'un tournoi
        print(tournament.name + tournament.location)
        self.view.prompt_wait_enter()

    def players_menu(self):
        while True:
            # menu joueurs
            menu_list = ["Afficher la liste des joueurs", "Ajouter un joueur", "Supprimer un joueur", "Retour au menu principal"]
            title = "Menu Joueurs"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                # affiche la liste des joueurs
                players_list = DataList(FULL_PATH_PLAYERS)
                self.view.print_players_list(players_list)
                self.view.prompt_wait_enter()
                
            elif choice == "2":
                # ajoute un joueur
                player = self.view.create_player("Ajout d'un Joueur dans la base de données ( data/players/players.json)")
                if player[0] != '' and player[1] != '':
                    player_instance = Player(player[0], player[1], player[2])
                    player_instance.save_player()
                self.view.prompt_wait_enter()
            elif choice == "3":
                # supprime un joueur
                player = self.view.create_player("Suppression d'un Joueur dans la base de données ( data/players/players.json)")
                player_instance = Player(player[0], player[1], player[2])
                player_instance.delete_player()
                self.view.prompt_wait_enter()
            elif choice == "4":
                break
            else:
                self.view.invalid_choice()

    def rapports_menu(self):
        while True:
            # menu rapports
            menu_list = ["Afficher la liste des joueurs", "Liste des tournois", "Nom et Date d'un tournoi", "Liste des Joueurs d'un tournoi", "Liste des Tours et matchs d'un tournoi", "Retour au menu principal"]
            title = "Menu Rapports"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                # affiche la liste des joueurs
                players_list = DataList(FULL_PATH_PLAYERS)
                self.view.print_players_list(players_list)
                self.view.prompt_wait_enter()
            elif choice == "2":
                # affiche la liste des tournois
                tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
                self.view.print_tournaments_list(tournaments_list)
                self.view.prompt_wait_enter()
            elif choice == "3":
                print("Nom et Date d'un tournoi")
            elif choice == "4":
                print("Liste des Joueurs d'un tournoi")
            elif choice == "5":
                print("Liste des Tours et matchs d'un tournoi")
            elif choice == "6":
                break
            else:
                self.view.invalid_choice()

    
