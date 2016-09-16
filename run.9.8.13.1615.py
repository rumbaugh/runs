import numpy as np

cr1 = np.loadtxt('EVLA/light_curves/1244.edt')
cr2 = np.loadtxt('EVLA/light_curves/1400.edt')

S1,S2 = cr1[:,2],cr2[:,2]
rms1,rms2 = cr1[:,6],cr2[:,6]

g = np.where((S1!=0)&(S2!=0)&(rms1!=0)&(rms2!=0))[0]

S1norm,S2norm = S1[g]/np.mean(S1[g]),S2[g]/np.mean(S2[g])
Smed = 0.5*(S1norm+S2norm)
S1med,S2med = S1norm/Smed,S2norm/Smed

Sscatter = np.std(np.append(S1med,S2med))

avgrat = np.mean(S1[g])/np.mean(S2[g])
avgrat2 = np.mean(S1[g]/S2[g])

raterr = np.sqrt(np.sum((S1[g]/S2[g]*np.sqrt((rms1[g]/S1[g])**2+(rms2[g]/S2[g])**2))**2))

