import os
import secrets


class Match:

    MATCH_WIN = 1
    MATCH_NUL = 0.5

    def __init__(self, player_1, player_2):
        self.id = secrets.token_hex(4)
        self.player_1 = player_1
        self.player_2 = player_2

    def __repr__(self):
        return f"{self.player_1} - {self.player_2}"

    def to_dict(self):
        return {
            'id': self.id,
            'player_1': self.player_1,
            'player_2': self.player_2
        }

    def result(self, number):
        if number == 1:
            self.player_1[1] = Match.MATCH_WIN
            self.player_1[0]['score'] += Match.MATCH_WIN
            self.player_2[1] = 0
            return True
        elif number == 2:
            self.player_1[1] = 0
            self.player_2[1] = Match.MATCH_WIN
            self.player_2[0]['score'] += Match.MATCH_WIN
            return True
        elif number == 0:
            self.player_1[1] = Match.MATCH_NUL
            self.player_1[0]['score'] += Match.MATCH_NUL
            self.player_2[1] = Match.MATCH_NUL
            self.player_2[0]['score'] += Match.MATCH_NUL
            return True
        else:
            return False

    def not_finished(self):
        if self.player_1[1] == 0 and self.player_2[1] == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    os.system('cls')
    match = Match(['player1', 0], ['player2', 0])
    match.result(2)
    print(match)