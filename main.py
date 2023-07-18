from datetime import datetime
import time


while True:
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)