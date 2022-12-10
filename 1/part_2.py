import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    calories_list = []
    current_calories = 0
    for line in lines:
        line = line.strip()
        if line != "":
            current_calories += int(line)
        else:
            calories_list.append(current_calories)
            current_calories = 0
    calories_topthree = sorted(calories_list, reverse=True)[:3]

    return sum(calories_topthree)


if __name__ == "__main__":
    print(main())
