import requests
from envirophat import weather
import time


def sendTemp(myTemp):
    payload = {'temperature': myTemp}
    try:
        requests.get('http://10.0.0.114:3000', params=payload)
    except:
        pass

while True:
    myTemp = weather.temperature()
    print(myTemp)
    sendTemp(myTemp)
    time.sleep(1)
