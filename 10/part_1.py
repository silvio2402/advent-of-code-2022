import os

operation_cycle_amounts = {
    "noop": 1,
    "addx": 2,
}


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    signal_strengths = []
    register_x = 1
    execution_address = 0
    cmd = lines[execution_address].split(" ", 1)
    operation = cmd[0]
    parameter_v = cmd[1] if len(cmd) > 1 else None
    operation_index = 0
    cycle = 0
    while True:
        if cycle != 0 and (cycle - 20) % 40 == 0:
            signal_strengths.append(cycle * register_x)

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

    return sum(signal_strengths)


if __name__ == "__main__":
    print(main())
