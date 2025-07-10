import pygame  # type: ignore
from config import TILE_SIZE
from path_finding import find_path, get_strategy

class Ghost:
    def __init__(self, row, col, strategy=None):
        self.row = row
        self.col = col
        self.move_counter = 0
        self.move_delay = 5
        self.frame = 0
        self.frame_count = 0
        self.strategy = strategy
        self.images = [
            pygame.transform.scale(pygame.image.load("assets/ghost1.png"), (TILE_SIZE, TILE_SIZE)),
            pygame.transform.scale(pygame.image.load("assets/ghost2.png"), (TILE_SIZE, TILE_SIZE))
        ]

    def chase(self, target_pos, maze):
        self.move_counter += 1
        if self.move_counter >= self.move_delay:
            current_strategy = self.strategy if self.strategy else get_strategy()
            
            path = find_path((self.row, self.col), target_pos, maze, strategy=current_strategy)
            if path and len(path) > 1:
                self.row, self.col = path[1]
            self.move_counter = 0

    def set_strategy(self, strategy):
        self.strategy = strategy

    def draw(self, win):
        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame = (self.frame + 1) % 2
            self.frame_count = 0
        image = self.images[self.frame]
        win.blit(image, (self.col * TILE_SIZE, self.row * TILE_SIZE))