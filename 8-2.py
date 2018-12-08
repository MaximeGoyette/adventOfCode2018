data = open('8.txt').read().split(' ')

data = map(int, data)

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

    return {
        'children': children,
        'metadata': metadata
    }, data

tree, data = parser(data)

def value(node):
    if node['children']:
        return sum([value(node['children'][m - 1]) if m <= len(node['children']) else 0 for m in node['metadata']])
    else:
        return sum(node['metadata'])

print value(tree)