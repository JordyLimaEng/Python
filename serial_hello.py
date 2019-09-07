import serial
import time
import matplotlib.pyplot as plt
import math

ser = serial.Serial('COM13', 9600, timeout=0)

while 1:
    try:
        print(ser.readline())
        time.sleep(0.8)
    except ser.SerialTimeoutException:
        print('Dados nao pode ser lido')
        time.sleep(0.8)