C=int(input())

for _ in range(C):
    board = list(map(int, input().split()))
    avg=sum(board[1:])/board[0]
    cnt=0
    for j in board[1:]:
        if j > avg:
            cnt += 1
    print(f'{cnt/board[0]*100:.3f}%')