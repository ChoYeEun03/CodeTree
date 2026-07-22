n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0]*101

for k,l in segments:
    for j in range(k,l+1):
        arr[j] +=1
max= arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print(max)

        



