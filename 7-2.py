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


resolved = []
queue = sorted(letters - set(g))

workers = {i:[0, '.'] for i in xrange(5)}

def get_cost(l):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(l) + 61

def update_queue(q):
    for x in list(g):
        g[x] = filter(lambda y: not y in resolved, g[x])

    for x in list(g):
        if len(g[x]) == 0:
            del g[x]
            q.append(x)

    return q

total_time = 0

while True:
    for w in sorted(workers):
        if workers[w][0] > 0:
            workers[w][0] -=1
        if workers[w][0] == 0:
            if workers[w][1] != '.':
                resolved.append(workers[w][1])
                workers[w][1] = '.'
                queue = update_queue(queue)

    for w in sorted(workers):
        if workers[w][0] == 0:
            if len(queue) > 0:
                task = queue.pop(0)
                workers[w] = [get_cost(task), task]

    print '\t'.join(map(str, [total_time, ' '.join(map(lambda w: workers[w][1], workers)), ''.join(resolved)]))

    if len(queue) == 0 and all([workers[w][0] == 0 for w in workers]):
        break

    if any([workers[w] == 0 for w in workers]) and len(queue) > 0:
        continue

    total_time += 1