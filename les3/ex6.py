def word2Title (word):
    return word.title()

userInput = input("Введите строку: ").split()

for item in userInput:
    print(word2Title(item), end = ' ')