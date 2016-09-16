execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")

try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '3.16.14'

try:
    ylimits
except NameError:
    ylimits = 0.001

for pair in range(1,11):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/Nick_pair%i.txt'%pair)
    ltime,Aflux,Bflux = cr[:,0],cr[:,1],cr[:,2]
    Aerr,Berr = cr[:,3],cr[:,4]
    ltime = (ltime-ltime[0])#/86400
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    CalcStructureFunction(Aflux,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/logstrucfunc.VLA_pair%i_A_norm.%s.png'%(pair,date),ylimits=ylimits)
Astd = np.std(Aflux)
Amean = np.average(Aflux)
Arand = np.random.normal(Amean,Astd,len(Aflux))
Arand_werr = np.random.normal(Amean,Astd,len(Aflux))
for i in range(0,len(Aflux)):
    Arand_werr[i] += np.random.normal(0,Aerr[i])
    CalcStructureFunction(Arand,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/logstrucfunc.VLA_rand_pair%i_A_norm.%s.png'%(pair,date),ylimits=ylimits)
    CalcStructureFunction(Arand_werr,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/logstrucfunc.VLA_rand_werr_pair%i_A_norm.%s.png'%(pair,date),ylimits=ylimits)
