m1, d1, m2, d2 = map(int, input().split())
A = input()

mon=[0,31,29,31,30,31,30,31,31,30,31,30,31]
week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day =0
count =0
for i in week:
    if A==i:
        break
    else:
        count+=1

while True:
    if m1==m2 and d1==d2:
        break
    day+=1
    d1+=1

    if d1 > mon[m1]:
        d1=1
        m1+=1
final = day - count
final = int(final/7 + 1)
print(final)


















