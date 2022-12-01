import os
import time
import random

from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from program.old_versions.work_with_data import work_volume_calculation
from program.old_versions.parsing_tmm import get_trade_data


def get_work_volume(url, email, password, html_name='index.html'):
    chrome_service = Service(r'../../tech_zone/driver_chrome_selenium/chromedriver.exe')
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

        wait = WebDriverWait(driver, 15)
        clickable_element = '/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/button/span/i'
        wait.until(ec.presence_of_element_located((By.XPATH, clickable_element)))
        wait.until(ec.element_to_be_clickable((By.XPATH, clickable_element)))
        driver.find_element(By.XPATH, clickable_element).click()

        while True:
            time.sleep(3)
            console_input = input('--------------------------------------\n'
                                  '> "0" - для вывода базового объема; > ENTER - для расчета актуального объема; > exit - завершение работы программы.\n'
                                  '--------------------------------------\n'
                                  '>>> Введите значение: ')
            if console_input == '0':
                work_volume_calculation()
                continue

            elif console_input.lower().strip() in ('close', 'exit', 'end', 'stop', 'off', 'quit'):
                print('Завершение работы программы...')
                raise SystemExit('Работа программы завершена.')

            else:
                print('Произвожу сбор информации и вычисления...')
                driver.get(url=url)
                time.sleep(10)

            with open(Path(Path(__file__).parent, f'tech_zone/html/{html_name}'), 'w', encoding='utf8') as file:
                file.write(driver.page_source)

                trade_data = get_trade_data()

                if trade_data == 'continue':
                    continue

                trade_percent = trade_data[0]
                trade_volume = trade_data[1]
                trade_commission = trade_data[2]
                current_trade_id = trade_data[3]

                work_volume_calculation(trade_percent, trade_volume, trade_commission, current_trade_id)

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()


def main():
    url = 'https://tradermake.money/app/account/my-trades'

    load_dotenv(Path(Path(__file__).parent, '../../tech_zone', 'env', '.env'))
    email = os.environ.get('email_tmm')
    password = os.environ.get('password_tmm')

    get_work_volume(url, email, password)


if __name__ == '__main__':
    main()