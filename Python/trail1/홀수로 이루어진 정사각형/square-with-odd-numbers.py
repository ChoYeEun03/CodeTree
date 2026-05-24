n=int(input())

for i in range(0,n+n,2):
    for j in range(11,11+n+n,2):
        print(j+i, end =' ')
    print()