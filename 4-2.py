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

from collections import Counter

score = []

for g in guards:
    guard = guards[g]
    minutes = [item for sublist in guard for item in sublist]
    try:
        score.append((Counter(minutes).most_common()[0], g))
    except:
        pass

score.sort(reverse=True, key=lambda x: x[0][1])

print int(score[0][1])*score[0][0][0]