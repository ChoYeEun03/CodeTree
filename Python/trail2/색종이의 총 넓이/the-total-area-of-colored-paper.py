n = int(input())
arr = [[0]*200 for _ in range(200)]
offset = 100
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    a +=100
    b+=100
    for j in range(8):
        for k in range(8):
            arr[a+j][b+k] =1

for row in arr:
    cnt += row.count(1)

print(cnt)









