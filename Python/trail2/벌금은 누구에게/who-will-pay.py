N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
arr = [0]*N
flag = False
for i in range(M):
    if flag:
        break
    x=student[i]
    arr[x-1] +=1
    if arr[x-1] >= K:
        print(x)
        flag = True
if not flag:
    print(-1)









