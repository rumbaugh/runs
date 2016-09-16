execfile('/home/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
import time
import matplotlib.pyplot as plt

date = '8.19.15'

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
    nbins = 50

afracs = np.array([1/3.,0.5,2/3.,0.8,1])
akeys = np.array(['1/3','1/2','2/3','4/5','all'])
alpha_dict = {x: np.zeros(ntrials) for x in akeys}
st = time.time()

tau_o,mu_o = np.random.gamma(2,10,ntrials),1-np.random.gamma(2,0.15,ntrials)
#while len(tau_o[tau_o<=0])>0:tau_o[tau_o<=0]=np.random.gamma(2,10,len(tau_o[tau_o<=0]))
while len(mu_o[mu_o<=0])>0:mu_o[mu_o<=0]=1-np.random.gamma(2,0.15,len(mu_o[mu_o<=0]))
arr = np.zeros((ntrials,),dtype=[('tau','f8'),('mu','f8')])
arr['tau'],arr['mu']=tau_o,mu_o
np.savetxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.%s.dat'%date,arr,fmt='%.3f %.4f')
cr=np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.%s.dat'%date)
tau,mu=cr[:,0],cr[:,1]
for i in np.arange(0,ntrials):
    stime = np.arange(220.,880.,3.)
    F_dict = GenerateMockCurve(stime,errstd=errstd,tau=tau_o[i],mu=mu_o[i],return_lc_params=True,curves=2)
    F1,F2 = F_dict['flux'][1],F_dict['flux'][2]
    F=F1+F2
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(stime,F1,color='blue')
    plt.scatter(stime,F2,color='red')
    plt.scatter(stime,F,color='cyan')
    plt.xlabel('Time (days)',fontsize=14)
    plt.ylabel('Flux')
    plt.title('Lightcurve %i'%(i+1))
    plt.savefig('/home/rumbaugh/Fermi/plots/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(i+1,tau[i],mu[i],date))
    FILE=open('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau[i],mu[i],date),'w')
    FILEA=open('/home/rumbaugh/Fermi/data/test/testlightcurve_%i_A.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau[i],mu[i],date),'w')
    FILEB=open('/home/rumbaugh/Fermi/data/test/testlightcurve_%i_B.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau[i],mu[i],date),'w')
    for j in range(0,len(F)/2):
        FILE.write('%E %E\n'%(stime[j],F[j]))
        FILEA.write('%E %E\n'%(stime[j],F[j]))
    for j in range(len(F)/2,len(F)):
        FILE.write('%E %E\n'%(stime[j],F[j]))
        FILEB.write('%E %E\n'%(stime[j],F[j]))
    FILE.close()
    FILEA.close()
    FILEB.close()
    arr = np.zeros((len(F_dict['Tfl']),),dtype=[('flr_times','f8'),('amp','f8'),('skew','f8'),('Tfl','f8'),('obs_flr_times','f8')])
    arr['flr_times'],arr['amp'],arr['skew'],arr['Tfl'],arr['obs_flr_times']=F_dict['flare_times'],F_dict['amps'],F_dict['skew'],F_dict['Tfl'],F_dict['flare_times']+stime[0]
    np.savetxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.flare_params_truthvalues.%s.dat'%(i+1,tau[i],mu[i],date),arr,fmt='%f %f %f %f %f')
