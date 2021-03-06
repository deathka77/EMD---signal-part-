!pip install EMD-signal
from __future__ import division, print_function

from PyEMD import EEMD
import numpy as np
import pylab as plt

!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
import pandas as pd
import soundfile as sf
#import peakdetect

file = wave.open('1.wav')
data, samplerate = sf.read('1.wav')
S=data
sf.write('2.flac', data, samplerate)
data
samplerate
S

from PyEMD import EMD
import numpy as np

#s = data
#emd = EMD()
#IMFs = emd(s)
#series = IMFs
#plot(IMFs)
#show()

# Define signal
t = np.linspace(0, 1, 200)

#sin = lambda x,p: np.sin(2*np.pi*x*t+p)
#S = 3*sin(18,0.2)*(t-0.2)**2
#S += 5*sin(11,2.7)
#S += 3*sin(14,1.6)
#S += 1*np.sin(4*2*np.pi*(t-0.8)**2)
# += t**2.1 -t

# Assign EEMD to `eemd` variable
eemd = EEMD()

# Say we want detect extrema using parabolic method
emd = eemd.EMD
emd.extrema_detection="parabol"

# Execute EEMD on S
#eIMFs = eemd.eemd(S, t)
nIMFs = eIMFs.shape[0]

# Plot results
plt.figure(figsize=(12,9))
plt.subplot(
