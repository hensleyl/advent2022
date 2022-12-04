contained_count = 0
overlap_count = 0
with open('data/day4.txt') as data:
    for line in data:
        line = line.rstrip()
        low, high = sorted([[int(s) for s in sections.split('-')] for sections in line.split(',')],
                           key=lambda sec: [sec[0], -1 * sec[1]])
        if low[0] <= high[0] and low[1] >= high[1]:
            contained_count += 1
        if low[1] >= high[0]:
            overlap_count += 1

print('Part 1')
print(contained_count)

print('Part 2')
print(overlap_count)
