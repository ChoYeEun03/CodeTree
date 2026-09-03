a,b = map(int, input().split())
lista=[]
listb=[]
atotal = []
btotal = []
sa = 0
sb = 0
count =0
for i in range(a):
    lista.append(list(input().split()))
for i in range(b):
    listb.append(list(input().split()))

for i in range(len(lista)):
    for j in range(int(lista[i][0])):
        if lista[i][1] =='R':
            sa += 1
            atotal.append(sa)
        else:
            sa -=1
            atotal.append(sa)
for i in range(len(listb)):
    for j in range(int(listb[i][0])):
        if listb[i][1] =='R':
            sb += 1
            btotal.append(sb)
        else:
            sb -=1
            btotal.append(sb)

mini = min(len(atotal), len(btotal))
maxi = max(len(atotal),len(btotal))

for i in range(maxi):
    if i==0:
        continue
    if i < mini:
        if atotal[i]==btotal[i] and atotal[i-1]!=btotal[i-1]:
            count +=1
    elif i >= mini and len(atotal) ==mini:
            if atotal[mini-1]==btotal[i] and atotal[mini-1]!=btotal[i-1]:
                count +=1
    elif i >= mini and len(btotal) ==mini:
            if btotal[mini-1]==atotal[i] and btotal[mini-1]!=atotal[i-1]:
                count +=1

print(count)






