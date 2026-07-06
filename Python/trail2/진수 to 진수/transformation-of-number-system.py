a, b = map(int, input().split())
n = input()
digits=[]
m=0
for i in n:
    m=m*a + int(i)


while True:
    if m<b:
        digits.append(m)
        break
    digits.append(m%b)
    m//=b

for i in digits[::-1]:
    print(i, end = "")




