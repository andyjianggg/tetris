import shapes

class Controller:
    def __init__(self, num):
        self.num = num

    def play(self):


    def get_shape(self, num):
        if num == 0:
            return shapes.ShapeI()
        elif num == 1:
            return shapes.ShapeJ()
        elif num == 2:
            return shapes.ShapeL()
        elif num == 3:
            return shapes.ShapeO()
        elif num == 4:
            return shapes.ShapeS()
        elif num == 5:
            return shapes.ShapeZ()
        else:
            return shapes.ShapeT()

    def add_to_fixed_shapes(self, shape, fixed_shapes):
        for shape_grid in shape.grid:
            fixed_shapes[shape_grid[1]].append((shape_grid[0], shape_grid[1], shape.colour))

    def check_blocked(self, shape, curr_blocked):
        for grid in shape.grid:
            if grid[1] >= curr_blocked[grid[0]] - 1:
                return True
        return False

    def check_blocked_side(self, shape, fixed_shapes, direction):
        if direction == "left":
            for grid in shape.grid:
                if grid[0] == 0:
                    return False
                for x in fixed_shapes[grid[1]]:
                    if grid[0] - 1 == x[0]:
                        return True
            return False
        elif direction == "right":
            for grid in shape.grid:
                if grid[0] == 9:
                    return False
                for x in fixed_shapes[grid[1]]:
                    if grid[0] + 1 == x[0]:
                        return True
            return False
        else:
            return False

    def check_blocked_rotate(self, shape, fixed_shapes):
        for grid in shape.grid:
            if grid != shape.central_grid[0]:
                i = grid[1] - shape.central_grid[0][1]
                y = shape.central_grid[0][1] + grid[0] - shape.central_grid[0][0]
                x = shape.central_grid[0][0] - i
                if y > 19 or y < 0:
                    return True
                for n in fixed_shapes[y]:
                    if x == n[0]:
                        return True
        return False

    def check_line_clear(self, fixed_shapes, curr_blocked):
        for row in fixed_shapes:
            if len(row) == 10:
                fixed_shapes.remove(row)
                fixed_shapes.insert(0, [])
                for grid in curr_blocked:
                    grid += 1
                for i in range(len(curr_blocked)):
                    skip = True
                    while skip:
                        print(curr_blocked[i])
                        for grid in fixed_shapes[curr_blocked[i]]:
                            print(grid)
                            if grid[0] == i:
                                skip = False
                                break
                        else:
                            curr_blocked[i] += 1
                        if curr_blocked[i] == 20:
                            skip = False

    def check_lose(self, curr_blocked):
        for x in curr_blocked:
            if x == 0:
                return True
        return False