import os
import time
import random

from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from program.tech_zone.modules_t_a.work_with_data import work_volume_calculation
from program.tech_zone.modules_t_a.parsing_tmm import get_trade_data


def get_work_volume(url, email, password, html_name='index.html'):
    chrome_service = Service(r'./tech_zone/driver_chrome_selenium/chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=190.61.88.147:8080')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        print('Перехожу на сайт...')
        driver.get(url=url)

        time.sleep(2)
        print('Ввожу логин и пароль...')
        email_input = driver.find_element(By.ID, 'input-27')
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(random.randrange(1, 2))
        print('Авторизация...')
        password_input = driver.find_element(By.ID, 'input-31')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(1, 2))
        print('Перехожу на страницу со сделками...')
        password_input.send_keys(Keys.ENTER)

        time.sleep(random.randrange(5, 6))
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/button/span/i').click()

        while True:
            time.sleep(3)
            console_input = input('--------------------------------------\n'
                                  '> "0" - для вывода базового объема; > ENTER - для расчета актуального; > exit - завершение работы программы.\n'
                                  '--------------------------------------\n'
                                  '>>> Введите значение: ')
            if console_input == '0':
                work_volume_calculation()
                continue

            elif console_input.lower() in ('close', 'exit', 'quit', 'end'):
                print('Завершение работы программы...')
                raise SystemExit('Работа программы завершена.')

            else:
                driver.get(url=url)
                time.sleep(10)

            with open(Path(Path(__file__).parent, f'data/{html_name}'), 'w', encoding='utf8') as file:
                file.write(driver.page_source)

                trade_data = get_trade_data()

                trade_percent = trade_data[0]
                trade_volume = trade_data[1]
                trade_commission = trade_data[2]

                work_volume_calculation(trade_percent, trade_volume, trade_commission)

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()


def main():
    url = 'https://tradermake.money/app/account/my-trades'

    load_dotenv(Path(Path(__file__).parent, 'tech_zone', 'env', '.env'))
    email = os.environ.get('email_tmm')
    password = os.environ.get('password_tmm')

    get_work_volume(url, email, password)


if __name__ == '__main__':
    main()