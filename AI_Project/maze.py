import pygame # type: ignore
from config import TILE_SIZE, BLUE, BLACK,GREEN

MAZE = [
    "###################",
    "#........#........#",
    "#.####.#.#.####.#.#",
    "#.#....#.#......#.#",
    "#.#.##.#####.##.#.#",
    "#.#.............#.#",
    "#.####.###.###.##.#",
    "#......#.....#....#",
    "#.######.###.######",
    "#........P........#",
    "#.####.#.#.####.#.#",
    "#.#....#.#......#.#",
    "#.#.##.#####.##.#.#",
    "#.#.............#.#",
    "#.####.###.###.##.#",
    "#......#.....#....#",
    "#.######.###.####.#",
    "#........#........#",
    "###################"
]

DOTS = set()
for y in range(len(MAZE)):
    for x in range(len(MAZE[0])):
        if MAZE[y][x] == '.' or MAZE[y][x] == 'P':
            DOTS.add((y, x))


def draw_grid(win):
    for y in range(len(MAZE)):
        for x in range(len(MAZE[0])):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if MAZE[y][x] == '#':
                pygame.draw.rect(win, BLUE, rect)
            else:
                pygame.draw.rect(win, BLACK, rect)
                if (y, x) in DOTS:
                    pygame.draw.circle(win, GREEN, rect.center, 4)