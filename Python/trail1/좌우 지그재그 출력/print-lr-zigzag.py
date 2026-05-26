n = int(input())
cnt =0
for i in range(n):
    for j in range(n):
        if i %2==0:
            print(cnt+j+1, end = " ")
        else:
            print(n-j+cnt, end =" ")
    cnt +=n
    print()