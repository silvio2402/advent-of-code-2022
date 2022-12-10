import os
import math


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    total_priority = 0
    for rucksack in lines:
        compartment_1 = rucksack[:math.floor(len(rucksack)/2)]
        compartment_2 = rucksack[math.floor(len(rucksack)/2):]
        compartment_1 = set(list(compartment_1))
        compartment_2 = set(list(compartment_2))
        common = set.intersection(compartment_1, compartment_2)
        for item in common:
            priority = ord(
                item) - ord('a') + 1 if ord(item) > ord('Z') else ord(item) - ord('A') + 27
            total_priority += priority

    return total_priority


if __name__ == "__main__":
    print(main())
