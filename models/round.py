import secrets

class Round:
    def __init__(self, number, matchs_list=None, start_date='', end_date=''):
        self.id = secrets.token_hex(4)
        self.number = number
        self.matchs_list = matchs_list if matchs_list else []
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.__dict__}"
    
    def to_dict(self):
        return self.__dict__
    
    def matchs_list(self, filter):
        """ retourne la liste des matchs selon un filtre ( all ou not_finished) """
        if filter == 'all':
            return self.matchs_list
        elif filter == 'not_finished':
            matchs_list_not_finished = []
            for match in self.matchs_list:
                if not match.finished():
                    matchs_list_not_finished.append(match)
            return matchs_list_not_finished
        
