arr = list(map(int, input().split()))
arr2=list()
sum=0
cnt =0
for elem in arr:
    if elem >= 250:
        break
    else:
        arr2.append(elem)

for i in arr2:
    sum+= i
    cnt +=1
print(sum, end = " ")
print(round(sum/cnt, 1), end = " ")
