import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
#nside=16384
nside=64
sdict={16:16,64:4}

def covplot(ras,decs,pcol,nside=16):
    hpix=hp.ang2pix(nside,(90-decs)*np.pi/180.,ras*np.pi/180)
    b=np.bincount(hpix)
    hpixb=np.nonzero(b)
    b,hpixb=b[b>0],hpixb[0]
    HPang=np.array(hp.pix2ang(nside,hpixb))
    HPra,HPdec=HPang[1]*180/np.pi,90-HPang[0]*180/np.pi
    opacs=b*0.6/np.max(b)
    for ra,dec,op in zip(HPra,HPdec,opacs): plt.scatter(ra,dec,color=pcol,marker='h',s=sdict[nside],alpha=op)
    plt.xlabel('RA')
    plt.ylabel('Dec.')
    plt.xlim(0,360)
    plt.ylim(-90,90)
plt.figure(1)
plt.clf()
def do_plots(ras,decs,pcol,i,fname,nside=16):
    plt.figure(1)
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    covplot(ras,decs,pcol,nside=nside)
    plt.figure(i+2)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    covplot(ras,decs,pcol,nside=nside)
    plt.savefig(fname)
    if i==1:
        plt.figure(10 )
        plt.clf()
        execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
        covplot(ras,decs,pcol,nside=nside)
        covplot(cr3['ra'],cr3['dec'],'cyan',nside=nside)
        plt.savefig('/home/rumbaugh/coverage_plot.SDSS+POSS.png')
        

cr1=np.loadtxt('milliquas_y1a1_match.tab',dtype={'names':('MQ','ra','dec','hpix','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1)
cr2=np.loadtxt('TID_randsamp2_rumbaugh.csv',dtype={'names':('ra','dec','id'),'formats':('f8','f8','i8')},delimiter=',',skiprows=1)
cr3=np.loadtxt('sdss-poss+healpix.txt',dtype={'names':('n','ra','dec','id'),'formats':('i8','f8','f8','i8')})
for i,crs,cols,fnames in zip(np.arange(3),[cr1,cr2,cr3],['green','magenta','cyan'],['/home/rumbaugh/coverage_plot.milliquas.png','/home/rumbaugh/coverage_plot.SDSS.png','/home/rumbaugh/coverage_plot.POSS.png']):
    if i<2: do_plots(crs['ra'],crs['dec'],cols,i,fnames,nside)
plt.figure(1)
cry=np.loadtxt('Y1A1_TILE_CORNERS.tab',usecols=(1,2,3,4,5,6,7,8),skiprows=1)
for i in range(0,np.shape(cry)[0]):
    ras,decs=cry[i][:4],cry[i][4:]
    if np.max(ras)-np.min(ras)>200:
        ghi,glo=np.where(ras>200)[0],np.where(ras<100)[0]
        rahi,ralo=np.copy(ras),np.copy(ras)
        rahi[glo],ralo[ghi]=360.,0.
        plt.fill(rahi,decs,color='orange',alpha=0.2,edgecolor='None')
        plt.fill(ralo,decs,color='orange',alpha=0.2,edgecolor='None')
    else:
        plt.fill(ras,decs,color='orange',alpha=0.2,edgecolor='None')

#cro=np.loadtxt('ozdes_lightcurve_entries_y1a1.tab',dtype={'names':('MJD_OBS','IMAGEID','COADD_OBJECTS_ID','SVA1_COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','BAND','EXPTIME'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S2','f8')},skiprows=1)
hdu=py.open('/home/rumbaugh/Downloads/OzDES_QSO_20160627.fits')
cro=hdu[1].data
plt.scatter(cro['RA'],cro['DEC'],s=2,color='red',edgecolor='None')
plt.savefig('/home/rumbaugh/coverage_plot.all.png')
