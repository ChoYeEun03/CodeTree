n = int(input())

for i in range(n):
    for j in range(n):
        if j %2==0:
            print(i+(j%2)+1, end = "")
        else:
            print(n+1-(j%2)-i, end ='')
    
    print()
    