import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/milliquas_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'psfmag_%s'%b for b in SDSSbands}

ge=np.argsort(exps)[::-1]

con=ea.connect()

def plot_band(gid,band,connectpoints=True):
    gband=np.where(bands[gid]==band)[0]
    magplot=mag[gid][gband]
    magploterr=magerr[gid][gband]
    g100=np.where(magplot<100)[0]
    try:
        curcol=coldict[band]
    except KeyError:
        print '%s is not a valid band'%band
        return
    if connectpoints:
        gsort=np.argsort(mjd[gid][gband][g100])
        plt.plot(mjd[gid][gband][g100][gsort],magplot[g100][gsort],color=curcol,lw=2)
    plt.errorbar(mjd[gid][gband][g100],magplot[g100],yerr=magploterr[g100],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(mjd[gid][gband][g100],magplot[g100],color=curcol,label=band)
    #return

def plot_lightcurve(cid,band='all',fname=None,connectpoints=True):
    band=band.lower()
    g=np.where(cID==cid)[0]
    if len(g)==0:
        print 'No matches for %i'%cid
        return
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if band=='all':
        for b in coldict.keys():
            plot_band(g,b,connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        plt.legend()
    else:
        plot_band(g,band,connectpoints=connectpoints)
    plt.xlabel('MJD')
    plt.ylabel('Mag_PSF')
    plt.title(cid)
    if fname!=None: plt.savefig(fname)
    return

outputdir='/home/rumbaugh/var_database'
IDsteplen=10

curIDstep=0
laststep=len(IDs)
steps_arr=np.arange(0,laststep,IDsteplen,dtype='i8')
for curIDstep in steps_arr:
    idsstr=''
    if curIDstep!=steps_arr[-1]:
        for s in IDs[curIDstep:curIDstep+10]: idsstr='%s, %i'%(idsstr,s)
        curIDs=IDs[curIDstep:curIDstep+10]
    else:
        for s in IDs[curIDstep:laststep]: idsstr='%s, %i'%(idsstr,s)
        curIDs=IDs[curIDstep:laststep]
    idsstr=idsstr[1:]

    query='SELECT e.mjd_obs,o.imageid,o.object_id,y.COADD_OBJECTS_ID,y.RA,y.DEC,o.mag_auto+i.zeropoint as magauto,o.magerr_auto+i.sigma_zeropoint as magerr_auto,o.mag_psf+i.zeropoint as magpsf,o.magerr_psf+i.sigma_zeropoint as magerr_psf,o.band,i.exptime FROM des_admin.Y1A1_COADD_OBJECTS y, des_admin.y1a1_objects o, des_admin.y1a1_image i,des_admin.y1a1_exposure e where o.imageid=i.id and i.exposureid=e.id and y.coadd_objects_id=o.coadd_objects_id and y.coadd_objects_id in (%s)'%idsstr

    DF=con.query_to_pandas(query)
)
    mjd,mag,magerr,cID,bands,yra,ydec=np.array(DF['MJD_OBS']),np.array(DF['MAGPSF']),np.array(DF['MAGERR_PSF']),np.array(DF['COADD_OBJECTS_ID']),np.array(DF['BAND']),np.array(DF['RA']),np.array(DF['DEC'])
    for idcur,iid in zip(curIDs,np.arange(len(curIDs))):
        #print idcur
        DBID=curIDstep+iid
        gci=np.where(idcur==cID)[0]
        plot_lightcurve(idcur,fname='/home/rumbaugh/var_database/plots/DES_lightcurve_%s.png'%idcur)
