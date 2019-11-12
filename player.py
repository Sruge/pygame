import pygame
from bullet import Bullet

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self, lifes, posX, posY, velX, velY):
        super(Player, self).__init__()
        self.lifes = lifes
        self.velX = velX
        self.velY = velY
        self.invulnerable = 0
        self.surf = pygame.image.load("rose.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(posX, posY))
        self.airtime = 0
        self.bullets = pygame.sprite.Group()

    def draw(self, screen):
        if self.invulnerable > 0:
            surf = pygame.image.load("hirsch.png").convert()
            surf.set_colorkey((0, 0, 0), RLEACCEL)
            rect = surf.get_rect(
                center=((self.rect.left + self.rect.right) // 2, (self.rect.top + self.rect.bottom) // 2))
            screen.blit(surf, rect)
        else:
            screen.blit(self.surf, self.rect)

    def fire(self, size):
        bullet = Bullet(size, self.rect.left + 23, self.rect.bottom - 32)
        self.bullets.add(bullet)

    def lose_life(self):
        if self.invulnerable <= 0:
            if self.lifes <= 1:
                self.lifes = 0
                self.kill()
            else:
                self.lifes -= 1
                self.invulnerable = 30
                self.velX = 0

    def update(self, pressed_keys):
        self.airtime += 0.2
        self.velX *= 0.9
        self.rect.move_ip(self.velX, self.velY)
        if pressed_keys[K_UP]:
            self.velY -= 2
        if pressed_keys[K_DOWN]:
            self.velY += 2
        if pressed_keys[K_LEFT]:
            self.velX -= 4
        if pressed_keys[K_RIGHT]:
            self.velX += 4
        self.velY += self.airtime

        if self.rect.left < 0:
            self.rect.left = 0
            self.velX = -self.velX * 0.2
        if self.rect.right > 1280:
            self.rect.right = 1280
            self.velX = -self.velX * 0.2
        if self.rect.top < 0:
            self.rect.top = 0
            self.velY = -self.velY * 0.2
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.velY = -self.velY * 0.2
            self.airtime = 0

        if self.invulnerable > 0:
            self.invulnerable -= 1
