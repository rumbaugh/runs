import numpy as np

def CalcACF(tau,truetau,sig):
    return np.exp(-((tau+truetau)*0.5/sig)**2)*(1.+np.exp(tau*truetau*1./sig**2)+2*np.exp(truetau*(truetau+2.*tau)*0.25/sig**2))*sig*np.sqrt(np.pi)

def CalcDer(tau,truetau,sig):
    return np.exp(-((tau+truetau)*0.5/sig)**2)*((np.exp(tau*truetau*1./sig**2)-1)*truetau-tau*(1.+np.exp(tau*truetau*1./sig**2)+2*np.exp(truetau*(truetau+2.*tau)*0.25/sig**2)))*0.5*np.sqrt(np.pi)/sig

def Calc2ndDer(tau,truetau,sig):
    return np.exp(-((tau+truetau)*0.5/sig)**2)*((1+np.exp(tau*truetau*1./sig**2))*truetau**2-2*(np.exp(tau*truetau*1./sig**2)-1)*truetau*tau-(2*sig**2-tau**2)*(1.+np.exp(tau*truetau*1./sig**2)+2*np.exp(truetau*(truetau+2.*tau)*0.25/sig**2)))*0.25*np.sqrt(np.pi)/sig**3
                                               
truetaus=np.arange(3.3,4,0.001)
taus=np.arange(0.5,1,0.001)

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
