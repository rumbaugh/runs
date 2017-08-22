import numpy as np
import pyfits as py
import os
import scipy.ndimage.filters as filt
from astropy.io import fits
from astropy import wcs
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/centroid_wcontours.8.19.17.pdf')

cendf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.6.26.17.csv')
RFcendf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.RF.csv')
cdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clusters.dat',skiprows=1,names=['field_uc','cluster','ra','dec','z','sig0.5Mpc','N0.5Mpc','sig0.5Mpcerr','sig1Mpc','N1Mpc','sig1Mpcerr','logMvir','err','nh'],delim_whitespace=True)
mmcgdf=pd.read_csv('/home/rumbaugh/Chandra/MMCG_spec_1.5Rvir.07.20.17.cat',delim_whitespace=True)

df=pd.merge(cendf,cdf,on=['cluster'],how='left',suffixes=('_cen','_clus'))
df=pd.merge(df,RFcendf,on=['field','cluster'],how='outer',suffixes=('_old',''))



name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'SC0849C','Lynx_W':'SC0849D','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

level_dict={'RXJ1716A': [30,60,90,120],'Cluster_A':[3,6,9,12],'Cluster_B':[2,4,6,7.5],'Cluster_D':[1,2,3],'Cluster_I':(1,2,3,4,5),'1324+3011':[4,8,12,16,19],'1324+3013':[2.5,5.,7.5,10,12.5],'0910+5422':[5,10,15,20,25],'0910+5419':[2.5,5.,7.5,10,12.5],'0848+4451':[4,8,12,16],'Lynx_W':[1.5,3,4.5,6],'RCS0224B':[6,12,18,24],'RXJ1221B':[20,40,60,80],'RXJ1757':[7,14,21,28],'RXJ1821':[10,20,30,40],'Cl1350C':[10,20,30,40]}


stampwid=480

rdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clus_rad.dat',delim_whitespace=True,names=['field','cluster','rad(pix)','RA','Dec','ImageX','ImageY'],skiprows=1)

pcdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.precontour_info.csv',delim_whitespace=True)

XCdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',delim_whitespace=True,skiprows=1,names=['field','cluster','RA(deg)','Dec(deg)','RA(sex)','Dec(sex)'])

cr=np.loadtxt('/home/rumbaugh/cc_out.1.26.16.dat',dtype={'names':('field','z','omegaM','omegaVac','H0','age(Gyr)','zage(Gyr)','LTT(Gyr)','comov.rad.dist.(Mpc)','comov.rad.dist.(Gyr)','comov.vol.(Gpc^3)','DA(Mpc)','DA(Gyr)','kpc_DA','DL(Mpc)','DL(Gyr)','DistMod','E(z)','4piDL^2(Gpc^2)','4piDL^2(cm^2)'),'formats':('|S32','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

AMs=0.5/(cr['kpc_DA']/1000.)/60.
#fields=cr['ID']
#kpcDA=cr['kpc_DA']


ordered_clus=['RCS0224B','0848+4451','Lynx_W','0910+5419','0910+5422','RXJ1221B','1324+3011','1324+3013','Cluster_I','Cl1350C','Cluster_A','Cluster_B','Cluster_D','RXJ1716A','RXJ1757','RXJ1821']
g=np.zeros(len(pcdf),dtype='i8')
for clus,ic in zip(ordered_clus,np.arange(len(ordered_clus))):
    g[ic]=np.where(pcdf.cluster.values==clus)[0][0]
    try:
        name_dict[clus]
    except KeyError:
        name_dict[clus]=clus
pcdf=pcdf.loc[g]

for i in range(0,len(pcdf)):
    field=pcdf.field.iloc[i]
    cluster=pcdf.cluster.iloc[i]
    dftmp=df[df.cluster.values==cluster]
    if field=='cl1324':
        if pcdf.cluster.iloc[i]=='Cluster_I':
            field='cl1324_north'
        else:
            field='cl1324_south'
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    gcr=np.where(cr['field']==field)[0][0]
    gr=np.where(rdf.cluster.values==cluster)[0][0]
    #rc_as=rc/kpcDA[gcr]
    infits='{}/{}_full_nops.vig_corr.smoothed.z_{:4.2f}.beta_0.67.rc_180kpc.img'.format(curdir,field,pcdf.z.iloc[i])
    hdu=fits.open(infits)
    data=np.copy(hdu[0].data)
    wdata=wcs.WCS(hdu[0].header)
    bkgarr=data[pcdf.bkgcenY.iloc[i]-pcdf.bkgheight.iloc[i]/2:pcdf.bkgcenY.iloc[i]+pcdf.bkgheight.iloc[i]/2,pcdf.bkgcenX.iloc[i]-pcdf.bkgwid.iloc[i]/2:pcdf.bkgcenX.iloc[i]+pcdf.bkgwid.iloc[i]/2]
    bkglevel=np.sum(bkgarr)/(pcdf.bkgwid.iloc[i]*pcdf.bkgheight.iloc[i])
    bkgrms=np.sqrt(np.sum(1./np.size(bkgarr)*(bkgarr-bkglevel)**2))
    stamparr=data[np.int(np.round(rdf.ImageY.iloc[gr]))-stampwid/2:np.int(np.round(rdf.ImageY.iloc[gr]))+stampwid/2,np.int(np.round(rdf.ImageX.iloc[gr]))-stampwid/2:np.int(np.round(rdf.ImageX.iloc[gr]))+stampwid/2]
    iy,ix=np.arange(np.int(np.round(rdf.ImageY.iloc[gr]))-stampwid/2,np.int(np.round(rdf.ImageY.iloc[gr]))+stampwid/2),np.arange(np.int(np.round(rdf.ImageX.iloc[gr]))-stampwid/2,np.int(np.round(rdf.ImageX.iloc[gr]))+stampwid/2)
    ixy_meshgrid=np.meshgrid(ix,iy)
    ixy_pairs=np.zeros((len(ix)**2,2))
    ixy_pairs[:,0],ixy_pairs[:,1]=ixy_meshgrid[0].flatten(),ixy_meshgrid[1].flatten()
    wcspairs=wdata.wcs_pix2world(ixy_pairs,1)
    radec_meshgrid=np.zeros(np.shape(ixy_meshgrid))
    radec_meshgrid[0],radec_meshgrid[1]=wcspairs[:,0].reshape(np.shape(ixy_meshgrid[0])),wcspairs[:,1].reshape(np.shape(ixy_meshgrid[1]))
    plt.clf()
    fig=plt.figure(1,figsize=(8,8))
    xRA,xDEC=dftmp.Xray_ra.iloc[0],dftmp.Xray_dec.iloc[0]
    plt.scatter([xRA],[xDEC],marker='x',s=80,color='r',label='X-ray',lw=2)
    plt.scatter([dftmp.BCG_ra.iloc[0]],[dftmp.BCG_dec.iloc[0]],marker='o',s=80,color='green',label='BCG')
    plt.scatter([dftmp.MMCG_ra.iloc[0]],[dftmp.MMCG_dec.iloc[0]],marker='*',s=80,color='blue',label='MMCG')
    plt.scatter([dftmp.ra.iloc[0]],[dftmp.dec.iloc[0]],marker='+',s=100,lw=2,color='orange',label='LWM')
    plt.scatter([dftmp.MWM_ra.iloc[0]],[dftmp.MWM_dec.iloc[0]],marker='d',s=80,color='magenta',label='MWM')
    phidummy=np.linspace(0,2*np.pi,1000)
    xdummy,ydummy=AMs[gcr]*1./60*np.cos(phidummy),AMs[gcr]*1./60*np.sin(phidummy)
    xdummy,ydummy=dftmp.Xray_ra.iloc[0]+xdummy/np.cos(dftmp.Xray_dec.iloc[0]*np.pi/180.),dftmp.Xray_dec.iloc[0]+ydummy
    plt.plot(xdummy,ydummy,color='k',ls='dashed')
    plt.xlabel(r'RA - RA$_{Xray}$ (arcminutes)')
    plt.ylabel(r'Dec - Dec$_{Xray}$ (arcminutes)')
    a=plt.contour(radec_meshgrid[0],radec_meshgrid[1],(stamparr-bkglevel)/bkgrms,colors='r',levels=level_dict[cluster])
    xlim=plt.xlim()
    #plt.title(pcdf.cluster.iloc[i])
    ax=plt.gca()
    ax.text(0.5,0.95,name_dict[pcdf.cluster.iloc[i]],color='k',horizontalalignment='center',verticalalignment='top',transform=ax.transAxes,fontsize=20)
    xticks,yticks=np.arange(xRA-1.5/60/np.cos(xDEC*np.pi/180.),xRA+2./60/np.cos(xDEC*np.pi/180.),.5/60/np.cos(xDEC*np.pi/180.)),np.arange(xDEC-1.5/60,xDEC+2./60,.5/60)
    xlabs,ylabs=['{:+0g}'.format(x) for x in np.arange(-1.5,2,0.5)],['{:+0g}'.format(x) for x in np.arange(-1.5,2,0.5)]
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xticklabels(xlabs)
    ax.set_yticklabels(ylabs)
    plt.xlim(xlim[1],xlim[0])
    plt.xlim(np.max(radec_meshgrid[0]),np.min(radec_meshgrid[0]))
    plt.ylim(np.min(radec_meshgrid[1]),np.max(radec_meshgrid[1]))
    if cluster=='Cluster_I': plt.ylim(np.min(radec_meshgrid[1])-0.1/60,np.max(radec_meshgrid[1])-0.1/60)
    fig.savefig(psfpdf,format='pdf')
    print pcdf.cluster.iloc[i],a.levels,np.max((stamparr-bkglevel)/bkgrms),SphDist(dftmp.Xray_ra.iloc[0],dftmp.Xray_dec.iloc[0],dftmp.BCG_ra.iloc[0],dftmp.BCG_dec.iloc[0])
psfpdf.close()
