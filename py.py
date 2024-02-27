import pygame
import colorsys


def draw(screen):
    screen.fill("black")
    color = (255, 255, 255)
    color0 = pygame.Color(color)
    color1 = pygame.Color(color)
    color2 = pygame.Color(color)
    color0.hsva = (Hue, 100, 100)
    color1.hsva = (Hue, 100, 75)
    color2.hsva = (Hue, 100, 50)
    pygame.draw.polygon(screen, color0,
                        [((300 - W) // 2, (300 - W) // 2), ((300 - W) // 2 + W // 2, (300 - W) // 2 - W // 2),
                         ((300 - W) // 2 + W // 2 * 3, (300 - W) // 2 - W // 2), ((300 - W) // 2 + W, (300 - W) // 2)])
    screen.fill(pygame.Color(color1), pygame.Rect((300 - W) // 2, (300 - W) // 2, W, W))
    pygame.draw.polygon(screen, color2,
                        [((300 - W) // 2 + W // 2 * 3, (300 - W) // 2 + W // 2),
                         ((300 - W) // 2 + W // 2 * 3, (300 - W) // 2 + W // 2), (W + (300 - W) // 2, (300 - W) // 2 + W),
                         ((300 - W) // 2 + W, (300 - W) // 2), ((300 - W) // 2 + W // 2 * 3, (300 - W) // 2 - W // 2)])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Куб")
    try:
        W, Hue = map(int, input().split())
        if W % 4 != 0 or Hue > 360 or Hue < 0 or W > 100:
            raise ValueError
    except ValueError:
        print("Неправильный формат ввода")
        pygame.quit()
    else:
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
