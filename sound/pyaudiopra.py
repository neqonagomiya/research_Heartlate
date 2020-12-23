import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import suonare

py_audio = pyaudio.PyAudio()
#recoding 
CHUNK          = 1024
FORMAT         = pyaudio.paInt16
CHANNELS       = 1
SAMPLERATE     = 48000 
RECORD_SECONDS = int(input("何秒間録音する？ >> "))
INDEX          = 1

frames = []

if input("Are you Ready ?") == "":
    stream = py_audio.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=SAMPLERATE,
                           input=True,
                           frames_per_buffer=CHUNK,
                           input_device_index=INDEX)

    print('Now recoding')

    for i in range(0, int(SAMPLERATE/CHUNK * RECORD_SECONDS)):
        frame = stream.read(CHUNK)
        frames.append(frame)

    print('Done recoding !')
    print("frame="+str(type(frame)))
    #End stream
    stream.stop_stream()
    stream.close()
    py_audio.terminate()

sound_file_name = "output.wav"

suonare.make_wav_file(py_audio,
                      sound_file_name,
                      CHANNELS,
                      FORMAT,
                      SAMPLERATE,
                      frames)

frames_bin = b"".join(frames)            
print('frames='+str(type(frames)))
print('frames_bin'+str(type(frames_bin)))
frames_nparray = np.frombuffer(frames_bin, dtype='int16')
plt.plot(frames_nparray)
#plt.plot(frames)
plt.show()