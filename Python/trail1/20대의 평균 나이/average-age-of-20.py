cnt=0
sum=0
while True:
    a=int(input())
    if a>=30 or a<20:
        break
    
    sum+=a
    cnt+=1
if cnt>0:
    avg = sum/cnt
print(f"{avg:.2f}")
