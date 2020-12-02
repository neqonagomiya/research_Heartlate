import serial 
import csv
import re

port = "/dev/cu.usbmodem14501"
rate = 9600

srl_Heartrate = serial.Serial(port,rate)
srl_Heartrate.close()
srl_Heartrate.open()

myfile = open("Ardu_heart.csv","w")
'''
while(1):
        val = srl_Heartrate.readline()
        byte_to_str = val.decode()
        dec = int(byte_to_str)
        myfile.write(dec)
        myfile.write('¥n')
        print(dec)
        #writer = csv.writer(file)
        #writer.writerow()

myfile.close()
'''
try:                        # try:の部分にループ処理を書く
    while True:
        val = srl_Heartrate.readline()
        byte_to_str = val.decode()
        #dec = int(byte_to_str)
        myfile.write(byte_to_str)
        print(byte_to_str)
        #writer = csv.writer(file)
        #writer.writerow()
except KeyboardInterrupt:   # exceptに例外処理を書く
    print('stop!')
    myfile.close()


'''
while(1):
    val = srl_Heartrate.readline()
    byte_to_str = val.decode()
    dec = int(byte_to_str)
    print(dec)
    with open("Ardu_Heartrate.csv","w") as file:
        writer = csv.writer(file)
        writer
'''
