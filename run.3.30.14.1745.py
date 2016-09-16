execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/StructureFunction.py')
execfile('/home/rumbaugh/LinReg.py')
execfile('/home/rumbaugh/KStest.py')
import time
import matplotlib.pyplot as plt

date = '3.30.14'

try:
    ntrials
except NameError:
    ntrials = 10000

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
for i in range(0,ntrials):
    stime = np.arange(220.,550.,3.)
    F = GenerateMockCurve(stime,errstd=errstd)
    if i<10: 
        tau,V = CalcStructureFunction(F,stime,nbins=20,doplot=True,plotfile='/mnt/data2/rumbaugh/Fermi/plots/strucfuncofMockCurves_%i.%s.png'%(i,date),output=True)
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
        plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testlightcurve_%i.%s.png'%(i,date))
    else: tau,V = CalcStructureFunction(F,stime,nbins=20,doplot=False,output=True)
    for key,fr in zip(akeys,afracs):
        con,alpha = LinReg(np.log10(tau[:int(len(tau)*fr)]),np.log10(V[:int(len(tau)*fr)]))
        alpha_dict[key][i] = alpha+1
print 'Elapsed time: %f seconds'%(time.time()-st)
for key,fr in zip(akeys,afracs):
    if key != 'all': 
        md,prob = KStest(alpha_dict[key],alphadists[key])
        print 'Prob for %s: %f\n'%(key,prob)
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.hist(alpha_dict[key],bins=nbins)
    plt.xlabel(r'$\alpha$',fontsize=14)
    plt.title('Distribution of Structure Function Power Index using %s of data'%key)
    keystr = key
    if key != 'all':
        keystr = '%4.2f'%fr
    plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/stattestofMockCurves.hist.%s_of_data.%s.png'%(keystr,date))
    
