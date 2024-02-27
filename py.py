import pygame


def draw(screen):
    screen.fill("black")
    for i in range(n):
        pygame.draw.ellipse(screen, "white", (0, (300 // n) * i // 2, 300, 300 - i * 300 // n), 1)
        pygame.draw.ellipse(screen, "white", ((300 // n) * i // 2, 0, 300 - i * 300 // n, 300), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Сетка")
    size = width, height = 300, 300
    try:
        n = int(input())
    except ValueError:
        print("Неправильный формат ввода")
        pygame.quit()
    else:
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
