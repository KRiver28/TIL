board=[]
for _ in range(8):
    board.append(list(map(str,input())))

#n+m=짝수면 하얀색이다
cnt=0 #말의 수 확인


for n in range(8):
    for m in range(8):
        if (n+m)%2==0:
            if board[n][m]=='F':
                cnt+=1

print(cnt)