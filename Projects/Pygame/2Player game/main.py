import pygame

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Shooter")
WHITE = (255, 255, 255)
FPS = 60
VEL = 5

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    "Python/Projects/Pygame/2Player game/assets/spaceship_yellow.png"
)
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)), 90
)


RED_SPACESHIP_IMAGE = pygame.image.load(
    "Python/Projects/Pygame/2Player game/assets/spaceship_red.png"
)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), 270
)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a]:  #!Left
        yellow.x -= VEL
    if key_pressed[pygame.K_d]:  #!Right
        yellow.x += VEL
    if key_pressed[pygame.K_w]:  #!Up
        yellow.y -= VEL
    if key_pressed[pygame.K_s]:  #!Down
        yellow.y += VEL


def handle_red_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT]:  #!Left
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT]:  #!Right
        red.x += VEL
    if key_pressed[pygame.K_UP]:  #!Up
        red.y -= VEL
    if key_pressed[pygame.K_DOWN]:  #!Down
        red.y += VEL


def main():

    red = pygame.Rect(700, 300, 55, 40)
    yellow = pygame.Rect(100, 300, 55, 40)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        handle_yellow_movement(key_pressed, yellow)
        handle_red_movement(key_pressed, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
