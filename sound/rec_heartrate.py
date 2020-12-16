# -*- coding:utf-8 -*-
import pyaudio
import suonare

#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
py_audio = pyaudio.PyAudio()
devices = suonare.list_audio_devices(py_audio)

if len(devices)==0:
    #not found audio devices
    print("error:device not found")
elif len(devices)==1:
    #found only one audio device
    print("only found %s" % devices[0]["name"])
else:
    #found some audio device
    suonare.display_audio_devices(devices)
    flag = input("Rubix22を使うけどいい？ y/n >> ")
    if flag == "y" or flag=="":
        #search Rubix22
        use_audio_device_index = suonare.find_rubix22(devices)
        print(use_audio_device_index)
    elif flag == "n":
        #
        #use_audio_device_index = int(input()
        print("n")