n= int(input())
segments = [tuple(input().split()) for _ in range(n)]

max = 100000
arr=[0]*(max*2 +1)
cur = max
bc=0
wc =0
for a, b in segments:
    x= int(a)
    while x>0:
        if b=='R':
            arr[cur]= 1
            x-=1
            if x:
                cur +=1
        else:
            arr[cur]=2
            x-=1
            if x:
                cur -=1

for i in arr:
    if i == 1:
        bc+=1
    if i==2:
        wc +=1
print(f'{wc} {bc}')








