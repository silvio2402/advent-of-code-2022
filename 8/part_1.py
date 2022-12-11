import os
import math


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    width = len(lines[0])

    tree_heights = []

    for char in ''.join(lines):
        try:
            height = int(char)
            tree_heights.append(height)
        except ValueError:
            pass

    def is_visible(i: int, heights: list[int], width: int) -> bool:
        row = math.floor(i / width)
        col = i % width
        left = heights[row*width:i]
        right = heights[i+1:(row+1)*width]
        up = [heights[i] for i in range(col, i, width)]
        down = [heights[i] for i in range(i+width, len(heights), width)]
        value = heights[i]

        def visible(dir, value):
            return len(list(filter(lambda v: v >= value, dir))) <= 0

        return visible(left, value) or visible(right, value) or visible(up, value) or visible(down, value)

    tree_visibilities = [is_visible(i, tree_heights, width)
                         for i in range(len(tree_heights))]

    return len(list(filter(lambda v: v, tree_visibilities)))


if __name__ == "__main__":
    print(main())
