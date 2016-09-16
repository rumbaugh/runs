import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scstats
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/SCRed_vs_i_z.4.19.16.pdf')

adamcorrval=-1.3975614258700002
ierrmax=99999999

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]
zarr=np.linspace(0.1,2,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}
fig=figure(1)
icuts={x:0 for x in targets[np.argsort(zlist)]}
FILE=open('/home/rumbaugh/SC_to_iz_cuts.4.19.16.dat','w')
FILE.write('# field icut zcut\n')
for field in targets[np.argsort(zlist)]:
    crSC=np.loadtxt('/home/rumbaugh/Chandra/coadd_cats/supercolors_cut-20.9.%s.4.11.16.dat'%field,dtype={'names':('ID','RA','Dec','magR','magI','magZ','dmagR','dmagI','dmagZ','SCmagRed','SCmagBlue','dRed','dBlue'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
    m,y0,r,p,stderr=scstats.linregress(crSC['magI'],crSC['SCmagRed'])
    icuts[field]=(-20.9-y0)/m
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(crSC['magI'],crSC['SCmagRed'])
    xlim=plt.xlim()
    ylim=plt.ylim()
    xdummy=np.linspace(xlim[0],xlim[1],1000)
    plt.plot(xdummy,m*xdummy+y0,lw=2,color='r',ls='dashed')
    ax.axhline(-20.9,lw=2,color='k',ls='dashed')
    ax.set_xlabel("m_i'")
    ax.set_ylabel("m_red")
    ax.set_title("%s - i' cut = %.1f"%(field,icuts[field]))
    plt.xlim(xlim)
    plt.ylim(ylim)
    fig.savefig(psfpdf,format='pdf')

    gzol=np.where(crSC['magZ']>16.5)[0]
    m,y0,r,p,stderr=scstats.linregress(crSC['magZ'][gzol],crSC['SCmagRed'][gzol])
    icuts[field]=(-20.9-y0)/m
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(crSC['magZ'][gzol],crSC['SCmagRed'][gzol])
    xlim=plt.xlim()
    ylim=plt.ylim()
    xdummy=np.linspace(xlim[0],xlim[1],1000)
    plt.plot(xdummy,m*xdummy+y0,lw=2,color='r',ls='dashed')
    ax.axhline(-20.9,lw=2,color='k',ls='dashed')
    ax.set_xlabel("m_z'")
    ax.set_ylabel("m_red")
    ax.set_title("%s - z' cut = %.1f"%(field,icuts[field]))
    plt.xlim(xlim)
    plt.ylim(ylim)
    fig.savefig(psfpdf,format='pdf')
    zcut=(-20.9-y0)/m
    FILE.write('%12s %f %f\n'%(field,icuts[field],zcut))
FILE.close()
psfpdf.close()
