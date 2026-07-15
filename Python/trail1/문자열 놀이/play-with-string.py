a,b =input().split()
a=list(a)
def first(n,m):
    n=int(n)
    m=int(m)

    a[n-1], a[m-1]=a[m-1],a[n-1]
    print(''.join(a))


def second(n,m):
    for i in range(len(a)):
        if a[i] == n:
            a[i]=m
            
    print(''.join(a))

for i in range(int(b)):
    c,d,e = input().split()
    if c=="1":
        first(d,e)
    elif c=="2":
        second(d,e)
    
