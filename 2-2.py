boxes = open('2.txt').read().split('\n')

for box1 in boxes:
    for box2 in boxes:
        if box1 == box2:
            continue
        if sum([int(x != y) for x, y in zip(box1, box2)]) == 1:
            print ''.join([x for x, y in zip(box1, box2) if x == y])