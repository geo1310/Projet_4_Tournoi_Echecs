from controllers.base import Controller
from views.base import View


def main():
    view = View()
    chess_app = Controller(view)
    chess_app.run()


if __name__ == "__main__":
    main()
