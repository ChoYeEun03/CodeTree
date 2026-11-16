n,t = map(int, input().split(" "))
r,c,d= input().split()
dx, dy = [1,0,-1,0],[0,-1,0,1]
dic = {"U":1, "D":3, "R":0, "L":2}
a = dic[d]



flag = True
ny = int(c)
nx = int(r)
for i in range(t):
    if ((ny ==1 and d =="L") or (ny ==n and d =="R")) and flag :
        a= (a+2)%4
        if d =="L":
            d = "R"
        else:
            d = "L"
        flag = not flag
        continue
    elif ((nx ==n and d =="D") or (nx ==1 and d =="U"))and flag:
        a= (a+2)%4
        if d=="D":
            d = "U"
        else:
            d = "D"
        flag = not flag
        continue
    ny = dx[a] + ny 
    nx = dy[a] + nx
    flag = True

print(f"{nx} {ny}")

        




