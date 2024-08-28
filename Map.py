# Handles the 2D Map

import pygame as pg

class Map:
    def __init__(self, dimension, win_size: int, grid_size:int , block_filled_color: tuple, block_empty_color: tuple, grid_col: tuple) -> None:
        self.dimension = dimension
        self.win_size = win_size
        self.grid_size = grid_size
        self.blk_filled_col = block_filled_color
        self.blk_empty_col = block_empty_color
        self.grid_col = grid_col
        # self.map = list((list(int) * dimension)) * dimension

        # The reason for not using a 2D list instead of a 1D list is while iteration through it we are going to need , nvm maybe this is bullsjit
        self.map = [int] * (dimension * dimension)

    def block_size(self) -> int:
        return (int) (self.win_size - (self.grid_size * (self.dimension + 1))) / self.dimension

    def draw(self, win: pg.Surface) -> None:
        # Draw the blocks
        for i in range(self.dimension * self.dimension):
            # Improve this

            y = int(i / self.dimension)
            x = i - (y * self.dimension)

            if self.map[i]:
                pg.draw.rect(win, self.blk_filled_col, (self.grid_size + x * (self.grid_size + self.block_size()), self.grid_size + y * (self.grid_size + self.block_size()), self.block_size(), self.block_size()))
            else:
                pg.draw.rect(win, self.blk_empty_col, (self.grid_size + x * (self.grid_size + self.block_size()), self.grid_size + y * (self.grid_size + self.block_size()), self.block_size(), self.block_size()))

        # Draw the grid
        for i in range(self.dimension + 1):
            # Draw the vertical grid
            pg.draw.rect(win, self.grid_col, (i * (self.grid_size + self.block_size()), 0, self.grid_size, self.win_size))

            # Draw the horizontal grid
            pg.draw.rect(win, self.grid_col, (0, i * (self.grid_size + self.block_size()), self.win_size, self.grid_size))