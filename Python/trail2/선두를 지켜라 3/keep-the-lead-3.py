n,m = map(int, input().split())
arn = [0]
arm=[0]
flag = -1
count = 0
#a가 선두 0 b가 선두 1 둘다 선두 2
for _ in range(n):
    a,b = map(int, input().split())
    for j in range(b):
        arn.append(arn[-1]+a)
for _ in range(m):
    a,b = map(int, input().split())
    for j in range(b):
        arm.append(arm[-1]+a)

for i in range(min(len(arn),len(arm))):
    if i==0:
        continue
    if arn[i]> arm[i]:
        if flag != 0:
            count +=1
            flag = 0
    elif arn[i]<arm[i]:
        if flag != 1:
            count +=1
            flag = 1
    else:
        if flag !=2:
            count +=1
            flag =2


print(count)



