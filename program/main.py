import os
import time
import random

from pathlib import Path
from dotenv import load_dotenv
from emoji import emojize

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

from program.tech_zone.modules.parsing_tmm import get_trade_data
from program.tech_zone.modules.work_with_data import work_volume_calculation


def last_trade_parsing(email, password, html_name='index.html'):
    chrome_service = Service(str(Path(Path(__file__).parent, r'tech_zone/driver_chrome_selenium/chromedriver.exe')))
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=190.61.88.147:8080')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(executable_path=r'program/tech_zone/driver_chrome_selenium/chromedriver',
    #                           options=chrome_options)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    url = 'https://tradermake.money/app/account/my-trades'
    try:
        driver.get(url=url)
        time.sleep(2)
        email_input = driver.find_element(By.ID, 'input-1166')
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(random.randrange(1, 2))
        password_input = driver.find_element(By.ID, 'input-1170')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(1, 2))
        password_input.send_keys(Keys.ENTER)
        try:
            wait = WebDriverWait(driver, 20)
            clickable_element = '/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/button/span/i'
            wait.until(ec.presence_of_element_located((By.XPATH, clickable_element)))
            wait.until(ec.element_to_be_clickable((By.XPATH, clickable_element)))
            driver.find_element(By.XPATH, clickable_element).click()
        except (TimeoutException, ElementClickInterceptedException):
            time.sleep(2)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div[3]/div/button/span/i').click()

        # work_volume_message = get_new_data()

        # return work_volume_message

        while True:
            driver.get(url=url)
            time.sleep(10)
            with open(Path(Path(__file__).parent, f'tech_zone/html/{html_name}'), 'w', encoding='utf8') as file:
                file.write(driver.page_source)
            trade_data = get_trade_data()
            if trade_data == 'no data':
                continue
            elif trade_data == 'nothing_trades':
                work_volume_message = emojize(':collision: Новых сделок не обнаружено.')
                return work_volume_message
            else:
                if trade_data is None:
                    return
                else:
                    trade_percent = trade_data[0]
                    trade_volume = trade_data[1]
                    trade_commission = trade_data[2]
                    current_trade_id = trade_data[3]

                    work_volume_message = work_volume_calculation(trade_percent, trade_volume, trade_commission, current_trade_id)
                return work_volume_message

    except Exception as ex:
        print(ex)
        # mb.showerror('Остановка процессов', 'Программа завершила работу.')
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()


# def auto_mode():
#     count = 0
#     while True:
#         work_volume_message = main()
#         if work_volume_message and ('Ваш актуальный объем' in work_volume_message):
#             return work_volume_message
#         else:
#             count += 1
#             if count == 100:
#                 return
#             time.sleep(60)
#             continue


def main():
    load_dotenv(Path(Path(__file__).parent, 'tech_zone/env/.env'))
    email = os.environ.get('email_tmm')
    password = os.environ.get('password_tmm')

    work_volume_message = last_trade_parsing(email, password)
    return work_volume_message


if __name__ == '__main__':
    main()
