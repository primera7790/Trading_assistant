from decimal import Decimal
from emoji import emojize


def work_volume_rewrite(item):
    work_volume_file_new = open("../data/volume.txt", "w")
    work_volume_file_new.write(item)
    work_volume_file_new.close()


def results_rewrite(item):
    results_file_new = open("../data/results.txt", "w")
    results_file_new.write(item)
    results_file_new.close()


def day_results_rewrite(item):
    day_results_file_new = open("../data/day_results.txt", "w")
    day_results_file_new.write(item)
    day_results_file_new.close()


balance = open("../data/balance.txt")
read_balance = balance.read()

work_volume_file = open("../data/volume.txt")
read_work_volume = work_volume_file.read()

results_file = open("../data/results.txt")
read_results_file = results_file.read()

day_results_file = open("../data/day_results.txt")
read_day_results = day_results_file.read()

while True:
    results = input("  Результат сделки, %: ")

    try:
        results = Decimal(results)
        break
    except ArithmeticError:
        print(emojize(":collision::collision::collision: Вводимое значение должно быть числом, повторите попытку."
                      "\n      Также не принимаются числа через запятую."))

work_volume_day = Decimal(read_balance) * Decimal(12.5) // 100 * 100
new_volume = Decimal(read_work_volume)
changed_balance = new_volume * (100 + results - Decimal(str(0.1))) / 100
new_balance = int((Decimal(read_balance) + changed_balance - new_volume) * 100) / 100

results_rewrite(str(Decimal(read_results_file) + results - Decimal(str(0.1))))

day_results_rewrite(str(Decimal(read_day_results) + results))

results_file = open("../data/results.txt")
read_results_file = results_file.read()

if Decimal(read_results_file) < -0.5:
    work_volume_rewrite(str(int(read_work_volume) - 100))
    results_rewrite(str(0))

elif Decimal(read_results_file) > 1:
    work_volume_rewrite(str(int(read_work_volume) + 100))
    results_rewrite(str(0))

if results == 0:
    work_volume_rewrite(str(int(work_volume_day)))
    day_results_rewrite(str(results))
    results_rewrite(str(0))
else:
    new_balance_file = open("../data/balance.txt", "w")
    new_balance_file.write(str(new_balance))
    new_balance_file.close()

work_volume_file = open("../data/volume.txt")
work_volume = work_volume_file.read()

results_file = open("../data/results.txt")
read_results_file = results_file.read()

day_results_file = open("../data/day_results.txt")
read_day_results = day_results_file.read()

if Decimal(read_day_results) < -1.5:
    print(emojize(":chart_decreasing:  На сегодня торговля окончена"))
else:
    if read_results_file == "0":
        print(emojize(":warning:Ваш актуальный объем: " + work_volume + "$"))
    else:
        print("  Ваш актуальный объем: " + work_volume + "$")