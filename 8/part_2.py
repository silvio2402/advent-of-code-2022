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

    def scenic_score(i: int, heights: list[int], width: int) -> bool:
        row = math.floor(i / width)
        col = i % width
        left = heights[row*width:i][::-1]
        right = heights[i+1:(row+1)*width]
        up = [heights[i] for i in range(col, i, width)][::-1]
        down = [heights[i] for i in range(i+width, len(heights), width)]
        value = heights[i]

        def viewdist(dir, value):
            dist = 0
            for h in dir:
                dist += 1
                if h >= value:
                    break
            return dist

        return viewdist(left, value) * viewdist(right, value) * viewdist(up, value) * viewdist(down, value)

    tree_scenic_scores = [scenic_score(
        i, tree_heights, width) for i in range(len(tree_heights))]

    return max(tree_scenic_scores)


if __name__ == "__main__":
    print(main())
