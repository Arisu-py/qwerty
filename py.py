import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('К щелчку')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    screen.fill("black")
    pygame.draw.circle(screen, ("red"), (251, 251), 20)
    k = 0
    x_pos = 251
    y_pos = 251
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                k = 1
                a = 1
                b = 1
                if x < x_pos and y < y_pos:
                    a = -1
                    b = -1
                elif x < x_pos and y > y_pos:
                    a = -1
                    b = 1
                elif x > x_pos and y < y_pos:
                    a = 1
                    b = -1

        if k == 1:
            if x_pos == x and y_pos == y:
                k = 0
            elif x_pos == x or y_pos == y:
                if x == x_pos:
                    y_pos += b
                else:
                    x_pos += a
                screen.fill("black")
                pygame.draw.circle(screen, "red", (x_pos, y_pos), 20)
            else:
                x_pos += a
                y_pos += b
                screen.fill("black")
                pygame.draw.circle(screen, "red", (x_pos, y_pos), 20)
            pygame.display.flip()

        clock.tick(fps)

pygame.quit()
