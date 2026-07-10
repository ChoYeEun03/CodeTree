n, q = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

def first(n):
    print(arr[n-1])
def second(n):
    for i in range(len(arr)):
        if arr[i]==n:
            print(i+1)
            return True
    print(0)

def third(n,m):
    for i in range(n-1,m):
        print(arr[i], end = " ")
    print()





for i in range(q):
    arr2 = list(map(int, input().split()))
    if arr2[0]==1:
        first(arr2[1])
    if arr2[0]==2:
        second(arr2[1])
    if arr2[0]==3:
        third(arr2[1], arr2[2])
