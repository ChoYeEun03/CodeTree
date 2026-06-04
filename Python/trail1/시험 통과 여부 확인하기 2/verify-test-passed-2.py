n=int(input())
flag=0
for i in range(n):
    arr = map(int, input().split())
    cnt=4
    sum=0
    for j in arr:
        sum+=j
    if sum/cnt >=60:
        print("pass")
        flag+=1
    else:
        print("fail")
print(flag)
        