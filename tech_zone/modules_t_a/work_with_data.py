import os
from emoji import emojize
from pathlib import Path
from decimal import Decimal

data_path = Path(Path(__file__).parent.parent.parent, 'data')


def read(file_name):
    if os.path.exists(file_name) is False:
        with open(file_name, 'w') as file:
            file.write('0')
    with open(file_name) as file:
        return file.read()


def rewrite(item, file_name):
    with open(file_name, 'w') as file:
        file.write(str(item))


def work_volume_calculation(trade_percent='0', trade_volume='0', trade_commission='0'):
    balance = read(Path(data_path, 'balance.txt'))
    while True:
        try:
            if balance == '':
                input_balance = input('  Укажите сумму на Вашем балансе, $: ')
            elif balance == '0':
                input_balance = input('  Укажите сумму на Вашем балансе, $: ')
            else:
                break
            Decimal(input_balance)
            rewrite(input_balance, Path(data_path, 'balance.txt'))
            balance = read(Path(data_path, 'balance.txt'))
        except ArithmeticError:
            print(emojize(':collision::collision::collision: Вводимое значение должно быть числом, повторите попытку.'
                          '\n      Также не принимаются числа через запятую.'))

    base_work_volume = Decimal(balance) * Decimal(12.5) // 100 * 100

    current_work_volume = read(Path(data_path, 'volume.txt'))

    try:
        Decimal(current_work_volume)
    except ArithmeticError:
        rewrite(base_work_volume, Path(data_path, 'volume.txt'))
        current_work_volume = read(Path(data_path, 'volume.txt'))
    results = read(Path(data_path, 'results.txt'))
    try:
        Decimal(results)
    except ArithmeticError:
        rewrite(0, Path(data_path, 'results.txt')
                )
    day_results = read(Path(data_path, 'day_results.txt'))
    try:
        Decimal(day_results)
    except ArithmeticError:
        rewrite(0, Path(data_path, 'day_results.txt'))

    change_volume = (Decimal(trade_volume) * (100 + Decimal(trade_percent)) / 100) - Decimal(trade_commission)
    new_balance = Decimal(balance) + change_volume - Decimal(trade_volume)

    if Decimal(trade_percent) == 0:
        rewrite(int(base_work_volume), Path(data_path, 'volume.txt'))
        rewrite(0, Path(data_path, 'day_results.txt'))
        rewrite(0, Path(data_path, 'results.txt'))

        current_work_volume = read(Path(data_path, 'volume.txt'))
        print(emojize(':warning:Ваш актуальный объем: ' + current_work_volume + '$'))

    else:
        rewrite(new_balance, Path(data_path, 'balance.txt'))
        rewrite(Decimal(results) + Decimal(trade_percent) - Decimal(trade_commission) / Decimal(trade_volume) * 100, Path(data_path, 'results.txt'))
        rewrite(Decimal(day_results) + Decimal(trade_percent), Path(data_path, 'day_results.txt'))

        day_results = read(Path(data_path, 'day_results.txt'))

        if Decimal(day_results) < -1.5:
            print(emojize(':chart_decreasing:  На сегодня торговля окончена'))
            rewrite(int(base_work_volume), Path(data_path, 'volume.txt'))
            rewrite(0, Path(data_path, 'day_results.txt'))
            rewrite(0, Path(data_path, 'results.txt'))
            exit()
        else:
            results = read(Path(data_path, 'results.txt'))

            if Decimal(results) < -0.5:
                rewrite(int(current_work_volume) - 100, Path(data_path, 'volume.txt'))
                rewrite(0, Path(data_path, 'results.txt'))

            elif Decimal(results) > 1:
                rewrite(int(current_work_volume) + 100, Path(data_path, 'volume.txt'))
                rewrite(0, Path(data_path, 'results.txt'))

            current_work_volume = read(Path(data_path, 'volume.txt'))
            results = read(Path(data_path, 'results.txt'))

            if results == '0':
                print(emojize(':warning:Ваш актуальный объем: ' + current_work_volume + '$'))
            else:
                print('  Ваш актуальный объем: ' + current_work_volume + '$')
