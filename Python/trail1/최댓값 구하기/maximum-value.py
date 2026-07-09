a,b,c = map(int,input().split())

max=a
if b>= a and b>=c:
    max =b
if c>=b and c>=a:
    max =c
if a>=b and a>=c:
    max =a



print(max)