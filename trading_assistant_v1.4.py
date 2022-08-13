from decimal import Decimal
from emoji import emojize


def read(file_name):
    with open(file_name) as file:
        return file.read()


def rewrite(item, file_name):
    with open(file_name, "w") as file:
        file.write(item)
        
        
balance = read("balance.txt")
while True:
    try:
        if balance == "":
            input_balance = input("  Укажите сумму на Вашем балансе, $: ")
        elif balance == "0":
            input_balance = input("  Укажите сумму на Вашем балансе, $: ")
        else:
            break
        Decimal(input_balance)
        rewrite(str(input_balance), "balance.txt")
        balance = read("balance.txt")
    except ArithmeticError:
        print(emojize(":collision::collision::collision: Вводимое значение должно быть числом, повторите попытку."
                      "\n      Также не принимаются числа через запятую."))

volume = read("volume.txt")
while True:
    try:
        Decimal(volume)
        break
    except ArithmeticError:
        rewrite(str(Decimal(balance) * Decimal(12.5) // 100 * 100), "volume.txt")
        volume = read("volume.txt")

results = read("results.txt")
while True:
    try:
        Decimal(results)
        break
    except ArithmeticError:
        rewrite(str(0), "results.txt")

day_results = read("day_results.txt")
while True:
    try:
        Decimal(day_results)
        break
    except ArithmeticError:
        rewrite(str(0), "day_results.txt")

while True:
    while True:
        one_trade_result = input("  Результат сделки, %: ")

        try:
            one_trade_result = Decimal(one_trade_result)
            break
        except ArithmeticError:
            print(emojize(":collision::collision::collision: Вводимое значение должно быть числом, повторите попытку."
                          "\n      Также не принимаются числа через запятую."))

    work_volume_day = Decimal(balance) * Decimal(12.5) // 100 * 100
    new_volume = Decimal(volume)
    changed_balance = new_volume * (100 + one_trade_result - Decimal(str(0.1))) / 100
    new_balance = int((Decimal(balance) + changed_balance - new_volume) * 100) / 100

    rewrite(str(Decimal(results) + one_trade_result - Decimal(str(0.1))), "results.txt")

    rewrite(str(Decimal(day_results) + one_trade_result), "day_results.txt")

    results = read("results.txt")

    if Decimal(results) < -0.5:
        rewrite(str(int(volume) - 100), "volume.txt")
        rewrite(str(0), "results.txt")

    elif Decimal(results) > 1:
        rewrite(str(int(volume) + 100), "volume.txt")
        rewrite(str(0), "results.txt")

    if one_trade_result == 0:
        rewrite(str(int(work_volume_day)), "volume.txt")
        rewrite(str(one_trade_result), "day_results.txt")
        rewrite(str(0), "results.txt")
    else:
        rewrite(str(new_balance), "balance.txt")

    volume = read("volume.txt")
    results = read("results.txt")
    day_results = read("day_results.txt")

    if Decimal(day_results) < -1.5:
        print(emojize(":chart_decreasing:  На сегодня торговля окончена"))
        break
    else:
        if results == "0":
            print(emojize(":warning:Ваш актуальный объем: " + volume + "$"))
        else:
            print("  Ваш актуальный объем: " + volume + "$")
