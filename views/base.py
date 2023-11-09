import os


class View:

    def display_menu(self, title, menu_list):
        '''Affiche le menu d'apres un titre et une liste de menus et renvoie le choix'''
        self.underline_title_and_cls(title)
        # affichage du menu
        for menu in menu_list:
            print(f"\t{menu[0]} - {menu[1]}")
        choice = input("\nchoix :")
        return choice
   
    """ Affichage concernant les joueurs """

    def display_players_list(self, players_list, title_complement=''):
        '''Affiche la liste des joueurs à partir d'une liste par ordre alphabétique (nom)'''
        self.underline_title_and_cls("Liste des Joueurs : " + title_complement)
        sorted_players_list = sorted(players_list, key=lambda x: x["last_name"])
        index = 1
        for player in sorted_players_list:
            nom = player['last_name']
            prenom = player['first_name']
            date_naissance = player['birthday']
            print("{:<2} - Nom : {:<15} Prénom : {:<15} Date de Naissance : {:<15}".format(index, nom, prenom, date_naissance))
            index += 1

    def create_player(self, text):
        '''Demande les coordonnées d'un joueur'''
        self.underline_title_and_cls(text)
        last_name = input("Nom du joueur : ")
        first_name = input("Prénom du joueur : ")
        birthday = input("Date de naissance du joueur : ")

        return last_name, first_name, birthday

    """ Affichage concernant les Tournois """

    def display_tournaments_list(self, tournaments_list):
        '''Affiche la liste des tournois à partir d'une liste'''
        self.underline_title_and_cls("Liste des Tournois")
        index = 1
        for tournament in tournaments_list:
            print("{:<2}- Nom : {:<10} Lieu : {:<10} Nb de Rounds : {:<10} Round en cours : {:<10} Date de début : {:<15} Date de fin : {:<15}\n".format(index, tournament['name'], tournament['location'], tournament['nb_rounds'], tournament['act_round'], tournament['start_date'], tournament['end_date']))
            index += 1

    def create_tournament(self):
        '''Demande les donnees pour la création d'un tournoi'''
        self.underline_title_and_cls("Création et lancement d'un Tournoi")
        id = None
        name = input("Nom du Tournoi : ")
        location = input("Lieu du Tournoi : ")
        description = input("Description : ")
        nb_rounds = input("Nombre de Tours : ")

        return id, name, location, description, nb_rounds
    
    """ Affichage concernant les matchs """

    def display_match(self, player_1, player_2):
        print(f"\n\t{player_1[0]['last_name']} {player_1[0]['first_name']}  -  {player_2[0]['last_name']} {player_2[0]['first_name']}")
    
    def display_match_result(self, player_1, player_2):
        print("Joueur 1 : {:<10} {:<10} Score : {:<5}  Joueur 2 : {:<10} {:<10} Score : {:<5}".format(player_1[0]['last_name'], player_1[0]['first_name'], player_1[1], player_2[0]['last_name'], player_2[0]['first_name'], player_2[1]))


    """ Affichage divers """

    def ask_question(self, text):
        """pose une question avec le texte en argument - reponse oui ou non"""
        print("\n" + text, end="")
        choice = input("o/n ? : ").lower()
        if choice == "o":
            return True
        return False

    def return_choice(self, text):
        """ pose une question selon un texte et renvoie la réponse"""
        answer = input(text)
        return answer

    def invalid_choice(self):
        '''affiche choix invalide'''
        print("\nChoix invalide. Veuillez réessayer.\n")

    def prompt_wait_enter(self):
        '''Pause de l'affichage, Attente de la touche Entrée'''
        print()
        input("Appuyer sur Entrée")
        return True
    
    def underline_title_and_cls(self, title):
        '''efface l'ecran et affiche le titre souligné'''
        os.system("cls")
        # affichage du titre du menu souligné
        souligne = '-'*len(title) + '\n'
        print('\n' + title)
        print(souligne)

    def display_something(self, text):
        print(text)


if __name__ == "__main__":
    view = View()
    view.main_menu()
