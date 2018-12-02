data = open('1.txt').read().split('\n')
data = map(int, data)

f = 0
seen = set([f])
i = 0

while True:
    f += data[i%len(data)]
    if f in seen:
        print f
        exit(0)
    seen.add(f)
    i += 1