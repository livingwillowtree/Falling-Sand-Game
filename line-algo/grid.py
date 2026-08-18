
class Grid:
    def __init__(
        self,
        row_count = 36,
        col_count = 28,
        ):

        self.row_count = row_count
        self.col_count = col_count

        self._gridMatrix = [[0 for _ in range(self.col_count)] for _ in range(self.row_count)]

        self.previous_point = None
        self.current_point = None
    def add_point(self, row, col):
        if self._gridMatrix[row][col] == 0:
            self._gridMatrix[row][col] = 1
            print(f"Added point to: {col, row}")
            self.current_point = (col, row)
            if self.previous_point:
                self.connect_dots(self.previous_point, self.current_point)
            self.previous_point = self.current_point

        else:
            print(f"Failed to add, cell occupied!")
        
    
    def connect_dots(self, previous, current):
        x0, y0 = previous
        x1, y1 = current
        
        dx = abs(x0 - x1)
        dy = abs(y0 - y1)
        
        sx, sy = x0, y0
        
        vx = 1 if x0 < x1 else -1
        vy = 1 if y0 < y1 else -1

        is_steep = dx < dy

        if is_steep:
            pk = 2*dx - dy
            for step in range(dy + 1):
                self._gridMatrix[sy][sx] = 2
                if pk < 0:
                    pk += 2*dx
                else:
                    pk += 2*dx - 2*dy
                    sx += vx                    
                sy += vy
        else: 
            pk = 2*dy - dx
            for step in range(dx + 1):
                self._gridMatrix[sy][sx] = 2
                if pk < 0:
                    pk += 2*dy
                else:
                    pk += 2*dy - 2*dx
                    sy += vy
                sx += vx
    

    def get_grid_data(self):
        return self._gridMatrix