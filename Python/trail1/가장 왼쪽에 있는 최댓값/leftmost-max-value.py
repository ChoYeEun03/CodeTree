n = int(input())
a = list(map(int, input().split()))
max=a[0]

while True:
    l=0
    for i in range(n):
        if a[i]>max:
            max = a[i]
            l=i
    print(l+1, end = " ")
    if max ==a[0]:
        break
    k=n-1

    while k!= l-1:
        a.pop(k)
        k=k-1
        n=n-1

    max=a[0]

    
    
    
