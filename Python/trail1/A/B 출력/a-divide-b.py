a, b= map(int, input().split())
remind =  a%b
print(a // b, end=".") 

for i in range(20):
    remind *=10
    print(remind//b, end = "")
    remind %=b
