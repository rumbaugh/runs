execfile('/home/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
import time
import matplotlib.pyplot as plt

date = '7.1.15'

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

redo_pairs=np.array([70])-1

for i in redo_pairs:
    stime = np.arange(220.,550.,3.)
    F_dict = GenerateMockCurve(stime,errstd=errstd,tau=None,mu=None,return_lc_params=True,curves=1)
    F = F_dict['flux']
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(stime,F,color='cyan')
    plt.xlabel('Time (days)',fontsize=14)
    plt.ylabel('Flux')
    plt.title('Lightcurve %i'%(i+1))
    plt.savefig('/home/rumbaugh/Fermi/plots/testlightcurve_notau_%i.%s.png'%(i+1,date))
    FILE=open('/home/rumbaugh/Fermi/data/test/testlightcurve_notau_%i.%s.dat'%(i+1,date),'w')
    for j in range(0,len(F)):
        FILE.write('%E %E\n'%(stime[j],F[j]))
    FILE.close()
    arr = np.zeros((len(F_dict['Tfl']),),dtype=[('flr_times','f8'),('amp','f8'),('skew','f8'),('Tfl','f8'),('obs_flr_times','f8')])
    arr['flr_times'],arr['amp'],arr['skew'],arr['Tfl'],arr['obs_flr_times']=F_dict['flare_times'],F_dict['amps'],F_dict['skew'],F_dict['Tfl'],F_dict['flare_times']+stime[0]
    np.savetxt('/home/rumbaugh/Fermi/data/test/testlightcurve_notau_%i.flare_params_truthvalues.%s.dat'%(i+1,date),arr,fmt='%f %f %f %f %f')
