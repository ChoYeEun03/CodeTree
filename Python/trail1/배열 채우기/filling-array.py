arr = list()
a = list(map(int, input().split()))
for i in range(10):
    b = a[i]
    if b==0:
        break
    else:
        arr.append(b)
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = " ")
    
    