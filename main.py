import pygame
import shapes
import gameConst
from random import randrange

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((gameConst.WINDOW_WIDTH, gameConst.WINDOW_HEIGHT))
    shape = get_shape(randrange(0, 7))
    saved_shape = shapes.Shapes(0, 0, 0)
    swapped = False
    fixed_shapes = []
    for i in range(20):
        fixed_shapes.append([])
    curr_blocked = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    clock = pygame.time.Clock()
    time_elapsed_since_last_action = 0

    while True:
        if check_lose(curr_blocked):
            pygame.quit()
        draw_grid()
        draw_shape(shape)
        draw_fixed_shapes(fixed_shapes)
        if not type(saved_shape) is shapes.Shapes:
            draw_saved_shape(saved_shape)
        dt = clock.tick()
        time_elapsed_since_last_action += dt
        if time_elapsed_since_last_action > 1000:
            if not check_blocked(shape, curr_blocked):
                shape.move_down()
                draw_grid()
                draw_shape(shape)
                draw_fixed_shapes(fixed_shapes)
            else:
                for grid in shape.grid:
                    if curr_blocked[grid[0]] > grid[1]:
                        curr_blocked[grid[0]] = grid[1];
                add_to_fixed_shapes(shape, fixed_shapes)
                check_line_clear(fixed_shapes, curr_blocked)
                print(curr_blocked)
                shape = get_shape(randrange(0, 7))
                swapped = False
            time_elapsed_since_last_action = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_blocked_side(shape, fixed_shapes, "left"):
                        shape.move_left()
                elif event.key == pygame.K_RIGHT:
                    if not check_blocked_side(shape, fixed_shapes, "right"):
                        shape.move_right()
                elif event.key == pygame.K_UP:
                    if not check_blocked_rotate(shape, fixed_shapes):
                        shape.rotate_left()
                elif event.key == pygame.K_DOWN:
                    if not check_blocked(shape, curr_blocked):
                        shape.move_down()
                elif event.key == pygame.K_c:
                    if not swapped:
                        if type(saved_shape) is shapes.Shapes:
                            saved_shape = shape
                            shape = get_shape(randrange(0, 7))
                        else:
                            temp_shape = shape
                            shape_type = saved_shape.__class__
                            shape = shape_type()
                            saved_shape = temp_shape
                        swapped = True
                elif event.key == pygame.K_SPACE:
                    min_diff = 25
                    for grid in shape.grid:
                        if curr_blocked[grid[0]] - grid[1] < min_diff:
                            min_diff = curr_blocked[grid[0]] - grid[1]
                    for grid in shape.grid:
                        grid[1] += min_diff - 1
                    time_elapsed_since_last_action = 2000
        pygame.display.update()


def draw_grid():
    screen.fill(gameConst.BLACK)
    for x in range(10):
        for y in range(20):
            rect = pygame.Rect(x * gameConst.BLOCK_SIZE, y * gameConst.BLOCK_SIZE, gameConst.BLOCK_SIZE, gameConst.BLOCK_SIZE)
            pygame.draw.rect(screen, gameConst.WHITE, rect, 1)
    for x in range(5):
        for y in range(4):
            rect = pygame.Rect(x * gameConst.BLOCK_SIZE + 330, y * gameConst.BLOCK_SIZE + 180, gameConst.BLOCK_SIZE, gameConst.BLOCK_SIZE)
            pygame.draw.rect(screen, gameConst.WHITE, rect, 1)


def draw_shape(shape):
    for i in range(4):
        grid = pygame.Rect(shape.grid[i][0] * gameConst.BLOCK_SIZE + 1, shape.grid[i][1] * gameConst.BLOCK_SIZE + 1,
                           gameConst.BLOCK_SIZE - 2, gameConst.BLOCK_SIZE - 2)
        pygame.draw.rect(screen, shape.colour, grid, 0)


def draw_saved_shape(shape):
    shape_type = shape.__class__
    new_shape = shape_type()
    for grid in new_shape.grid:
        square = pygame.Rect(grid[0] * gameConst.BLOCK_SIZE + 271, grid[1] * gameConst.BLOCK_SIZE + 211,
                             gameConst.BLOCK_SIZE - 2, gameConst.BLOCK_SIZE - 2)
        pygame.draw.rect(screen, new_shape.colour, square, 0)


def draw_fixed_shapes(fixed_shapes):
    for i in range(len(fixed_shapes)):
        for grid in fixed_shapes[i]:
            curr_grid = pygame.Rect(grid[0] * gameConst.BLOCK_SIZE + 1, i * gameConst.BLOCK_SIZE + 1,
                                    gameConst.BLOCK_SIZE - 2, gameConst.BLOCK_SIZE - 2)
            pygame.draw.rect(screen, grid[2], curr_grid, 0)


def get_shape(num):
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


def add_to_fixed_shapes(shape, fixed_shapes):
    for shape_grid in shape.grid:
        fixed_shapes[shape_grid[1]].append((shape_grid[0], shape_grid[1], shape.colour))


def check_blocked(shape, curr_blocked):
    for grid in shape.grid:
        if grid[1] >= curr_blocked[grid[0]] - 1:
            return True
    return False


def check_blocked_side(shape, fixed_shapes, direction):
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


def check_blocked_rotate(shape, fixed_shapes):
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


def check_line_clear(fixed_shapes, curr_blocked):
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


def check_lose(curr_blocked):
    for x in curr_blocked:
        if x == 0:
            return True
    return False


main()
