import pygame

class Display:
    def __init__(
        self,
        screen_height = 900,
        screen_width = 700,
        pixel_len = 25,
        title = "Line Algorithm For Sandgame",
        ):

        pygame.init()

        self.screen_height = screen_height
        self.screen_width = screen_width
        self.pixel_len = pixel_len

        self.bg_color = (51, 69, 79)
        self.dot_color = (214, 211, 167)
        self.line_color = (21, 136, 219)

        self.color_map = {
            0: self.bg_color,
            1: self.dot_color,
            2: self.line_color
        }

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.fps = 15

    def render(self, grid):
        self.screen.fill((20,20,20))
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                y_pos = y * self.pixel_len
                x_pos = x * self.pixel_len
                color = self.color_map.get(cell, self.bg_color)

                pygame.draw.rect(self.screen, color, (x_pos, y_pos, self.pixel_len, self.pixel_len))
        pygame.display.flip()

    def tick(self):
        self.clock.tick(self.fps)