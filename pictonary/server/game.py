
class Game(object):

    def __inint__(self, id, players):
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = None

    def player_guess(self, player, guess):
        pass

    def player_disconnected(self, player):
        pass

    def skip(self):
        pass

    def round_ended(self):
        pass

    def update_board(self):
        pass
