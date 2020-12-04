import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

filename = input("filename.csv->")
df = pd.read_csv(filename,header=None)
df = df.iloc[:,0]

#sample_freq = int(int(1.0/(6204)*(10**6)) / 2) * 2
sample_freq = 1.0/(6204)*(10**6)
print(sample_freq)
dt = 1.0/sample_freq
f1 = 0
f2 = 30
#t = np.arange(0.N*dt,dt)

# filter_LPF = signal.firwin(numtaps=1000,cutoff=f2,fs=sample_freq,pass_zero=False)
filter_LPF = signal.firwin(numtaps=1000,cutoff=[0.3,f2],fs=sample_freq,pass_zero=False)

y1 = signal.lfilter(filter_LPF,1,df)
FFT = np.fft.fft(y1)
df_FFT = np.fft.fft(df)

freq = np.fft.fftfreq(len(FFT),dt)

plt.plot(filter_LPF)
plt.legend()
plt.show()

plt.plot(y1, label="filtered")
plt.plot(df, label="original")
plt.legend()
plt.show()

#plt.plot(freq, FFT,    label="filtered")
#plt.plot(freq, df_FFT, label="original")
#plt.legend()
#plt.show()

amp_FFT=np.abs(FFT/(len(df)/2))
amp_df =np.abs(df_FFT/(len(df)/2))

plt.plot(freq,amp_FFT, label="filtered")
plt.plot(freq,amp_df, label="original")
plt.legend()
plt.show()
