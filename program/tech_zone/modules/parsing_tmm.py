import time
from pathlib import Path
from bs4 import BeautifulSoup

from program.tech_zone.modules.database_admin import table_select


def get_trade_data(html_name='index.html', iter_on=None):
    with open(Path(Path(__file__).parent.parent, f'html/{html_name}'), encoding='utf8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    try:
        previous_trade_id = table_select('previous_trade_id')

        current_trade_id = soup.find(class_='v-data-table__wrapper').\
            find('tr').\
            find_next('tr').\
            get_attribute_list('class')[0]

        trade_percent = soup.\
            find(class_='v-chip__content')

        trade_info = soup.find(class_='v-data-table__wrapper').\
            find('tr').\
            find_next('tr').\
            find_all('td')
        trade_volume = trade_info[23]
        trade_commission = trade_info[24]
    except (AttributeError, IndexError):
        return 'no data'
    print('get_trade_data3')
    if trade_percent is not None and trade_volume is not None and trade_commission is not None:
        trade_percent = trade_percent.text.replace('%', '').strip().replace(',', '.')
        trade_volume = trade_volume.text.replace('$', '').strip().replace(',', '.')
        trade_commission = trade_commission.text.replace('$', '').strip().replace(',', '.')

        if current_trade_id == previous_trade_id:
            if iter_on is None:
                return 'nothing_trades'
            return

        elif trade_percent.replace('.', '').isdigit() and \
                trade_volume.replace('.', '').isdigit() and \
                trade_commission.replace('.', '').isdigit():
            return [trade_percent, trade_volume, trade_commission, current_trade_id]

    if iter_on is None:
        time.sleep(10)
        return 'no data'
    else:
        return


def main():
    get_trade_data()


if __name__ == '__main__':
    main()
