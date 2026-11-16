A = input()
start = list()
stop = list()
sum=0
for i in range(len(A)):
    if A[i]=="(":
        start.append(i)
    else:
        stop.append(i)

for i in range(len(start)):
    for j in range(len(stop)):
        if start[i] < stop[j]:
            sum+=1
print(sum)

    

