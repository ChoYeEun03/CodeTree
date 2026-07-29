n= int(input())
cnt=0


arr=[[0]*200 for _ in range(200)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 +=100
    y1+=100
    y2+=100
    x2+=100
    for i in range(y2-y1):
        for j in range(x2-x1):
            arr[x1+j][y1+i] +=1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]>0:
            cnt+=1
print(cnt)
    
    



