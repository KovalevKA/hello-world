n = input("Введите число: ")

summ = 0

for i in range(1, int(n) + 1):
    summ += int(n*i)

print("Сумма = ", summ)