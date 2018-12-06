data = open('6.txt').read().split('\n')

min_x = None
max_x = None
min_y = None
max_y = None

for c in data:
    c = map(int, c.split(', '))
    if not min_x or c[0] < min_x:
        min_x = c[0]
    if not max_x or c[0] > max_x:
        max_x = c[0]
    if not min_y or c[1] < min_y:
        min_y = c[1]
    if not max_y or c[1] > max_y:
        max_y = c[1]

grid = [['.' for x in xrange(min_x, max_x+1)] for y in xrange(min_y, max_y+1)]


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

valid = 0

for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        total = 0
        for z, c in enumerate(data):
            c = map(int, c.split(', '))
            d = manhattan([x+min_x, y+min_y], c)
            total += d
        if total < 10000:
            grid[y][x] = '#'
            valid += 1
print valid