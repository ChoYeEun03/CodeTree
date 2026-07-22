n = int(input())
arr = [0]*1000
point = 499
cnt =0
for i in range(n):
    k,l = input().split()
    if l =='R':
        for _ in range(int(k)):
            arr[point] +=1
            point +=1
    if l =='L':
        for _ in range(int(k)):
            point -=1
            arr[point] +=1

for i in arr:
    if i>=2:
        cnt +=1
print(cnt)
