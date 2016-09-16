execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
import time
import matplotlib.pyplot as plt

date = '5.27.14'

try:
    ntrials
except NameError:
    ntrials = 10

try:
    errstd
except NameError:
    errstd = 7.5

try:
    nbins
except NameError:
    nbins = 20

afracs = np.array([1/3.,0.5,2/3.,0.8,1])
akeys = np.array(['1/3','1/2','2/3','4/5','all'])
alpha_dict = {x: np.zeros(ntrials) for x in akeys}
st = time.time()
Farr = np.zeros((len(np.arange(220.,550.,3.)),11))
Farr[:,0] = np.arange(220.,550.,3.)
tau,mu = np.random.gamma(2,10,ntrials),1-np.random.gamma(2,0.15,ntrials)
while len(mu[mu<=0]) > 0: mu = 1-np.random.gamma(2,0.15,ntrials)
arr = np.zeros((ntrials,),dtype=[('tau','f8'),('mu','f8')])
arr['tau'],arr['mu']=tau,mu
np.savetxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.%s.dat'%date,arr,fmt='%.3f %.4f')
for i in range(0,ntrials):
    stime = np.arange(220.,550.,3.)
    F = GenerateMockCurve(stime,errstd=errstd,tau=tau[i],mu=mu[i])
    if i<10: 
        Farr[:,i+1] = F
        plt.figure(1)
        plt.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        plt.scatter(stime,F)
        plt.xlabel('Time (days)',fontsize=14)
        plt.ylabel('Flux')
        plt.title('Lightcurve %i'%i)
        plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(i+1,tau[i],mu[i],date))
        FILE=open('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau[i],mu[i],date),'w')
        for j in range(0,len(F)):
            FILE.write('%E %E\n'%(stime[j],F[j]))
        FILE.close()
