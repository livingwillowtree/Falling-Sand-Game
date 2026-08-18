import time
import random
class Grid:
    def __init__(self, row_count = 32, col_count = 24):
        self.row_count = row_count
        self.col_count = col_count
        self.particle_to_add = 4
        self.particle_checking = 4

        self._gridMatrix = [[0 for _ in range(self.col_count)] for _ in range(self.row_count)]

    def add_particle(self, row, col):
        """Adds particle to matrix"""
        if self._gridMatrix[row][col] != 0:
            print("Failed, Cell occupied")
            return

        print(f"Placed {self.particle_to_add} at {col, row}")
        self._gridMatrix[row][col] = self.particle_to_add
    
    def clear_grid(self):
        """Did you seriously just hover this bro?"""
        self._gridMatrix = [[0 for _ in range(self.col_count)] for _ in range(self.row_count)]
    
    def move_down(self, row, col):
        """Attempts straight down movement"""
        if row + 1 >= self.row_count:
            return False

        if self._gridMatrix[row+1][col] == 0 or (self.particle_checking != 1 and self._gridMatrix[row+1][col] == 1):
            temp = self._gridMatrix[row+1][col]
            self._gridMatrix[row+1][col] = self.particle_checking
            self._gridMatrix[row][col] = temp
            return True
        
        return False
        
    def move_diagonal(self, row, col):
        """Attempts diagonal movement, right and left, randomized if both"""
        if row + 1 >= self.row_count:
            return False

        def check_diagonal(d_col):
            return (
                # check if index movement is within bounds
                0 <= col + d_col < self.col_count and 
                (
                    (   # check if the particle is not water, and if the target is water
                        self.particle_checking != 1 and
                        self._gridMatrix[row][col+d_col] == 1 and
                        self._gridMatrix[row+1][col+d_col] == 1
                    ) or 
                    (   
                        # check if the target is air
                        self._gridMatrix[row][col+d_col] == 0 and
                        self._gridMatrix[row+1][col+d_col] == 0
                    )
                )
            )

        def move(d_col):
            temp = self._gridMatrix[row+1][col+d_col]
            self._gridMatrix[row+1][col+d_col] = self.particle_checking
            self._gridMatrix[row][col] = self._gridMatrix[row][col+d_col]
            self._gridMatrix[row][col+d_col] = temp

        diagonal_r_okay = check_diagonal(1)

        diagonal_l_okay = check_diagonal(-1)

        if diagonal_r_okay and diagonal_l_okay:
            if random.randint(0,1):
                move(1)
            else:
                move(-1)
        elif diagonal_r_okay:
            move(1)
        elif diagonal_l_okay:
            move(-1)
        else:
            return False
        
        return True

    def move_sides(self, row, col):
    """Attempts sideways movement, right and left, randomized if both"""

        def check_side(d_col):
            return (
                    # check if index movement is within bounds
                    0 <= col + d_col < self.col_count and 
                    (
                        (   # check if the particle is not water, and if the target is water
                            self.particle_checking != 1 and
                            self._gridMatrix[row][col+d_col] == 1 and
                            self._gridMatrix[row][col+d_col] == 1
                        ) or 
                        (   
                            # check if the target is air
                            self._gridMatrix[row][col+d_col] == 0 and
                            self._gridMatrix[row][col+d_col] == 0
                        )
                    )
                )

        def move(d_col):
            self._gridMatrix[row][col+d_col] = self.particle_checking
            self._gridMatrix[row][col] = 0

        side_r_okay = check_side(1)
        side_l_okay = check_side(-1)

        if side_r_okay and side_l_okay:
            if random.randint(0,1):
                move(1)
            else:
                move(-1)
        elif side_r_okay:
            move(1)
        elif side_l_okay:
            move(-1)

    def update(self):
        """Iterates through each cell, each particle has its own rules"""
        for i in range(self.row_count):
            for j in range(self.col_count):
                row = self.row_count - i - 1
                col = self.col_count - j - 1
                self.particle_checking = self._gridMatrix[row][col]
                
                # steel and air: stay in place
                if self.particle_checking == 0 or self.particle_checking == 4: 
                    continue
                    
                # stone: gravity only
                if self.particle_checking == 3:
                    self.move_down(row, col) 
                    continue
                
                # sand: gravity and diagonal
                if self.particle_checking == 2:
                    if self.move_down(row, col): 
                        continue 
                    self.move_diagonal(row, col)
                    continue

                # water: gravity, diagonal, and sides
                if self.particle_checking == 1:
                    if self.move_down(row, col): 
                        continue 
                    elif self.move_diagonal(row, col): 
                        continue
                    self.move_sides(row, col)
                    continue

    def get_grid_data(self):
        """Did you just really hover over this?"""
        return self._gridMatrix