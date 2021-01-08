import pyaudio
import datetime
import wave
import numpy as np

# About Audio_Devices
#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
#this function is listing up audio devices
#returned devices is list
def list_audio_devices(py_audio):
    devices=[]
    for i in range(py_audio.get_device_count()):
        devices.append(py_audio.get_device_info_by_index(i))
    return devices

#device[0]["name"]

#this function is displaying list including audio devices
def display_audio_devices(devices):
    for index,audio_name in enumerate(devices):
        print(index,audio_name["name"])

#this function is find rubix22's index
def find_rubix22(devices):
    for i in range(len(devices)):
        if devices[i]["name"] == "Rubix22":
            rubix22_index = int(i)
        else:
            continue
    return rubix22_index

#this function is finding audio_device's index you want
#def find_audio_device(devices):
#    for i in range(len(devices)):

#this function check if the audio_device to be used can be input
#if audio_device you used can be inputed , return audio_device index(int)
def check_inputtable_device(devices,use_audio_device_index):
    check_inputtable_device_index = devices[use_audio_device_index]["maxInputChannels"]
    if check_inputtable_device_index == 0:
        #print("you cant use this audio_device")
        return None
    else:
        #print("OK")
        return check_inputtable_device_index


#Setting Filename
#this function is to add datetime to filename
#ex.
#file_name = input("not input extension. like .wav >> ")
#file_name = input("please only input file name >> ")
#date_file_name = add_datetime(file_name)
def add_datetime(file_name):
    now = datetime.datetime.now()
    date_file_name = file_name + now.strftime("%Y%m%d_%H%M%S")
    return date_file_name

def add_L(date_file_name):
    date_file_name_L = date_file_name + "L"
    return date_file_name_L

def add_R(date_file_name):
    date_file_name_R = date_file_name + "R"
    return date_file_name_R

def add_wav(date_file_name):
    date_file_name_wav = date_file_name + ".wav"
    return date_file_name_wav

def add_datetime_L_wav(sound_file_name):
    sound_file_name_date = add_datetime(sound_file_name)
    sound_file_name_date_L = add_L(sound_file_name_date)
    sound_file_name_date_L_wav = add_wav(sound_file_name_date_L)
    return sound_file_name_date_L_wav

def add_datetime_R_wav(sound_file_name):
    sound_file_name_date = add_datetime(sound_file_name)
    sound_file_name_date_R = add_R(sound_file_name_date)
    sound_file_name_date_R_wav = add_wav(sound_file_name_date_R)
    return sound_file_name_date_R_wav


#Recoding
def make_wav_file(py_audio,sound_file_name_date,CHANNELS,FORMAT,SAMPLERATE,frames):
    wf = wave.open(sound_file_name_date, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(py_audio.get_sample_size(FORMAT))
    wf.setframerate(SAMPLERATE)
    wf.writeframes(b''.join(frames))
    wf.close()


