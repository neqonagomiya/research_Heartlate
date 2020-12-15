import pyaudio

#py_audio = pyaudio.PyAudio()
#py_audio is pyaudio class (ex. py_audio=pyaudio.PyAudio())
def display_audio_device(py_audio):
    for i in range(py_audio.get_device_count()):
        print(py_audio.get_device_info_by_index(i))

display_audio_device(py_audio)
