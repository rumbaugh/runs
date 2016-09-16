execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py")

import matplotlib.pyplot as plt

date = '6.10.14'

try:
    ntrials
except NameError:
    ntrials = 10

try:
    errstd
except NameError:
    errstd = 10.
try:
    nbins
except NameError:
    nbins = 10


Xr_dict = {2: np.zeros(ntrials), 3: np.zeros(ntrials)}

ltime,flux_arr,flux_err_arr = LoadVLA_2001('1030')
ltime -= ltime[0]
tau,tau2,mu = np.random.gamma(2,10,ntrials),np.random.gamma(2,10,ntrials),1-np.random.gamma(2,0.15,ntrials)
while len(mu[mu<=0]) > 0: mu = 1-np.random.gamma(2,0.15,ntrials)
for i in range(0,ntrials):
    F_dict = GenerateMockCurve(ltime,errstd=errstd,tau=tau[i],mu=mu[i],curves=2)
    Aflux,Aerr,Bflux,Berr = F_dict[1],errstd*np.ones(len(F_dict[1])),F_dict[2],errstd*np.ones(len(F_dict[1]))
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    Berr /= np.mean(Bflux)
    Bflux /= np.mean(Bflux)
    X,Y = (Aflux-Bflux)/np.sqrt(2),(Aflux+Bflux)/np.sqrt(2)
    Xerr = np.sqrt((Aerr**2+Berr*2)/2)
    Xr = np.sum((X/Xerr)**2)/len(X)
    Xr_dict[2][i] = Xr
    F_dict = GenerateMockCurve(ltime,errstd=errstd,tau=tau[i],mu=mu[i],curves=3,tau2=tau2[i])
    Aflux,Aerr,Bflux,Berr,Cflux,Cerr = F_dict[1],errstd*np.ones(len(F_dict[1])),F_dict[2],errstd*np.ones(len(F_dict[1])),F_dict[3],errstd*np.ones(len(F_dict[1]))
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    Berr /= np.mean(Bflux)
    Bflux /= np.mean(Bflux)
    Cerr /= np.mean(Cflux)
    Cflux /= np.mean(Cflux)
    X,Y = (2*Aflux-Bflux-Cflux)/np.sqrt(6),(Bflux-Cflux)/np.sqrt(2)
    R = np.sqrt(X**2+Y**2)
    Rerr = np.sqrt((6*(X*Aerr)**2+(2*Bflux-Aflux-Cflux)**2*Berr**2+(2*Cflux-Aflux-Bflux)**2*Cerr**2)/(9*R**2))
    Xr = np.sum((R/Rerr)**2)/len(X)
    Xr_dict[3][i] = Xr
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14 
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(Xr_dict[2],bins=nbins)
plt.xlabel('Xr',fontsize=14)
plt.title('Two curves')
plt.savefig('/home/rumbaugh/Xr_testing_2curveserr_%2.1f.%s.png'%(errstd,date))
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(Xr_dict[3],bins=nbins)
plt.xlabel('Xr',fontsize=14)
plt.title('Three curves')
plt.savefig('/home/rumbaugh/Xr_testing_3curveserr_%2.1f.%s.png'%(errstd,date))
Xr_dict = {2: np.zeros(ntrials), 3: np.zeros(ntrials)}
for i in range(0,ntrials):
    base = GenerateBaseAmp()
    Aflux,Aerr,Bflux,Berr = np.random.normal(base,errstd,len(ltime)),errstd*np.ones(len(ltime)),np.random.normal(base,errstd,len(ltime)),errstd*np.ones(len(ltime))
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    Berr /= np.mean(Bflux)
    Bflux /= np.mean(Bflux)
    X,Y = (Aflux-Bflux)/np.sqrt(2),(Aflux+Bflux)/np.sqrt(2)
    Xerr = np.sqrt((Aerr**2+Berr*2)/2)
    Xr = np.sum((X/Xerr)**2)/len(X)
    Xr_dict[2][i] = Xr
    base = GenerateBaseAmp()
    Aflux,Aerr,Bflux,Berr,Cflux,Cerr = np.random.normal(base,errstd,len(ltime)),errstd*np.ones(len(ltime)),np.random.normal(base,errstd,len(ltime)),errstd*np.ones(len(ltime)),np.random.normal(base,errstd,len(ltime)),errstd*np.ones(len(ltime))
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    Berr /= np.mean(Bflux)
    Bflux /= np.mean(Bflux)
    Cerr /= np.mean(Cflux)
    Cflux /= np.mean(Cflux)
    X,Y = (2*Aflux-Bflux-Cflux)/np.sqrt(6),(Bflux-Cflux)/np.sqrt(2)
    R = np.sqrt(X**2+Y**2)
    Rerr = np.sqrt((6*(X*Aerr)**2+(2*Bflux-Aflux-Cflux)**2*Berr**2+(2*Cflux-Aflux-Bflux)**2*Cerr**2)/(9*R**2))
    Xr = np.sum((R/Rerr)**2)/len(X)
    Xr_dict[3][i] = Xr
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(Xr_dict[2],bins=nbins)
plt.xlabel('Xr',fontsize=14)
plt.title('Two curves')
plt.savefig('/home/rumbaugh/Xr_testing_2curves.control.err_%2.1f.%s.png'%(errstd,date))
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(Xr_dict[3],bins=nbins)
plt.xlabel('Xr',fontsize=14)
plt.title('Three curves')
plt.savefig('/home/rumbaugh/Xr_testing_3curves.controlerr_%2.1f.%s.png'%(errstd,date))
