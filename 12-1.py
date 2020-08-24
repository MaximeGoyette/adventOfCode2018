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
####. => #'''
#data = open('12.txt').read()

initial_state = data.split('\n')[0].split(': ')[1]

spread = [x.split(' => ') for x in data.split('\n')[2:]]
spread = {x:y for x, y in spread}
#spread = {frozenset([i - 2 for i, x in enumerate(k) if x == '#']):v == '#' for k, v in spread}

def next_state(previous_state):
    previous_state = '.....' + previous_state + '.....'
    state = ''
    for i in xrange(2, len(previous_state) - 2):
        x = previous_state[i - 2:i + 3]
        state += spread.get(x, '.')
    return state.strip('.')

state = initial_state

for _ in xrange(20):
    state = next_state(state)

print sum([i for i, x in enumerate(state) if x == '#'])


