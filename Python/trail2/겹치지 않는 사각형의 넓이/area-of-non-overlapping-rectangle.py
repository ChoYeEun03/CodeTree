arr = [[0] * 2000 for _ in range(2000)]

for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())

    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000

    for y in range(y1, y2):
        for x in range(x1, x2):
            if i < 2:     
                arr[y][x] = 1
            else:               
                arr[y][x] = 0

cnt = 0

for y in range(2000):
    for x in range(2000):
        if arr[y][x] == 1:
            cnt += 1

print(cnt)