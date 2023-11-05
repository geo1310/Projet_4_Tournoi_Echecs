import os
import secrets


class Round:
    def __init__(self, number, matchs_list=None, start_date='', end_date=''):
        self.id = secrets.token_hex(4)
        self.number = number
        self.matchs_list = matchs_list if matchs_list is not None else []
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.to_json()}"
   
    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'matchs_list': self.matchs_list,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
    
    def matchs_list(self, filter):
        if filter == 'all':
            return self.matchs_list
        elif filter == 'finished':
            matchs_list_finished = []
            for match in self.matchs_list:
                if match['finished'] is False:
                    matchs_list_finished.append(match)
            return matchs_list_finished


if __name__ == "__main__":
    os.system('cls')
