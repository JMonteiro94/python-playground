import time as t
from _thread import *
from chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, players, game):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.game = game
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self):
        self.skips += 1
        if self.skips > len(self.players) - 1:
            self.skips = 0
            return True
        return False

    def get_scores(self):
        return self.player_scores

    def get_score(self, player):
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("Player not in game")

    def time_thread(self):
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round()

    def guess(self, player, wrd):
        """
        :returns bool if player guess correctly
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)

    def player_left(self, player):
        if player in self.player_scores:
            del self.player_scores[player]
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        if player == self.player_drawing:
            self.end_round("Drawing player left")

    def end_round(self, msg):
        for player in self.players:
            player.update_score(self.player_scores[player])
        self.game.round_ended()
