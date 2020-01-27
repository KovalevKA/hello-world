userTime = int(input("Введите колличество секунд: "))

hours = userTime // 3600
userTime -= (hours * 3600)

minutes = userTime // 60
userTime -= (minutes * 60)

print("{} часов {} минут {} секунд".format(hours, minutes, userTime))