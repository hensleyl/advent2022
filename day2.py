part1_scores = {'A X': 4,
                'A Y': 8,
                'A Z': 3,
                'B X': 1,
                'B Y': 5,
                'B Z': 9,
                'C X': 7,
                'C Y': 2,
                'C Z': 6}

part2_scores = {'A X': 0 + 3,
                'A Y': 3 + 1,
                'A Z': 6 + 2,
                'B X': 0 + 1,
                'B Y': 3 + 2,
                'B Z': 6 + 3,
                'C X': 0 + 2,
                'C Y': 3 + 3,
                'C Z': 6 + 1}

part1_total = 0
part2_total = 0
with open('data/day2.txt') as data:
    for line in data:
        part1_total += part1_scores[line.rstrip()]
        part2_total += part2_scores[line.rstrip()]

print("Part 1")
print(part1_total)

print("Part 2")
print(part2_total)
