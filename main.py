import pygame
from player import Player
from enemy import Enemy
from network import Network

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("bg.png").convert()
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 36)

network = Network()
p1 = network.get_player()

fire_radius = 0

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(p1)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 3000)


def redraw_window(screen, all_sprites, bullets):
    text = font.render("Lifes: {}".format(p1.lifes), True, (255, 255, 255))
    text2 = font.render("Kinetic Energy: {}".format(1 / 2 * (p1.velY ** 2 + p1.velX ** 2) // 1), True, (255, 255, 255))

    screen.blit(bg, (0, 0))
    screen.blit(text, (30, 30))
    screen.blit(text2, (30, 60))
    for i in all_sprites:
        i.draw(screen)
    for i in p1.bullets:
        i.draw(screen)
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                fire_radius += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                p1.fire(fire_radius)
                fire_radius = 0
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)

    # Update positions and velocities
    p1.update(pygame.key.get_pressed())
    network.send(p1)
    for i in enemies:
        i.update()
    for i in p1.bullets:
        i.update()

    if pygame.sprite.spritecollideany(p1, enemies):
        p1.lose_life()

    pygame.sprite.groupcollide(enemies, p1.bullets, dokilla=True, dokillb=True)
    redraw_window(screen, all_sprites, p1.bullets)

    clock.tick(30)
pygame.quit()
