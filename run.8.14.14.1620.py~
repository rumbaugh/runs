execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/Load1938.py")
execfile("/home/rumbaugh/LinReg.py")

import matplotlib.pyplot as plt


try:
    nbins
except NameError:
    nbins = 20

try:
    date
except NameError:
    date = '8.14.14'

try:
    ylimits
except NameError:
    ylimits = None
nbins = 20
FILE = open('/home/rumbaugh/EVLA/light_curves/fit_output.strucfunc_VLA.norm.nbins_%i.%s.dat'%(nbins,date),'w')
FILE.write('# lens  image  alpha(all) err(all) con(all) err(all) \n')

for lens in ['0414','0712','1030','1127','1152']:
    source = lens
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    ltime = (ltime-ltime[0])#/86400
    if source == '0414':
        imgnames = ['A1','A2','B','C']
        nimg = 4
    elif source == '0712':
        imgnames = ['(A+B)','C','D']
        nimg = 3
    else:
        imgnames = ['A','B']
        nimg = 2
    for img in range(nimg):
        if source == '0712':
            Aflux,Aerr = flux_arr[img+1],flux_err_arr[img+1]
            if img == 0:
                A1flux,A1err = flux_arr[0],flux_err_arr[0]
                Aflux,Aerr = Aflux+A1flux,np.sqrt(Aerr**2+A1err**2)
        else: Aflux,Aerr = flux_arr[img],flux_err_arr[img]
        g = np.arange(len(ltime))[:len(ltime)-10]
        Aerr /= np.mean(Aflux[g])
        Aflux /= np.mean(Aflux[g])
        tau,V,terr_arr,Verr_arr = CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.nbins_%i.%s.png'%(lens,nbins,date),ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc.%s_A_norm.nbins_%i.%s.dat'%(lens,nbins,date),output_errors=True)
        g = np.where(tau >= 10)[0]
        con,alpha,errcon,erralpha = LinReg(np.log10(tau[g]),np.log10(V[g]),err=True)
        print '%4s %5s - alpha = %f +/- %f\n'%(lens,imgnames[img],alpha,erralpha)
        FILE.write('%6s %5s %f %f %f %f\n'%(lens,imgnames[img],alpha,erralpha,con,errcon))
        if img == 0:
            plt.figure(1)
            plt.rc('axes',linewidth=2)
            plt.fontsize = 14
            plt.tick_params(which='major',length=8,width=2,labelsize=14)
            plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
            plt.clf()
            plt.errorbar(np.log10(tau),np.log10(V),xerr=np.log10(np.e)*terr_arr/tau,yerr=np.log10(np.e)*Verr_arr/V,fmt='ro',lw=2,capsize=3,mew=1)
            curlims = plt.axis()
            xtmp = np.array([0,2.5])
            ytmp = con+(alpha)*xtmp
            plt.plot(xtmp,ytmp,lw=2)
            plt.xlim(0,2.5)
            plt.ylim(curlims[2],curlims[3])
            plt.xlabel('log(' + r'$\tau$)',fontsize=14)
            plt.ylabel('log(V)',fontsize=14)
            plt.fontsize = 14
            plt.tick_params(which='major',length=8,width=2,labelsize=14)
            plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
            plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc_VLA.%s_%s_norm.w_fit.%s.png'%(lens,imgnames[0],date))
FILE.close()
