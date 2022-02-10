board = list(sum(map(int, input().split())) for _ in range(5))
won=max(board)
print(board.index(won)+1, won)