data = open('1.txt').read().split('\n')

print sum(map(int, data))