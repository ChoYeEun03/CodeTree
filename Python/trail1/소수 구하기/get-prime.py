n=int(input())

for i in range(1,n+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j==0:
            cnt +=1
    if cnt ==2:
        print(i, end = " ")

# 아래는 정답 코드인데 for i in range(2,2)면 그냥 넘어가서 true를 유지한다는 게 신기해서 남김
# 2도 소수로 출력됨
#n = int(input())
    
# 1부터 n까지 소수를 구합니다.
# for i in range(1, n + 1):
#     if i == 1:
#         continue
#     isprime = True
    
#     for j in range(2, i):
#         if i % j == 0:
#             isprime = False

#     if isprime:
#         print(i, end=" ")
