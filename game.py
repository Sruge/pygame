import pygame
from network import Network
import time
import pickle
from player import Player
from information import Information


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.hight = 600
        self.screen = pygame.display.set_mode((self.width, self.hight))
        self.bg = pygame.image.load("bg.png").convert()
        self.font = pygame.font.SysFont("comicsansms", 28)
        self.clock = pygame.time.Clock()
        self.network = Network()
        print("zack")
        self.player = Player(self.network.playerInfo, 5, 0, 0)
        print("zack")
        self.players = pygame.sprite.Group()
        self.playersIds = []
        self.players.add(self.player)
        self.playersIds.append(self.player.id)
        self.enemies = pygame.sprite.Group()
        self.run()

    def draw(self):
        text = self.font.render("Lifes: {}".format(11), True, (255, 255, 255))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(text, (30, 30))
        for player in self.players:
            player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.flip()

    def run(self):
        running = True

        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.update()
            info = self.player.get_info()
            data = pickle.loads(self.network.send(pickle.dumps(info)))
            #print(data)
            self.enemies = []
            for info in data:
                if info.count == self.player.id:
                    pass
                else:
                    self.enemies.append(Player(info, 5, 1, 0))

            # print(data)
            self.draw()

        pygame.quit()
