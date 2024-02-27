import pygame


class Board:
    # создание поля
    def __init__(self, board_width, board_height):
        self.width = board_width
        self.height = board_height
        self.board = [[None] * self.width for _ in range(self.height)]

        self.left = 50
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                r = (self.left + j * self.cell_size,
                     self.top + i * self.cell_size,
                     self.cell_size, self.cell_size)
                if self.board[i][j] is not None:
                    pygame.draw.rect(screen, self.board[i][j], r)
                pygame.draw.rect(screen, (255, 255, 255), r, 1)

    def get_cell(self, mouse_pos):
        row = (mouse_pos[1] - self.top) // self.cell_size
        col = (mouse_pos[0] - self.left) // self.cell_size
        return (row, col) if (0 <= row < self.height and
                              0 <= col < self.width) else None

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)

    running = True
    fps = 30
    clock = pygame.time.Clock()
    board = Board(4, 3)
    board.set_view(20, 50, 100)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.process_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()