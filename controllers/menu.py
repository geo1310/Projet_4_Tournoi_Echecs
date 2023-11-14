import sys


class MenuManage:
    '''
    Gestion des Menus

    '''

    def __init__(self, view, player_manage, rapport_manage, tournament_manage):
        self.view = view
        self.player_manage = player_manage
        self.rapport_manage = rapport_manage
        self.tournament_manage = tournament_manage

    def run(self):
        self.main_menu()

    def main_menu(self):
        # menu principal
        menu_items = ["Menu principal du Club d'echec : ", {
            "Tournois":
                self.tournaments_menu,
            "Rapports":
                self.rapports_menu,
            "Joueurs":
                self.players_menu,
            "Quitter":
                self.quit_menu
        }]
        self.run_menu(menu_items)

    def tournaments_menu(self):
        # menu tournois
        menu_items = ["Menu Tournois", {
            "Afficher la liste des Tournois":
                self.tournament_manage.tournaments_list,
            "Créer/Lancer un Tournoi":
                self.tournament_manage.create_tournament,
            "Continuer un tournoi en cours":
                self.tournament_manage.continue_tournament,
            "Retour au menu principal":
                self.main_menu
        }]
        self.run_menu(menu_items)

    def players_menu(self):
        # menu joueurs
        menu_items = ["Menu Joueurs", {
            "Afficher la liste des Joueurs":
                self.player_manage.players_list,
            "Ajouter un Joueur":
                self.player_manage.add_player,
            "Supprimer un Joueur ":
                self.player_manage.del_player,
            "Retour au menu principal":
                self.main_menu
        }]
        self.run_menu(menu_items)

    def rapports_menu(self):
        # menu rapports
        menu_items = ["Menu Rapports", {
            "Afficher la liste des Joueurs":
                self.player_manage.players_list,
            "Liste des Tournois":
                self.tournament_manage.tournaments_list,
            "Liste des Joueurs d'un Tournoi ":
                self.rapport_manage.players_tournament,
            "Liste des Tours et Matchs d'un Tournoi ":
                self.rapport_manage.rounds_matches_tournament,
            "Classement des Joueurs d'un Tournoi ":
                self.rapport_manage.players_classification,
            "Retour au menu principal":
                self.main_menu
        }]
        self.run_menu(menu_items)

    def quit_menu(self):
        sys.exit()

    def run_menu(self, menu_items):
        ''' gestion de l'affichage du menu et du choix utilisateur '''
        title = menu_items[0]
        menu_list = []
        menu_boucle = True
        for index, menu in enumerate(menu_items[1], start=1):
            menu_list.append((index, menu))

        while menu_boucle:
            choice = self.view.display_menu(title, menu_list)
            # analyse du choix utilisateur
            if choice.isdigit():
                choice = int(choice)
                for menu in menu_list:
                    if menu[0] == choice:
                        menu_items[1][menu[1]]()
            else:
                self.view.invalid_choice()
                self.view.prompt_wait_enter()
