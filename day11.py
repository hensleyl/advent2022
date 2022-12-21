import re
from math import prod


class Monkey:
    def __init__(self, f):
        self._queue = [int(item) for item in self.extract(r'items: (.+)', f)[0].split(', ')]

        op, arg = self.extract(r'Operation: new = old (.) (.+)', f)
        second = lambda x: x if arg == 'old' else int(arg)
        self._inspect = lambda x: x * second(x) if op == '*' else x + second(x)
        self._divisible = int(self.extract(r'divisible by (\d+)', f)[0])
        self._pos = int(self.extract(r'throw to monkey (\d+)', f)[0])
        self._neg = int(self.extract(r'throw to monkey (\d+)', f)[0])
        self._inspect_count = 0
        f.readline()

    @staticmethod
    def extract(regex, f):
        return re.search(regex, f.readline().rstrip()).groups()

    def turn(self, worry_reducer):
        retval = []
        for item in self._queue:
            item = worry_reducer(self._inspect(item))
            self._inspect_count += 1
            retval.append((self._pos if item % self._divisible == 0 else self._neg, item))
        self._queue.clear()
        return retval

    def catch(self, item):
        self._queue.append(item)

    def inspect_count(self):
        return self._inspect_count

    def divisor(self):
        return self._divisible


def monkey_business(monkeys, worry_factor, turns):
    for _ in range(turns):
        for monkey in monkeys:
            tosses = monkey.turn(worry_factor)
            for toss in tosses:
                monkeys[toss[0]].catch(toss[1])
    first, second = sorted(map(lambda m: m.inspect_count(), monkeys))[-2:]
    return first * second


def load_monkeys(fn):
    monkeys = []
    with open(fn) as data:
        while True:
            if data.readline():
                monkeys.append(Monkey(data))
            else:
                break
    return monkeys


print("Part 1")
print(monkey_business(load_monkeys('data/day11.txt'), lambda x: x // 3, 20))  # 54054

print("Part 2")
monkeys = load_monkeys('data/day11.txt')
lcm = prod(map(lambda m: m.divisor(), monkeys))
print(monkey_business(monkeys, lambda x: x % lcm, 10000))  # 14314925001
