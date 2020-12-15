import sys
import pyaudio

p = pyaudio.PyAudio()
count = p.get_device_count()

devices = []
#音声デバイス毎のインデックス番号を一覧表示
for i in range(count):
	devices.append(p.get_device_info_by_index(i))

print(devices)

#index番号とオーディオ機器の名前を表示
for i,dev in enumerate(devices):
	print(i,dev["name"])


