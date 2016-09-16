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
    ylimits = 0.0005

for lens in ['0414','0712','1030','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    Aerr /= np.mean(Aflux[g])
    Aflux /= np.mean(Aflux[g])
    CalcStructureFunction(Aflux[g],ltime[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/strucfunc.%s_A_norm.%s.png'%(lens,date),ylimits=ylimits)
Astd = np.std(Aflux[g])
Amean = np.average(Aflux[g])
Arand = np.random.normal(Amean,Astd,len(g))
Arand_werr = np.random.normal(Amean,Astd,len(g))
for i in range(0,len(g)):
    Arand_werr[i] += np.random.normal(0,Aerr[g[i]])
CalcStructureFunction(Arand,ltime[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/strucfunc.rand_%s_A_norm.%s.png'%(lens,date),ylimits=ylimits)
CalcStructureFunction(Arand_werr,ltime[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/strucfunc.rand_werr_%s_A_norm.%s.png'%(lens,date),ylimits=ylimits)
