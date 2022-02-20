from tkinter import Menu
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
POINT = pygame.mixer.Sound("Python/Projects/Pygame/Flappy Bird/audio/point.ogg")

BACKGROUND_DAY = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/background-day.png"
)
GAME_OVER = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/gameover.png")
BASE = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/base.png")
MENU = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/message.png")

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

PIPE_IMG = pygame.image.load("Python/Projects/Pygame/Flappy Bird/assets/pipe-green.png")
INVERTED_PIPE_IMG = pygame.image.load(
    "Python/Projects/Pygame/Flappy Bird/assets/pipe-green-inverted.png"
)

BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 150)

BIRD_HIT = pygame.USEREVENT + 1
font = pygame.font.Font("Python/Projects/Pygame/Flappy Bird/assets/04B_19.ttf", 64)
font2 = pygame.font.Font("Python/Projects/Pygame/Flappy Bird/assets/04B_19.ttf", 30)


class Pipe:
    def __init__(self, x) -> None:
        self.x = x
        self.y = random.randint(200, 380)
        self.width = 40
        self.height = 320
        self.rectangle_down = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rectangle_up = pygame.Rect(self.x, self.y - 420, self.width, self.height)

    def draw(self):
        self.rectangle_down = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rectangle_up = pygame.Rect(self.x, self.y - 420, self.width, self.height)

        WIN.blit(PIPE_IMG, (self.rectangle_down.x, self.rectangle_down.y))
        WIN.blit(INVERTED_PIPE_IMG, (self.rectangle_up.x, self.rectangle_up.y))


def draw_window(base_x, bird, n, BIRD_MOVEMENT, pipe1, pipe2, pipe3, score):
    rotated_bird = pygame.transform.rotozoom(YELLOW_BIRD[n], BIRD_MOVEMENT * -10, 1)

    WIN.blit(BACKGROUND_DAY, (0, 0))
    WIN.blit(rotated_bird, (bird.x, bird.y))
    pipe1.draw()
    pipe2.draw()
    pipe3.draw()
    WIN.blit(BASE, (base_x, 450))

    points = font.render(str(score), True, (255, 255, 255))
    WIN.blit(points, (30, 30))
    pygame.display.update()


def handle_collision(bird, pipe1, pipe2, pipe3):
    if bird.colliderect(pipe1.rectangle_down) or bird.colliderect(pipe1.rectangle_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe2.rectangle_down) or bird.colliderect(pipe2.rectangle_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.colliderect(pipe3.rectangle_down) or bird.colliderect(pipe3.rectangle_up):
        pygame.event.post(pygame.event.Event(BIRD_HIT))
    if bird.y >= 450:
        pygame.event.post(pygame.event.Event(BIRD_HIT))


def show_gameover(high_score, score):

    if score > high_score:
        with open("Python/Projects/Pygame/Flappy Bird/High Score.txt", "w") as f:
            f.write(str(score))

    WIN.blit(GAME_OVER, (WIDTH / 2 - 192 / 2, HEIGHT / 2 - 42 / 2))
    pygame.display.update()
    pygame.time.delay(3000)

    main()


def getHighScore():
    with open("Python/Projects/Pygame/Flappy Bird/High Score.txt", "r") as f:
        return f.read()


def main():
    bird = pygame.Rect(WIDTH / 2 - 60, HEIGHT / 2 - 50, 34, 24)

    base_x = 0
    run = True
    n = 0

    score = 0
    speed = 1

    high_score = int(getHighScore())

    pipe1 = Pipe(360)
    pipe2 = Pipe(497)
    pipe3 = Pipe(634)

    GRAVITY = 0.1
    BIRD_MOVEMENT = 0

    show_menu = True

    clock = pygame.time.Clock()
    while run:
        pygame.init()
        clock.tick(FPS)
        if show_menu:
            WIN.blit(BACKGROUND_DAY, (0, 0))
            WIN.blit(MENU, (WIDTH / 2 - 184 / 2, HEIGHT / 2 - 267 // 2))
            points = font2.render(
                "Highscore: " + str(high_score), True, (255, 255, 255)
            )
            WIN.blit(points, (52, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_menu = False
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break

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
                    show_gameover(high_score, score)

            if bird.x == pipe1.x + 52:
                POINT.play()
                score += 1
            if bird.x == pipe2.x + 52:
                POINT.play()
                score += 1
            if bird.x == pipe3.x + 52:
                POINT.play()
                score += 1

            BIRD_MOVEMENT += GRAVITY
            bird.y += BIRD_MOVEMENT
            base_x -= speed
            if base_x <= -50:
                base_x = 0

            pipe1.x -= speed
            if pipe1.x < -52:
                pipe1.x = 360
                pipe1.y = random.randint(200, 380)

            pipe2.x -= speed
            if pipe2.x < -52:
                pipe2.x = 360
                pipe2.y = random.randint(200, 380)

            pipe3.x -= speed
            if pipe3.x < -52:
                pipe3.x = 360
                pipe3.y = random.randint(200, 380)

            handle_collision(bird, pipe1, pipe2, pipe3)
            draw_window(base_x, bird, n, BIRD_MOVEMENT, pipe1, pipe2, pipe3, score)
            pygame.display.update()
    main()


if __name__ == "__main__":
    main()
