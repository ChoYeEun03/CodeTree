a, b = map(int,input().split())
arra=[]
arrb=[]
atotal = []
btotal = []
sa = 0
sb = 0
count = 0
flag = True
#a가 앞서면 True b면 False
for i in range(a):
    arra.append(list(map(int,input().split())))

for i in range(b):
    arrb.append(list(map(int,input().split())))

for i in range(len(arra)):
    for j in range(arra[i][1]):
        sa +=arra[i][0]
        atotal.append(sa)

for i in range(len(arrb)):
    for j in range(arrb[i][1]):
        sb +=arrb[i][0]
        btotal.append(sb)

for i in range(len(atotal)):
    if i==0:
        if atotal[0]>btotal[0]:
            flag = True
        elif btotal[0]>atotal[0]:
            flag = False
        continue
    
    if atotal[i]>btotal[i]:
        if flag:
            continue
        else:
            count +=1
            flag = True
    elif btotal[i]> atotal[i]:
        if not flag:
            continue
        else:
            count +=1
            flag =False

print(count)














