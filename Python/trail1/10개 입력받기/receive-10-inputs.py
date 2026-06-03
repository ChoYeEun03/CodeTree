arr = list(map(int, input().split()))
arr2=list()
sum=0
cnt=0
for i in arr:
    if i==0:
        break
    else:
        arr2.append(i)
        cnt+=1
        sum+=i
print(f"{sum} {round(sum/cnt,1)}")

