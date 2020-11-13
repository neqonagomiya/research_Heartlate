#Am_modulation.py
#2つの異なる周波数をもつ波をAM変調し､その.wavを生成する
#信号波(音源):400Hz 搬送波:40000Hz
#coding:utf-8
#https://qiita.com/tmtakashi_dist/items/b76350e304ef8e33fc1a

import numpy as np
import matplotlib.pyplot as plt
import wave 
import pyaudio
import struct

#波形データを作る
fs = 96000
#nsamples = 320
#t=arange(nsamples)/fs
t=3

#信号波のデータ
f_signal = 400
A_signal = 1
Vin= A_signal * np.cos(2*np.pi*f_signal*t)

#変調波
f_carrier = 40000
A_carrier = 3

Vam = A_signal*(np.cos(2*np.pi*f_carrier*))
#波形データのバイナリ化
#波形データを.wavで書きだし
