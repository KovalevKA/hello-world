list = []
dict = dict()
for i in range(1, 13):
    if i > 2 and i < 6: text = "Весна"
    elif i > 5 and i < 9: text = "Лето"
    elif i > 8 and i < 12: text = "Осень"
    else: text = "Зима"
    list.insert(i, text)
    dict[i] = text

userMonth = int(input("Введите номер месяца: "))

if userMonth > 12 or userMonth < 1:
    print("Нет такого месяца")
    exit(0)

print(list[userMonth-1])
print(dict[userMonth])
