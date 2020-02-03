myList = []

resultDict = dict()

nameField1 = "Название"
nameField2 = "Цена"
nameField3 = "Количество"
nameField4 = "ед"


i = 1;
while True:
    tempDict = dict()
    name = input("Введите название или 0 для выхода: ")
    if name == "0":
        break
    if name == "":
        continue
    tempDict[nameField1] = name
    cash = float(input("Введите цену: "))
    tempDict[nameField2] = cash
    count = int(input("Введите количество: "))
    tempDict[nameField3] = count
    ed = input("Введите единицы измерения: ")
    tempDict[nameField4] = ed
    print(tempDict)
    myList.append(tuple((i, tempDict)))
    i += 1
    del tempDict
del i

print(myList)
