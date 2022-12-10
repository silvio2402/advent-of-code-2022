import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        buffer = f.read()

    distinct_amount = 4
    pos = 0
    small_buffer = buffer[pos:pos+distinct_amount]
    while pos <= len(buffer)-distinct_amount:
        if (len(set(small_buffer)) >= distinct_amount):
            break
        pos += 1
        small_buffer = buffer[pos:pos+distinct_amount]

    return pos + distinct_amount


if __name__ == "__main__":
    print(main())
