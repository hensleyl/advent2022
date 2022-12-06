import re


def block(line, i):
    return line[i * 4 + 1:i * 4 + 2]


def parse_stack(lines):
    lines = lines.copy()
    num_stacks = int(lines.pop().split()[-1])
    lines = list(reversed(lines))
    return [[block(line, i) for line in lines if block(line, i).strip()] for i in range(num_stacks)]


def print_tops(stacks):
    print(''.join([s.pop() for s in stacks]))


def move(stacks, f, t, count, method):
    bottom = len(stacks[f - 1]) - count
    stacks[t - 1] += method(stacks[f - 1][bottom:])
    del stacks[f - 1][bottom:]


with open('data/day5.txt') as data:
    stack_lines = []
    for line in data:
        line = line.rstrip()
        if line == '':
            break
        stack_lines.append(line)
    p1_stacks = parse_stack(stack_lines)
    p2_stacks = parse_stack(stack_lines)

    for line in data:
        m = re.match(r'move (\d+) from (\d) to (\d)', line)
        count, f, t = [int(x) for x in m.groups()]
        move(p1_stacks, f, t, count, reversed)
        move(p2_stacks, f, t, count, list)

    print('Part 1')
    print_tops(p1_stacks)

    print('Part 2')
    print_tops(p2_stacks)
