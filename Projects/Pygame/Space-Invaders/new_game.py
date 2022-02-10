import pygame

#!initialise pygame
pygame.init()

# *start a screen
screen = pygame.display.set_mode((800, 600))

# *title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

# *player
player_img = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# *enemy
enemy_img = pygame.image.load("enemy.png")
enemyX = 370
enemyY = 50
enemyX_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (enemyX, enemyY))


# *screen on loop
running = True
while running:

    # *RGB background values (red, green, blue)
    screen.fill((50, 25, 197))

    for event in pygame.event.get():

        # *exit checker
        if event.type == pygame.QUIT:
            running = False

        # *event check for movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.3
            if event.key == pygame.K_d:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()