execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")
execfile("/home/rumbaugh/LinReg.py")

import matplotlib.pyplot as plt

date = '6.9.14'

try:
    ylimits
except NameError:
    ylimits = None
nbins = 20
for lens in ['0414','0712','1030','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    Aerr /= np.mean(Aflux[g])
    Aflux /= np.mean(Aflux[g])
    tau,V,terr_arr,Verr_arr = CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.w_noiseSF.nbins_%i.%s.png'%(lens,nbins,date),ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc.%s_A_norm.w_noiseSF.nbins_%i.%s.dat'%(lens,nbins,date),output_errors=True,noiseSF=True,ntrials=1000)
    num2skip = 2
    if lens == '1127':
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[num2skip+1:2*len(tau)/3]),np.log10(V[num2skip+1:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[num2skip+1:len(tau)/2]),np.log10(V[num2skip+1:len(tau)/2]),err=True)
        con3,alpha3,errcon3,erralpha3 = LinReg(np.log10(tau[num2skip+1:]),np.log10(V[num2skip+1:]),err=True)
    elif lens == '1152':
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[num2skip+2:2*len(tau)/3]),np.log10(V[num2skip+2:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[num2skip+2:len(tau)/2]),np.log10(V[num2skip+2:len(tau)/2]),err=True)
        con3,alpha3,errcon3,erralpha3 = LinReg(np.log10(tau[num2skip+2:]),np.log10(V[num2skip+2:]),err=True)
    else:
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[num2skip:2*len(tau)/3]),np.log10(V[num2skip:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[num2skip:len(tau)/2]),np.log10(V[num2skip:len(tau)/2]),err=True)
        con3,alpha3,errcon3,erralpha3 = LinReg(np.log10(tau[num2skip:]),np.log10(V[num2skip:]),err=True)
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
    ytmp = con3+alpha3*xtmp
    ytmp2 = con+alpha*xtmp
    ytmp3 = con2+alpha2*xtmp
    plt.plot(xtmp,ytmp,lw=2)
    plt.plot(xtmp,ytmp2,lw=2,ls='dashed')
    plt.plot(xtmp,ytmp3,lw=2,ls='dotted')
    plt.xlim(0,2.5)
    plt.ylim(curlims[2],curlims[3])
    plt.xlabel('log(' + r'$\tau$)',fontsize=14)
    plt.ylabel('log(V)',fontsize=14)
    plt.fontsize = 15
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.w_fit.w_noiseSF.%s.png'%(lens,date))
