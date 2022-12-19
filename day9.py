DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def decode_segment(index):
    if index == 0:
        return 'H'
    else:
        return str(index)


def print_board(size, snake):
    for i in reversed(range(size)):
        for j in range(size):
            try:
                print(decode_segment(snake.index([j, i])), end='')
            except:
                print('.', end='')
        print('')


def print_seen(size, seen):
    for i in reversed(range(size)):
        for j in range(size):
            if (i, j) in seen:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def step_snake(snake, direction):
    snake[0][0] += DIRECTIONS[direction][0]
    snake[0][1] += DIRECTIONS[direction][1]
    for i in range(len(snake) - 1):
        front, current = snake[i: i + 2]
        delta_x = front[0] - current[0]
        delta_y = front[1] - current[1]
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            current[0] += max(min(delta_x, 1), -1)
            current[1] += max(min(delta_y, 1), -1)
        else:
            break


def wiggle_snake(length, fn):
    snake = [[26, 26] for _ in range(length)]
    seen = set()
    seen.add(tuple(snake[-1]))
    with open(fn) as data:
        for line in data:
            line = line.rstrip()
            direction, count = line.split()
            count = int(count)
            for _ in range(count):
                step_snake(snake, direction)
                seen.add(tuple(snake[-1]))
    return len(seen)


print("Part 1")
print(wiggle_snake(2, 'data/day9.txt'))

print("Part 2")
print(wiggle_snake(10, 'data/day9.txt'))
