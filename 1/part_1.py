import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        calories_list = []
        current_calories = 0
        for line in lines:
            if line != "":
                current_calories += int(line)
            else:
                calories_list.append(current_calories)
                current_calories = 0
    return max(calories_list)


if __name__ == "__main__":
    print(main())
