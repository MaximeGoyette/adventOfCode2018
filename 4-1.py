import re

data = open('4.txt').read().split('\n')

data.sort()

guards = {}

last_g = None
start = None

for i in xrange(len(data)):
    line = data[i]
    if 'Guard' in line:
        y, month, d, h, m, g = re.match(r'\[(\d+)-(\d+)-(\d+)\ (\d+)\:(\d+)\]\ Guard\ \#(\d+)\ ', line).groups()
        last_g = g
        if not g in guards:
            guards[g] = []
    elif 'falls' in line:
        y, month, d, h, m = re.match(r'\[(\d+)-(\d+)-(\d+)\ (\d+)\:(\d+)\]\ falls\ ', line).groups()
        start = m
    else:
        y, month, d, h, m = re.match(r'\[(\d+)-(\d+)-(\d+)\ (\d+)\:(\d+)\]\ wakes\ ', line).groups()
        guards[last_g].append(range(int(start), int(m)))

best_guard = None
best_guard_score = 0

for g in guards:
    guard = guards[g]
    total = sum(map(len, guard))
    if total > best_guard_score:
        best_guard_score = total
        best_guard = g

from collections import Counter

all_minutes = []

for m in guards[best_guard]:
    all_minutes += m

print int(Counter(all_minutes).most_common()[0][0])*int(best_guard)