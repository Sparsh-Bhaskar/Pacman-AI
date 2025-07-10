import pygame # type: ignore
from config import TILE_SIZE
from maze import DOTS

class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = 'right'
        self.frame = 0
        self.frame_count = 0
        self.images = {
            'up': [
                pygame.transform.scale(pygame.image.load("assets/pacman_up1.png"), (TILE_SIZE, TILE_SIZE)),
                pygame.transform.scale(pygame.image.load("assets/pacman_up2.png"), (TILE_SIZE, TILE_SIZE))
            ],
            'down': [
                pygame.transform.scale(pygame.image.load("assets/pacman_down1.png"), (TILE_SIZE, TILE_SIZE)),
                pygame.transform.scale(pygame.image.load("assets/pacman_down2.png"), (TILE_SIZE, TILE_SIZE))
            ],
            'left': [
                pygame.transform.scale(pygame.image.load("assets/pacman_left1.png"), (TILE_SIZE, TILE_SIZE)),
                pygame.transform.scale(pygame.image.load("assets/pacman_left2.png"), (TILE_SIZE, TILE_SIZE))
            ],
            'right': [
                pygame.transform.scale(pygame.image.load("assets/pacman_right1.png"), (TILE_SIZE, TILE_SIZE)),
                pygame.transform.scale(pygame.image.load("assets/pacman_right2.png"), (TILE_SIZE, TILE_SIZE))
            ]
        }
        self.eat_sound = pygame.mixer.Sound("assets/eating.wav")

    def move(self, dx, dy, maze):
        if dx == -1: self.direction = 'up'
        elif dx == 1: self.direction = 'down'
        elif dy == -1: self.direction = 'left'
        elif dy == 1: self.direction = 'right'

        new_row = self.row + dx
        new_col = self.col + dy
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
            self.row = new_row
            self.col = new_col
            if (self.row, self.col) in DOTS:
                DOTS.remove((self.row, self.col))
                if not pygame.mixer.Channel(1).get_busy():
                    pygame.mixer.Channel(1).play(self.eat_sound)


    def draw(self, win):
        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame = (self.frame + 1) % 2
            self.frame_count = 0
        image = self.images[self.direction][self.frame]
        win.blit(image, (self.col * TILE_SIZE, self.row * TILE_SIZE))