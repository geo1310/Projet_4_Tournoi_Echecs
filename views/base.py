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
            nom = player['nom']
            prenom = player['prenom']
            date_naissance = player['date_de_naissance']
            print("Nom : {:<15} Prénom : {:<15} Date de Naissance : {:<15}".format(nom, prenom, date_naissance))

    def create_player(self):
        '''Demande les coordonnées d'un joueur'''
        self.underline_title_and_cls("Ajout d'un Joueur")
        nom = input("Nom du joueur : ")
        prenom = input("Prénom du joueur : ")
        date_de_naissance = input("Date de naissance du joueur : ")

        return nom, prenom, date_de_naissance

    def create_tournament(self):
        '''Demande les donnees pour la création d'un tournoi'''
        self.underline_title_and_cls("Création et lancement d'un Tournoi")
        name = input("Nom du Tournoi : ")
        location = input("Lieu du Tournoi : ")
        rounds = input("Nombre de Tours : ")
        description = input("Description : ")

        return name, location, rounds, description

    def invalid_choice(self):
        '''affiche choix invalide'''
        print("\nChoix invalide. Veuillez réessayer.\n")

    def prompt_wait_enter(self):
        '''Pause de l'affichage, Attente de la touche Entréé'''
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


if __name__ == "__main__":
    view = View()
    view.main_menu()
