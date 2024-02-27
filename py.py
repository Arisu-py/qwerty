import pygame


def draw(screen):
    if n % 2 == 0:
        color_fill = "black"
        color = "white"
    else:
        color_fill = "white"
        color = "black"
    screen.fill(color_fill)
    width = a // n
    for i in range(n):
        k = i % 2
        for j in range(k, n, 2):
            screen.fill(pygame.Color(color), pygame.Rect(j * width, i * width, width, width))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Шахматная клетка")
    try:
        a, n = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        pygame.quit()
    else:
        size = width, height = a, a
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
