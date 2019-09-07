import serial
import time

ser = serial.Serial('COM13', 9600, timeout=0)

while 1:
    try:
        print(ser.readline())
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Dados nao pode ser lido')
        time.sleep(1)