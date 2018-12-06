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

for y, line in enumerate(grid):
    for x, cell in enumerate(line):
        pairs = []
        for z, c in enumerate(data):
            c = map(int, c.split(', '))
            d = manhattan([x, y], c)
            pairs.append((d, str(z)))
        pairs.sort()
        if pairs[0][0] == pairs[1][0]:
            continue
        grid[y][x] = pairs[0][1]


flat_grid = [item for sublist in grid for item in sublist]

from collections import Counter

def is_infinite(c):
    for x in xrange(min_x, max_x+1):
        if grid[min_y-min_y][x-min_x] == c:
            return True
        if grid[max_y-min_y][x-min_x] == c:
            return True
    for y in xrange(min_y, max_y+1):
        if grid[y-min_y][min_x-min_x] == c:
            return True
        if grid[y-min_y][max_x-min_x] == c:
            return True
    return False

for candidate in Counter(flat_grid).most_common():
    if is_infinite(candidate[0]):
        continue

    print candidate
    exit()