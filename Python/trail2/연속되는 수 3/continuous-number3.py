n=int(input())
arr=[]

cnt =1
maxcnt =1
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if i==0:
        continue
    if arr[i] >0 and arr[i-1]>0:
        cnt+=1
    elif arr[i]<0 and arr[i-1]<0:
        cnt +=1
    else:
        if cnt > maxcnt:
            maxcnt = cnt
        cnt =1
if cnt > maxcnt:
        maxcnt = cnt
print(maxcnt)











