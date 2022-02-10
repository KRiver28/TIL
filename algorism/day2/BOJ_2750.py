n = int(input())
lst = [int(input()) for i in range(n)]
lst.sort()
print(*lst,sep='\n')
    