class Match:
    MATCH_WIN = 1
    MATCH_NUL = 0.5

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def __repr__(self):
        return f"{self.player_1} - {self.player_2}"

    def to_dict(self):
        return {"player_1": self.player_1, "player_2": self.player_2}

    def result(self, number):
        if number == 0:
            self.player_1[1] = Match.MATCH_NUL
            self.player_2[1] = Match.MATCH_NUL

        elif number == 1:
            self.player_1[1] = Match.MATCH_WIN
            self.player_2[1] = 0

        elif number == 2:
            self.player_1[1] = 0
            self.player_2[1] = Match.MATCH_WIN

    def finished(self):
        if self.player_1[1] == 0 and self.player_2[1] == 0:
            return False
        else:
            return True
