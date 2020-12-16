import pyaudio
import serial

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

def find_rubix22(devices):
    for i in range(len(devices)):
        if devices[i]["name"] == "Rubix22":
            rubix22_index = int(i)
        else:
            continue
    return rubix22_index

#def find_audio_device(devices):
#    for i in range(len(devices)):
#def device_can_input(devices,use_audio_device_index):
    