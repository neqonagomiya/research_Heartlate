# -*- coding:utf-8 -*-
import pyaudio
import suonare
import sys

#py_audio
#use_audio_device_index

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

frames = []

stream = py_audio.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=SAMPLERATE,
                       input=True,
                       frames_per_buffer=CHUNK,
                       input_device_index=use_audio_device_index)

print('Now recoding')

for i in range(0, int(SAMPLERATE/CHUNK * RECORD_SECONDS)):
    frame = stream.read(CHUNK)
    frames.append(frame)

print('Done recoding !')

#End stream
stream.stop_stream()
stream.close()
py_audio.terminate()

#save .wav
sound_file_name = input("ファイルの名前は? >> ")
sound_file_name_date = suonare.add_datetime(sound_file_name)











