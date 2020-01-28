myList = [7, 5, 3, 3, 2]

while True:

    userInput = int(input("Введите число: "))

    count = myList.count(userInput)

    if count != 0:
        count += myList.index(userInput)
    elif myList[len(myList) - 1] > userInput:
        print(myList)
        count = len(myList)
    else:
        for i in range(0, len(myList)):
            if myList[i] < userInput:
                count = i
                break

    myList.insert(count, userInput)

    print(myList)