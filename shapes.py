class Shapes:
    def __init__(self, grid, colour, central_grid):
        self.grid = grid
        self.colour = colour
        self.central_grid = central_grid

    def move_left(self):
        if self.grid[0][0] != 0 and self.grid[1][0] != 0 \
                and self.grid[2][0] != 0 and self.grid[3][0] != 0:
            for grid in self.grid:
                grid[0] -= 1

    def move_right(self):
        if self.grid[0][0] != 9 and self.grid[1][0] != 9 \
                and self.grid[2][0] != 9 and self.grid[3][0] != 9:
            for grid in self.grid:
                grid[0] += 1

    def move_down(self):
        for grid in self.grid:
            grid[1] += 1

    def rotate_left(self):
        for grid in self.grid:
            if grid != self.central_grid[0]:
                i = grid[1] - self.central_grid[0][1]
                grid[1] = self.central_grid[0][1] + grid[0] - self.central_grid[0][0]
                grid[0] = self.central_grid[0][0] - i
        while self.grid[0][1] < 0 or self.grid[1][1] < 0 or self.grid[2][1] < 0 or self.grid[3][1] < 0:
            for grid in self.grid:
                grid[1] += 1
        while self.grid[0][0] < 0 or self.grid[1][0] < 0 or self.grid[2][0] < 0 or self.grid[3][0] < 0:
            for grid in self.grid:
                grid[0] += 1
        while self.grid[0][0] > 9 or self.grid[1][0] > 9 or self.grid[2][0] > 9 or self.grid[3][0] > 9:
            for grid in self.grid:
                grid[0] -= 1

    def rotate_right(self):
        for grid in self.grid:
            if grid != self.central_grid[1]:
                i = grid[1] - self.central_grid[1][1]
                grid[1] = self.central_grid[1][1] - grid[0] + self.central_grid[1][0]
                grid[0] = self.central_grid[1][0] + i
        while self.grid[0][1] < 0 or self.grid[1][1] < 0 or self.grid[2][1] < 0 or self.grid[3][1] < 0:
            for grid in self.grid:
                grid[1] += 1
        while self.grid[0][0] < 0 or self.grid[1][0] < 0 or self.grid[2][0] < 0 or self.grid[3][0] < 0:
            for grid in self.grid:
                grid[0] += 1
        while self.grid[0][0] > 9 or self.grid[1][0] > 9 or self.grid[2][0] > 9 or self.grid[3][0] > 9:
            for grid in self.grid:
                grid[0] -= 1


class ShapeI(Shapes):
    def __init__(self):
        self.grid = [[3, 0], [4, 0], [5, 0], [6, 0]]
        self.colour = (0, 255, 255)
        self.central_grid = [self.grid[1], self.grid[2]]


class ShapeO(Shapes):
    def __init__(self):
        self.grid = [[4, 0], [5, 0], [4, 1], [5, 1]]
        self.colour = (255, 255, 0)
        self.central_grid = [self.grid[1], self.grid[2]]

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass


class ShapeT(Shapes):
    def __init__(self):
        self.grid = [[3, 1], [4, 0], [4, 1], [5, 1]]
        self.colour = (255, 0, 255)
        self.central_grid = [self.grid[2], self.grid[2]]


class ShapeS(Shapes):
    def __init__(self):
        self.grid = [[3, 1], [4, 1], [4, 0], [5, 0]]
        self.colour = (0, 255, 0)
        self.central_grid = [self.grid[2], self.grid[2]]


class ShapeZ(Shapes):
    def __init__(self):
        self.grid = [[3, 0], [4, 0], [4, 1], [5, 1]]
        self.colour = (255, 0, 0)
        self.central_grid = [self.grid[1], self.grid[1]]


class ShapeJ(Shapes):
    def __init__(self):
        self.grid = [[3, 0], [3, 1], [4, 1], [5, 1]]
        self.colour = (0, 0, 255)
        self.central_grid = [self.grid[2], self.grid[2]]


class ShapeL(Shapes):
    def __init__(self):
        self.grid = [[3, 1], [4, 1], [5, 1], [5, 0]]
        self.colour = (255, 165, 0)
        self.central_grid = [self.grid[1], self.grid[1]]
