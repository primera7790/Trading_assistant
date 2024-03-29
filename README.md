# Trading_assistant
### Description of functionality:
1. Launch the desired operating mode through the site;
2. Parsing data from the Internet resource with the current statistics;
3. In case of detecting a transaction (trade), new data is entered into the database;
4. An algorithm for calculating work volume is launched;
5. The final value is displayed on the site or sent by a Telegram bot (depending on the selected mode).

### Tools used:
- site: django, html, css;
- parsing: requests, bs4, lxml, selenium;
- database: sqlite3;
- telegram bot: aiogram;
- auto mode: asyncio, apscheduler, celery, rabbitmq, docker;
- gui(old version): tkinter.

### About program
 The task of the program - reduction of the psychological burden, by mathematically reasonable regulation of volumes and exclusion of unreasonable risk, if necessary - restriction of trade. Also, an important aspect - isolation of the trader from the information on the intermediate financial result that allows to concentrate on the deal, not on the balance state.
