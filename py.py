import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    k = 0
    v = 20  # пикселей в секунду
    fps = 60
    a = []
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                k += 1
                x_pos = list(event.pos)[0]
                y_pos = list(event.pos)[1]
                a.append([x_pos, y_pos, 0, 0])
        if k != 0:
            screen.fill((0, 0, 0))
            k1, k0 = -1, -1
            for i in a:
                k0 += 1
                for j in i:
                    pygame.draw.circle(screen, (255, 0, 0), (a[k0][0], a[k0][1]), 20)
                    if a[k0][0] == 0:
                        a[k0][2] = 1
                    if a[k0][1] == 0:
                        a[k0][3] = 1
                    if a[k0][0] == 800:
                        a[k0][2] = 0
                    if a[k0][1] == 400:
                        a[k0][3] = 0
                    if a[k0][2] == 0:
                        a[k0][0] -= 1
                    if a[k0][3] == 0:
                        a[k0][1] -= 1
                    if a[k0][2] == 1:
                        a[k0][0] += 1
                    if a[k0][3] == 1:
                        a[k0][1] += 1



        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
