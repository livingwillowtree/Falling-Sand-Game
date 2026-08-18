import pygame
import sys
import time

from display import Display
from grid import Grid

def main():
    display = Display()
    grid = Grid()

    running = True
    while running:
        running = handle_events(display, grid)
        # grid.update()

        grid_data = grid.get_grid_data()
        display.render(grid_data)
        display.tick()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()