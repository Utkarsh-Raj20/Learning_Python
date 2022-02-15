import pygame

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Shooter")
WHITE = (255, 255, 255)
FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    "Python/Projects/Pygame/2Player game/assets/spaceship_yellow.png"
)
YELLOW_SPACESHIP = pygame.transform(YELLOW_SPACESHIP_IMAGE)
RED_SPACESHIP_IMAGE = pygame.image.load(
    "Python/Projects/Pygame/2Player game/assets/spaceship_red.png"
)


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
