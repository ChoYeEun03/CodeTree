a,b = map(int, input().split())
arr=[0]*10
total = 0
while True:
    if a<=1:
        break
    c = a%b
    arr[c] +=1
    a//=b
for x in arr:
    total += x*x
print(total)
