m1, d1, m2, d2 = map(int, input().split())


def total_days(m,d):
    mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(1,m):
        total += mon[i]
    total += d
    return total

total = total_days(m2,d2) - total_days(m1,d1)

date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
a = total % 7
print(date[a])




















# Please write your code here.