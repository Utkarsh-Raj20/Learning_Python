import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Shooter")
WHITE = (255, 255, 255)
FPS = 60
VEL = 5
BORDER = pygame.Rect(448, 0, 5, HEIGHT)
BULLET_VEL = 7
MAX_BULLETS = 3

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

BULLET_FIRE_SOUND = pygame.mixer.Sound(
    "Python/Projects/Pygame/2Player game/assets/Gun+Silencer.mp3"
)
BULLET_HIT_SOUND = pygame.mixer.Sound(
    "Python/Projects/Pygame/2Player game/assets/Grenade+1.mp3"
)

FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

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
SPACE_IMAGE = pygame.image.load("Python/Projects/Pygame/2Player game/assets/space.png")
SPACE = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    health_of_yellow = FONT.render("HEALTH: " + str(yellow_health), 1, (255, 255, 255))
    WIN.blit(health_of_yellow, (0, 0))
    health_of_red = FONT.render("HEALTH: " + str(red_health), 1, (255, 255, 255))
    WIN.blit(health_of_red, (641, 0))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)

    pygame.display.update()


def handle_yellow_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x > 0:  #!Left
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x < 405:  #!Right
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y > 0:  #!Up
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y < 441:  #!Down
        yellow.y += VEL


def handle_red_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x > 455:  #!Left
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x < 860:  #!Right
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y > 0:  #!Up
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y < 441:  #!Down
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > 900:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    winning_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(
        winning_text,
        (
            WIDTH / 2 - winning_text.get_width() / 2,
            HEIGHT / 2 - winning_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(5000)
    main()


def main():
    red = pygame.Rect(700, 250, 55, 40)
    yellow = pygame.Rect(100, 250, 55, 40)

    yellow_bullets = []
    red_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    Bullet = pygame.Rect(
                        yellow.x + yellow.width / 2,
                        yellow.y + yellow.height / 2 - 2,
                        10,
                        5,
                    )
                    yellow_bullets.append(Bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    Bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(Bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

            winner_text = ""
            if red_health <= 0:
                winner_text = "YELLOW WINS!"
            if yellow_health <= 0:
                winner_text = "RED WINS!"
            if winner_text != "":
                draw_winner(winner_text)

        key_pressed = pygame.key.get_pressed()
        handle_yellow_movement(key_pressed, yellow)
        handle_red_movement(key_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()


if __name__ == "__main__":
    main()
