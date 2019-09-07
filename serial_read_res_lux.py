import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM13', 115200, timeout=0)
Valores = []

plt.axis([0, 300, 0, 1000000])
plt.xlabel("in LUX")
plt.ylabel("in OHM")

fg = False
fg_y = False
cont = 0
x=0
y=0
Valores = []

f= open("lux_res.txt","w+")

while 1:   
   data = ser.readline().decode('utf-8').strip()   
   if data != "":
       Valores.append(data)
       print(Valores)
       
       if fg == False:
           f.write(data + ", ") #valores em y (res)
           fg = True
       else:
           f.write(data + ";\n") #valores em x (lux)
           fg = False
       
       #time.sleep(0.2)
       #cont = cont + 1
