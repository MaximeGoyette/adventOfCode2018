data = open('5.txt').read()

types = set(data.lower())
l = []

for typ in types:
    c_data = data
    c_data = c_data.replace(typ, '').replace(typ.upper(), '')

    pairs = []

    for t in types:
        pairs.append('{}{}'.format(t, t.upper()))
        pairs.append('{}{}'.format(t.upper(), t))

    while any([p in c_data for p in pairs]):
        for p in pairs:
            c_data = c_data.replace(p, '')

    l.append((len(c_data), c_data))

l.sort()

print l[0][0]