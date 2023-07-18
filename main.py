from datetime import datetime
import time


while True:
    print(f"времечко вот такая: {datetime.now().strftime('%H:%M:%S')}")
    time.sleep(1)
