T=int(input())
for _ in range(T):
    a, b = input().split()
    a=int(a)
    print(f'{b[:a-1]+b[a:]}')