import pygame
import random

pygame.init()

WIDTH = 288
HEIGHT = 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(
    pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/yellowbird-upflap.png")
)
FPS = 60

WING = pygame.mixer.Sound("Python/Projects/Pygame/Flappy Bird/audio/wing.ogg")
HIT = pygame.mixer.Sound("Python/Projects/Pygame/Flappy Bird/audio/hit.ogg")

BACKGROUND_DAY = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/background-day.png"
)
GAME_OVER = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/gameover.png")
BASE = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/base.png")

YELLOW_BIRD_UPFLAP = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/yellowbird-upflap.png"
)
YELLOW_BIRD_MIDFLAP = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/yellowbird-midflap.png"
)
YELLOW_BIRD_DOWNFLAP = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/yellowbird-downflap.png"
)
YELLOW_BIRD = [YELLOW_BIRD_UPFLAP, YELLOW_BIRD_MIDFLAP, YELLOW_BIRD_DOWNFLAP]

PIPE = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/pipe-green.png")
INVERTED_PIPE = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/pipe-green-inverted.png"
)

BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 150)

BIRD_HIT = pygame.USEREVENT + 1


def draw_window(
    base_x,
    bird,
    n,
    BIRD_MOVEMENT,
    pipe_1_down,
    pipe_1_up,
    pipe_2_down,
    pipe_2_up,
    pipe_3_down,
    pipe_3_up,
):

    rotated_bird = pygame.transform.rotozoom(YELLOW_BIRD[n], BIRD_MOVEMENT * -10, 1)

    WIN.blit(BACKGROUND_DAY, (0, 0))
    WIN.blit(rotated_bird, (bird.x, bird.y))

    WIN.blit(PIPE, (pipe_1_down.x, pipe_1_down.y))
    WIN.blit(INVERTED_PIPE, (pipe_1_up.x, pipe_1_up.y))

    WIN.blit(PIPE, (pipe_2_down.x, pipe_2_down.y))
    WIN.blit(INVERTED_PIPE, (pipe_2_up.x, pipe_2_up.y))

    WIN.blit(PIPE, (pipe_3_down.x, pipe_3_down.y))
    WIN.blit(INVERTED_PIPE, (pipe_3_up.x, pipe_3_up.y))

    WIN.blit(BASE, (base_x, 450))
    pygame.display.update()


def handle_collision(
    bird,
    pipe_1_down,
    pipe_1_up,
    pipe_2_down,
    pipe_2_up,
    pipe_3_down,
    pipe_3_up,
):
    if bird.colliderect(pipe_1_down):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe_1_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe_2_down):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe_2_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe_3_down):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe_3_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.y >= 450:
        pygame.event.post(pygame.event.Event(BIRD_HIT))


def show_gameover():
    WIN.blit(GAME_OVER, (WIDTH / 2 - 192 / 2, HEIGHT / 2 - 42 / 2))
    pygame.display.update()
    pygame.time.delay(3000)
    main()


def main():
    bird = pygame.Rect(WIDTH / 2 - 60, HEIGHT / 2 - 50, 34, 24)

    base_x = 0
    run = True
    n = 0

    score = 0

    # *  pipe 1
    pipe_1_down = pygame.Rect(360, 400, 52, 320)
    pipe_1_down.y = random.randint(150, 370)

    pipe_1_up = pygame.Rect(360, 400, 52, 320)
    pipe_1_up.x = pipe_1_down.x
    pipe_1_up.y = pipe_1_down.y - 420

    # *  pipe 2
    pipe_2_down = pygame.Rect(497, 400, 52, 320)
    pipe_2_down.y = random.randint(150, 370)

    pipe_2_up = pygame.Rect(497, 400, 52, 320)
    pipe_2_up.x = pipe_2_down.x
    pipe_2_up.y = pipe_2_down.y - 420

    # *  pipe 3
    pipe_3_down = pygame.Rect(634, 400, 52, 320)
    pipe_3_down.y = random.randint(150, 370)

    pipe_3_up = pygame.Rect(634, 400, 52, 320)
    pipe_3_up.x = pipe_3_down.x
    pipe_3_up.y = pipe_3_down.y - 420

    GRAVITY = 0.1
    BIRD_MOVEMENT = 0

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    WING.play()
                    BIRD_MOVEMENT = 0
                    BIRD_MOVEMENT -= 2

            if event.type == BIRD_FLAP:
                n += 1
                if n > 2:
                    n = 0

            if event.type == BIRD_HIT:
                HIT.play()
                show_gameover()

        BIRD_MOVEMENT += GRAVITY
        bird.y += BIRD_MOVEMENT
        base_x -= 1
        if base_x <= -50:
            base_x = 0

        pipe_1_down.x -= 1
        pipe_1_up.x -= 1
        if pipe_1_down.x < -52:
            pipe_1_down.x = 360
            pipe_1_up.x = 360
            pipe_1_down.y = random.randint(145, 375)
            pipe_1_up.y = pipe_1_down.y - 410

        pipe_2_down.x -= 1
        pipe_2_up.x -= 1
        if pipe_2_down.x < -52:
            pipe_2_down.x = 360
            pipe_2_up.x = 360
            pipe_2_down.y = random.randint(145, 375)
            pipe_2_up.y = pipe_2_down.y - 410

        pipe_3_down.x -= 1
        pipe_3_up.x -= 1
        if pipe_3_down.x < -52:
            pipe_3_down.x = 360
            pipe_3_up.x = 360
            pipe_3_down.y = random.randint(145, 375)
            pipe_3_up.y = pipe_3_down.y - 410

        handle_collision(
            bird,
            pipe_1_down,
            pipe_1_up,
            pipe_2_down,
            pipe_2_up,
            pipe_3_down,
            pipe_3_up,
        )

        draw_window(
            base_x,
            bird,
            n,
            BIRD_MOVEMENT,
            pipe_1_down,
            pipe_1_up,
            pipe_2_down,
            pipe_2_up,
            pipe_3_down,
            pipe_3_up,
        )
    main()


if __name__ == "__main__":
    main()
