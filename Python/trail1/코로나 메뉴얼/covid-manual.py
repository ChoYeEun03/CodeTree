cnt=0
dict={"A":0, "B":0, "C":0, "D": 0}
for i in range(3):
    a,b = input().split(" ")
    if a =='Y' and int(b)>=37:
        flag ="A"
    elif a=='N' and int(b)>=37:
        flag = "B"
    elif a=="Y" and int(b)<37:
        flag = "C"
    else:
        flag = "D"
    dict[flag] +=1


if dict["A"] >=2:
    print("E")
else:
    print("N")
