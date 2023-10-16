import os


class View:

    def display_menu(self, title, menu_list):
        '''Affiche le menu d'apres un titre et une liste de menus'''
        self.underline_title_and_cls(title)
        # affichage du menu
        for i in range(len(menu_list)):
            print(f"\t{i+1} - {menu_list[i]}")
        choice = input("\nchoix :")
        return choice
   
    def print_players_list(self, players_list):
        '''Affiche la liste des joueurs à partir d'une liste'''
        self.underline_title_and_cls("Liste des Joueurs")
        for player in players_list:
            nom = player['first_name']
            prenom = player['last_name']
            date_naissance = player['birthday']
            print("Nom : {:<15} Prénom : {:<15} Date de Naissance : {:<15}".format(nom, prenom, date_naissance))

    def create_player(self, text):
        '''Demande les coordonnées d'un joueur'''
        self.underline_title_and_cls(text)
        first_name = input("Prénom du joueur : ")
        last_name = input("Nom du joueur : ")
        birthday = input("Date de naissance du joueur : ")

        return first_name, last_name, birthday

    def create_tournament(self):
        '''Demande les donnees pour la création d'un tournoi'''
        self.underline_title_and_cls("Création et lancement d'un Tournoi")
        name = input("Nom du Tournoi : ")
        location = input("Lieu du Tournoi : ")
        description = input("Description : ")
        nb_rounds = input("Nombre de Tours : ")

        return name, location, description, nb_rounds
    
    def ask_question(self, text):
        """pose une question avec le texte en argument"""
        print("\n" + text, end="")
        choice = input("o/n ? : ").lower()
        if choice == "n":
            return False
        return True

    def invalid_choice(self):
        '''affiche choix invalide'''
        print("\nChoix invalide. Veuillez réessayer.\n")

    def prompt_wait_enter(self):
        '''Pause de l'affichage, Attente de la touche Entrée'''
        print()
        input("Appuyer sur Entrée pour revenir au menu")
        return True
    
    def underline_title_and_cls(self, title):
        '''efface l'ecran et affiche le titre souligné'''
        os.system("cls")
        # affichage du titre du menu souligné
        souligne = '-'*len(title) + '\n'
        print('\n' + title)
        print(souligne)

    def print_something(self, text):
        print(text)


if __name__ == "__main__":
    view = View()
    view.main_menu()
