n,k,p,t = map(int, input().split())
order = []
person = [[-1]*2 for _ in range(n)]
person[p-1][0] = 1
person[p-1][1] = k

for i in range(t):
    tm, a, b = map(int, input().split())
    order.append([tm-1,a-1,b-1])

order.sort(key=lambda x: x[0])

for i in range(len(order)):
    u, x = order[i][1], order[i][2]
    if person[u][0] == 1 and person[u][1] > 0:
        if person[x][0] !=1:
            person[x][0] =1
            person[x][1] = k
        elif person[x][0]==1:
            person[x][1] -=1
        person[u][1] -=1
            
    elif person[x][0] == 1 and person[x][1] > 0:
        if person[u][0] !=1:
            person[u][0] =1
            person[u][1] = k
        elif person[u][0]==1:
            person[u][1] -=1
        person[x][1] -=1



for i in range(n):
    if person[i][0] == 1:
        print("1", end = "")
    elif person[i][0] == 0 or person[i][0] ==-1:
        print("0", end = "")






