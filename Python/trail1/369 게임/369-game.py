n = int(input())

for i in range(1, n+1):
    if i %3 ==0:
        print(0, end = " ")
        continue
    if i <10:
        print(i, end = " ")
        continue
    m = i //10 
    if m == 3 or m ==6 or m==9:
        print(0, end = " ")
        continue
    k = i %(10*m)
    if k ==3 or k ==6 or k ==9:
        print(0, end = " ")
        continue
    print(i, end = " ")
    
    

