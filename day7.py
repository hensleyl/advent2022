DISK_SIZE = 70000000
NEEDED_FREE = 30000000
working_path = []
sizes = {}
with open('data/day7.txt') as data:
    for line in data:
        line = line.rstrip()
        if line.startswith('$ cd'):
            d = line.split()[-1]
            if d == '..':
                working_path.pop()
            else:
                working_path.append(d)
        else:
            size = line.split()[0]
            if size.isdecimal():
                for i in range(1, len(working_path)+1):
                    subpath = '/'.join(working_path[:i])
                    sizes.setdefault(subpath, 0)
                    sizes[subpath] += int(size)

additional_free = NEEDED_FREE - (DISK_SIZE - sizes['/'])

print('Part 1')
print(sum([s for s in sizes.values() if s <= 100000]))

print('Part 2')
print(next(s for s in sorted(sizes.values()) if s > additional_free))
