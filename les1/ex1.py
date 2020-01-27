var1 = 1
var2 = "два"

var3 = 0
var4 = ""

print("Переменаая 1 = ", var1, "переменная 2 = ", var2)

while True:
    var3 = input("Введите число:")
    if var3 == "exit" : break
    var4 = input("Введите текст:")
    if var4 == "exit" : break
    print("Переменаая 3 = ", var3, "переменная 4 = ", var4)

print("Завершено")
