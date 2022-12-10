import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    total_score = 0
    for line in lines:
        opponent, end = line.split(" ")
        opponent = ord(opponent) - ord('A')
        score = 0
        if end == "X":
            # Lose
            you = (opponent + 2) % 3
            score += 1 + you
        elif end == "Y":
            # Draw
            score += 3
            you = opponent
            score += 1 + you
        else:
            # Win
            score += 6
            you = (opponent + 1) % 3
            score += 1 + you
        total_score += score

    return total_score


if __name__ == "__main__":
    print(main())
