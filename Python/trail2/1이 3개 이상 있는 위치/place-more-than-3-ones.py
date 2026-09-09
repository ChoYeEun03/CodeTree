n= int(input())
dx , dy = [1,-1,0,0], [0,0,1,-1]
arr = list()
cnt =0
mcnt=0
for i in range(n):
    arr.append(input().split())

def rightplace(k,l):
    return 0<=k and k<n and l>=0 and l<n

for i in range(n):
    for j in range(n):
        for x, y in zip(dx, dy):
            nx, ny = x+i, y+j
            if rightplace(nx,ny) and arr[nx][ny]=='1':
                cnt +=1   
        if cnt >=3:
            mcnt +=1
        cnt =0
print(mcnt)








