execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadEVLA_2011.py")
execfile("/home/rumbaugh/LinReg.py")

import matplotlib.pyplot as plt

date = '6.8.14'

try:
    ylimits
except NameError:
    ylimits = None
nbins = 10

FILE = open('/home/rumbaugh/EVLA/light_curves/fit_output.strucfunc_EVLA.norm.nbins_%i.%s.dat'%(nbins,date),'w')
FILE.write('# lens  image  alpha(all) err(all)  alpha(2/3) err(2/3) alpha(1/2) err(1/2)  con(all) err(all)   con(2/3) err(2/3) con(1/2) err(1/2)\n')

for lens in ['MG0414','B0712','B1938']:
    source = lens
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    ltime = crS['day']
    rms = crS['rms']
    fluxratio_err = 0.0043
    if source == 'MG0414':
        fluxratio_err = 0.0048
        imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
        nimg = 4
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
        nimg = 3
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
        nimg = 3
    errnames,imgshnames = np.copy(imgnames),np.copy(imgnames)
    for n in np.arange(0,len(errnames)): 
        errnames[n] = 'err%s'%errnames[n][4:]
        imgshnames[n] = '%s'%imgshnames[n][4:]
    if source == 'B1938': imgshnames = np.append('C',imgshnames[2:])
    if source == 'B0712': imgshnames = np.append('(A+B)',imgshnames[2:])
    fluxA1 = crS[imgnames[0]]
    A1err = crS[errnames[0]]
    fluxA2 = crS[imgnames[1]]
    A2err = crS[errnames[1]]
    Aflux = fluxA1+fluxA2
    Aerr = np.sqrt(A1err**2+A2err**2)

    for img in np.arange(nimg):
        if source == 'MG0414':
            Aflux,Aerr = crS[imgnames[img]],crS[errnames[img]]
        elif img > 0:
            Aflux,Aerr = crS[imgnames[img+1]],crS[errnames[img+1]]
        g = np.where((Aflux > 0) & (Aerr > 0))[0]
        Aflux,Aerr = Aflux[g],Aerr[g]
        Aerr /= np.mean(Aflux)
        Aflux /= np.mean(Aflux)
        plotfile=None
        if img == 0: plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_%s_norm.nbins_%i.%s.png'%(lens,imgshnames[0],nbins,date)
        tau,V,terr_arr,Verr_arr = CalcStructureFunction(Aflux,ltime[g],Aerr,nbins=nbins,plotfile=plotfile,ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc_EVLA.%s_%s_norm.nbins_%i.%s.dat'%(lens,imgshnames[img],nbins,date),output_errors=True)
        num2skip=2
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[num2skip:2*len(tau)/3]),np.log10(V[num2skip:2*len(tau)/3]),err=True)
        con2,alpha2,errcon2,erralpha2 = LinReg(np.log10(tau[num2skip:len(tau)/2]),np.log10(V[num2skip:len(tau)/2]),err=True)
        con3,alpha3,errcon3,erralpha3 = LinReg(np.log10(tau[num2skip:]),np.log10(V[num2skip:]),err=True)
        alpha,alpha2,alpha3 = alpha+1,alpha2+1,alpha3+1
        FILE.write('%6s %2s %f %f %f %f %f %f %f %f %f %f %f %f\n'%(lens,imgshnames[img],alpha3,erralpha3,alpha,erralpha,alpha2,erralpha2,con3,errcon3,con,errcon,con2,errcon2))
        if img == 0:
            print '%s - alpha = %f +/- %f\n'%(lens,alpha,erralpha)

            plt.figure(1)
            plt.rc('axes',linewidth=2)
            plt.fontsize = 14
            plt.tick_params(which='major',length=8,width=2,labelsize=14)
            plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
            plt.clf()
            plt.errorbar(np.log10(tau),np.log10(V),xerr=np.log10(np.e)*terr_arr/tau,yerr=np.log10(np.e)*Verr_arr/V,fmt='ro',lw=2,capsize=3,mew=1)
            curlims = plt.axis()
            xtmp = np.array([0,2.5])
            ytmp = con3+(alpha3-1)*xtmp
            ytmp2 = con+(alpha-1)*xtmp
            ytmp3 = con2+(alpha2-1)*xtmp
            plt.plot(xtmp,ytmp,lw=2)
            plt.plot(xtmp,ytmp2,lw=2,ls='dashed')
            plt.plot(xtmp,ytmp3,lw=2,ls='dotted')
            plt.xlim(0,2.0)
            plt.ylim(curlims[2],curlims[3])
            plt.xlabel('log(' + r'$\tau$)',fontsize=14)
            plt.ylabel('log(V)',fontsize=14)
            plt.fontsize = 14
            plt.tick_params(which='major',length=8,width=2,labelsize=14)
            plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
            plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc_EVLA.%s_%s_norm.w_fit.%s.png'%(lens,imgshnames[0],date))
            
FILE.close()
