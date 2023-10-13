import os


class View:

    def main_menu(self):
        # menu principal
        os.system("cls")
        print()
        print("Menu Principal :\n")
        print("\t0 - Quitter")
        print("\t1 - Tournois")
        print("\t2 - Rapports")
        print("\t3 - Joueurs")
        print()
        choice = input("choix :")
        return choice

    def tournaments_menu(self):
        # menu tournois
        os.system("cls")
        print()
        print("Menu Tournois :\n")
        print("\t1 - Créer/Lancer un Tournoi")
        print("\t2 - Continuer un tournoi en cours")
        print("\t3 - Retour au menu principal")
        print()
        choice = input("choix :")
        return choice

    def players_menu(self):
        # menu joueurs
        os.system("cls")
        print()
        print("Menu Joueurs :\n")
        print("\t1 - Afficher la liste des joueurs")
        print("\t2 - Ajouter un joueur")
        print("\t3 - Retour au menu principal")
        print()
        choice = input("choix :")
        return choice
    
    def rapports_menu(self):
        # menu rapports
        os.system("cls")
        print()
        print("Menu Rapports :\n")
        print("\t1 - Afficher la liste des joueurs")
        print("\t2 - Liste des tournois")
        print("\t3 - Nom et Date d'un tournoi")
        print("\t4 - Liste des Joueurs d'un tournoi")
        print("\t5 - Liste des Tours et matchs d'un tournoi")
        print("\t6 - Retour au menu principal")
        print()
        choice = input("choix :")
        return choice

    def invalid_choice(self):
        print("\nChoix invalide. Veuillez réessayer.\n")

    def prompt_wait_enter(self):
        """Request to return menu"""
        print()
        input("Appuyer sur Entrée pour revenir au menu")
        return True

    def print_players_list(self, players_list):
        texte = '\nListe des joueurs :'
        souligne = '-'*len(texte) + '\n'
        print(texte)
        print(souligne)
        for player in players_list:
            nom = player['nom']
            prenom = player['prenom']
            date_naissance = player['date_de_naissance']
            print("Nom : {:<15} Prénom : {:<15} Date de Naissance : {:<15}".format(nom, prenom, date_naissance))


if __name__ == "__main__":
    view = View()
    view.main_menu()
