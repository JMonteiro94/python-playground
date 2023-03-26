from board import Board
from round import Round
import random


class Game(object):

    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_count = 1
        self.start_new_round()

    def start_new_round(self):
        try:
            round_word = self.get_word()
            self.round = Round(round_word, self.players[self.player_draw_ind], self)
            self.round_count += 1

            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()

            self.player_draw_ind += 1
        except Exception as e:
            print(e)
            self.end_game()

    def create_board(self):
        self.board = Board()
        self.board.clear()

    def player_guess(self, player, guess):
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind >= self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
            self.round.chat.update_chat(f"Player {player.get_name()} disconnected.")
        else:
            raise Exception("Player not in game")

        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        scores = {player: player.get_score() for player in self.players}
        return scores

    def skip(self):
        if self.round:
            new_round = self.round.skip()
            self.round.chat.update_chat(f"Player has votes to skip ({self.round.skips}/{len(self.players) - 2})")
            if new_round:
                self.round.chat.update_chat(f"Round has been skipped")
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round")

    def round_ended(self):
        self.round.chat.update_chat(f"Player has votes to skip ({self.round.skips}/{len(self.players) - 2})")
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, word):
        if not self.board:
            raise Exception("No board")
        self.board.update(x, y, word)

    def end_game(self):
        print(f'[GAME] Game {self.id} ended')
        for player in self.players:
            player.game = None

    def get_word(self):
        with open("words.txt", "r") as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)

            self.words_used.add(wrd)

            r = random.randint(0, len(words) - 1)
            return words[r].strip()
