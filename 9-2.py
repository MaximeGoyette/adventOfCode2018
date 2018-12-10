from blist import blist

data = '10 players; last marble is worth 1618 points'

data = open('9.txt').read()

n_players = int(data.split(' ')[0])
final_score = int(data.split(' ')[-2])*100

board = blist([0])

current_i = 0
current_p = 0
last_score = 0

scores = [0 for _ in xrange(n_players)]

for next_m in xrange(1, final_score):

    if next_m%23 == 0:
        last_score = next_m
        next_i = (current_i - 7)%len(board)
        last_score += board.pop(next_i)
        scores[current_p] += last_score
    else:
        next_i = (current_i + 1)%len(board) + 1
        board.insert(next_i, next_m)

    next_m += 1
    current_i = next_i
    current_p = (current_p + 1)%n_players


print max(scores)