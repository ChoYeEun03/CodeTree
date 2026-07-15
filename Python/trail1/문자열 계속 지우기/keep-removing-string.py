A = list(input())
B = list(input())

def callb(n):
    if len(B) > len(A)-n:
            return 0
    for i in range(len(B)):
        if A[n] == B[i]:
            n+=1
        else:
            return 0
    return 1

while True:
    flag = False
    c=0
    for i in range(len(A)):
        if A[i] ==B[0]:
            c=callb(i)
            if c==1:
                m=i
                break
    if c==1:
        for j in range(m+len(B)-1,m-1,-1):
            A.pop(j)
            flag=True
    if flag == False:
        break
    

for i in A:
    print(i, end = "")
        