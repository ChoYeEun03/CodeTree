n = int(input())
arr = [int(input()) for _ in range(n)]
cnt=1
mcnt=1
for i in range(1, n):
    if arr[i]> arr[i-1]:
        cnt +=1
    else:
        if cnt > mcnt:
            mcnt = cnt
        cnt =1

if cnt > mcnt:
    mcnt =cnt
print(mcnt)
        