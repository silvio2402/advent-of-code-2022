import os


def main():
    with open(os.path.join(os.path.dirname(__file__), "./input.txt"), 'r') as f:
        lines = f.readlines()

    divider_index = lines.index('\n')
    stack_str, instructions = lines[:divider_index], lines[divider_index+1:]
    stack_count = int(stack_str[-1].split()[-1])
    stack_str = stack_str[:-1][::-1]

    stacks = [[] for _ in range(stack_count)]
    for row in stack_str:
        crates = [row[i*4 + 1] for i in range(stack_count)]
        [(stacks[i].append(crates[i]) if crates[i] != ' ' else None)
            for i in range(len(crates))]

    for instruction in instructions:
        if instruction.startswith('move '):
            amount, rest = instruction[5:].split(' from ', 1)
            amount = int(amount)
            from_stack, to_stack = rest.split(' to ', 1)
            from_stack = int(from_stack)-1
            to_stack = int(to_stack)-1
            stacks[to_stack] += stacks[from_stack][-amount:][::-1]
            stacks[from_stack] = stacks[from_stack][:-amount]

    return ''.join([stack[-1] if len(stack) > 0 else '' for stack in stacks])


if __name__ == "__main__":
    print(main())
