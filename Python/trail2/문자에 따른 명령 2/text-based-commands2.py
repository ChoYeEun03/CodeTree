arr = list(input())
dx, dy = [0,-1, 0,1], [1,0,-1,0]
dist = 0
nx, ny = 0,0
for i in arr:
    if i =='L':
        dist = (dist+1)%4
    elif i =='R':
        dist = (dist-1)%4
    elif i=='F':
        nx, ny = nx + dx[dist], ny+ dy[dist]
print(f'{nx} {ny}')





