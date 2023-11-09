from controllers.menu import MenuManage
from controllers.player import PlayerManage
from controllers.rapport import RapportManage
from controllers.tournament import TournamentManage
from views.base import View


def main():
    view = View()
    rapport_manage = RapportManage(view)
    player_manage = PlayerManage(view)
    tournament_manage = TournamentManage(view)
    chess_app = MenuManage(view, player_manage, rapport_manage, tournament_manage)
    chess_app.run()


if __name__ == "__main__":
    main()
