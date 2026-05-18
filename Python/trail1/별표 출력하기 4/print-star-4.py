n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(n-1):
    for j in range(i+2):
        print("*", end = " ")
    print()