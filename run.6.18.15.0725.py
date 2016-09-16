execfile('/home/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
import time
import matplotlib.pyplot as plt

date = '6.10.15'

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
#Farr = np.zeros((len(np.arange(220.,550.,3.)),ntrials+1))
#Farr[:,0] = np.arange(220.,550.,3.)
#tau,mu = np.random.gamma(2,10,ntrials),1-np.random.gamma(2,0.15,ntrials)
#mu5,mu10,mu15,mu20 = 1-np.random.gamma(2,0.15,ntrials),1-np.random.gamma(2,0.15,ntrials),1-np.random.gamma(2,0.15,ntrials),1-np.random.gamma(2,0.15,ntrials)
#arr = np.zeros((ntrials,),dtype=[('tau5','f8'),('mu5','f8'),('tau10','f8'),('mu10','f8'),('tau15','f8'),('mu15','f8'),('tau20','f8'),('mu20','f8')])
#arr['tau5'],arr['mu5'],arr['tau10'],arr['mu10'],arr['tau15'],arr['mu15'],arr['tau20'],arr['mu20']=np.ones(ntrials)*5.,mu5,np.ones(ntrials)*10.,mu10,np.ones(ntrials)*15.,mu15,np.ones(ntrials)*20.,mu20
cr=np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.%s.dat'%date)
#for i in np.array([10,30,34,45,50,64,85,87,98])-1:
redo_dict={20:np.array([3,96])}

for tau,it in zip([20],[3]):
    for i in redo_dict[tau]-1:
        mu=cr[:,2*it+1]
        stime = np.arange(220.,550.,3.)
        F_dict = GenerateMockCurve(stime,errstd=errstd,tau=tau,mu=mu[i],return_lc_params=True,curves=2)
        F1,F2 = F_dict['flux'][1],F_dict['flux'][2]
        F=F1+F2
        #Farr[:,i+1] = F
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
        plt.savefig('/home/rumbaugh/Fermi/plots/testlightcurve.tau_%i_%i.mu_%.3f.%s.png'%(tau,i+1,mu[i],date))
        FILE=open('/home/rumbaugh/Fermi/data/test/testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(tau,i+1,mu[i],date),'w')
        for j in range(0,len(F)):
            FILE.write('%E %E\n'%(stime[j],F[j]))
        FILE.close()
        arr = np.zeros((len(F_dict['Tfl']),),dtype=[('flr_times','f8'),('amp','f8'),('skew','f8'),('Tfl','f8'),('obs_flr_times','f8')])
        arr['flr_times'],arr['amp'],arr['skew'],arr['Tfl'],arr['obs_flr_times']=F_dict['flare_times'],F_dict['amps'],F_dict['skew'],F_dict['Tfl'],F_dict['flare_times']+stime[0]
        np.savetxt('/home/rumbaugh/Fermi/data/test/testlightcurve.tau_%i_%i.flare_params_truthvalues.mu_%.3f%s.dat'%(tau,i+1,mu[i],date),arr,fmt='%f %f %f %f %f')
