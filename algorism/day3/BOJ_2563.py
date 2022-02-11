#큰 도화지 만들기 100 * 100 size
paper = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x,y =map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[i+x][j+y]=1

total=0
for i in range(100):
    for j in range(100):
        total+=paper[i][j]
print(total)