
poul = list(input().split())
dic = {}
cnt = len(poul)
for i in poul:
    dic[i] = poul.count(i)
    if cnt > poul.count(i):
        cnt = poul.count(i)
for i in dic:
    if dic[i] == cnt:
        print(i)
print(cnt)
