import serial
from time import sleep


port='COM10'
ser=serial.Serial(port=port)

sleep(2)

#читаем данные из ардуино
data =ser.readline()
print(data)

#отправляем сообшение
ser.write(b"b")
data=ser.readline()
print(data)

def send_msg(msg : str):
    ser.write(msg.encode('utf-8'))