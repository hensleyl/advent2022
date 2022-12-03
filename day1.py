max_elves = []
elf_total = 0
with open('data/day1.txt') as data:
    for line in data:
        if line == '\n':
            max_elves = sorted(max_elves + [elf_total], reverse=True)[:3]
            elf_total = 0
        else:
            elf_total += int(line.rstrip())
max_elves = sorted(max_elves + [elf_total], reverse=True)[:3]

print("Part 1")
print(max_elves[0])

print("Part 2")
print(sum(max_elves))
