a, b, c, d = map(int, input().split())
x, y, p, q = map(int, input().split())
area = 0
if x<=a and y<=b and p>=c and q>=d:
    area = 0
elif c>x and p>=c and q>=d and b>=y:
    area = (x-a)*(d-b)
elif p>a and a>=x and q>=d and b >=y:
    area = (c-p)*(d-b)
elif d>y and q>=d and p>=c and a>=x and y>b:
    area = (c-a)*(y-b)
elif b>y and q>b and x<=a and c<=p and d>q:
    area = (c-a)*(d-q)
else:
    area = (c-a)*(d-b)
print(area)








