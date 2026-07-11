n, m = map(int, input().split(" "))
arr1= list(map(int, input().split(" ")))
arr2= list(map(int, input().split(" ")))
arr3=[]
cnt =0
def find(k):
    global m
    for i in range(m):
        if k >=n:
            return 0
        if arr1[k]==arr2[i]:
            arr3.append(0)
            if k>n:
                return 0
            k+=1
            continue
        else:
            return 0
    return 1
for i in range(n):
    if arr1[i] == arr2[0]:
        k = i
        cnt +=find(k)

if cnt >=1:
    print("Yes")
else:
    print("No")
    




