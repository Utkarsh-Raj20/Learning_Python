import pygame

pygame.init()

pygame.display.set_mode((500, 500))
pygame.display.set_caption("Start-GameOver")
pygame.display.set_icon(
    pygame.image.load("Python/Projects/pygame/Space-Invaders/assets/enemy2.png")
)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
