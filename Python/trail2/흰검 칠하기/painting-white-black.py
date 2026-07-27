n=int(input())
segments = [tuple(input().split()) for _ in range(n)]
dic ={
    0 : ['0', 0, 0]
}
wc =0
bc=0
gc=0
current =0
cnt=0
def confirm(n):
    if n not in dic:
        dic[n] = ['0', 0, 0]
        # black white

def gray(n):
    if dic[n][1] >=2 and dic[n][2]>=2:
        dic[n][0]='gray'
        return True

for a, b in segments:
    for i in range(int(a)):
        if b=='R':
            confirm(current)
            dic[current][0]='black'
            dic[current][1] +=1
            if gray(current):
                cnt+=1
                if cnt==int(a):
                    cnt=0
                    break
                current +=1
                continue       
            cnt+=1
            if cnt==int(a):
                cnt=0
                break
            current +=1
        else:
            confirm(current)
            dic[current][0]='white'
            dic[current][2] +=1
            if gray(current):
                cnt+=1
                if cnt==int(a):
                    cnt=0
                    break
                current -=1          
                continue
            cnt+=1
            if cnt==int(a):
                cnt=0
                break
            current-=1

for key, value in dic.items():
    if value[0] == 'white':
        wc +=1
    elif value[0]=='black':
        bc+=1
    elif value[0]=='gray':
        gc+=1

print(f'{wc} {bc} {gc}')









