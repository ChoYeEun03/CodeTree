N = input()
n=0
digits=[]
for i in N:
    n= n*2 + int(i)
n= n*17

while True:
    if n<2:
        digits.append(n)
        break
    digits.append(n%2)
    n//=2

for i in digits[::-1]:
    print(i, end = "")



