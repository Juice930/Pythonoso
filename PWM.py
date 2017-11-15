import numpy as np
import matplotlib.pyplot as plt
import json
from scipy import signal

def PWMmodulator(port,mod,samp):
    x=[]
    for i in range(samp):
        if port[i]>mod[i]:
            x.append(1)
        else:
            x.append(0)
    return x
    
def compressor(x,samp):
    a=1
    b=x[0]
    arr=[]
    arr.append(b)
    for i in range(samp//2):
        if i<samp//2-1:
            if b==x[i+1]:
                a+=1
            else:
                arr.append(a)
                a=1
                b=x[i+1]
        else:
            arr.append(a)
    return arr

def decompressor(x):
    x=x.copy()
    arr=[]
    a=x.pop(0)
    b=True
    for i in x:
        if b==True:
            arr+=[a for j in range(i)]
        else:
            arr+=[int(not a) for j in range(i)]
        b=not b
    return arr

samp=400*16
t=np.linspace(0,1/60,samp)
y1=np.sin(2*np.pi*60*t)
y2=signal.sawtooth(2*np.pi*24000*t,0.5)
plt.plot(t,y1,t,y2)
y3=PWMmodulator(y1,y2,samp)
plt.plot(t,y3)
y4=compressor(y3,samp)

f = open('Modulación.txt', 'w')
json.dump(y4,f)
f.close()

y5=decompressor(y4)