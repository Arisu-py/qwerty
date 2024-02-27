import pygame


def draw(screen):
    screen.fill("white")
    for i in range(12):
        for j in range(11):
            if i % 2 == 0:
                screen.fill(pygame.Color('red'), pygame.Rect(j * 32, i * 17, 30, 15))
            else:
                screen.fill(pygame.Color('red'), pygame.Rect(j * 32 - 15, i * 17, 30, 15))
                screen.fill(pygame.Color('white'), pygame.Rect(15, 17 * i, 2, 15))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Кирпичи")
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
