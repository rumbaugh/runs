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
    date = '6.11.14'

try:
    ylimits
except NameError:
    ylimits = None
nbins = 20
FILE = open('/home/rumbaugh/EVLA/light_curves/fit_output.strucfunc_VLA.norm.nbins_%i.%s.dat'%(nbins,date),'w')
FILE.write('# lens  image  alpha(all) err(all)  alpha(2/3) err(2/3) alpha(1/2) err(1/2)  con(all) err(all)   con(2/3) err(2/3) con(1/2) err(1/2)\n')

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
                Aflux,Aerr = Aflux+A1flux,np.sqrt(Aflux**2+A1flux**2)
        else: Aflux,Aerr = flux_arr[img],flux_err_arr[img]
        g = np.arange(len(ltime))[:len(ltime)-10]
        Aerr /= np.mean(Aflux[g])
        Aflux /= np.mean(Aflux[g])
        tau,V,terr_arr,Verr_arr = CalcStructureFunction(Aflux[g],ltime[g],Aerr[g],nbins=nbins,plotfile='/home/rumbaugh/EVLA/light_curves/plots/logstrucfunc.%s_A_norm.nbins_%i.%s.png'%(lens,nbins,date),ylimits=ylimits,output=True,outfile='/home/rumbaugh/EVLA/light_curves/strucfunc.%s_A_norm.nbins_%i.%s.dat'%(lens,nbins,date),output_errors=True)
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
        alpha,alpha2,alpha3 = alpha+1,alpha2+1,alpha3+1
        print '%4s - alpha = %f +/- %f\n'%(lens,alpha,erralpha)
        FILE.write('%6s %5s %f %f %f %f %f %f %f %f %f %f %f %f\n'%(lens,imgnames[img],alpha3,erralpha3,alpha,erralpha,alpha2,erralpha2,con3,errcon3,con,errcon,con2,errcon2))
FILE.close()
