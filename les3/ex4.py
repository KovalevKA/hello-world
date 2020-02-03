def stNum1 (x, y):
    rez = 1
    for i in range(0, abs(y)):
        rez *= (1/x)
    return rez

def stNum2(x, y):
    rez = 0;
    for i in range(0, abs(y)):
        for j in range(0, (i*(abs(y)))):
            rez += x

    return rez

print (stNum2(5, 5))