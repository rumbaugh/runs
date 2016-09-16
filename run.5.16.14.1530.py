import numpy as np
CSOs = ['1244+408','1400+621']
CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1S,CSO2S = CSO1cr[:,2]/1000,CSO2cr[:,2]/1000

g = np.where(((CSO1S>0)&(CSO2S>0)))[0]#&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]

CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

S1,S2 = CSO1S[g]/np.mean(CSO1S[g])/CSOnorm,CSO2S[g]/np.mean(CSO2S[g])/CSOnorm

print np.std(np.append(S1,S2))
