from collections import Counter

boxes = open('2.txt').read().split('\n')

def has_n(box, n):
    c = Counter(box)
    return any([c[l] == n for l in c])

two = 0
three = 0

for box in boxes:
    if has_n(box, 2):
        two += 1
    if has_n(box, 3):
        three += 1

print two*three