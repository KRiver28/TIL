blocks= [int(i) for i in input().split()]
a=0
while blocks!=sorted(blocks):
    for i in range(4):
        if blocks[i]>blocks[i+1]:
           blocks[i+1],blocks[i]=blocks[i],blocks[i+1]
           print(' '.join(map(str, blocks))) 
