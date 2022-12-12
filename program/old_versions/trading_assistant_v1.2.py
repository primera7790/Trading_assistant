from decimal import Decimal

balance = open("../data/balance.txt")
read_balance = balance.read()

work_volume_day = Decimal(read_balance) * Decimal(12.5) // 100 * 100

new_volume = Decimal(input("Объём сделки, $: "))
all_results = [Decimal(input("Результат сделки, %: "))]   # "0" - сброс до объема начала дня.

day_all_results = [0]  # TODO нужно додумать так, чтобы значения грамотно парсились в файл (списком?),
# TODO грамотно извлекались из файла списком и отрабатывали

changed_balance = new_volume * (100 + Decimal(all_results[-1]) - Decimal(0.1)) / 100
new_balance = int((Decimal(read_balance) + changed_balance - new_volume) * 100) / 100

work_volume_file = open("../data/volume.txt")
read_work_volume = work_volume_file.read()

if sum(day_all_results) < -1:
    print("На сегодня торговля окончена")

else:
    if sum(all_results) < -0.5:
        work_volume_file_new = open("../data/volume.txt", "w")
        work_volume_file_new.write(str(int(read_work_volume) - 100))
        work_volume_file_new.close()

    if sum(all_results) > 1:
        work_volume_file_new = open("../data/volume.txt", "w")
        work_volume_file_new.write(str(int(read_work_volume) + 100))
        work_volume_file_new.close()

    if all_results[0] == 0:
        work_volume_file_new = open("../data/volume.txt", "w")
        work_volume_file_new.write(str(int(work_volume_day)))
        work_volume_file_new.close()

    else:
        new_balance_file = open("../data/balance.txt", "w")
        new_balance_file.write(str(new_balance))
        new_balance_file.close()

    work_volume_file = open("../data/volume.txt")
    work_volume = work_volume_file.read()

    print(work_volume)
