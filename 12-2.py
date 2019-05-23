from progressbar import progressbar
from PIL import Image

data = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''.split('\n')

data = open('12.txt').read().split('\n')

state = data[0].split(': ')[1]
state = {i for i, x in enumerate(state) if x == '#'}

previous_sums = set()
repeated_sums = set()

results = []

rules = {x.split(' ')[0]: x.split(' ')[-1] for x in data[2:]}

def draw(results, repeated_sums):
    try:
        min_s = min(results)
        max_s = max(results)
        im = Image.new('RGB', (len(results), max_s - min_s + 1), 'white')
        px = im.load()

        for i, r in enumerate(results):
            px[i, r - min_s] = (0, 0, 0)

        if len(results)%100 == 0:
            im.show()
            exit()
    except Exception as e:
        print e
        exit()

for g in progressbar(xrange(50000000000)):
    total = sum(state)
    if total in previous_sums:
        repeated_sums.add(total)

    previous_sums.add(total)

    next_state = set()
    for s in state:
        for i in xrange(s - 5, s + 5):
            current = ''.join(['#' if i + j in state else '.' for j in xrange(-2, 3)])
            if current in rules and rules[current] == '#':
                next_state.add(i)
    state = next_state
    results.append(sum(state))

    draw(results, repeated_sums)

print sum(state)
