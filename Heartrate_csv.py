# -*- coding:utf-8 -*-
import serial
import csv

port = "/dev/cu.usbmodem14501"
rate = 9600

srl_Heartrate = serial.Serial(port,rate)

f = open('Heartrate_data.csv', 'wb')
csvWriter = csv.writer(f)

while True:
    listData = []
    line = srl_Heartrate.readline()
    data = line.split(",")
    del data[-1]
    print(data)
    csvWriter.writerow(data)

srl_Heartrate.close()
