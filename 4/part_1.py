import os


def contains(this, that):  # is that contained in this?
    from_this, to_this = this
    from_that, to_that = that
    return from_that >= from_this and to_that <= to_this


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    containment_count = 0
    for pair in lines:
        assignments = pair.split(',', 1)
        assignments = [[int(i) for i in assignment.split('-', 1)]
                       for assignment in assignments]
        ass0, ass1 = assignments
        if contains(ass0, ass1) or contains(ass1, ass0):
            containment_count += 1

    return containment_count


if __name__ == "__main__":
    print(main())
