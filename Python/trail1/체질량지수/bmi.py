a, b= map(int,input().split())

bmi = 10000 * b // (a * a)



if bmi >=25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)