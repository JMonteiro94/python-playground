import pygame.draw


class LeaderBoard(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 80
        self.players = []
        self.name_font = pygame.font.SysFont("comicsans", 30, bold=True)
        self.score_font = pygame.font.SysFont("comicsans", 20)
        self.rank_font = pygame.font.SysFont("comicsans", 50, bold=True)

    def draw(self, win):
        scores = [(player.name, player.score) for player in self.players]
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (255,255,255)
            else:
                color = (120,120,120)

            pygame.draw.rect(win, color, (self.x, self.y + i * self.HEIGHT_ENTRY, self.WIDTH, self.HEIGHT_ENTRY))

            rank = self.rank_font.render("#" + str(i + 1), 1, (0,0,0))
            win.blit(rank, (self.x + 10, self.y + i * self.HEIGHT_ENTRY + 10))

            name = self.name_font.render(score[0], 1, (0,0,0))
            win.blit(name, (self.x - name.get_width() / 2 + self.WIDTH / 2, self.y + i * self.HEIGHT_ENTRY + 20))

            score = self.name_font.render(score[0], 1, (0,0,0))
            win.blit(score, (self.x - name.get_width() / 2 + self.WIDTH / 2, self.y + i * self.HEIGHT_ENTRY + 40))


    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
