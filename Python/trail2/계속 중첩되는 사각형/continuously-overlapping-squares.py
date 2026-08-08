red=[[0]*200 for _ in range(200)]
blue = [[0]*200 for _ in range(200)]

n=int(input())
offset = 100
cnt=0
def mkred(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            red[i][j]=1
            blue[i][j]=0
def mkblue(a,b,c,d):
    for i in range(a,c):
        for j in range(b,d):
            red[i][j]=0
            blue[i][j]=1


for i in range(n):
    a,b,c,d = map(int,input().split())
    a+=100
    b+=100
    c+=100
    d+=100
    if i%2==0:
        mkred(a,b,c,d)
    else:
        mkblue(a,b,c,d)

for row in blue:
    cnt +=row.count(1)
print(cnt)