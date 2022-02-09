test=int(input())

for i in range(test):
    R,S=input().split()
    R=int(R)
    result=""
    for j in S:
        result+=j*R
    print(result)
    
