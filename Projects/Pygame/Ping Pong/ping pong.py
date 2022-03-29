import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60
White = (255, 255, 255)
VEL = 7


class Player:
    def __init__(self, x) -> None:
        self.x = x
        self.y = 200
        self.body = pygame.Rect(self.x, self.y, 15, 100)

    def draw(self):
        self.body = pygame.Rect(self.x, self.y, 15, 100)
        pygame.draw.rect(WIN, White, self.body)


def draw_window(one, two):
    WIN.fill((0, 0, 0))

    one.draw()
    two.draw()

    pygame.display.update()


def handle_player_one(key, one):
    if key[pygame.K_w] and one.body.y >= 5:
        one.y -= VEL
    if key[pygame.K_s] and one.body.bottom <= HEIGHT - 5:
        one.y += VEL


def handle_player_two(key, two):
    if key[pygame.K_UP] and two.body.y >= 5:
        two.y -= VEL
    if key[pygame.K_DOWN] and two.body.bottom <= HEIGHT - 5:
        two.y += VEL


def main() -> None:

    player_two = Player(680)
    player_one = Player(5)

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key_pressed = pygame.key.get_pressed()

        handle_player_two(key_pressed, player_two)
        handle_player_one(key_pressed, player_one)
        draw_window(player_one, player_two)
        pygame.display.update()
        
    pygame.display.quit()


if __name__ == "__main__":
    main()
