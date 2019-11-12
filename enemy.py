import random
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("topf.png").convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(1280, 1480), random.randint(0, 600)))
        self.speed = random.randint(1, 2)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
