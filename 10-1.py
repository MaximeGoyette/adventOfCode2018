import re
from PIL import Image

data = open('10.txt').read().split('\n')


positions = []
velocities = []

for x in data:
    m = re.match(r'position=<([- ]\d+), ([- ]\d+)> velocity=<([- ]\d+), ([- ]\d+)>', x)

    x, y, vx, vy = tuple(map(int, m.groups()))

    positions.append((x, y))
    velocities.append((vx, vy))

def draw(positions, j):
    min_x, max_x, min_y, max_y = None, None, None, None

    for x, y in positions:
        x = x
        y = y
        if min_x == None or x < min_x:
            min_x = x
        elif max_x == None or x > max_x:
            max_x = x
        if min_y == None or y < min_y:
            min_y = y
        elif max_y == None or y > max_y:
            max_y = y

    im = Image.new('RGB', (max_x - min_x + 1, max_y - min_y  + 1), 'black')
    px = im.load()

    for x, y in positions:
        px[x - min_x, y - min_y] = (255, 255, 255)

    im.save('10/{}.png'.format(str(j).zfill(8)))

j = 0

while True:
    print j

    if 10500 < j < 10600:
        draw(positions, j)

    for i, p in enumerate(positions):
        v = velocities[i]
        positions[i] = (p[0] + v[0], p[1] + v[1])

    j += 1