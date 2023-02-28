from .game import Game


class Player(object):
    def __init__(self, ip, name):
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        self.game = game

    def update_score(self, x):
        self.score += x

    def guess(self, word):
        return self.game.player_guess(self, word)

    def disconnect(self):
        self.game.player_disconnected(self)

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score