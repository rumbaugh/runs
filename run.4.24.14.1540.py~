execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")
execfile("/home/rumbaugh/LinReg.py")

import matplotlib.pyplot as plt


try:
    nbins
except NameError:
    nbins = 10

try:
    date
except NameError:
    date = '4.24.14'

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
    tau,V,terr_arr,Verr_arr = CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.%s.png'%(lens,date),ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc.%s_A_norm.nbins_%i.%s.dat'%(lens,nbins,date),output_errors=True)
    if lens == '1127':
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[3:2*len(tau)/3]),np.log10(V[3:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[3:len(tau)/2]),np.log10(V[3:len(tau)/2]),err=True)
    elif lens == '1152':
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[4:2*len(tau)/3]),np.log10(V[4:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[4:len(tau)/2]),np.log10(V[4:len(tau)/2]),err=True)
    else:
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[2:2*len(tau)/3]),np.log10(V[2:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[2:len(tau)/2]),np.log10(V[2:len(tau)/2]),err=True)
    print '%4s - alpha = %f +/- %f\n'%(lens,alpha,erralpha)

    plt.figure(1)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.clf()
    plt.errorbar(np.log10(tau),np.log10(V),xerr=np.log10(np.e)*terr_arr/tau,yerr=np.log10(np.e)*Verr_arr/V,fmt='ro',lw=2,capsize=3,mew=1)
    curlims = plt.axis()
    xtmp = np.array([0,2.5])
    ytmp = con+alpha*xtmp
    ytmp2 = con2+alpha2*xtmp
    plt.plot(xtmp,ytmp,lw=2)
    plt.plot(xtmp,ytmp2,lw=2,ls='dashed')
    plt.xlim(0,2.5)
    plt.ylim(curlims[2],curlims[3])
    plt.xlabel('log(' + r'$\tau$)')
    plt.ylabel('log(V)')
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.w_fit.%s.png'%(lens,date))

ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()
Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

ltime = (ltime-ltime[0])/86400.
tau,V,terr_arr,Verr_arr = CalcStructureFunction(Cflux,ltime,Cerr,nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.1938_C_norm.%s.png'%(date),ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc.%s_A_norm.nbins_%i.%s.dat'%(lens,nbins,date),output_errors=True)
con,alpha,errcon,erralpha = LinReg(np.log10(tau[1:]),np.log10(V[1:]),err=True)
print '1938 - alpha = %f +/- %f\n'%(alpha,erralpha)

plt.figure(1)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.clf()
plt.errorbar(np.log10(tau),np.log10(V),xerr=np.log10(np.e)*terr_arr/tau,yerr=np.log10(np.e)*Verr_arr/V,fmt='ro',lw=2,capsize=3,mew=1)
curlims = plt.axis()
xtmp = np.array([0,2.5])
ytmp = con+alpha*xtmp
plt.plot(xtmp,ytmp)
plt.xlim(0,2.0)
plt.ylim(curlims[2],curlims[3])
plt.xlabel('log(' + r'$\tau$)')
plt.ylabel('log(V)')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.1938_A_norm.w_fit.%s.png'%(date))

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
