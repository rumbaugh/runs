import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/LFC_color_param.py')

crf=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S32')
crpre=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S6')

for year in np.arange(1,14):
    gy=np.where(crpre=='graz%02i'%year)[0]
    psfpdf=bpdf.PdfPages('/home/rumbaugh/LFC_color_param_plots_graz%02i.2.20.16.pdf'%year)
    fig=plt.figure(1)
    for SED in crf[gy]:
        curcr=np.loadtxt(SED)
        w,S=np.copy(curcr[:,0]),np.copy(curcr[:,1])
        z=np.linspace(0.1,2,191)
        Ablue,Ared=np.zeros(len(z)),np.zeros(len(z))
        for i in range(0,len(z)): Ablue[i],Ared[i]=find_color_param(w,S,z[i])
    
        fig.clf()
        ax=fig.add_subplot(1,1,1)
        ax.plot(z,Ablue,color='b',label='A(Blue)')
        ax.plot(z,Ared,color='r',label='A(Red)')
        ax.set_xlabel("Redshift")
        ax.set_ylabel("A")
        ax.set_title("%s"%SED)
        ax.set_xlim(0,2)
        ax.set_ylim(0,1.05)
        ax.legend()
        fig.savefig(psfpdf,format='pdf')
    psfpdf.close()

