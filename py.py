import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    r = 0
    v = 10  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    screen.fill("black")
    screen.fill(pygame.Color('green'), pygame.Rect(0, 0, 100, 100))
    x_pos = 0
    y_pos = 0
    k = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and k == 1:
                x = event.pos[0]
                y = event.pos[1]
                screen.fill("black")
                screen.fill(pygame.Color('green'), pygame.Rect(x + x_drow, y + y_drow, 100, 100))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if x_pos <= x <= x_pos + 100 and y_pos <= y <= y_pos + 100:
                    k = 1
                    x_drow = x_pos - x
                    y_drow = y_pos - y

            if event.type == pygame.MOUSEBUTTONUP and k == 1:
                x = event.pos[0]
                y = event.pos[1]
                x_pos = x + x_drow
                y_pos = y + y_drow
                k = 0

        r += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
