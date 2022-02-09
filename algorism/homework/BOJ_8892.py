T=int(input())

for i in range(T):
    k=int(input())
    dic=[]
    check=0
    for i in range(k):
        dic.append(input())
       
    for i in range(k):
        for j in range(k):
            if i==j:
                pass
            else:
                combine=dic[i]+dic[j]
                if combine == combine[::-1]:
                    check=combine
    if check !=0:
        print(check)
    else:
        print(0)
                    