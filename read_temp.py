from socketIO_client import SocketIO, LoggingNamespace
from envirophat import weather
import time

def on_connect():
    print('connect')
    while True:
        temp = weather.temperature()
        print(temp)
        socketIO.emit(temp)
        time.sleep(1)

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

socketIO = SocketIO('10.0.0.114', 3000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# socketIO.wait(seconds=1)
print('start')