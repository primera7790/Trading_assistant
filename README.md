# Trading_assistant
### Description of functionality:
1. Launching the site;
2. Selecting the desired mode of operation (stay on the site, or interaction via Telegram);
3. Parsing of data from an Internet resource displaying actual trade statistics;
4. In case of detecting a transaction (trade), new data is entered into the database;
5. Based on the information about the transaction, the algorithm calculates the relevant volume of the next one, or informs about the need to stop trading;
6. The result is displayed on the site or sent to the Telegram bot (depending on the selected mode).

File to run: program/main.py

### Tools:
- language: &nbsp; `python` ;
- site: &nbsp; `django` , `html` , `css` ;
- parsing: &nbsp; `requests` , `bs4` , `lxml` , `selenium` ;
- database: &nbsp; `sqlite3` ;
- telegram bot: &nbsp; `aiogram` ;
- auto mode: &nbsp; `asyncio` , `apscheduler` , `celery` , `rabbitmq` , `docker` ;
- gui(old version): &nbsp; `tkinter` .

### About program
&nbsp; &nbsp; __Program objective:__ &nbsp; reduction of psychological burden on a trader during cryptocurrency trading.<br>
  &nbsp; &nbsp; __Method of achievement:__ &nbsp; mathematically justified regulation of transaction volumes and exclusion of unreasonable risk. If necessary - limitation of trading.<br>
  &nbsp; &nbsp; __Advantages of using it:__ &nbsp; the trader is isolated from information about the intermediate financial result, which allows him not to think about the state of the balance, but to concentrate on the deal.

## !! IMPORTANT NOTICE
### Support of the project is terminated due to the termination of Binance exchange in the Russian Federation. The project is for review only.
<br>
<br>

## Additionally

<img width=900px src='https://github.com/primera7790/Trading_assistant/blob/master/media/images/base_volume.PNG' alt='base_volume'>
<img width=900px src='https://github.com/primera7790/Trading_assistant/blob/master/media/images/current_balance.PNG' alt='current_balance'>
<img width=900px src='https://github.com/primera7790/Trading_assistant/blob/master/media/images/balance_change.PNG' alt='balance_change'>
