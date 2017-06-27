import requests
from envirophat import weather
import time

while True:
    myTemp = weather.temperature()
    print(myTemp)
    payload = {temperature: myTemp}
    requests.get('http://10.0.0.114:3000', params=payload)
    time.sleep(1)
