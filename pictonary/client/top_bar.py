import pygame


class TopBar(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = ""
        self.round = 1
        self.max_round = 8
        self.round_font = pygame.font.SysFont("comicsans", 50)
        self.BORDER_THICKNESS = 5

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), self.BORDER_THICKNESS)
        txt = self.round_font.render("Round {round} of {max_round}".format(round=self.round, max_round=self.max_round), 1, (0, 0, 0))

        win.blit(txt, (self.x + 10, self.y + self.height / 2 - txt.get_height() / 2))

        txt = self.round_font.render(TopBar.underscore_text(self.word), 1, (0, 0, 0))
        win.blit(txt, (self.x + self.width / 2 - txt.get_width() / 2, self.y + self.height / 2 - txt.get_height() / 2 + 10))

    @staticmethod
    def underscore_text(text):
        new_str = ""

        for char in text:
            if char != " ":
                new_str += "_"
            else:
                new_str += " "
        return new_str

    def change_word(self, word):
        self.word = word

    def change_round(self, round):
        self.round = round
