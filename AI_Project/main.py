import pygame
from maze import MAZE, draw_grid, DOTS
from pacman import Pacman
from ghost import Ghost
from config import WIDTH, HEIGHT, FPS, TILE_SIZE, BLACK, BLUE
import path_finding as pf

pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man AI")
clock = pygame.time.Clock()
maze = MAZE

pacman = Pacman(9, 9)
ghosts = [
    Ghost(1, 2),   # Default ghost using global strategy
    Ghost(1, 17, 'a_star'),  # Ghost with fixed A* strategy
]

font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
game_over = False
win_game = False

game_over_sound = pygame.mixer.Sound("assets/gameover.wav")
win_sound = pygame.mixer.Sound("assets/win.wav")

# Set initial strategy
current_strategy = pf.get_strategy()

def handle_strategy_key(key):
    global current_strategy
    strategy_changed = False
    
    if key == pygame.K_1:
        pf.set_strategy('bfs')
        current_strategy = 'bfs'
        strategy_changed = True
        print("Switched to BFS")
    elif key == pygame.K_2:
        pf.set_strategy('dfs')
        current_strategy = 'dfs'
        strategy_changed = True
        print("Switched to DFS")
    elif key == pygame.K_3:
        pf.set_strategy('a_star')
        current_strategy = 'a_star'
        strategy_changed = True
        print("Switched to A*")
    elif key == pygame.K_4:
        pf.set_strategy('hill_climbing')
        current_strategy = 'hill_climbing'
        strategy_changed = True
        print("Switched to Hill Climbing")
    elif key == pygame.K_5:
        pf.set_strategy('dfs_id')
        current_strategy = 'dfs_id'
        strategy_changed = True
        print('Switched to DFS_ID')
        
    # Force redraw when strategy changes to immediately update the display
    if strategy_changed:
        # Clear the screen to prevent text overlap
        win.fill((0, 0, 0))
        draw_grid(win)
        pacman.draw(win)
        for ghost in ghosts:
            ghost.draw(win)
        pygame.display.update()

def check_collision(ghost, pacman):
    # Check direct collision
    if ghost.row == pacman.row and ghost.col == pacman.col:
        return True
    
    # Check adjacent cells (this is from the original code)
    if ghost.row == pacman.row-1 and ghost.col == pacman.col:
        return True
    elif ghost.row == pacman.row+1 and ghost.col == pacman.col:
        return True
    elif ghost.row == pacman.row and ghost.col == pacman.col-1:
        return True
    elif ghost.row == pacman.row and ghost.col == pacman.col+1:
        return True
    
    return False

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            handle_strategy_key(event.key)

    if not game_over and not win_game:
        # Controls
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]: dy = -1
        elif keys[pygame.K_RIGHT]: dy = 1
        elif keys[pygame.K_UP]: dx = -1
        elif keys[pygame.K_DOWN]: dx = 1

        pacman.move(dx, dy, MAZE)
        
        # Move ghosts - they will use their individual strategies or the global one
        for ghost in ghosts:
            ghost.chase((pacman.row, pacman.col), MAZE)
        
        # Check collisions with ghosts
        for ghost in ghosts:
            if check_collision(ghost, pacman):
                game_over_sound.play()
                game_over = True
                break

        if not DOTS:
            win_game = True
            win_sound.play()

    # Draw everything
    draw_grid(win)
    pacman.draw(win)
    for ghost in ghosts:
        ghost.draw(win)

    # Display current strategy
    strategy_text = small_font.render(f"Strategy: {current_strategy}", True, (255, 255, 255))
    win.blit(strategy_text, (10, HEIGHT - 40))
    
    # Display controls hint
    controls_text = small_font.render("Press 1-5 to change strategy", True, (255, 255, 255))
    win.blit(controls_text, (WIDTH - 350, HEIGHT - 40))

    if game_over:
        text = font.render("GAME OVER", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)
    elif win_game:
        text = font.render("RESPECT++", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)

    pygame.display.update()

pygame.quit()