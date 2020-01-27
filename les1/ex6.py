firstDistance = float(input("Км за первый день: "))
expectedResult = float(input("Ожидаемый результат: "))
growth = 0.1

distanceNow = firstDistance
day = 1
while distanceNow < expectedResult:
    distanceNow += (firstDistance * growth)
    day += 1

print("На", day, "день достигнут результат не менее",round(expectedResult) , "км")