import sys
import random
import datetime
from models.player import Player


class Controller:
    def __init__(self, view):
        # models
        self.view = view

    def run(self):
        # menu principal
        menu_items = ["Menu principal du Club d'echec : ", {
            "Tournois": self.tournaments_menu,
            "Rapports": self.rapports_menu, 
            "Joueurs": self.players_menu,
            "Quitter": self.quit_menu
        }]
        self.run_menu(menu_items)
        
    '''
    Gestion des Menus
    
    '''
    def tournaments_menu(self):
        # menu tournois
        menu_items = ["Menu Tournois", {
            "Afficher la liste des Tournois": self.tournaments_list,
            "Créer/Lancer un Tournoi": self.create_tournament,
            "Continuer un tournoi en cours": self.continue_tournament,
            "Retour au menu principal": self.run
        }]
        self.run_menu(menu_items)
    
    def players_menu(self):
        # menu joueurs
        menu_items = ["Menu Joueurs", {
            "Afficher la liste des Joueurs": self.players_list,
            "Ajouter un Joueur": self.add_player,
            "Supprimer un Joueur ": self.del_player,
            "Retour au menu principal": self.run
        }]
        self.run_menu(menu_items)

    def rapports_menu(self):
        # menu rapports
        menu_items = ["Menu Rapports", {
            "Afficher la liste des Joueurs": self.players_list,
            "Liste des Tournois": self.tournaments_list,
            "Liste des Joueurs d'un Tournoi ": self.players_tournament,
            "Liste des Tours et Matchs d'un Tournoi ": self.rounds_matches_tournament,
            "Retour au menu principal": self.run
        }]
        self.run_menu(menu_items)

    def run_menu(self, menu_items):
        ''' gestion de l'affichage du menu et du choix utilisateur par rapport à menu_items'''
        title = menu_items[0]
        menu_list = []
        menu_boucle = True
        index = 1
        for menu in menu_items[1]:
            menu_list.append((index, menu))
            index += 1

        while menu_boucle:
            choice = self.view.display_menu(title, menu_list)
            # analyse du choix utilisateur
            if choice.isdigit():
                choice = int(choice)
                for menu in menu_list:
                    if menu[0] == choice:
                        if menu_items[1][menu[1]]() is False:
                            menu_boucle = False
                            break
            else:
                self.view.invalid_choice()
                self.view.prompt_wait_enter()
            
    def quit_menu(self):
        self.view.display_something("\nAu Revoir !!!\n")
        sys.exit()
        return False

    '''
    Gestion des Joueurs

    '''
    def players_list(self):
        # affiche la liste des joueurs
        players_list = Player.list()
        self.view.display_players_list(players_list)
        self.view.prompt_wait_enter()

    def add_player(self):
        # ajoute un joueur
        player = self.view.create_player("Ajout d'un Joueur dans la base de données (players.json)")
        if player[0] != '' and player[1] != '':
            player_instance = Player(player[0], player[1], player[2])
            self.view.display_something(player_instance.save())
        else:
            self.view.display_something("\nVeuillez renseigner au minimum le nom et le prénom du joueur.")
        self.view.prompt_wait_enter()

    def del_player(self):
        # supprime un joueur
        player = self.view.create_player("Suppression d'un Joueur dans la base de données (players.json)")
        player_instance = Player(player[0], player[1], player[2])
        self.view.display_something(player_instance.delete())
        self.view.prompt_wait_enter()

    '''
        Gestion des Tournois
   
    '''

    def tournaments_list(self):
        # affiche la liste des tournois
        tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
        self.view.display_tournaments_list(tournaments_list)
        self.view.prompt_wait_enter()

    def create_tournament(self):
        # création d'un tournoi
        tournament = Tournament(*self.view.create_tournament())
        # ajout des joueurs au tournoi
        index = 1
        while True:
            new_player = Player(*self.view.create_player(f"Ajout du joueur {index} au tournoi {tournament.name} de {tournament.location}. "))
            if new_player.last_name != "" and new_player.first_name !="":
                tournament.players_list.append(new_player.to_json())
                self.view.display_something(new_player.save_player())
                index += 1
            elif len(tournament.players_list) % 2 == 0 and len(tournament.players_list) != 0:
                break
            else:
                self.view.display_something("\nLe nombre de joueurs d'un tournoi doit etre pair et au moins de deux joueurs !!!")
                self.view.prompt_wait_enter()

        # sauvegarde du tournoi
        self.view.display_something(tournament.save_tournament())
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
            self.view.display_tournaments_list(tournaments_list_not_finished)
            choice = self.view.return_choice("Entrer le Numéro de tournoi que vous souhaiter lancer : ")
            try:
                choice = int(choice)
                tournament_choice = tournaments_list_not_finished[choice-1]
                del tournament_choice['national_id']
                new_tournament = Tournament(**tournament_choice)
                self.start_tournament(new_tournament)
            except Exception:  # as e --> print(f"{str(e)}")
                self.view.display_something("\nChoix invalide !!!")
                self.view.prompt_wait_enter()
        else:
            self.view.display_something("\nAucun Tournoi à continuer !!!")
            self.view.prompt_wait_enter()

    def start_tournament(self, tournament):
        '''
        lancement début d'un tournoi
        ajoute date de début et le round 1 si tournoi pas deja commencé
        '''
        players_list = tournament.players_list
        date = datetime.date.today().strftime("%d/%m/%Y")
        
        if tournament.start_date == "":
            tournament.start_date = date
            # creation du round 1
            round_one = Round(1)
            # creation de la liste des matchs ( joueurs choisis au hasard)
            random.shuffle(players_list)
            index = 0
            while True:
                try:
                    match = Match([players_list[index], 0], [players_list[index+1], 0])
                    round_one.matchs_list.append(match.to_json())
                except Exception:
                    break
                else:
                    index += 2
            tournament.rounds_list.append(round_one.to_json())
            tournament.save_tournament()
        self.view.underline_title_and_cls(f"{tournament.name} de {tournament.location} en {tournament.nb_rounds} Rounds , commencé le {tournament.start_date}")
        self.run_tournament(tournament)

    def run_tournament(self, tournament):
        """ Lance les rounds non finis d'un tournoi et éxécute les matchs non executés"""
        rounds_list = tournament.rounds_list
        for round_enum in rounds_list:
            #print(round_enum)
            act_round = Round(**round_enum)
            if act_round.finished is False:
                self.view.display_something(f"\nRound : {act_round.number} : ")
                matchs_list = act_round.matchs_list
                
                for match_enum in matchs_list:
                    act_match = Match(**match_enum)
                    if act_match.finished is False:
                        self.view.display_match(act_match.to_json())
                        choice = self.view.return_choice("\t\nRésultat du match ( victoire joueur 1 : 1 , victoire joueur 2 :2 , match nul : 0 ): ")
                        act_match.result(int(choice))
                        act_match.finished = True
                        print(act_match)

                self.view.prompt_wait_enter()

    '''
    Gestion des Rapports
    
    '''

    def players_tournament(self):
        # affiche la liste des joueurs d'un tournoi
        tournaments_list = DataList(FULL_PATH_TOURNAMENTS)
        self.view.underline_title_and_cls("Liste des Joueurs d'un Tournoi :")
        self.view.display_tournaments_list(tournaments_list)
        choice = self.view.return_choice("Entrer le Numéro de tournoi pour voir la liste des joueurs : ")
        try:
            choice = int(choice)
            tournament_choice = tournaments_list[choice-1]
            players_list = tournament_choice['players_list']
            tournament_name = tournament_choice['name']
            tournament_location = tournament_choice['location']
            title = f"{tournament_name} de {tournament_location}"
            self.view.display_players_list(players_list, title)
        except Exception:
            self.view.display_something("\nChoix invalide !!!")
        self.view.prompt_wait_enter()

    def rounds_matches_tournament(self):
        print("Liste des Tours et matchs d'un tournoi")
        self.view.prompt_wait_enter()