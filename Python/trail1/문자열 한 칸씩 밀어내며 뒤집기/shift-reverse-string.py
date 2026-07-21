input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

def first():
    global input_str
    input_str = input_str[1:] + input_str[0]
    return input_str

def second():
    global input_str
    input_str= input_str[-1]+input_str[:-1]

def third():
    global input_str
    real = list()
    for i in range(len(input_str)-1, -1, -1):
        real += input_str[i]
    input_str = ''.join(real)


for i in queries:
    if i==1:
        first()
    elif i==2:
        second()
    else:
        third()
    print(input_str)


