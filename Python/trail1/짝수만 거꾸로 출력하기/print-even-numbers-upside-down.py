n=int(input())
arr = list(map(int, input().split()))
arr2=list()
for i in arr:
    if i %2==0:
        arr2.append(i)
for i in range(len(arr2)):
    print(arr2.pop(), end = " ")
