import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import os
#import pandas as pd
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

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

CHANNELS = int(input("MONO: 1, STEREO: 2 >> "))
SAMPLERATE = 48000

#setting plot param
plt.rcParams["xtick.direction"] = "in"               
plt.rcParams["ytick.direction"] = "in"               
plt.rcParams["xtick.minor.visible"] = True           
plt.rcParams["ytick.minor.visible"] = True           
plt.rcParams["xtick.major.width"] = 1             
plt.rcParams["ytick.major.width"] = 1          
plt.rcParams["xtick.minor.width"] = 0.5              
plt.rcParams["ytick.minor.width"] = 0.5              
plt.rcParams["xtick.major.size"] = 5                
plt.rcParams["ytick.major.size"] = 5                
plt.rcParams["xtick.minor.size"] = 2.5                 
plt.rcParams["ytick.minor.size"] = 2.5               

if CHANNELS == 1:
    frames_abs = np.abs(frames)
    maxval = np.amax(frames_abs)

    frames_plot = frames/maxval

    print(frames_plot)
    print("frames type:",type(frames_plot))
    print('size',len(frames_plot))
    #print('size(pd)',len(frames_pd))
    print("MAXVALUE:",maxval)

    print('time',(len(frames_plot)/CHANNELS/SAMPLERATE))
    print('len(frames)/SAMPLERATE',(len(frames_plot)/SAMPLERATE))
    time = len(frames_plot)/CHANNELS/SAMPLERATE
    

    fig0 = plt.figure()
    ax1 = fig0.add_subplot(111)
    t = np.arange(start=0, stop=time,step=(1/SAMPLERATE))
    t = t[:-1]
    #setting axis
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Amplitude")
    #ax1.set_xlim([0,time+0.1])
    ax1.set_xlim([0,3.0])
    ax1.grid(which='major',axis='both',color='#666666',alpha=0.25,linestyle=':',linewidth=1)

    ax1.plot(t,frames_plot)

    fig0.tight_layout()
    plt.show()

################################################
else:

    frames_L = frames[::2]
    frames_L_abs = np.abs(frames_L)
    maxval_L = np.amax(frames_L_abs)
    frames_L_plot = frames_L/maxval_L
    
    frames_R = frames[1::2]
    frames_R_abs = np.abs(frames_R)
    maxval_R = np.amax(frames_R_abs)
    frames_R_plot = frames_R/maxval_R
    
    min_val_L = 0
    com_val_L = 0
    for i in range(0,38400):
        com_val_L = frames_L_plot[i]
        if min_val_L > com_val_L:
            min_val_L = com_val_L
            min_loc_L = i
        else:
            continue
    
    min_val_R = 0
    com_val_R = 0
 
    for i in range(0,38400):
        com_val_R = frames_R_plot[i]
        if min_val_R > com_val_R:
            min_val_R = com_val_R
            min_loc_R = i
        else:
            continue


    print("min_loc_L:" ,min_loc_L)
    print("min_loc_L numpy:",np.argmin(frames_L_plot[0:38400]))
    print("min_val_L:", min_val_L)

    print("min_loc_R:" ,min_loc_R)
    print("min_loc_R numpy:",np.argmin(frames_R_plot[0:38400]))
    print("min_val_R:", min_val_R)

    ########################################################################################
    # ECG　心拍間隔測定
    ########################################################################################
    min2_val_L = 0
    com_val_L = 0
    for i in range(48000,96000):
        com_val_L = frames_L_plot[i]
        if min2_val_L > com_val_L:
            min2_val_L = com_val_L
            min2_loc_L = i
        else:
            continue

    print("min2_loc_L: ", min2_loc_L)
    print("min2_loc_L_numpy: ", np.argmin(frames_L_plot[48000:96000]))
    print("sample difference L :",(min2_loc_L)-(min_loc_L))
    ########################################################################################
    # mic 間隔
    ########################################################################################
    min2_val_R = 0
    com_val_R = 0
    for i in range(48000,96000):
        com_val_R = frames_R_plot[i]
        if min2_val_R > com_val_R:
            min2_val_R = com_val_R
            min2_loc_R = i
        else:
            continue

    print("min2_loc_R: ", min2_loc_R)
    print("min2_loc_R_numpy: ", np.argmin(frames_R_plot[48000:96000]))
    print("sample difference R:",(min2_loc_R)-(min_loc_R))
    ########################################################################################

    print(frames)
    print("frames type:",type(frames))
    print('size',len(frames))
    #print('size(pd)',len(frames_pd))
    print("MAXVALUE_L:",maxval_L)
    print("MAXVALUE_R:",maxval_R)

    print('time',(len(frames)/CHANNELS/SAMPLERATE))
    print('len(frames)/SAMPLERATE',(len(frames)/SAMPLERATE))
    time = len(frames)/CHANNELS/SAMPLERATE
    t = np.arange(start=0, stop=time,step=(1/SAMPLERATE))
    t = t[:-1]
    
    with open(os.path.dirname(select_filename)+"param.txt","w") as f:
        print("param",file=f)
        print("CHANNNEL: "+str(CHANNELS),file=f)
        print("min_loc_L:" + str(min_loc_L),file=f)
        print("min_loc_L numpy:"+str(np.argmin(frames_L_plot[0:38400])),file=f)
        print("min_val_L: "+str(min_val_L),file=f)
        print("min2_loc_L: ", min2_loc_L)
        print("min2_loc_L_numpy: ", np.argmin(frames_L_plot[48000:96000]))
        print("sample difference L :",(min2_loc_L)-(min_loc_L))

        print("min_loc_R: "+str(min_loc_R),file=f)
        print("min_loc_R numpy:"+str(np.argmin(frames_R_plot[0:38400])),file=f)
        print("min_val_R:"+ str(min_val_R),file=f)
        print("min2_loc_R: ", min2_loc_R)
        print("min2_loc_R_numpy: ", np.argmin(frames_R_plot[48000:96000]))
        print("sample difference R:",(min2_loc_R)-(min_loc_R))
        #print(frames)
        print("frames type: "+str(type(frames)),file=f)
        print('size: '+str(len(frames)),file=f)
        print("MAXVALUE_L: "+str(maxval_L),file=f)
        print("MAXVALUE_R: "+str(maxval_R),file=f)
        print('time: '+str((len(frames)/CHANNELS/SAMPLERATE)), file=f)
        print('len(frames)/SAMPLERATE: '+str((len(frames)/SAMPLERATE)),file=f)
        print('timelen(frames)/CHANNELS/SAMPLERATE: '+ str(time), file=f)
    
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(211)
    ax2 = fig1.add_subplot(212)

    #setting axis
    ax1.grid(which='major',axis='both',color='#666666',alpha=0.25,linestyle=':',linewidth=1)
    ax2.grid(which='major',axis='both',color='#666666',alpha=0.25,linestyle=':',linewidth=1)
    
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Amplitude")
    ax1.set_xlim([0,3.0])
    ax1.set_ylim([-1.1,1.1])
    ax1.set_title('(a) ECG',y=-0.45)
   
    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("Amplitude")
    ax2.set_xlim([0,3.0])
    ax2.set_ylim([-1.1,1.1])
    ax2.set_title('(b) Mic output',y=-0.45)

    ##########################################################################################
    ax1.vlines(min_loc_L/SAMPLERATE,-1.1,1.1,colors='#333333',linestyle='dashed',linewidth=2)    
    ax1.vlines(min2_loc_L/SAMPLERATE,-1.1,1.1,colors='#333333',linestyle='dashed',linewidth=2)
    ax2.vlines(min_loc_R/SAMPLERATE,-1.1,1.1,colors='#333333',linestyle='dashed',linewidth=2)
    ##########################################################################################

    ax1.plot(t,frames_L_plot,color='#ff4500')
    ax2.plot(t,frames_R_plot)
    
    fig1.tight_layout()
    plt.show()

    #enlarged
    fig2 = plt.figure()
    ax3 = fig2.add_subplot(211)
    ax4 = fig2.add_subplot(212)

    ax3.grid(which='major',axis='both',color='#666666',alpha=0.25,linestyle=':',linewidth=1)
    ax4.grid(which='major',axis='both',color='#666666',alpha=0.25,linestyle=':',linewidth=1)
    
    ax3.set_xlabel("Time [s]")
    ax3.set_ylabel("Amplitude")
    ax3.set_xlim([0.5,1.0])
    ax3.set_ylim([-1.1,1.1])
    ax3.set_title('(a) ECG',y=-0.45)

    ax4.set_xlabel("Time [s]")
    ax4.set_ylabel("Amplitude")
    ax4.set_xlim([0.5,1.0])
    ax4.set_ylim([-1.1,1.1])
    ax4.set_title('(b) Mic output',y=-0.45)

    #########################################################################################
    # ax3.vlines(min_loc_L/SAMPLERATE,-1.1,1.1,colors='#333333',linestyle='dashed',linewidth=2)
    # ax4.vlines(min_loc_R/SAMPLERATE,-1.1,1.1,colors='#333333',linestyle='dashed',linewidth=2)
    ##########################################################################################

    ax3.plot(t,frames_L_plot,color='#ff4500')
    ax4.plot(t,frames_R_plot)
    
    fig2.tight_layout()
    plt.show()



okflag = input('保存する? y or n >> ')
if okflag=="y" or okflag=="": 
    dirpath = os.path.dirname(select_filename)
    print(dirpath,' << ここに保存するね')
    if CHANNELS==1:
        fig0.savefig(os.path.dirname(select_filename)+'plot.png')
    elif CHANNELS==2:
        fig1.savefig(os.path.dirname(select_filename)+'plot.png')
        extent1 = ax1.get_window_extent().transformed(fig1.dpi_scale_trans.inverted())
        extent2 = ax2.get_window_extent().transformed(fig1.dpi_scale_trans.inverted())
        #サブプロットの周りの領域は、x方向の10%、y方向の20%で埋める。 
        fig1.savefig(os.path.dirname(select_filename)+'plot_L.png',bbox_inches=extent1.expanded(1.17, 1.3))
        fig1.savefig(os.path.dirname(select_filename)+'plot_R.png',bbox_inches=extent2.expanded(1.15, 1.3))
        
        fig2.savefig(os.path.dirname(select_filename)+'enlarged.png')
    else:
        print("対応してないよ")
        sys.exit()
else:        
    print("お疲れ様!")                        
    sys.exit()


#######################################################################
#FFT
#######################################################################
# 高速フーリエ変換(FFT)
#fft_frames = np.fft.fft(frames_nparray)

# FFT結果（複素数）を絶対値に変換
#amp_fft_frames =np.abs(fft_frames/(len(frames_nparray)/2))
#print("fft",len(amp_fft_frames))
#plt.yscale('log')

# グラフ表示（データ数の半分の周期を表示）
#plt.plot(amp_fft_frames[:int(len(frames_nparray)/2)+1])
#plt.show()
######################################################################
