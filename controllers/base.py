from models.base import Player, PlayersList, Match, Round, Tournament


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
                self.tournaments()
            elif choice == "2":
                self.rapports()
            elif choice == "3":
                self.players()
            else:
                self.view.invalid_choice()

    def tournaments(self):
        while True:
            # menu tournois
            menu_list = ["Créer/Lancer un Tournoi", "Continuer un tournoi en cours", "Retour au menu principal"]
            title = "Menu Tournois"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                tournement = self.view.create_tournament()
            elif choice == "2":
                print("Continuer un tournoi en cours")
            elif choice == "3":
                break
            else:
                self.view.invalid_choice()

    def players(self):
        while True:
            # menu joueurs
            menu_list = ["Afficher la liste des joueurs", "Ajouter un joueur", "Supprimer un joueur", "Retour au menu principal"]
            title = "Menu Joueurs"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                # ----- affiche la liste des joueurs -----
                players_list = PlayersList('players.json')
                self.view.print_players_list(players_list)
                self.view.prompt_wait_enter()
                
            elif choice == "2":
                # ----- ajoute un joueur -----
                player = self.view.create_player()
                if player[0] != '' and player[1] != '' and player[2] != '':
                    player_instance = Player(player[1], player[0], player[2])
                    player_instance.save_player()
                self.view.prompt_wait_enter()
            elif choice == "3":
                # ----- supprime un joueur -----
                player = self.view.create_player()
                player_instance = Player(player[1], player[0], player[2])
                player_instance.delete_player()
                self.view.prompt_wait_enter()
            elif choice == "4":
                break
            else:
                self.view.invalid_choice()

    def rapports(self):
        while True:
            # menu rapports
            menu_list = ["Afficher la liste des joueurs", "Liste des tournois", "Nom et Date d'un tournoi", "Liste des Joueurs d'un tournoi", "Liste des Tours et matchs d'un tournoi", "Retour au menu principal"]
            title = "Menu Rapports"
            choice = self.view.display_menu(title, menu_list)
            if choice == "1":
                # ----- affiche la liste des joueurs -----
                players_list = PlayersList('players.json')
                self.view.print_players_list(players_list)
                self.view.prompt_wait_enter()
            elif choice == "2":
                print("Liste des tournois")
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
