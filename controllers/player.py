from models.player import Player


class PlayerManage:
    '''
    Gestion des Joueurs

    '''

    def __init__(self, view):
        self.view = view

    def players_list(self):
        # affiche la liste des joueurs
        players_list = Player.list()
        self.view.display_players_list(players_list)
        self.view.prompt_wait_enter()

    def add_player(self):
        # ajoute un joueur
        player = self.view.create_player(
            "Ajout d'un Joueur dans la base de données ( champs vide pour revenir au menu)"
            )
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
        if player[0] != '' and player[1] != '':
            player_instance = Player(player[0], player[1], player[2])
            self.view.display_something(player_instance.delete())
        else:        
            self.view.display_something("\nVeuillez renseigner au minimum le nom et le prénom du joueur.")
        self.view.prompt_wait_enter()
