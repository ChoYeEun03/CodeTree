cnt=int(input())
arr=list(map(float,input().split()))

sum1=sum(arr)
avg= round(sum1/cnt,1)
print(avg)
if avg>= 4.0:
    print("Perfect")
elif avg>=3.0:
    print("Good")
else:
    print("Poor")



