Y, M, D = map(int, input().split())
monthy = [0,31,29,31,30,31,30,31,31,30,31,30,31]
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
mon=month
a= False

def yunyun():
    if Y%100 == 0 and Y%400==0:
        return True
    elif Y%100==0 and Y%400!=0:
        return False
    else:
        return True  
        
def season():
    if M>=3 and M<=5:
        return 'Spring'
    elif M>=6 and M<=8:
        return 'Summer'
    elif M>=9 and M<=11:
        return 'Fall'
    else:
        return 'Winter'


if Y%4==0:
    a = yunyun()
if a:
    mon = monthy
if mon[M] >=D:
    print(season())
else:
    print(-1)
        
