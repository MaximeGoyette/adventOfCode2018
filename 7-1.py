import pydash
from copy import deepcopy

data = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''.split('\n')

data = open('7.txt').read().split('\n')

g = {}
letters = set()

for step in data:
    a = step.split(' ')[1]
    b = step.split(' ')[7]

    letters.add(a)
    letters.add(b)

    if not b in g:
        g[b] = []
    g[b].append(a)


final_order = []

while len(g) > 0:
    candidates = []
    for l in letters:
        if not l in g:
            candidates.append(l)
    candidates.sort()

    final_order.append(candidates[0])

    letters.remove(candidates[0])

    for x in g:
        g[x] = list(filter(lambda y: y != candidates[0], g[x]))

    for x in list(g):
        if len(g[x]) == 0:
            del g[x]

if len(letters):
    final_order.append(list(letters)[0])

print ''.join(final_order)
