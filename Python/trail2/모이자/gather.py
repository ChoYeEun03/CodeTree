import sys
near = sys.maxsize
n= int(input())
arr= list(map(int, input().split()))

for i in range(n):
    sum = 0
    for j in range(n):
        if i>j:
            sum += (i-j)*arr[j]
        elif i<j:
            sum +=(j-i)*arr[j]
    if near>sum:
        near = sum
print(near)


