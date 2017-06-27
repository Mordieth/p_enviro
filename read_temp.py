import requests
from envirophat import weather
import time

while True:
    myTemp = weather.temperature()
    print(myTemp)
    requests.post('http://10.0.0.114:3000', data={'temperature': myTemp})
    time.sleep(1)
