def find_overlap(c1, c2):
    return set([x for x in c1 if x in c2])


def total_priority(o):
    return sum([min(ord(x) - ord('a') + 1, ord(x) - ord('A') + 27, key=lambda y: y if y > 0 else 99) for x in o])


part1_total = 0
part2_total = 0
group = []
with open('data/day3.txt') as data:
    for line in data:
        line = line.rstrip()
        overlap = find_overlap(line[:len(line)//2], line[len(line)//2:])
        part1_total += total_priority(overlap)
        group.append(line)
        if len(group) == 3:
            badge = find_overlap(find_overlap(group[0], group[1]), group[2])
            part2_total += total_priority(badge)
            group = []

print('Part 1')
print(part1_total)

print('Part 2')
print(part2_total)

