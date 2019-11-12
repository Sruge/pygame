import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, posX, posY):
        super(Bullet, self).__init__()
        self.size = size
        self.posX = posX
        self.posY = posY
        self.surf = pygame.Surface((size, size))
        self.rect = self.surf.get_rect(center=(posX, posY))
        self.vel = 4

    def update(self):
        self.rect.move_ip(self.vel, 0)
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > 1280:
            self.kill()
