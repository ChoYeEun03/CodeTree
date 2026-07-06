N, B = map(int, input().split())
digits=[]
if B==4:
    while True:
        if N<4:
            digits.append(N)
            break
        digits.append(N%4)
        N//=4
else:
    while True:
        if N<8:
            digits.append(N)
            break
        digits.append(N%8)
        N//=8
for digit in digits[::-1]:
    print(digit, end = "")






