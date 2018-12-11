serial_number = int(open('11.txt').read())

fuel_cell = [[0 for _ in xrange(300)] for _ in xrange(300)]

def get_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id

    digit = int(str(power_level).zfill(3)[-3])
    return digit - 5

for y in xrange(300):
    for x in xrange(300):
        fuel_cell[y][x] = get_power_level(x, y, serial_number)

v = []

for y in xrange(300 - 2):
    for x in xrange(300 - 2):
        total = 0
        for i in xrange(3):
            for j in xrange(3):
                total += fuel_cell[y + i][x + j]
        v.append((total, x, y))

v.sort(reverse=True)

print ','.join(map(str, v[0][1:]))
