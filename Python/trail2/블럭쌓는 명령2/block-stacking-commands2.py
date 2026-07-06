n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
list = [0]*n

for a,b in commands:
    for i in range(a-1,b):
        list[i] +=1
max = list[0] 
for i in list:
    if i>max:
        max = i

print(max)




