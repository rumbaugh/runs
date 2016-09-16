execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")

try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '3.14.14'

try:
    ylimits
except NameError:
    ylimits = 0.001

for pair in ['10','205','305','325','345','385','405','505']:
    cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung4/tdc1_rung4_double_pair%s.txt'%pair)
    ltime,Aflux,Bflux = cr[:,0],cr[:,1],cr[:,2]
    Aerr,Berr = cr[:,3],cr[:,4]
    ltime = (ltime-ltime[0])#/86400
    Aerr /= np.mean(Aflux)
    Aflux /= np.mean(Aflux)
    CalcStructureFunction(Aflux,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/strucfunc.TDC_rung4_double_pair%s_A_norm.%s.png'%(pair,date),ylimits=ylimits)
Astd = np.std(Aflux)
Amean = np.average(Aflux)
Arand = np.random.normal(Amean,Astd,len(Aflux))
Arand_werr = np.random.normal(Amean,Astd,len(Aflux))
for i in range(0,len(Aflux)):
    Arand_werr[i] += np.random.normal(0,Aerr[i])
    CalcStructureFunction(Arand,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/strucfunc.TDC_rung4_double_pair%s_A_rand_norm.%s.png'%(pair,date),ylimits=ylimits)
    CalcStructureFunction(Arand_werr,ltime,nbins=nbins,plotfile='/home/rumbaugh/sim_ltcurve_testing/strucfuncts/strucfunc.TDC_rung4_double_pair%s_A_rand_werr_norm.%s.png'%(pair,date),ylimits=ylimits)
