n=int(input())
dic={}
for _ in range(n):
    country, capital = input().split()
    dic[country] = capital
question=input()
print(dic.get(question, 'Unknown Country'))