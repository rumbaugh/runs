execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/Dispersion.py')
import time
import matplotlib.pyplot as plt

try:
    ntrials
except NameError:
    ntrials = 100

try:
    errstd
except NameError:
    errstd = 7.5

try:
    nbins
except NameError:
    nbins = 20

delta = 10.5

ldate = '6.3.14'
date = '7.30.14'

level_dict = dict(zip(np.arange(20)+1,np.zeros(20)))
crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

afracs = np.array([1/3.,0.5,2/3.,0.8,1])
akeys = np.array(['1/3','1/2','2/3','4/5','all'])
alpha_dict = {x: np.zeros(ntrials) for x in akeys}
st = time.time()
Farr = np.zeros((len(np.arange(220.,550.,1.)),11))
Farr[:,0] = np.arange(220.,550.,1.)
for i,pair in zip(np.arange(len(level_dict.keys())),level_dict.keys()):
    tau,mu = crt[:,0][pair-1],crt[:,1][pair-1]
    cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ldate))
    stime,F = cr[:,0],cr[:,1]
    disparr,muarr,tarr = calc_disp_delay(F,F,stime,stime,errstd*np.ones(len(stime)),errstd*np.ones(len(stime)),100,0.237,0.05,1,0.001,'D_4_2',delta,mintime=0,output=2,disparray=True,outfile='/mnt/data2/rumbaugh/Fermi/output/test/Dispersion.testlightcurve_%i.tau_%.2f.mu_%.3f.D_4_2.delta_%.1f.%s.dat'%(pair,tau,mu,delta,date))
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.plot(tarr,disparr)
    plt.axvline(tau)
    plt.axvline()
    plt.xlabel('Time (days)',fontsize=14)
    plt.ylabel('D_2')
    plt.title('Lightcurve %i - tau = %5.2f'%(i,tau))
    plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testdispcalc_%i.tau_%5.2f.D_4_2.delta_%.1f.%s.png'%(i,tau,delta,date))
