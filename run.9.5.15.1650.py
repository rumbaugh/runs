import numpy as np
import scipy.optimize
#cr1=np.loadtxt('comb_spec_skysub_noCR.0737_2_blue_2.19.dat')
#cr2=np.loadtxt('comb_spec_skysub_noCR.0737_2_red_2.19.dat')
#cr=np.append(cr1,cr2,axis=0)
#w,f,v=cr[:,0],cr[:,1],cr[:,2]
g=np.where((((w>5187)&(w<5213))|((w>5234)&(w<5259))|((w>5687)&(w<5715))|((w>5888)&(w<5910))))[0]

def HandKfunc(x,redshift, base, amp1, amp2, sig1, sig2):
    #parameters: redshift, base, amp1, amp2, sig1, sig2
    Kcen=3933.667
    Hcen=3968.472
    return base-(amp1*np.exp(-0.5*((x-(redshift+1)*Kcen)/sig1)**2)+amp2*np.exp(-0.5*((x-(redshift+1)*Hcen)/sig2)**2))

def HandKplusGandCafunc(x,redshift, base, amp1, amp2, sig1, sig2,baseG,ampG,sigG,baseCa,ampCa,sigCa):
    #parameters: redshift, base, amp1, amp2, sig1, sig2
    Kcen=3933.667
    Hcen=3968.472
    Gcen=4305.00
    Cacen=4455.00
    bc1=0.5*(redshift+1)*(Hcen+Gcen)
    bc2=0.5*(redshift+1)*(Gcen+Cacen)
    basearr=np.ones(len(x))*base
    basearr[x>bc1]=baseG
    basearr[x>bc2]=baseCa
    output=np.zeros(len(x))
    output[x<bc1]=base-(amp1*np.exp(-0.5*((x[x<bc1]-(redshift+1)*Kcen)/sig1)**2)+amp2*np.exp(-0.5*((x[x<bc1]-(redshift+1)*Hcen)/sig2)**2))
    output[((x>bc1)&(x<bc2))]=baseG-(ampG*np.exp(-0.5*((x[((x>bc1)&(x<bc2))]-(redshift+1)*Gcen)/sigG)**2))
    output[x>bc2]=baseCa-(ampCa*np.exp(-0.5*((x[x>bc2]-(redshift+1)*Cacen)/sigCa)**2))
    return output

def GandCafunc(x,redshift, baseG,ampG,sigG,baseCa,ampCa,sigCa):
    #parameters: redshift, base, amp1, amp2, sig1, sig2
    Kcen=3933.667
    Hcen=3968.472
    Gcen=4305.00
    Cacen=4455.00
    bc1=0.5*(redshift+1)*(Hcen+Gcen)
    bc2=0.5*(redshift+1)*(Gcen+Cacen)
    basearr=np.ones(len(x))
    basearr[x<bc2]=baseG
    basearr[x>bc2]=baseCa
    output=np.zeros(len(x))
    output[x<bc2]=baseG-(ampG*np.exp(-0.5*((x[x<bc2]-(redshift+1)*Gcen)/sigG)**2))
    output[x>bc2]=baseCa-(ampCa*np.exp(-0.5*((x[x>bc2]-(redshift+1)*Cacen)/sigCa)**2))
    return output


guess=np.array([0.3228,40./5,24./5,24./5,10.,6.,87.,60.,12.,125.,100.,6.])
pout1=scipy.optimize.curve_fit(HandKplusGandCafunc,w[g],f[g],guess,sigma=np.sqrt(v[g]))
print pout1[0]

g=np.where((((w>5687)&(w<5715))|((w>5888)&(w<5910))))[0]
guess=np.array([0.3228,87.,60.,12.,125.,100.,6.])

pout2=scipy.optimize.curve_fit(GandCafunc,w[g],f[g],guess,sigma=np.sqrt(v[g]))
print pout2[0]
