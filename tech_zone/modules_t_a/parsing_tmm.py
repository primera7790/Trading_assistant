import time
from pathlib import Path
from emoji import emojize
from bs4 import BeautifulSoup

from program.tech_zone.modules_t_a.work_with_data import read

data_path = Path(Path(__file__).parent.parent.parent, 'data')


def get_trade_data(html_name='index.html'):
    with open(Path(data_path, f'{html_name}'), encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    previous_trade_id = read(Path(data_path, 'previous_trade_id.txt'))

    current_trade_id = soup.find(class_='v-data-table__wrapper').\
        find('tr').\
        find_next('tr').\
        get_attribute_list('class')[0]

    trade_percent = soup.\
        find(class_='v-chip__content')
    print(trade_percent)

    trade_volume = soup.find(class_='v-data-table__wrapper').\
        find('tr').\
        find_next('tr').\
        find_next('tr').\
        find_previous().\
        find_previous()
    print(trade_volume)

    trade_commission = soup.find(class_='v-data-table__wrapper').\
        find('tr').\
        find_next('tr').\
        find_next('tr').\
        find_previous()
    print(trade_commission)

    while True:
        if trade_percent is not None and trade_volume is not None and trade_commission is not None:
            trade_percent = trade_percent.text.replace('%', '').strip().replace(',', '.')
            trade_volume = trade_volume.text.replace('$', '').strip().replace(',', '.')
            trade_commission = trade_commission.text.replace('$', '').strip().replace(',', '.')

            if current_trade_id == previous_trade_id:
                print(emojize(':collision: Новых сделок не обнаружено. Возможны неполадки на сайте.'))
                return ['0', '0', '0']
            elif trade_percent.replace('.', '').isdigit() and \
                    trade_volume.replace('.', '').isdigit() and \
                    trade_commission.replace('.', '').isdigit():

                with open(Path(data_path, 'previous_trade_id.txt'), 'w') as file:
                    file.write(current_trade_id)

                return [trade_percent, trade_volume, trade_commission]

        print('  Данные не подгрузились. Повторяю запрос...')
        time.sleep(5)


# get_trade_data()