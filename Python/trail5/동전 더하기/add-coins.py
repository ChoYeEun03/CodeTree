n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
sum =0
for i in coins[::-1]:
    sum+=  k//i
    k = k %i
print(sum)
    




