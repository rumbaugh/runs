import numpy as np
import matplotlib.pyplot as plt
import scale_estimators as SE
execfile("/home/rumbaugh/scale_estimators.py")
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')
import matplotlib.backends.backend_pdf as bpdf
import pandas as pd
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/velplots.RF.8.16.17.pdf')

velbound=3250
binwid=500

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))
MMCGdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.MMCG_vels.csv')

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.
c = 3.0*10**5

name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}
clusters=MMCGdf.cluster.values
for i in np.arange(len(clusters)): 
    try:
        name_dict[clusters[i]]
    except KeyError:
        name_dict[clusters[i]]=clusters[i]

for clus,ic in zip(MMCGdf.cluster.values,np.arange(len(MMCGdf))):
    try:
        CMdf=pd.read_csv('/home/rumbaugh/MMCGs_fotNick/cluster_member_1Mpc/Cluster_member_{}_spec_1Mpc.cat'.format(clus),delim_whitespace=True)
    except IOError:
        print 'No MMCG file for %s'%clus
        continue
    try:
        gcr=np.where(cr['cluster']==clus)[0][0]
        raC,decC,zC=cr['RA'][gcr],cr['Dec'][gcr],cr['z'][gcr]
        Mpc_am=1./Mpc[gcr]/60.
        field=cr['field'][gcr].lower()
    except:
        print '%s not found, using X-ray center'%clus
        try:
            gcr=np.where(crx['cluster']==clus)[0][0]
            raC,decC=crx['RA'][gcr],crx['DEC'][gcr]
            field=crx['field'][gcr].lower()
            zf=spec_dict[field]['z'][0]
            cosmocalc(zf,outfile='/home/rumbaugh/temp_cc.2.1.17.dat')
            crcctmp=np.loadtxt('/home/rumbaugh/temp_cc.2.1.17.dat')
            Mpc_am=1./(crcctmp[12]/1000.)/60.
            zC=None
        except:
            print 'X-ray center not found either'
            continue
    zs=CMdf.z_spec.values
    if zC==None: zC=SE.biweight_loc(zs)
    Qzs,SFzs=CMdf.z_spec.values[CMdf.Quiescent.values==1],CMdf.z_spec.values[CMdf.Quiescent.values==0]
    vels = (zs-SE.biweight_loc(zs))*c/(1.0+zs)
    Qvels,SFvels=(Qzs-SE.biweight_loc(zs))*c/(1.0+Qzs),(SFzs-SE.biweight_loc(zs))*c/(1.0+SFzs)
    sig,sigerr=CalcVelDisp(zs)
    if len(Qzs)>2:
        Qsig,Qsigerr=CalcVelDisp(Qzs)
    else:
        Qsig,Qsigerr=0,0
    if len(SFzs)>2:
        SFsig,SFsigerr=CalcVelDisp(SFzs)
    else:
        SFsig,SFsigerr=0,0

    fig=plt.figure(1)
    fig.clf()
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 20
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.hist(vels,range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='white',facecolor='None',lw=1)
    ax.hist(Qvels,range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='None',facecolor='#e23200',alpha=0.9,label='Quiescent Gals')
    ax.hist(SFvels,range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='None',facecolor='#33caff',alpha=0.5,label='Star-Forming Gals')
    ax.hist(vels,range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='k',facecolor='None',lw=3)
    ylim=ax.get_ylim()
    xdummy=np.linspace(-velbound,velbound,2000)
    a0=len(vels)/(np.sqrt(2*np.pi)*sig/binwid)
    ydummy=a0*np.exp(-(xdummy**2)/(2.*sig**2))
    ax.plot(xdummy,ydummy,color='green',lw=2)
    ax.set_ylim(0,ylim[1]+1)
    if a0*1.08>ylim[1]: ax.set_ylim(0,a0*1.1)
    ax.set_xlim(-velbound,velbound)
    ax.set_xlabel('Relative Velocity (km/s)')
    ax.set_ylabel('Num. of Galaxies')
    ylim=ax.get_ylim()
    dy=0.05*ylim[1]
    ax.arrow(MMCGdf.MMCGvel[MMCGdf['cluster']==clus].iloc[0],a0+dy*1.2,0,-dy,color='magenta',lw=3,head_width=binwid/2.5,head_length=ylim[1]/30.,width=binwid/20,overhang=0.5)
    ax.text(0.5,0.95,clus,color='k',fontsize=20,verticalalignment='center',horizontalalignment='center',transform=ax.transAxes)
    ax.text(0.95,0.97,'z=%04.2f'%zC,color='k',fontsize=14,verticalalignment='top',horizontalalignment='right',transform=ax.transAxes)
    ax.set_title(clus)
    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
