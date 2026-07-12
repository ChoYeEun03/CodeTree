n = int(input())
a = list(map(int, input().split()))
max1 =a[0]

for i in range(n):
    if a[i]>max1:
        max1=a[i]
a.remove(max1)
max2 =a[0]
for i in range(n-1):
    if a[i]>max2:
        max2 = a[i]

print(f"{max1} {max2}")