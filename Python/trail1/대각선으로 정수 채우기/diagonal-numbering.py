n, m = map(int, input().split())
arr=[[0]*m for _ in range(n)]
cnt = 1

k=0
l=0
q=0
p=0
for i in range(n*m):
    arr[k][l]=cnt
    cnt+=1
    if l==0:
        if q<m-1:
            q+=1
            l=q
            k=0
        else:
            p+=1
            k=p
            l=m-1
    elif k==n-1:
        if q<m-1:
            q+=1
            l=q
            k=0
        else:
            p+=1
            k=p
            l=m-1
    else:
        k+=1
        l-=1

    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
    





