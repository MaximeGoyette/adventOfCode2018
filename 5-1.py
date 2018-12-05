data = open('5.txt').read()

types = set(data.lower())
pairs = []

for t in types:
    pairs.append('{}{}'.format(t, t.upper()))
    pairs.append('{}{}'.format(t.upper(), t))

while any([p in data for p in pairs]):
    for p in pairs:
        data = data.replace(p, '')

print len(data)