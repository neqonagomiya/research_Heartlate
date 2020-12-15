import pyaudio

#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
def search_audio_device(py_audio):
    device=[]
    for i in range(py_audio.get_device_count()):
        device.append(py_audio.get_device_info_by_index(i))
    return device

#device[0]["name"]
