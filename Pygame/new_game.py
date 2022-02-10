import pygame

#!initialise pygame
pygame.init()

# *start a screen
screen = pygame.display.set_mode((800, 600))

# *title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

# *screen on loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # *RGB background values
    screen.fill((50, 25, 197))
    pygame.display.update()
