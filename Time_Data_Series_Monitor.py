import serial
import numpy as np
import matplotlib.pyplot as plt

#setup port which use by "Arduino + HeartRateModule"
#srl is serial port
srl_HeartArdu = serial.Serial()
srl_HeartArdu.baudrate = 9600
srl_HeartArdu.port = /dev/cu.usbmodem14501 #this port is located typeC-typeA
srl_HeartArdu.open()

#setup port which use by "hand made measuring instrument"
# i listen to Heart Rate from Ear
srl_HRE = serial.Serial()
srl_HRE.baudrate = 9600
srl_HRE.port = /dev/cu.usbmodem14301 #this port is located the most left "usb type-A port"
srl_HRE.open()

