import pygame
import numpy as np
import random


class Grid:

    def __init__(self, width, height, scale, offset):
        self.rows = width // 2
        self.columns = height // 2
        self.scale = scale
        self.offset = offset
        self.size = (self.rows, self.columns)
        self.grid = np.ndarray(shape=(self.size))

    def create_random_grid(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.grid[r][c] = random.randint(0, 1)


def main():
    width, height = 500, 500
    fps = 60
    scale = 40
    offset = 1

    grid = Grid(width, height, scale, offset)
    grid.create_random_grid()

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    while True:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

if __name__ == "__main__":
    main()
