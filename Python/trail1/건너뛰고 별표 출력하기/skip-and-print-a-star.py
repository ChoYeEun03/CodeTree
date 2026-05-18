n = int(input())

for i in range(n-1, -1, -1):
    for j in range(n-i):
        print("*", end = "")
    print()
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end = "")
    print()
    print()
