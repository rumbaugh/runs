import numpy as np
import matplotlib.pylab as plt


CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,2],CSO2cr[:,2]

CSO1day -= CSO1day[0]
CSO2day -= CSO2day[0]

g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

allpoints = np.append(CSO1S[g]/np.mean(CSO1S[g])/CSOnorm,CSO2S[g]/np.mean(CSO2S[g])/CSOnorm)

print np.std(allpoints)

g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)&(np.arange(len(CSO1S))<=len(CSO1S)-10)))[0]


CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

allpoints = np.append(CSO1S[g]/np.mean(CSO1S[g])/CSOnorm,CSO2S[g]/np.mean(CSO2S[g])/CSOnorm)

print np.std(allpoints)
