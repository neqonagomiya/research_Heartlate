import pyaudio
import suonare
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
import threading

#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
py_audio = pyaudio.PyAudio()
devices = suonare.list_audio_devices(py_audio)

#select audio_deveice

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


#recoding 
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
    time.sleep(RECORD_SECONDS)

    thread_list = threading.enumerate()
    thread_list.remove(threading.main_thread())
    print(len(thread_list))
    for thread in thread_list:
        thread.join()

    # stop stream 
    stream.stop_stream()
    stream.close()

    ##wf.close()
    # close PyAudio 
    py_audio.terminate()

    #save wav
    sound_file_name = "Callback_"
    sound_file_name_date_wav = suonare.add_wav(suonare.add_datetime(sound_file_name))
    print(sound_file_name_date_wav)
    suonare.make_wav_file(py_audio,
                          sound_file_name_date_wav,
                          CHANNELS,
                          FORMAT,
                          SAMPLERATE,
                          frames)

    print("Done Recording!")
else:
    print("またね！")
    sys.exit()

"""
#plot
#wf = wave.open(sound_file_name_date,"rb")
#print('ch:', wf.getnchannels())
#print('sample_width:', wf.getsampwidth())
#print('sample_rate:', wf.getframerate())
#print('frame:', wf.getnframes())
#print('param:', wf.getparams())

wf.rewind()
buf = wf.readframes(-1)

if wf.getsampwidth() == 2:
    data = np.frombuffer(buf, dtype='int16')
elif wf.getsampwidth() == 4:
    data = np.frombuffer(buf, dtype='int32')
else:
    print('Not support')
    sys.exit()

if wf.getnchannels() == 2:
    data_L = data[::2]
    data_R = data[1::2]
    plt.subplot(211)
    plt.plot(data_L)
    plt.subplot(212)
    plt.plot(data_R)
    plt.show()
else:
    plt.plot(data)
    plt.show()
"""

print("frames:",str(type(frames)))
frames_bin = b"".join(frames)
print("frames_bin:",str(type(frames_bin)))
frames_nparray = np.frombuffer(frames_bin,dtype='int16')

if CHANNELS == 2:
    frames_nparray_L = frames_nparray[::2]
    frames_nparray_R = frames_nparray[1::2]
    plt.subplot(211)
    plt.plot(frames_nparray_L)
    plt.subplot(212)
    plt.plot(frames_nparray_R)
    plt.show()
else:
    plt.plot(frames_nparray)
    plt.show()


print("お疲れ様！")