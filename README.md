# Trading_assistant
### Description of functionality:
1. Launch the desired operating mode through the site;
2. Parsing data from the Internet resource with the current statistics;
3. In case of detecting a transaction (trade), new data is entered into the database;
4. An algorithm for calculating work volume is launched;
5. The final value is displayed on the site or sent by a Telegram bot (depending on the selected mode).

File to run: program/main.py

### Tools used:
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
