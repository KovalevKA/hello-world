userInput = int(input("Введите число: "))

maxNum = 0

while userInput != 0:
    temp = userInput % 10
    maxNum = temp if temp > maxNum else maxNum
    userInput -= temp
    userInput //= 10

print("Самая большая цифра: ", maxNum)

