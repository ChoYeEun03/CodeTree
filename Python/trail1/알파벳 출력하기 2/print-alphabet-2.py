n = int(input())
a= ord('A')
b=ord('Z')
for i in range(n):
    for j in range(n):
        if i>j:
            print(" ", end = " ")
        else:
            print(chr(a), end = " ")
            a+=1
            if a==b+1:
                a=ord('A')
    print()
