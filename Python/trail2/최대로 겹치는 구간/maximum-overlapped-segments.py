n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

list = [0]*201
cnt=0
for a,b in segments:
    a+=100
    b+=100
    
    for j in range(a,b):
        list[j]+=1
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)









