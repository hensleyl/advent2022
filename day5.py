import re


def parse_stack(lines):
    lines = lines.copy()
    num_stacks = int(lines.pop().split()[-1])
    lines = list(reversed(lines))
    return [[line[i * 4 + 1:i * 4 + 2] for line in lines if line[i * 4 + 1:i * 4 + 2].strip()] for i
            in range(num_stacks)]


def print_tops(stacks):
    print(''.join([s.pop() for s in stacks]))


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
        for i in range(count):
            p1_stacks[t - 1].append(p1_stacks[f - 1].pop())
        p2_stacks[t-1] += p2_stacks[f-1][len(p2_stacks[f-1])-count:len(p2_stacks[f-1])]
        del p2_stacks[f-1][len(p2_stacks[f-1])-count:len(p2_stacks[f-1])]

    print('Part 1')
    print_tops(p1_stacks)

    print('Part 2')
    print_tops(p2_stacks)
