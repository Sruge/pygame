import pygame
from player import Player
from enemy import Enemy

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("bg.png").convert()

p1 = Player(50, 50, 0, 0)

fire_radius = 0

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(p1)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 10000)


running = True

while running:
    pygame.time.delay(50)

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
    for i in enemies:
        i.update()
    for i in p1.bullets:
        i.update()

    screen.fill((255, 255, 255))

    screen.blit(bg, (0, 0))
    for i in all_sprites:
        screen.blit(i.surf, i.rect)
    for i in p1.bullets:
        screen.blit(i.surf, i.rect)

    if pygame.sprite.spritecollideany(p1, enemies):
        #p1.kill()
        pass
    pygame.sprite.groupcollide(enemies, p1.bullets, dokilla=True,dokillb=True)

    pygame.display.flip()

pygame.quit()
