import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import os
#import pandas as pd

frames = []
file_name = []
#./sound のディレクトリに移動して実行する前提
for name in glob.glob('./**/*.csv',recursive=True):
    print(name)
    file_name.append(name)

#print(sys.argv)
#sys.exit(1)
select_filename = input('ファイルを選んでください >> ')
i=0
while True:
    if os.path.exists(select_filename) == True:
        print("ファイルありました！")
        break
    elif (i < 2)and(os.path.exists(select_filename) == False):
        print("そのファイルはないよ！")
        select_filename = input("もう一度ファイル名を入れてね >> ")
        i = i+1 
        continue
    else:
        print("またね！")
        sys.exit()
        

frames = np.loadtxt(select_filename,dtype='int' ,delimiter=',')
#frames_pd = pd.read_csv(select_filename, header=None)
print(frames)
print('size',len(frames))
#print('size(pd)',len(frames_pd))

CHANNELS = int(input("MONO: 1, STEREO: 2 >> "))
SAMPLERATE = 48000

print('time',(len(frames)/CHANNELS/SAMPLERATE))
print('len(frames)/SAMPLERATE',(len(frames)/SAMPLERATE))
fig = plt.figure()
ax1 = fig.add_subplot(111)
t = np.arange(start=0, stop=(len(frames)/SAMPLERATE),step=(1/SAMPLERATE))
t = t[:-1]
#setting axis
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Amplitude")
ax1.set_xlim([0,5])

ax1.plot(t,frames)
fig.tight_layout()
plt.show()
#######################################################################
#ax1 = fig.add_subplot(211)
#ax2 = fig.add_subplot(212)

#setting axis
#ax1.set_xlabel("Time [s]")
#ax1.set_ylabel("Amplitude")
#ax2.set_xlabel("Time [s]")
#ax2.set_ylabel("Amplitude")
#plot(x_axis,y_axis,label)
#ax1.plot(t,frames_nparray_L)
#ax2.plot(t,frames_nparray_R)
#fig.tight_layout()
#plt.show()
#########################################################################