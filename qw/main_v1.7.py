import os
import time
import random

from pathlib import Path
from dotenv import load_dotenv

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

from program.tech_zone.modules.parsing_tmm import get_trade_data
from program.tech_zone.modules.database_admin import table_select
from program.tech_zone.modules.work_with_data import check_balance
from program.tech_zone.modules.work_with_data import work_volume_calculation


chrome_service = Service(r'./tech_zone/driver_chrome_selenium/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=190.61.88.147:8080')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

url = 'https://tradermake.money/app/account/my-trades'


def start_program(email, password):
    try:
        driver.get(url=url)

        time.sleep(2)
        email_input = driver.find_element(By.ID, 'input-27')
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(random.randrange(1, 2))
        password_input = driver.find_element(By.ID, 'input-31')
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

        gui_main_window()

    except Exception as ex:
        print(ex)
        mb.showerror('Остановка процессов', 'Программа завершила работу.')
    finally:
        time.sleep(5)
        driver.close()
        driver.quit()


def gui_main_window():
    window = tk.Tk()
    window.title('Trading assistant v.1.7')
    window.geometry('500x300+1420+0')

    balance_menu = tk.Menu(window)
    balance_menu.add_command(label='Текущий баланс', command=lambda: mb.showinfo(title='Текущий баланс', message=f'Ваш баланс: {round(float(table_select("balance")), 2)}$'))
    balance_menu.add_command(label='Изменить баланс', command=gui_change_balance_window)
    window.config(menu=balance_menu)

    ttk.Label(text='Расчет рабочего объёма сделки', font='Arial 20').place(anchor='center', relx=0.5, rely=0.2)
    ttk.Button(text='БАЗОВЫЙ', width=300, command=lambda: work_volume_calculation()).place(anchor='center', relx=0.5, rely=0.5)
    ttk.Button(text='ТЕКУЩИЙ', width=300, command=lambda: get_new_data()).place(anchor='center', relx=0.5, rely=0.7)
    ttk.Button(text='Запустить авторежим', width=300, command=lambda: auto_mode()).place(anchor='center', relx=0.5, rely=0.9)
    # ttk.Button(text='Х', width=3, command=lambda: [auto_mode(stop=True), progressbar.stop()]).place(anchor='center', relx=0.95, rely=0.9)
    # progressbar = ttk.Progressbar(orient='horizontal', mode='indeterminate', length=206)
    # progressbar.place(anchor='center', relx=0.71, rely=0.9)

    window.mainloop()


def gui_change_balance_window(title=None, text=None):
    if title is None and text is None:
        title = 'Изменение баланса'
        text = 'Укажите новую сумму'
    window = tk.Tk()
    window.title(title)
    window.geometry('295x100+1420+30')

    ttk.Label(window, text=text, font='Arial 12').place(anchor='center', relx=0.5, rely=0.2)
    entry_balance = ttk.Entry(window)
    entry_balance.place(anchor='center', relx=0.5, rely=0.45)
    ttk.Button(window, text='Готово', command=lambda: check_balance(entry_balance.get())).place(anchor='center', relx=0.5, rely=0.75)

    window.mainloop()


def get_new_data(iter_on=None):
    # print('get_new_data')
    trade_data = last_trade_parsing(iter_on=iter_on)

    if trade_data is None:
        return
    else:
        trade_percent = trade_data[0]
        trade_volume = trade_data[1]
        trade_commission = trade_data[2]
        current_trade_id = trade_data[3]

        work_volume_calculation(trade_percent, trade_volume, trade_commission, current_trade_id, iter_on)
    return


def last_trade_parsing(html_name='index.html', iter_on=None):
    # print('last_trade_parsing')
    if iter_on is None:
        mb.showinfo('Формирование текущего объема', 'Производится сбор информации и вычисления...', type='ok')
    while True:
        driver.get(url=url)

        time.sleep(10)
        with open(Path(Path(__file__).parent, f'tech_zone/html/{html_name}'), 'w', encoding='utf8') as file:
            file.write(driver.page_source)

        trade_data = get_trade_data(iter_on=iter_on)
        if trade_data == 'no data':
            continue
        else:
            return trade_data


def auto_mode(stop=None):
    while True:
        if stop is None:
            # print('go')
            get_new_data(iter_on=True)
            time.sleep(60)
        else:
            return


def main():
    mb.showinfo('Процедура запуска', 'Производится подключение. Программа скоро будет запущена...')

    load_dotenv(Path(Path(__file__).parent, 'tech_zone', 'env', '.env'))
    email = os.environ.get('email_tmm')
    password = os.environ.get('password_tmm')

    start_program(email, password)


if __name__ == '__main__':
    main()
    # gui_main_window()
    # auto_mode()