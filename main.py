import sys
import pygame
from display import Window
from grid import Grid
from engine import Engine

def main():
    window = Window()
    grid = Grid() 
    engine = Engine()
    running = True

    while running:
        running = engine.handle_events(window, grid)
        grid.update()

        grid_data = grid.get_grid_data()
        window.render(grid_data)
        window.tick()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()