from models.player import Player
from models.tournament import Tournament


class RapportManage:
    """
    Gestion des Rapports

    """

    def __init__(self, view):
        self.view = view

    def players_tournament(self):
        # affiche la liste des joueurs d'un tournoi
        tournament_choice = self.choice_tournament()
        if tournament_choice:
            tournament_name = tournament_choice["name"]
            tournament_location = tournament_choice["location"]
            title = f"Tournoi {tournament_name} de {tournament_location} : "
            # conversion des id en nom
            players_list_id = tournament_choice["players_list"]
            players_list = []
            for player_tournament in players_list_id:
                player = Player.search("id", player_tournament["id"])
                players_list.append(player)
            self.view.display_players_list(players_list, title)
            self.view.prompt_wait_enter()

    def players_classification(self):
        # affiche le classement des joueurs d'un tournoi
        tournament_choice = self.choice_tournament()
        if tournament_choice:
            title = f"{tournament_choice['name']} de {tournament_choice['location']} qui a eu lieu du {tournament_choice['start_date']} au {tournament_choice['end_date'] if tournament_choice['end_date'] != '' else '...'}"
            # conversion des id en nom
            players_list_id = tournament_choice["players_list"]
            players_list = []
            for player_tournament in players_list_id:
                player = (
                    Player.search("id", player_tournament["id"]),
                    player_tournament["score"],
                )
                players_list.append(player)
            self.view.display_players_list_classification(players_list, title)
            self.view.prompt_wait_enter()

    def rounds_matches_tournament(self):
        # affiche les rounds et les matchs d'un tournoi
        tournament_choice = self.choice_tournament()
        if tournament_choice:
            rounds_list = tournament_choice["rounds_list"]
            self.view.underline_title_and_cls(
                f"Liste des Rounds et des Matchs : Tournoi {tournament_choice['name']} de {tournament_choice['location']} du {tournament_choice['start_date']} au {tournament_choice['end_date'] if tournament_choice['end_date'] != '' else '...'}"
            )
            for round in rounds_list:
                self.view.display_something(
                    f"\nRound {round['number']}  Date de début : {round['start_date']}  Date de fin : {round['end_date']}\n"
                )
                matchs_list = round["matchs_list"]
                for match in matchs_list:
                    player_1 = (
                        Player.search("id", match["player_1"][0]["id"]),
                        match["player_1"][1],
                    )
                    player_2 = (
                        Player.search("id", match["player_2"][0]["id"]),
                        match["player_2"][1],
                    )
                    self.view.display_match_result(player_1, player_2)
            self.view.prompt_wait_enter()

    def choice_tournament(self):
        # choisi un tournoi dans la liste des tournois et le retourne
        tournaments_list = Tournament.list("all")
        self.view.display_tournaments_list(tournaments_list)
        if tournaments_list != []:
            choice = self.view.return_choice("\nEntrer le Numéro de tournoi : ")
            try:
                choice = int(choice)
                tournament_choice = tournaments_list[choice - 1]
            except Exception:
                self.view.display_something("\nChoix invalide !!!")
            else:
                return tournament_choice
        else:
            self.view.display_something("\nAucun Tournoi enregistré !!!")
            self.view.prompt_wait_enter()
