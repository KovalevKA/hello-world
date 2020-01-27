i = 0
count = int(input("Количество элементов: "))

list = []

while i != count:
    list.insert(i, int(input("Введите {} элемент: ".format(i))))
    i += 1

print(list)

for index in range(1, len(list), 2):
    temp = list[index - 1]
    list[index - 1] = list[index]
    list[index] = temp

print(list)