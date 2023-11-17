import datetime
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match


class TournamentManage:
    """
    Gestion des Tournois

    """

    DATE = datetime.date.today().strftime("%d/%m/%Y")

    def __init__(self, view):
        self.view = view

    def tournaments_list(self):
        # affiche la liste des tournois
        tournaments_list = Tournament.list("all")
        self.view.display_tournaments_list(tournaments_list)
        self.view.prompt_wait_enter()

    def create_tournament(self):
        # création d'un tournoi
        tournament_data = self.view.create_tournament()
        if tournament_data[1] != "" and tournament_data[2] != "":
            tournament = Tournament(*tournament_data)
            # ajout des joueurs au tournoi
            index = 1
            while True:
                title = (
                    f"Ajout du joueur {index} au tournoi {tournament.name} de {tournament.location}"
                    "( Valider des champs vides pour terminer)"
                )
                new_player = Player(*self.view.create_player(title))
                if new_player.last_name != "" and new_player.first_name != "":
                    new_player.create()
                    tournament.players_list.append(new_player.to_dict_tournament())
                    index += 1
                elif (
                    len(tournament.players_list) % 2 == 0
                    and len(tournament.players_list) != 0
                ):
                    break
                else:
                    self.view.display_something(
                        "\nLe nombre de joueurs d'un tournoi doit etre pair !!"
                    )
                    self.view.prompt_wait_enter()
            tournament.save()
            if self.view.ask_question("Voulez-vous démarrer le tournoi "):
                self.start_tournament(tournament)

    def continue_tournament(self):
        # choix d'un tournoi à commencer parmis les tournois non finis
        tournaments_list_not_finished = Tournament.list("not_finished")
        if tournaments_list_not_finished != []:
            self.view.underline_title_and_cls("Liste des Tournois à effectuer :")
            self.view.display_tournaments_list(tournaments_list_not_finished)
            choice = self.view.return_choice(
                "\nEntrer le Numéro de tournoi que vous souhaitez lancer : "
            )
            try:
                choice = int(choice)
                tournament_choice = tournaments_list_not_finished[choice - 1]
                act_tournament = Tournament(**tournament_choice)
                self.start_tournament(act_tournament)
            except Exception:  # as e
                self.view.display_something("\nChoix invalide !!!")
                self.view.prompt_wait_enter()
        else:
            self.view.display_something("\nAucun Tournoi à continuer !!!")
            self.view.prompt_wait_enter()

    def start_tournament(self, act_tournament):
        """lancement d'un tournoi"""

        # verifie si le tournoi n'est pas encore commencé
        if act_tournament.start_date == "":
            act_tournament.start_date = TournamentManage.DATE
            act_tournament.act_round = 1
            act_tournament.save()

        # verifie si le round est deja dans la base ou le cree
        if not any(
            round_info["number"] == act_tournament.act_round
            for round_info in act_tournament.rounds_list
        ):
            act_round = Round(act_tournament.act_round)
            act_round.create_matchs_list(act_tournament.players_list)
            act_tournament.rounds_list.append(act_round.to_dict())
            act_tournament.save()

        # exectution du tournoi
        rounds_list = act_tournament.rounds_list
        act_round_number = act_tournament.act_round
        stop_tournament = False
        title = (
            f"Tournoi : {act_tournament.name} de {act_tournament.location} en {act_tournament.nb_rounds} Rounds"
            f", commencé le {act_tournament.start_date}"
        )
        self.view.underline_title_and_cls(title)
        self.view.display_something(f"Round : {act_round_number}")

        # instancation et lancement du round en cours
        for i, round_enum in enumerate(rounds_list):
            if round_enum.get("number") == act_round_number:
                act_round = Round(**round_enum)
                act_round.start_date = TournamentManage.DATE
                break
        rounds_list[i] = act_round.to_dict()
        act_tournament.save()

        # lancement des matchs
        act_matchs_list = act_round.matchs_list
        for match_enum in act_matchs_list:
            # instance du match actuel
            act_match = Match(**match_enum)
            if not act_match.finished():
                player_1 = Player.search("id", act_match.player_1[0]["id"])
                player_2 = Player.search("id", act_match.player_2[0]["id"])
                self.view.display_match(player_1, player_2)
                # execution du match
                title = (
                    "\n\tRésultat du match ( 1: Joueur 1 vainqueur, 0: match nul"
                    ", 2: Joueur 2 vainqueur, autre: quitter le tournoi ) :"
                )
                result = self.view.return_choice(title)
                # validation d'un match
                if result.isdigit() and (
                    result == "1" or result == "0" or result == "2"
                ):
                    act_match.result(int(result))
                    act_tournament.update_score_players(act_match)
                    act_tournament.rounds_list[i] = act_round.to_dict()
                    # tri les joueurs par leurs scores
                    act_tournament.players_list = sorted(
                        act_tournament.players_list,
                        key=lambda x: x["score"],
                        reverse=True,
                    )
                    # enregistrement des resultats
                    act_tournament.save()
                else:
                    stop_tournament = True
                    break
        # fin d'un round
        if not stop_tournament:
            act_round.end_date = TournamentManage.DATE
            act_tournament.save()
            if act_round_number < act_tournament.nb_rounds:
                act_tournament.act_round += 1
                act_tournament.save()
                self.start_tournament(act_tournament)
            else:
                act_tournament.end_date = TournamentManage.DATE
                act_tournament.save()
                self.view.display_something("\nLe Tournoi est fini !!!")
                self.view.prompt_wait_enter()
                return None
