import os
import math


# def print_state(knots, visited):
#     WIDTH = 26
#     HEIGHT = 21
#     START_X = 11
#     START_Y = 5
#     CHAR_MAP = 'H123456789'
#     grid = ['.' for _ in range(WIDTH*HEIGHT)]
#     for visit in list(visited):
#         visit_x, visit_y = visit
#         grid[math.floor((HEIGHT-1) - (visit_y+START_Y)) * WIDTH +
#              math.floor(visit_x+START_X)] = '#'
#     grid[((HEIGHT-1) - (START_Y)) * WIDTH + START_X] = 's'

#     for i, knot in list(enumerate(knots))[::-1]:
#         knot_x, knot_y = knot
#         grid[math.floor((HEIGHT-1) - (knot_y+START_Y)) * WIDTH +
#              math.floor(knot_x+START_X)] = CHAR_MAP[i]

#     for i in range(HEIGHT):
#         print(''.join(grid[i*WIDTH:(i+1)*WIDTH]))


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    knots = [(0, 0) for _ in range(10)]

    visited = set()
    visited.add(knots[-1])

    def rope_step(curr, prev):
        prev_x, prev_y = prev
        curr_x, curr_y = curr
        dist_x = prev_x - curr_x
        dist_y = prev_y - curr_y
        dist = abs(dist_x) ** 2 + abs(dist_y) ** 2
        if dist <= 2:
            # adjacent or overlapping
            return True

        curr = (curr_x + (math.copysign(1, dist_x) if abs(dist_x) > 0 else 0),
                curr_y + (math.copysign(1, dist_y) if abs(dist_y) > 0 else 0))

        return curr

    # print('\n==', 'Initial State', '==\n')
    # print_state(knots, visited)

    for motion in lines:
        # print('\n==', motion, '==\n')
        direction, magnitude = motion.split(' ', 1)
        dir_dict = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1),
        }
        direction = dir_dict[direction]
        magnitude = int(magnitude)
        for _ in range(magnitude):
            head_x, head_y = knots[0]
            dir_x, dir_y = direction
            knots[0] = (head_x + dir_x, head_y + dir_y)

            for i in range(1, len(knots)):
                knot = knots[i]
                next = knots[i-1]
                new_knot = False
                while new_knot != True:
                    new_knot = rope_step(knot, next)
                    if new_knot != True:
                        knot = new_knot
                        if i == len(knots)-1:
                            visited.add(new_knot)
                knots[i] = knot

        # print()
        # print_state(knots, visited)

    return len(visited)


if __name__ == "__main__":
    print(main())
