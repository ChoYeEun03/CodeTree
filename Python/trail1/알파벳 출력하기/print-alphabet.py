n = int(input())
a=ord('A')
b=ord('Z')
for i in range(n):
    for j in range(i+1):
        print(chr(a), end = "")
        a+=1
        if a== b+1:
            a = ord('A')
    print()
            