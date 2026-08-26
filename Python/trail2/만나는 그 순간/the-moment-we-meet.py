n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

n=[]
m=[]
tmp=0
for i in range(len(t)):
    for j in range(t[i]):
        if d[i]=='R':
            tmp +=1
            n.append(tmp)
        else:
            tmp -=1
            n.append(tmp)            
tmp=0
for i in range(len(t2)):
    for j in range(t2[i]):
        if d2[i]=='R':
            tmp +=1
            m.append(tmp)
        else:
            tmp -=1
            m.append(tmp)
k=-1

for i in range(min(len(n),len(m))):
    if n[i]==m[i]:
        k=i+1
        break
    
print(k)
