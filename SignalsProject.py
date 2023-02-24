from scipy.fftpack import fft
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
𝑁 = 3*1024
𝑓 = np. linspace(0 , 512 , int(𝑁/2))
𝑡 = np.linspace(0 , 3 , (12 * 1024))
NoOfFreqs = 4
Fi = [246.93 , 220 , 146.83 , 164.81]
fi = [293.66 , 349.23 , 493.88 , 440]
ti = [0 , 0.7 , 1.7 , 2.3]
Ti = [0.7 , 1 , 0.6 , 0.7]
summation = 0
for i in range(1,NoOfFreqs+1):
    first = (np.sin(2*np.pi*Fi[i-1]*t)+np.sin(2*np.pi*fi[i-1]*t))
    second = np.logical_and(t >= ti[i-1] ,t <= (ti[i-1]+Ti[i-1]) )
    signal = first*second
    summation = summation + signal
x = summation
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])
𝑓𝑛1 = np.random.randint(0, 512, 2)
n_t = 0
for j in range (2):
    n_t += np.sin(2 * fn1[j] * np.pi * t)
xn_t = x + n_t
xn_f = fft(xn_t)
xn_f = 2/N * np.abs(xn_f [0:np.int(N/2)])
maxSignal = (x_f)[0]
for k in range ((x_f).size):
    if (x_f)[k] > maxSignal:
        maxSignal = (x_f)[k]
maxSignal = np.ceil(maxSignal)
indices = [0,0]
index = 0
for z in range((xn_f).size):
    if ((xn_f)[z] > maxSignal):
        indices[index] = z
        index += 1
noiseSignal = [np.round(f[indices[0]]) , np.round(f[indices[1]])]
x_filtered = xn_t - (np.sin(2 * noiseSignal[0] * np.pi * t) + np.sin(2 * noiseSignal[1] * np.pi * t))    
x_filtered_f = fft(x_filtered)
x_filtered_f = 2/N * np.abs(x_filtered_f [0:np.int(N/2)])
plt.subplot(3,2,1)
plt.plot(t,x)
plt.subplot(3,2,2)
plt.plot(f,x_f)
plt.subplot(3,2,3)
plt.plot(t,xn_t)
plt.subplot(3,2,4)
plt.plot(f,xn_f)
plt.subplot(3,2,5)
plt.plot(t,x_filtered)
plt.subplot(3,2,6)
plt.plot(f,x_filtered_f)

sd.play(x, 3 * 1024) # original sound
sd.play(xn_t, 3 * 1024) # sound with noise
sd.play(x_filtered, 3 * 1024) # filtered sound
