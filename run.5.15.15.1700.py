import numpy as np

def CalcACF(tau,truetau,sig):
    return np.exp(-(tau+truetau)/sig)*(truetau*(1+np.exp(2*tau/sig))+sig*(2*np.exp(truetau/sig)+np.exp(2*tau/sig))+tau*(1+2*np.exp(truetau/sig)-np.exp(2*tau/sig)))

def CalcDer(tau,truetau,sig):
    return np.exp(-(tau+truetau)/sig)*(truetau*(-1+np.exp(2*tau/sig))-tau*(1+2*np.exp(truetau/sig)+np.exp(2*tau/sig)))*1./sig

def Calc2ndDer(tau,truetau,sig):
    return np.exp(-(tau+truetau)/sig)*(truetau*(1+np.exp(2*tau/sig))-sig*(1+2*np.exp(truetau/sig)+np.exp(2*tau/sig))+tau*(1+2*np.exp(truetau/sig)-np.exp(2*tau/sig)))*1./sig**2
                                               
truetaus=np.arange(3.,4.5,0.001)
taus=np.arange(0.2,1,0.001)

sig=1.
ACF,Der,Der2=np.zeros((len(truetaus),len(taus))),np.zeros((len(truetaus),len(taus))),np.zeros((len(truetaus),len(taus)))
for i in range(0,len(truetaus)):
    for j in range(0,len(taus)):
        truetau=truetaus[i]
        tau=taus[j]*truetau
        ACF[i][j]=CalcACF(tau,truetau,sig)
        Der[i][j]=CalcDer(tau,truetau,sig)
        Der2[i][j]=Calc2ndDer(tau,truetau,sig)
findsp = np.abs(Der)+np.abs(Der2)
g = np.where(findsp==np.min(findsp))
print truetaus[g[0]],taus[g[1]],findsp[g],Der[g],Der2[g]
plot(taus,ACF[-1])
