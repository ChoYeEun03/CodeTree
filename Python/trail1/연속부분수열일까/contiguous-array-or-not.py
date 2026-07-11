n, m = map(int, input().split(" "))
arr1= list(map(int, input().split(" ")))
arr2= list(map(int, input().split(" ")))

cnt =0
def find(k):
    for i in range(m):
        if k >=n:
            return 0
        # if arr1[k]==arr2[i]:
        #     if k>n:
        #         return 0
        #     k+=1
        #     continue
        # else:
        #     return 0
        if arr1[k]!=arr2[i]:
            return 0
        k+=1
    return 1
for i in range(n):
    if arr1[i] == arr2[0]:
        k = i
        cnt +=find(k)

if cnt >=1:
    print("Yes")
else:
    print("No")
    




