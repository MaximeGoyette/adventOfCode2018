claims = open('3.txt').read().split('\n')

covered = {}

for c in claims:
    idd = int(c.split('#')[1].split(' ')[0])
    x = int(c.split('@ ')[1].split(',')[0])
    y = int(c.split(',')[1].split(':')[0])
    w = int(c.split(': ')[1].split('x')[0])
    h = int(c.split('x')[1])

    for i in xrange(x, x+w):
        for j in xrange(y, y+h):
            a = (i,j)
            if not a in covered:
                covered[a] = []
            covered[a].append(idd)

for c in claims:
    idd = int(c.split('#')[1].split(' ')[0])
    x = int(c.split('@ ')[1].split(',')[0])
    y = int(c.split(',')[1].split(':')[0])
    w = int(c.split(': ')[1].split('x')[0])
    h = int(c.split('x')[1])

    total = 0
    for i in xrange(x, x+w):
        for j in xrange(y, y+h):
            if len(covered[(i, j)]) == 1:
                total += 1

    if total == w*h:
        print idd