from envirophat import weather
import time
from socketIO_client import SocketIO, LoggingNamespace
with SocketIO('localhost', 8000, LoggingNamespace) as socketIO:
    # socketIO.wait(seconds=1)
    socketIO.on('connect', on_connect)
    socketIO.on('disconnect', on_disconnect)
    socketIO.on('reconnect', on_reconnect)

    while True:
        temp = weather.temperature()
        socketIO.emit(temp)
        time.sleep(1)


def on_connect():
    print('connect')


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')
