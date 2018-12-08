data = open('8.txt').read().split(' ')

data = map(int, data)

total = 0

def parser(data):
    n = data[0]
    m = data[1]
    data = data[2:]

    children = []
    for i in xrange(n):
        child, data = parser(data)
        children.append(child)

    metadata = data[:m]
    data = data[m:]

    global total
    total += sum(metadata)

    return {
        'children': children,
        'metadata': metadata
    }, data

tree = parser(data)

print total