n=int(input())
dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
dist = 0
nx, ny = 0, 0
for i in range(n):
    a, b= input().split()
    if a=='E':
        dist = 0
    elif a =='W':
        dist = 1
    elif a =='N':
        dist = 2
    else:
        dist = 3
    nx, ny = nx+ int(b)*dx[dist], ny+int(b)*dy[dist]

print(f"{nx} {ny}")

