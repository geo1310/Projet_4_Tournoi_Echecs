import sys
import datetime
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match


class Controller:

    DATE = datetime.date.today().strftime("%d/%m/%Y")

    def __init__(self, view):
        # models
        self.view = view

    def run(self):
        
        self.main_menu()


    '''
    Gestion des Menus
    
    ''' 

    def main_menu(self):
        # menu principal
        menu_items = ["Menu principal du Club d'echec : ", {
            "Tournois": self.tournaments_menu,
            "Rapports": self.rapports_menu, 
            "Joueurs": self.players_menu,
            "Quitter": self.quit_menu
        }]
        self.run_menu(menu_items)
        
    def tournaments_menu(self):
        # menu tournois
        menu_items = ["Menu Tournois", {
            "Afficher la liste des Tournois": self.tournaments_list,
            "Créer/Lancer un Tournoi": self.create_tournament,
            "Continuer un tournoi en cours": self.continue_tournament,
            "Retour au menu principal": self.main_menu
        }]
        self.run_menu(menu_items)
    
    def players_menu(self):
        # menu joueurs
        menu_items = ["Menu Joueurs", {
            "Afficher la liste des Joueurs": self.players_list,
            "Ajouter un Joueur": self.add_player,
            "Supprimer un Joueur ": self.del_player,
            "Retour au menu principal": self.main_menu
        }]
        self.run_menu(menu_items)

    def rapports_menu(self):
        # menu rapports
        menu_items = ["Menu Rapports", {
            "Afficher la liste des Joueurs": self.players_list,
            "Liste des Tournois": self.tournaments_list,
            "Liste des Joueurs d'un Tournoi ": self.players_tournament,
            "Liste des Tours et Matchs d'un Tournoi ": self.rounds_matches_tournament,
            "Retour au menu principal": self.main_menu
        }]
        self.run_menu(menu_items)
            
    def quit_menu(self):
        sys.exit()

    def run_menu(self, menu_items):
        ''' gestion de l'affichage du menu et du choix utilisateur par rapport à menu_items'''
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
            if player_instance.create():
                self.view.display_something('Le joueur a bien été ajouté.')
            else:
                self.view.display_something('Le joueur est deja dans la liste des joueurs.')
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
        tournaments_list = Tournament.list('all')
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
                new_player.create()
                tournament.players_list.append(new_player.to_dict_tournament())
                index += 1
            elif len(tournament.players_list) % 2 == 0 and len(tournament.players_list) != 0:
                break
            else:
                self.view.display_something("\nLe nombre de joueurs d'un tournoi doit etre pair et au moins de deux joueurs !!!")
                self.view.prompt_wait_enter()
        tournament.save()
        if self.view.ask_question("Voulez-vous démarrer le tournoi "):
            self.start_tournament(tournament)
    
    def continue_tournament(self):
        # choix d'un tournoi à commencer parmis les tournois non finis
        tournaments_list_not_finished = Tournament.list('not_finished')
        if tournaments_list_not_finished != []:
            self.view.underline_title_and_cls("Liste des Tournois à effectuer :")
            self.view.display_tournaments_list(tournaments_list_not_finished)
            choice = self.view.return_choice("Entrer le Numéro de tournoi que vous souhaiter lancer : ")
            try:
                choice = int(choice)
                tournament_choice = tournaments_list_not_finished[choice-1]
                act_tournament = Tournament(**tournament_choice)
                self.start_tournament(act_tournament)
            except Exception:  # as e
                self.view.display_something("\nChoix invalide !!!")
                self.view.prompt_wait_enter()
        else:
            self.view.display_something("\nAucun Tournoi à continuer !!!")
            self.view.prompt_wait_enter()

    def start_tournament(self, act_tournament):
        '''
        lancement début d'un tournoi
        ajoute date de début et si tournoi pas commencé, crée le round 
        '''
        # verifie si le tournoi n'est pas encore commencé
        if act_tournament.start_date == "":
            act_tournament.start_date = Controller.DATE
            act_tournament.act_round = 1

        # verifie si le round est deja dans la base ou le cree
        if not any(round_info["number"] == act_tournament.act_round for round_info in act_tournament.rounds_list):
             act_round = Round(act_tournament.act_round)
             act_round.create_matchs_list(act_tournament.players_list)
             act_tournament.rounds_list.append(act_round.to_dict())

        act_tournament.save()

        self.run_tournament(act_tournament)
        
        
    def run_tournament(self, act_tournament):
        """ Execution d'un tournoi """

        rounds_list = act_tournament.rounds_list
        act_round_number = act_tournament.act_round

        self.view.underline_title_and_cls(f"{act_tournament.name} de {act_tournament.location} en {act_tournament.nb_rounds} Rounds , commencé le {act_tournament.start_date}")
        self.view.display_something(f"\nRound : {act_round_number}")

        # instancation et lancement du round en cours
        for i, round_enum in enumerate(rounds_list):
            if round_enum.get('number') == act_round_number:
                act_round = Round(**round_enum)
                act_round.start_date = Controller.DATE
                break

        rounds_list[i] = act_round.to_dict()
        act_tournament.save()

        # lancement des matchs
        act_matchs_list = act_round.matchs_list
        for match_enum in act_matchs_list:
            # instance du match actuel
            act_match = Match(**match_enum)
            if not act_match.finished():
                
                player_1 = Player.search('id', act_match.player_1[0]['id'])
                player_2 = Player.search('id', act_match.player_2[0]['id'])
                self.view.display_match(player_1, player_2)
                # execution du match
                result = self.view.return_choice("\n\tRésultat du match ( 1: Joueur 1 vainqueur, 0: match nul, 2: Joueur 2 vainqueur, autre: quitter le tournoi ) :")
                # validation d'un match
                if result.isdigit() and (result == '1' or result == '0' or result == '2'):
                    act_match.result(int(result))
                    # enregistrement des resultats
                    act_tournament.save()
                    
                else:
                    self.main_menu()
                    
        act_round.end_date = Controller.DATE
        rounds_list[i] = act_round.to_dict()
        act_tournament.players_list = sorted(act_tournament.players_list, key=lambda x: x["score"], reverse=True)
        act_tournament.save()
        if act_round_number < act_tournament.nb_rounds:
            act_tournament.act_round += 1
            act_tournament.save()
            self.start_tournament(act_tournament)
        else:
            act_tournament.end_date = Controller.DATE
            act_tournament.save()
            self.view.display_something("\nLe Tournoi est fini !!!")

        self.view.prompt_wait_enter()
        self.run()


    '''
    Gestion des Rapports
    
    '''

    def players_tournament(self):
        # affiche la liste des joueurs d'un tournoi
        tournament_choice = self.choice_tournament()
        tournament_name = tournament_choice['name']
        tournament_location = tournament_choice['location']
        title = f"Tournoi {tournament_name} de {tournament_location} : "
        # conversion des id en nom
        players_list_id = tournament_choice['players_list']
        players_list = []
        for player_tournament in players_list_id:
            player = Player.search("id", player_tournament['id'])
            players_list.append(player)
        self.view.display_players_list(players_list, title)
        self.view.prompt_wait_enter()

    def rounds_matches_tournament(self):
        # affiche les rounds et les matchs d'un tournoi
        tournament_choice = self.choice_tournament()
        rounds_list = tournament_choice['rounds_list']
        self.view.underline_title_and_cls(f"Liste des Rounds et des Matchs : Tournoi {tournament_choice['name']} de {tournament_choice['location']} du {tournament_choice['start_date']} au {tournament_choice['end_date']}")
        for round in rounds_list:
            self.view.display_something(f"\n\nRound {round['number']}  Date de début : {round['start_date']}  Date de fin : {round['end_date']}\n")
            matchs_list = round['matchs_list']
            for match in matchs_list:
                player_1 = Player.search("id", match['player_1'][0]['id']), match['player_1'][1]
                player_2 = Player.search("id", match['player_2'][0]['id']), match['player_2'][1]
                self.view.display_match_result(player_1, player_2)
        self.view.prompt_wait_enter()

    def choice_tournament(self): 
        # choisi un tournoi dans la liste des tournois et le retourne
        tournaments_list = Tournament.list('all')
        self.view.display_tournaments_list(tournaments_list)
        choice = self.view.return_choice("Entrer le Numéro de tournoi : ")
        try:
            choice = int(choice)
            tournament_choice = tournaments_list[choice-1]
        except Exception:
            self.view.display_something("\nChoix invalide !!!")
        else:
            return tournament_choice
