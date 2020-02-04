def stNum1 (x, y):
    rez = 1
    for i in range(0, abs(y)):
        rez *= (1/x)
    return rez

def stNum2(x, y):
    rez = 0
    return rez

print (stNum1(5, -5))
print (stNum2(5, 5))