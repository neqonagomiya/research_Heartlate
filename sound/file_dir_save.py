import os
import time
import datetime
import numpy as np
import wave 
import struct
import suonare

dir_name="dirpra_heartrate"

#make dire
now = datetime.datetime.now()
dir_file_name = dir_name + now.strftime("%Y%m%d_%H%M%S")
sound_file_name = dir_name + now.strftime("%Y%m%d_%H%M%S")+".wav"
path = os.getcwd()

save_wav_address = path + "/" + dir_file_name + "/" + sound_file_name

os.mkdir(dir_file_name)

#sin
ch = 1
width = 2
samplerate = 48000
time = 10
numsamples = time * samplerate

freq = 440
x=np.linspace(0,time,numsamples+1)
y=np.sin(2*np.pi*freq*x)
y=np.rint(32767*y/max(abs(y)))
y=y.astype(np.int16)
y=y[0:numsamples]
data = struct.pack("h"*numsamples,*y)

wf = wave.open(save_wav_address,"w")
wf.setnchannels(ch)
wf.setsampwidth(width)
wf.setframerate(samplerate)
wf.writeframes(data)
wf.close()


