from models.base import Player, PlayersList, Match, Round, Tournament
import os
import json


class Controller:
    def __init__(self, view):
        # models
        self.view = view

    def run(self):
        while True:
            choice = self.view.main_menu()
            if choice == "0":
                print("\nAu revoir!\n")
                break
            elif choice == "1":
                self.tournaments_menu_choice()
            elif choice == "2":
                self.rapports_menu_choice()
            elif choice == "3":
                self.players_menu_choice()
            else:
                self.view.invalid_choice()

    def tournaments_menu_choice(self):
        while True:
            choice = self.view.tournaments_menu()
            if choice == "1":
                print("Créer/Lancer un tournoi")
            elif choice == "2":
                print("Continuer un tournoi en cours")
            elif choice == "3":
                break
            else:
                self.view.invalid_choice()

    def players_menu_choice(self):
        while True:
            choice = self.view.players_menu()
            if choice == "1":
                # affiche la liste des joueurs
                players_list = PlayersList('players.json')
                self.view.print_players_list(players_list)
                self.view.prompt_wait_enter()
                
            elif choice == "2":
                # ajoute un joueur
                print("Ajouter un joueur")
            elif choice == "3":
                break
            else:
                self.view.invalid_choice()

    def rapports_menu_choice(self):
        while True:
            choice = self.view.rapports_menu()
            if choice == "1":
                print("Afficher la liste des joueurs")
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
