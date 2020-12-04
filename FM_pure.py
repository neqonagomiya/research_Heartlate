import numpy as np
import matplotlib.pyplot as plt
import wave 
import pyaudio
import struct
from scipy import signal
import sys

sample_rate = 192000.0 #サンプリング周波数
dt = 1.0/192000.0 #サンプリング周期
nsamples = 3600000.0
F_1 = 1000.0
F_2 = 40000.0
t = np.arange(nsamples) / sample_rate
vin = np.sin(2 * np.pi * F_1 * t) 
vfm_dirty = 1.0*np.sin(2.0 * np.pi * F_2 * t + ( 2000.0 /F_1 ) * np.sin(2.0 * np.pi * F_1 * t))     
#fig = plt.figure(1)
#ax = fig.add_subplot(311)
#ax.plot(vin[1:1000])
#ax = fig.add_subplot(312)
#ax.plot(vfm[1:1000])
#fig.set_tight_layout(True)
#plt.show()

#vfmをバンドパフィルタかけて中心周波数と搬送波周波数のみを取り出す(その他の高周波成分をなくす)
filter_BPF = signal.firwin(numtaps=255,cutoff=[39000,41000], fs=1/dt, pass_zero=False)
#plt.plot(filter_BPF)
#plt.show()

#設計したBPFをfftして､設計したBPFの周波数特性をプロット
f = np.fft.fft(filter_BPF)
freq = np.fft.fftfreq(len(filter_BPF), dt)
#plt.plot(freq, f)
#plt.show()

#vfm_dirtyにバンドパスフィルタをかけて少しでもきれいな波形にする(結果:vfm)
vfm=signal.lfilter(filter_BPF,1,vfm_dirty)

#vfm(周波数変調波vfm_dirtyにBPFをかけたもの)をfftして周波数領域でプロット
f = np.fft.fft(vfm)
freq = np.fft.fftfreq(len(vfm), dt)
#plt.plot(freq, f)
#plt.show()

#(こっちより下の(>v<)のやつを使え)縦軸をdBにしてf(fft後のvfm)プロットする
f_log =  20 * np.log(f)
#plt.plot(freq, f_log)
#plt.show()

#(>v<)縦軸をdBにしてf(fft後のvfm)プロットする
f = np.fft.fft(vfm_dirty)
f_log =  20 * np.log(f)
freq = np.fft.fftfreq(len(vfm_dirty), dt)
#plt.plot(freq, f_log)
#plt.show()

#16bit符号付き変数に変換
Vfm_16 = [int(x*32767.0) for x in vfm]

#波形データのバイナリ化
binVfm = struct.pack("h" * len(Vfm_16), *Vfm_16)

#波形データを.wavで書きだし
w = wave.Wave_write("vfp.wav")
p = (1, 2, sample_rate, len(binVfm), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(binVfm)
w.close
