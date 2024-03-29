from decimal import Decimal
from emoji import emojize
import os


def read(file_name):
    if os.path.exists(file_name) is False:
        with open(file_name, "w") as file:
            file.write("0")
    with open(file_name) as file:
        return file.read()


def rewrite(item, file_name):
    with open(file_name, "w") as file:
        file.write(item)


# def read_try(file_name):
#     var = read(file_name)
#     while True:
#         try:
#             Decimal(var)
#             return var
#         except ArithmeticError:
#             rewrite(str(0), file_name)
#             return read(file_name)


def get_work_volume():
    while True:
        balance = read("../data/balance.txt")
        while True:
            try:
                if balance == "":
                    input_balance = input("  Укажите сумму на Вашем балансе, $: ")
                elif balance == "0":
                    input_balance = input("  Укажите сумму на Вашем балансе, $: ")
                else:
                    break
                Decimal(input_balance)
                rewrite(str(input_balance), "../data/balance.txt")
                balance = read("../data/balance.txt")
            except ArithmeticError:
                print(emojize(":collision::collision::collision: Вводимое значение должно быть числом, повторите попытку."
                              "\n      Также не принимаются числа через запятую."))

        volume = read("../data/volume.txt")
        while True:
            try:
                Decimal(volume)
                break
            except ArithmeticError:
                rewrite(str(Decimal(balance) * Decimal(12.5) // 100 * 100), "../data/volume.txt")
                volume = read("../data/volume.txt")

        # results = read_try("results.txt")
        results = read("../data/results.txt")
        while True:
            try:
                Decimal(results)
                break
            except ArithmeticError:
                rewrite(str(0), "../data/results.txt")

        # day_results = read_try("day_results.txt")
        day_results = read("../data/day_results.txt")
        while True:
            try:
                Decimal(day_results)
                break
            except ArithmeticError:
                rewrite(str(0), "../data/day_results.txt")

        while True:
            one_trade_result = input("  Результат сделки, %: ")
            if one_trade_result == "close":
                break

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

        rewrite(str(Decimal(results) + one_trade_result - Decimal(str(0.1))), "../data/results.txt")

        rewrite(str(Decimal(day_results) + one_trade_result), "../data/day_results.txt")

        results = read("../data/results.txt")

        if Decimal(results) < -0.5:
            rewrite(str(int(volume) - 100), "../data/volume.txt")
            rewrite(str(0), "../data/results.txt")

        elif Decimal(results) > 1:
            rewrite(str(int(volume) + 100), "../data/volume.txt")
            rewrite(str(0), "../data/results.txt")

        if one_trade_result == 0:
            rewrite(str(int(work_volume_day)), "../data/volume.txt")
            rewrite(str(one_trade_result), "../data/day_results.txt")
            rewrite(str(0), "../data/results.txt")
        else:
            rewrite(str(new_balance), "../data/balance.txt")
            # new_balance_file = open("balance.txt", "w")
            # new_balance_file.write(str(new_balance))
            # new_balance_file.close()

        volume = read("../data/volume.txt")
        results = read("../data/results.txt")
        day_results = read("../data/day_results.txt")

        if Decimal(day_results) < -1.5:
            print(emojize(":chart_decreasing:  На сегодня торговля окончена"))
            break
        else:
            if results == "0":
                print(emojize(":warning:Ваш актуальный объем: " + volume + "$"))
            else:
                print("  Ваш актуальный объем: " + volume + "$")


def main():
    get_work_volume()


if __name__ == "__main__":
    main()