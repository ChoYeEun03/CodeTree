n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt=0
mcnt =0
def count(n):
    global cnt
    if n==0:
        if arr[n]>t:
            cnt +=1
        return cnt
    if arr[n]>t:
        cnt +=1
        return count(n-1)
    else:
        return cnt

for i in range(n):
    cnt = count(i)
    if cnt > mcnt:
        mcnt = cnt
    cnt =0

if cnt > mcnt:
    mcnt = cnt

print(mcnt)













