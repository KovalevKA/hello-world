take = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

message = "Фирма работает с "

if take < costs:
    print(message + "убытком")
    exit(0)

profit = ((take-costs) / costs * 100)
print(message + "прибылью. Рентабельность составила ", round(profit, 3), "%")

workers = int(input("Введите численность работников: "))

employeesProfit = ((take - costs)/workers)
print("Каждый работник получет по ", round(employeesProfit, 3))