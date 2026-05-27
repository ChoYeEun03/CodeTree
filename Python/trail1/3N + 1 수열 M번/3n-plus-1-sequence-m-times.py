n = int(input())
cnt=0
for i in range(n):
    m=int(input())
    while m!=1:
        if m%2==0:
            m=m/2
            cnt+=1
        else:
            m= m*3+1
            cnt+=1
    print(cnt)
    cnt=0

