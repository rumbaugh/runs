import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/k_Imp_test.3.7.16.pdf')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

FILE=open('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat','w')
FILE.write('# field k_soft k_hard k_full\n')

fig=figure(1)
ks=np.zeros(len(targets))
for field in targets:
    hdu=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    data=hdu[1].data
    FILE.write('%12s'%field)
    for band in ['soft','hard','full']:
        ncnts=data['%s_net_cts'%(band[0].upper()+band[1:])]
        flux=data['%s_flux'%(band[0].upper()+band[1:])]
        ktmp=flux[ncnts>0]/ncnts[ncnts>0]
        FILE.write(' %E'%(np.median(ktmp)))
        fig.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        ax=fig.add_subplot(1,1,1)
        ax.scatter(ncnts,flux*10**15)
        xlim=plt.xlim()
        ylim=plt.ylim()
        xdummy=np.linspace(xlim[0],xlim[1],1000)
        plt.plot(xdummy,xdummy*np.median(ktmp)*10**15,color='k',lw=2,ls='--')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_xlabel("Net Counts")
        ax.set_ylabel("Flux")
        ax.set_title('%s - %s'%(field,band))
        fig.savefig(psfpdf,format='pdf')
    FILE.write('\n')
FILE.close()
psfpdf.close()    
            
