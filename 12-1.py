data = open('12.txt').read().split('\n')

state = data[0].split(': ')[1]
state = {i for i, x in enumerate(state) if x == '#'}

rules = {x.split(' ')[0]: x.split(' ')[-1] for x in data[2:]}

for g in xrange(20):
    print g, ''.join(['#' if i in state else '.' for i in xrange(-3, max(state) + 1)])
    next_state = set()
    for i in xrange(min(state) - 5, max(state) + 5):
        current = ''.join(['#' if i + j in state else '.' for j in xrange(-2, 3)])
        if current in rules and rules[current] == '#':
            next_state.add(i)
    state = next_state

print sum(state)
