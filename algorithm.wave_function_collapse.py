import numpy as np
import pygame
import random

TILE_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 20, 15
WINDOW_WIDTH, WINDOW_HEIGHT = GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE

TILE_EMPTY, TILE_WALL, TILE_FLOOR, TILE_SPECIAL, TILE_UNDER = ' ','#','.','*','$'

COLORS = {
    TILE_EMPTY: (30, 30, 30),
    TILE_WALL: (100, 100, 100),
    TILE_FLOOR: (200, 200, 200),
    TILE_SPECIAL: (0, 255, 255), 
    TILE_UNDER: (255, 0, 255)
}

TILE_RULES = {
    TILE_WALL: [TILE_WALL, TILE_UNDER],
    TILE_FLOOR: [TILE_FLOOR, TILE_WALL, TILE_SPECIAL,TILE_UNDER],
    TILE_SPECIAL: [TILE_FLOOR, TILE_WALL],
    TILE_UNDER: [TILE_SPECIAL,TILE_UNDER ]
}

grid = np.full((GRID_HEIGHT,GRID_WIDTH), TILE_EMPTY, dtype= str)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Wave function Collapse")

def get_neighbors(x, y):
    neighbors = []
    if x > 0 :
        neighbors.append((x - 1, y))
    if x < GRID_WIDTH - 1:
        neighbors.append((x + 1,y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < GRID_HEIGHT - 1:
        neighbors.append((x, y + 1))
    return neighbors

def draw_grid():
    screen.fill((0, 0, 0)) 

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(
                screen,
                COLORS[grid[y, x]],
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

    pygame.display.flip()

def wave_function_collapse():
    uncollapsed = [(x,y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
    random.shuffle(uncollapsed)

    while uncollapsed:
        x, y = uncollapsed.pop()
        possible_tiles = list(TILE_RULES.keys())

        for nx, ny in get_neighbors(x, y):
            neightbor_tile = grid[ny, nx]
            if neightbor_tile in TILE_RULES:
                possible_tiles = [ t for t in possible_tiles if t in TILE_RULES[neightbor_tile]]
        if possible_tiles:
            grid[y, x] = random.choice(possible_tiles)

        draw_grid()
        pygame.display.flip()
        pygame.time.delay(50)


wave_function_collapse()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()