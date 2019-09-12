import serial

ser = serial.Serial('COM3', 115200, timeout=0) #Selecionar a porta correta, verificar antes em que porta está conectado o arduino
fg = False
fg_y = False
Valores = []

f= open("lux_res.txt","w+")

while 1:   
   data = ser.readline().decode('utf-8').strip()   
   if data != "":
       Valores.append(data)
       #print(Valores)
       
       if fg == False:
           f.write(data + "; ") #valores em y (res)
           fg = True
       else:
           f.write(data + ";\n") #valores em x (lux)
           fg = False
       
