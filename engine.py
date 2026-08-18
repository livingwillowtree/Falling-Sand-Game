import pygame
import time

class Engine:
    def __init__(
        self
        ):
        self.place_cooldown_ms = 100
        self.last_placement_time = 0
        self.current_time = 0
        self.previous_point = None
        self.current_point = None

    def handle_events(self, window, grid):
        """Handles pygame inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            # the labels are there, no need for me to tell you
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Water")
                    grid.particle_to_add = 1
                elif event.key == pygame.K_2:
                    print("Sand")
                    grid.particle_to_add = 2
                elif event.key == pygame.K_3:
                    print("Stone")
                    grid.particle_to_add = 3
                elif event.key == pygame.K_4:
                    print("Steel")
                    grid.particle_to_add = 4
                elif event.key == pygame.K_c:
                    print("Clear")
                    grid.clear_grid()
                elif event.key == pygame.K_ESCAPE:
                    return False
            # resets previous point on mouse release
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.previous_point = None

        if pygame.mouse.get_pressed()[0]:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.last_placement_time >= self.place_cooldown_ms:
                x, y = pygame.mouse.get_pos()
                print(f"Left clicked at: {x,y}")
                coords = window.check_grid_interaction(x,y)
                if coords:
                    row, col = coords
                    self.current_point = coords
                    grid.add_particle(row, col)
                    
                self.last_placement_time = self.current_time
                if self.previous_point:
                    print("Make Line")
                    points = self.connect_dots(self.previous_point, self.current_point)
                    if points:
                        for row, col in points:
                            grid.add_particle(row, col)
                self.previous_point = self.current_point

        return True

    def connect_dots(self, previous, current):
        """Connects the dots.. poetry - Thank you mr bresenhamburger"""
        points = []
        y0, x0 = previous
        y1, x1 = current
        
        dx = abs(x0 - x1)
        dy = abs(y0 - y1)
        
        sx, sy = x0, y0
        
        vx = 1 if x0 < x1 else -1
        vy = 1 if y0 < y1 else -1

        is_steep = dx < dy

        if is_steep:
            pk = 2*dx - dy
            for step in range(dy + 1):
                points.append((sy,sx))
                if pk < 0:
                    pk += 2*dx
                else:
                    pk += 2*dx - 2*dy
                    sx += vx                    
                sy += vy
        else: 
            pk = 2*dy - dx
            for step in range(dx + 1):
                points.append((sy,sx))
                if pk < 0:
                    pk += 2*dy
                else:
                    pk += 2*dy - 2*dx
                    sy += vy
                sx += vx

        print(f"Line Made: {points}")
        return points