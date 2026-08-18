import pygame

class Window:
    def __init__(
        self, 
        pixel_len = 25, 
        width = 700, 
        height = 950, 
        offset_header = 100,
        offset_border = 50,
        title = "FuckAssSandGame69420"
    ):
        pygame.init()
        self.width = width
        self.height = height
        self.pixel_len = pixel_len
        self.offset_header = offset_header
        self.offset_border = offset_border

        
        self.bg_color = (51, 69, 79)
        self.steel_color = (67, 72, 77)
        self.stone_color = (130, 139, 145)
        self.sand_color = (214, 211, 167)
        self.water_color = (21, 136, 219)

        self.color_map = {
            0:self.bg_color,
            1: self.water_color,
            2: self.sand_color,
            3: self.stone_color,
            4: self.steel_color
        }
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def render(self, grid_data):
        """Prints the grid and borders into the window"""
        self.screen.fill((20,20,20))

        for y, row in enumerate(grid_data):
            for x, cell_value in enumerate(row):
                y_pos = self.offset_header + y*self.pixel_len
                x_pos = self.offset_border + x*self.pixel_len
                color = self.color_map.get(cell_value, self.bg_color)

                pygame.draw.rect(self.screen, color, (x_pos, y_pos, self.pixel_len, self.pixel_len))
        pygame.display.flip()
    
    def check_grid_interaction(self, event_x, event_y):
        """Checks event position and return a grid coordinate if touched"""
        if self.offset_border < event_x < self.width - self.offset_border and self.offset_header < event_y < self.height - self.offset_border:
                grid_x = (event_x - self.offset_border)//self.pixel_len
                grid_y = (event_y - self.offset_header)//self.pixel_len

                return (grid_y, grid_x)
        else:
            return None

    def tick(self):
        """I dont know what this does honestly"""
        self.clock.tick(self.fps)
