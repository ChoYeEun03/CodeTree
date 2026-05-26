m,n=map(int, input().split())
j =1
for i in range(1, 10):
    for j in range(n,m-2,-2):
        print(f'{j} * {i} = {j * i}', end = " ")
        if j > m:
            print("/", end = " ")
    print()