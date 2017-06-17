import numpy as np
import matplotlib.pyplot as plt
import scale_estimators as SE

velbound=3250
binwid=500

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crCMD=np.loadtxt('/home/rumbaugh/Chandra/ORELSE_cluster_member_info_all.dat',dtype={'names':('field','cluster','ra','dec','z','mag','col','rso','isBCG','isBCG_tot'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8','i8','i8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))

c = 3.0*10**5

for clus,ic in zip(crBCG['cluster'],np.arange(len(crBCG))):
    zs=crCMD['z'][crCMD['cluster']==clus]
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
    try:
        propername=fielddict[field]
    except KeyError:
        propername=field.upper()
    if zC==None: zC=SE.biweight_loc(zs)
    vels = (zs-SE.biweight_loc(zs))*c/(1.0+zs)
    sig=CalcVelDisp(zs,ConfInvMethod=None)
    gblue,gred=np.where(crCMD['rso'][crCMD['cluster']==clus]>1)[0],np.where(crCMD['rso'][crCMD['cluster']==clus]<1)[0]

    fig=plt.figure(1)
    fig.clf()
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 20
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.hist(vels,range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='white',facecolor='None',lw=1)
    ax.hist(vels[gred],range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='None',facecolor='#e23200',alpha=0.9,label='Red Gals')
    ax.hist(vels[gblue],range=(-velbound,velbound),bins=(2*velbound)/binwid,edgecolor='None',facecolor='#33caff',alpha=0.5,label='Blue Gals')
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
    ax.arrow(vels[crCMD['isBCG'][crCMD['cluster']==clus]==1][0],a0+dy*1.2,0,-dy,color='magenta',lw=3,head_width=binwid/2.5,head_length=ylim[1]/30.,width=binwid/20,overhang=0.5)
    ax.text(0.5,0.95,clus,color='k',fontsize=20,verticalalignment='center',horizontalalignment='center',transform=ax.transAxes)
    ax.text(0.95,0.97,'z=%04.2f'%zC,color='k',fontsize=14,verticalalignment='top',horizontalalignment='right',transform=ax.transAxes)
    plt.savefig('/home/rumbaugh/Chandra/plots/velplots.%s.%s.png'%(field,clus))
