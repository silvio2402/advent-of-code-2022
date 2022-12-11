import os
import math


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add(tail)

    def rope_step(head, tail):
        head_x, head_y = head
        tail_x, tail_y = tail
        dist_x = head_x - tail_x
        dist_y = head_y - tail_y
        dist = abs(dist_x) ** 2 + abs(dist_y) ** 2
        if dist <= 2:
            # adjacent or overlapping
            return True

        tail = (tail_x + (math.copysign(1, dist_x) if abs(dist_x) > 0 else 0),
                tail_y + (math.copysign(1, dist_y) if abs(dist_y) > 0 else 0))

        return tail

    for motion in lines:
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
            head_x, head_y = head
            dir_x, dir_y = direction
            head = (head_x + dir_x, head_y + dir_y)
            new_tail = False
            while new_tail != True:
                new_tail = rope_step(head, tail)
                if new_tail != True:
                    tail = new_tail
                    visited.add(tail)

    return len(visited)


if __name__ == "__main__":
    print(main())
