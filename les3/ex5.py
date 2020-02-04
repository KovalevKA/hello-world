
def Summ (list):

    return sum(list)
summ = 0
flag = True
while flag:
    userInput = input("Строка или q для выхода: ").split()
    temp = []
    for item in userInput:
        if item == "q":
            flag = False
        if item.isdigit():
             temp.append(int(item))

    summ += Summ(temp)
    print(summ)

