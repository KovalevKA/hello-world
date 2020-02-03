def SumMax(temp):
    temp.remove(min(temp))
    summ = 0
    for item in temp:
        summ += item
    return summ

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(SumMax([x, y, z]))