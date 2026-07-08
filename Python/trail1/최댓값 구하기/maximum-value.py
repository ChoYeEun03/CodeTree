a,b,c = map(int,input().split())
max = a

if b> max:
    if c>b:
        max =c
    else:
        max = b
elif c>max:
    max = c
print(max)