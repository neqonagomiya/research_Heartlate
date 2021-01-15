import pyaudio
import suonare
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import os

###################################################################################################
# Audio device information by pyaudio
###################################################################################################
#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
py_audio = pyaudio.PyAudio()
devices = suonare.list_audio_devices(py_audio)

###################################################################################################
# Setting file and Directory 
###################################################################################################
#setting filename
file_flag = input("'heartrate_'ってフォルダの名前を付けてもいい? y/n >> ")
if file_flag== "y" or file_flag=="":
    sound_file_name = "heartrate_"
    print("heartrateって名前をつけたよ!")
elif file_flag == "n":
    file_flag2 = input("'test_'ってフォルダの名前を付けてもいい? y/n >> ")
    if file_flag2== "y" or file_flag2=="":
        sound_file_name = "test_"
        print("testって名前をつけたよ!")
    else:
        sound_file_name = input("好きにして >> ")
        print(sound_file_name)

#setting directory and .wav
now = datetime.datetime.now()
#directory name 
dir_name_date = sound_file_name + now.strftime("%Y%m%d_%H%M%S")
#.wav name
sound_file_name_date_wav = sound_file_name + now.strftime("%Y%m%d_%H%M%S") + ".wav"
#L signal's .wav name
sound_file_name_date_L_wav = sound_file_name + now.strftime("%Y%m%d_%H%M%S") + "L_signal" + ".wav"
#R signal's .wav name
sound_file_name_date_R_wav = sound_file_name + now.strftime("%Y%m%d_%H%M%S") + "R_signal" + ".wav"
# current directory
path = os.getcwd()
#address name to save .wav
save_address = path + "/" + dir_name_date + "/"

###################################################################################################
# Select audio devices
###################################################################################################
if len(devices)==0:
    #not found audio devices
    print("error:device not found")
elif len(devices)==1:
    #found only one audio device
    print("only found %s" % devices[0]["name"])
else:
    #found some audio device
    print()
    suonare.display_audio_devices(devices)
    print()
    flag = input("Rubix22を使うけどいい？ y/n >> ")
    if flag == "y" or flag=="":
        #search Rubix22
        use_audio_device_index = suonare.find_rubix22(devices)
        print(use_audio_device_index)
    elif flag == "n":
        use_audio_device_index = int(input("audio_deviceを選んでね >> "))
        print(use_audio_device_index)
        #check if the audio_device to be used can be input
        check_device_flag = suonare.check_inputtable_device(devices,use_audio_device_index)
        if check_device_flag is None:
            print("you CANT use this audio_device")
            print("またね!")
            sys.exit()
        else:
            print("OK!") 
    else:
        print("またね!")
        sys.exit()

###################################################################################################
# Recording 
###################################################################################################
# setting for recoding 
CHUNK          = 1024
FORMAT         = pyaudio.paInt16
CHANNELS       = int(input("MONO: 1, STEREO: 2 >> "))
SAMPLERATE     = 48000 
RECORD_SECONDS = int(input("何秒間録音する？ >> "))

print("CHANNELS "+str(CHANNELS)+" "+str(type(CHANNELS)))

frames = []
#setting wav file
#sound_file_name = "Callback_"
#sound_file_name_date = suonare.add_wav(suonare.add_datetime(sound_file_name))
##wf = wave.open(sound_file_name_date,"wb")
##wf.setsampwidth(2)
##wf.setframerate(SAMPLERATE)
##wf.setnchannels(CHANNELS)

#frames is original data
#frames_bin is data that summarizes frames
#frames_L is deta obtained by decomposing frames. frames_L is used to make a .wav file
#frames_R is data obtained by decomposing frames. frames_R is used to make a .wav file
#frames_nparray is the value obtained by changing frames to a numerical value.　frames_nparray　is used when plotting the original data on the graph.
#frames_nparray_L is deta obtained by decomposing frames. frames_nparray_L is used when plotting the L_data on the graph.
#frames_nparray_R is deta obtained by decomposing frames. frames_nparray_R is used when plotting the R_data on the graph.

if input("Are you Ready ?") == "":
    print("Now recording")
    #define callback
    def callback(in_data,frame_count,time_info,status):
        #wf.writeframes(in_data)
        frames.append(in_data)
        if len(frames) >= RECORD_SECONDS*48000:
            return (None, pyaudio.paComplete)

        return (None,pyaudio.paContinue)
    
    # open stream using callback 
    stream = py_audio.open(format = FORMAT,
                           channels = CHANNELS,
                           rate = SAMPLERATE,
                           input_device_index = use_audio_device_index,
                           input = True,
                           output = False,
                           stream_callback = callback)
                
    # start the stream 
    stream.start_stream()

    # wait for stream to finish 
    time.sleep(RECORD_SECONDS+1)

    # stop stream 
    stream.stop_stream()
    stream.close()

    ##wf.close()
    # close PyAudio 
    py_audio.terminate()

    #save wav
    ##make directory
    print("dir_name_date:"+ dir_name_date)
    os.mkdir(dir_name_date)

    ##save wav
    print("sound_file_name_date_wav:"+sound_file_name_date_wav)

    suonare.make_wav_file(py_audio,
                          save_address+sound_file_name_date_wav,
                          CHANNELS,
                          FORMAT,
                          SAMPLERATE,
                          frames)

    print("Done Recording!")
else:
    print("またね！")
    sys.exit()

###################################################################################################
# Type of frame
###################################################################################################
print("frames info:")
print("frames:",str(type(frames)))
frames_bin = b"".join(frames)
#print("frames_bin:",frames)
print("frames_bin:",str(type(frames_bin)))
frames_L = frames[::2]
print("frames_L", len(frames_L))
frames_R = frames[1::2]
print("frames_R", len(frames_R))
#frames_L = suonare.bytes_L_select(frames)
#frames_R = suonare.bytes_R_select(frames)
#print("frames_L:", frames_L)
#print("frames_R:", frames_R)
frames_nparray = np.frombuffer(frames_bin,dtype='int16')
print("frames_nparray:",str(type(frames_nparray)))
#print(frames_nparray)
print("len(frames_nparray):", len(frames_nparray))
print(type(frames_nparray[0]))

t = np.arange(0, (len(frames_nparray)/CHANNELS/SAMPLERATE),(1/SAMPLERATE))
print("time",(len(frames_nparray)/CHANNELS/SAMPLERATE))
###################################################################################################
# Plot figure and Save signal_data
###################################################################################################
if CHANNELS == 2:
    #separate_LR
    frames_nparray_L = frames_nparray[::2]
    frames_nparray_R = frames_nparray[1::2]
    #save .csv
    np.savetxt(save_address+"original_signal_data.csv",frames_nparray,fmt="%d",delimiter=",")
    np.savetxt(save_address+"L_signal_data.csv", frames_nparray_L, fmt="%d",delimiter=",")
    np.savetxt(save_address+"R_signal_data.csv", frames_nparray_R, fmt="%d",delimiter=",")
    #suonare.make_wav_file(py_audio,
    #                      save_address+sound_file_name_date_L_wav,
    #                      1,
    #                      FORMAT,
    #                      SAMPLERATE,
    #                      frames_L
    #                     )
    #suonare.make_wav_file(py_audio,
    #                      save_address+sound_file_name_date_R_wav,
    #                      1,
    #                      FORMAT,
    #                      SAMPLERATE,
    #                      frames_R
    #                     )
    
    #plot the L and R figure
    #setting plot
    #font
    #plt.rcParams["font.size"] = 14
    #plt.rcParams["font.family"] = "Time New Roman"

    # scale
    #plt.rcParams["xtick.direction"] = "in"
    #plt.rcParams["ytick.direction"] = "in"

    #fig = plt.figure()
    #ax1 = fig.add_subplot(211)
    #ax2 = fig.add_subplot(212)
    # setting axis
    #ax1.set_xlabel("Time [s]")
    #ax1.set_ylabel("Amplitude")
    #ax2.set_xlabel("Time [s]")
    #ax2.set_ylabel("Amplitude")
    #plot(x_axis,y_axis,label)
    #ax1.plot(t,frames_nparray_L)
    #ax2.plot(t,frames_nparray_R)

    #fig.tight_layout()
    #The smallest codes to plot
    plt.subplot(211)
    plt.plot(frames_nparray_L)
    plt.subplot(212)
    plt.plot(frames_nparray_R)
    plt.savefig(save_address+'original_signal_data.png')
    plt.show()
else:
    np.savetxt(save_address+"original_signal_data.csv",frames_nparray,fmt="%d",delimiter=",")
    plt.plot(frames_nparray)
    plt.show()

# 高速フーリエ変換(FFT)
fft_frames = np.fft.fft(frames_nparray)

# FFT結果（複素数）を絶対値に変換
amp_fft_frames =np.abs(fft_frames/(len(frames_nparray)/2))
print("fft",len(amp_fft_frames))
plt.yscale('log')

# グラフ表示（データ数の半分の周期を表示）
plt.plot(amp_fft_frames[0:int(len(frames_nparray)/2)+1])
plt.show()

print("お疲れ様！")

