from dataclasses import dataclass


@dataclass
class Handheld:
    x = 1
    cycle = 1
    crt = ''
    signal_strength = 0

    def tick(self):
        column = (self.cycle - 1) % 40
        if column == 0:
            self.crt += "\n"
        if column in (self.x - 1, self.x, self.x + 1):
            self.crt += '#'
        else:
            self.crt += '.'

        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.signal_strength += self.x * self.cycle

        self.cycle += 1


handheld = Handheld()
with open('data/day10.txt') as data:
    for line in data:
        line = line.rstrip()

        handheld.tick()
        if line != 'noop':
            handheld.tick()
            _, delta = line.split()
            handheld.x += int(delta)


print("Part 1")
print(handheld.signal_strength)

print("Part 2")
print(handheld.crt)

