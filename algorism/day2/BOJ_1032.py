n=int(input())
word = list(input())

for i in range(n - 1):
    #words = list(input())
    words = input()
    for j in range(len(word)):
        if word[j] != words[j]:
            word[j] = '?'

print(''.join(word))