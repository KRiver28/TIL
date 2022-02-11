#큰 도화지 만들기 100 * 100 size
paper = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1,y1,x2,y2 =map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j]=1

total=0
for i in range(100):
    for j in range(100):
        total+=paper[i][j]
print(total)