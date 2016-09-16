execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")
execfile("/home/rumbaugh/LinReg.py")


try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '3.27.14'

try:
    ylimits
except NameError:
    ylimits = None

for lens in ['0414','0712','1030','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    Aerr /= np.mean(Aflux[g])
    Aflux /= np.mean(Aflux[g])
    tau,V = CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.%s.png'%(lens,date),ylimits=ylimits,output=True)
    con,alpha,errcon,erralpha = LinReg(np.log10(tau),np.log10(V),err=True)
    print '%4s - alpha = %f +/- %f\n'%(lens,alpha,erralpha)
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()
Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

ltime = (ltime-ltime[0])/86400.
tau,V = CalcStructureFunction(Cflux,ltime,Cerr,nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.1938_C_norm.%s.png'%(date),ylimits=ylimits,output=True)
con,alpha,errcon,erralpha = LinReg(np.log10(tau),np.log10(V),err=True)
print '1938 - alpha = %f +/- %f\n'%(alpha,erralpha)

for lens in ['0414','0712','1030','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    Aerr /= np.mean(Aflux[g])
    Aflux /= np.mean(Aflux[g])
    CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/strucfunc.%s_A_norm.%s.png'%(lens,date),ylimits=ylimits,plotlog=False)
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()
Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

ltime = (ltime-ltime[0])/86400.
CalcStructureFunction(Cflux,ltime,Cerr,nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/strucfunc.1938_C_norm.%s.png'%(date),ylimits=ylimits,plotlog=False)
