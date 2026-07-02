a, b, c = map(int, input().split())

count = 0

if a==11:
    if 11>b:
        print(-1)
    elif b==11 and 11>c:
        print(-1)
    else:
        count += b-11
        count += c-11
        print(count)
else:
    count += (24-11-1)* 60
    count += 60-11
    count += (a-11-1)*1440
    count += b*60
    count += c
    print(count)








# Please write your code here.