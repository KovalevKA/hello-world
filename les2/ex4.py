string = input("Введите строку: ")

list = string.split()

i = 1
for item in list:
    print(i, ":", item[:10])
    i += 1