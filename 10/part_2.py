import os
import math

operation_cycle_amounts = {
    "noop": 1,
    "addx": 2,
}


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    crt = [list("." * 40), list("." * 40),
           list("." * 40), list("." * 40), list("." * 40), list("." * 40), ]
    register_x = 1
    execution_address = 0
    cmd = lines[execution_address].split(" ", 1)
    operation = cmd[0]
    parameter_v = cmd[1] if len(cmd) > 1 else None
    operation_index = 0
    cycle = 0
    while True:
        # draw sprite in crt
        if (cycle != 0 and cycle < 240):
            char_index = cycle - 1
            dist = abs((char_index) % 40 - register_x)
            should_draw = dist <= 1
            x = (char_index) % 40
            y = math.floor((char_index) / 40)
            crt[y][x] = '#' if should_draw else '.'

        operation_cycle_amount = operation_cycle_amounts[operation]
        if operation_index >= operation_cycle_amount:
            if operation == "addx":
                register_x += int(parameter_v)

            execution_address += 1
            if execution_address >= len(lines):
                break
            cmd = lines[execution_address].split(" ", 1)
            operation = cmd[0]
            parameter_v = cmd[1] if len(cmd) > 1 else None
            operation_index = 1
        else:
            operation_index += 1

        cycle += 1

    return "\n".join(["".join(line) for line in crt])


if __name__ == "__main__":
    print(main())
