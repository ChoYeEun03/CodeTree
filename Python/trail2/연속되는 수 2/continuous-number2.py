n= int(input())
cnt=1
maxcnt=1
arr=[]
for i in range(n):
    a = int(input())
    arr.append(a)

for i in range(1,n):
    if arr[i]==arr[i-1]:
        cnt +=1

    else:
        if cnt >maxcnt:
            maxcnt = cnt
        cnt =1
if cnt >maxcnt:
        maxcnt = cnt
print(maxcnt)