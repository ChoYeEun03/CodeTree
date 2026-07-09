n = int(input())
arr = list(map(int, input().split()))

#유클리드 호제법?!?!?!?!?
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

total = 1

for num in arr:
    total = lcm(total, num)
print(total)




