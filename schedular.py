import schedule
from datetime import datetime, timedelta
import time
from index import exporter


# Every day at 12am or 00:00 time exporter() is called.
schedule.every().day.at("00:00").do(exporter)

# Every defined minute exporter() is called.
schedule.every(1).minutes.do(exporter)

# run schedular in certain interval
while True:
    now = datetime.now()
    now = now.strftime("%Y-%b-%d %H:%M:%S")
    schedule.run_pending()
    print("Hello NCHL! I'm running to serve you at", now)
    time.sleep(5)
