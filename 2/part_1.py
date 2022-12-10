import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        total_score = 0
        for line in lines:
            opponent, you = line.split(" ")
            opponent = ord(opponent) - ord('A')
            you = ord(you) - ord('X')
            score = 1 + you
            if opponent == you:
                # Draw
                score += 3
            elif opponent == (you + 1) % 3:
                # Lose
                score += 0
            else:
                # Win
                score += 6
            total_score += score
    return total_score


if __name__ == "__main__":
    print(main())
