arr = list(map(int, input().split()))
n = len(arr)
arr2=[]
arr3=[]
sum =0
sum2=0
count = 0
for i in range(n):
    if i%2!=0:
        sum += arr[i]
    if i%3==2:
        sum2+=arr[i]
        count +=1
print(f'{sum} {round(sum2/count, 1)}')

