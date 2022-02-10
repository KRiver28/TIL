board = []
for _ in range(5):
    word = list(input())
    board.append(word+((15-len(word))*['']))

for i in zip(*board):
    print(''.join(i),end='')