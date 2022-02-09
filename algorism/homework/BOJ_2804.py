#크로스워드 만들기
first, second = input().split()
n,m=len(first),len(second)
first_line, second_line = "",""

#교차점 확인
for i in range(n):
    if first[i] in second:
        first_line = int(i)
        second_line = second.index(first[i])
        break

#크로스워드 작성
for i in range(m):
    if i == second_line:
        print(first)
    else:
        print('.'*(first_line)+second[i]+'.'*(n-first_line))