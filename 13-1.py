data = '''/->-\        
|   |  /----\\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''.split('\n')

#data = open('13.txt').read().split('\n')

data = map(list, data)

def draw(data):
    for line in data:
        print ''.join(line)

directions = ['^', '>', 'v', '<']
movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
turns = [-1, 0, 1]

def handle_intersection(cart, directions):
    pos, facing, next_turn = cart
    direction = (directions.index(facing) + next_turn)%len(directions)
    next_turn = (next_turn + 1)%len(turns)
    return pos, directions[direction], next_turn

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def move(data, cart, movements):
    pos, facing, next_turn = cart
    candidates = []
    for m in movements:
        next_pos = add(pos, m)
        if data[next_pos[1]][next_pos[0]] != ' ':
            candidates.append(next_pos)
    print candidates


carts = []

for y, line in enumerate(data):
    for x, elem in enumerate(line):
        if elem in directions:
            carts.append(((x, y), elem, 0))

for cart in carts:
    handle_turn(data, cart, movements)

def tick(data, carts):
    pass