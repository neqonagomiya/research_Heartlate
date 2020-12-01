# -*- coding:utf-8 -*-
import serial
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from matplotlib.widgets import Button #we can use Button widgets in matplotlib
#from matplotlib import animation
#import time 
#import sys 

#setup port which use by "Arduino + HeartRateModule"
#srl is serial port
srl_HeartArdu = serial.Serial()
srl_HeartArdu.baudrate = 9600 #arduinoと合わせる必要がある
srl_HeartArdu.port = /dev/cu.usbmodem14501 #this port is located typeC-typeA
#srl_HeartArdu.setDTR(False) #DTRを常にLOWにしReset阻止これがないと通信開始時にArduinoがリセットされて通信エラーになる可能性あり
srl_HeartArdu.close()
srl_HeartArdu.open()

#setup port which use by "hand made measuring instrument"
# i listen to Heart Rate from Ear
#srl_HRE = serial.Serial()
#srl_HRE.baudrate = 9600
#srl_HRE.port = /dev/cu.usbmodem14301 #this port is located the most left "usb type-A port"
#srl_HRE.open()

#csvに出力するための「arduinoからシリアル入力データを全て格納する変数」
srl_HeartArdu_totaldata = []
srl_HRE_totaldata = []

#