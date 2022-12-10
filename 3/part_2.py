import os
import math


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    total_priority = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        common = set(list(group[0]))
        for rucksack in group[1:]:
            common = set.intersection(common, set(list(rucksack)))
        item = list(common)[0]
        priority = ord(
            item) - ord('a') + 1 if ord(item) > ord('Z') else ord(item) - ord('A') + 27
        total_priority += priority

    return total_priority


if __name__ == "__main__":
    print(main())
