def walk_line(forest, visible, path):
    tallest = -1
    for x, y in path:
        if forest[x][y] > tallest:
            visible[x][y] = True
            tallest = forest[x][y]


def calc_score(forest, x, y):
    left = next((i for i, v in enumerate(reversed(forest[y][0:x])) if v >= forest[y][x]), x - 1) + 1
    right = next((i for i, v in enumerate(forest[y][x+1:]) if v >= forest[y][x]), len(forest[x]) - x - 2) + 1
    up = next((i for i, v in enumerate(f[x] for f in reversed(forest[0:y])) if v >= forest[y][x]), y - 1) + 1
    down = next((i for i, v in enumerate(f[x] for f in forest[y+1:]) if v >= forest[y][x]), len(forest) - y - 2) + 1
    return left * right * up * down


with open('data/day8.txt') as data:
    forest = [[int(x) for x in line.rstrip()] for line in data]

size = len(forest)
visible = [[False] * size for _ in range(size)]

for i in range(size):
    # rows right
    walk_line(forest, visible, zip(range(0, size, 1), [i]*size))
    # rows left
    walk_line(forest, visible, zip(range(size-1, -1, -1), [i]*size))
    # column down
    walk_line(forest, visible, zip([i]*size, range(0, size, 1)))
    # column up
    walk_line(forest, visible, zip([i]*size, range(size-1, -1, -1)))

print("Part 1")
print(sum([sum(row) for row in visible]))

part2_score = 0
for x in range(1, size-1):
    for y in range(1, size-1):
        part2_score = max(part2_score, calc_score(forest, x, y))

print("Part 2")
print(part2_score)
