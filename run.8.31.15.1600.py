import numpy as np
import scipy.optimize
cr=np.loadtxt('comb_spec_skysub_noCR.0956_blue.dat')
w,f,v=cr[:,0],cr[:,1],cr[:,2]
g=np.where((((w>4442)&(w<4462))|((w>4485.4)&(w<4504))))[0]

def HandKfunc(x,redshift, base, amp1, amp2, sig1, sig2):
    #parameters: redshift, base, amp1, amp2, sig1, sig2
    Kcen=3933.667
    Hcen=3968.472
    return base-(amp1*np.exp(-0.5*((x-(redshift+1)*Kcen)/sig1)**2)+amp2*np.exp(-0.5*((x-(redshift+1)*Hcen)/sig2)**2))


guess=np.array([0.1325,55.,29.,29.,6.,6.])

pout=scipy.optimize.curve_fit(HandKfunc,w[g],f[g],guess,sigma=np.sqrt(v[g]))
print pout
