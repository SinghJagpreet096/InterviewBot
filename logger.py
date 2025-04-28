import logging
import os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.makedirs('logs', exist_ok=True)

print(date)

# logging.basicConfig(
#     filename=.log',
#     format='%(asctime)s %(message)s', 
#     datefmt='%m/%d/%Y %I:%M:%S %p'
#     level=logging.DEBUG)

# logging.warning('is when this event was logged.')