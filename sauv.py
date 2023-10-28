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



class DataList(list):
    # crée une liste d'apres un fichier json et peut la mélanger
    def __init__(self, full_path):
        self.full_path = full_path
        if os.path.exists(self.full_path):
            with open(self.full_path, "r") as fichier:
                data = json.load(fichier)
        else:
            data = []
        self.extend(data)

    def shuffle(self):
        random.shuffle(self)