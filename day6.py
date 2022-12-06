def find_marker(line, size):
    i = 0
    while len(set(line[i:i+size])) < size:
        i += 1
    return i + size


with open('data/day6.txt') as data:
    line = data.read()

print("Part 1")
print(find_marker(line, 4))

print("Part 2")
print(find_marker(line, 14))
