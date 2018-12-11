serial_number = int(open('11.txt').read())

def get_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id

    digit = int(str(power_level).zfill(3)[-3])
    return digit - 5

grid = [[0 for _ in xrange(300)] for _ in xrange(300)]
for y in xrange(300):
    for x in xrange(300):
        total = 0
        if y == 0 and x == 0:
            grid[y][x] = get_power_level(x, y, serial_number)
        elif y == 0:
            grid[y][x] = get_power_level(x, y, serial_number) + grid[y][x-1]
        elif x == 0:
            grid[y][x] = get_power_level(x, y, serial_number) + grid[y-1][x]
        else:
            grid[y][x] = get_power_level(x, y, serial_number) + grid[y-1][x] + grid[y][x-1] - grid[y-1][x-1]

maximum = None
c = (0, 0, 0)

for y in xrange(300):
    for x in xrange(300):
        for z in xrange(0, 300 - max(x, y)):
            total = grid[y+z][x+z] - (grid[y+z][x-1] if x-1 >= 0 else 0) - (grid[y-1][x+z] if y-1 >= 0 else 0) + (grid[y-1][x-1] if x-1 >= 0 and y-1 >= 0 else 0)
            if maximum == None or total > maximum:
                maximum = total
                c = (x, y, z+1)

print ','.join(map(str, c))