import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/milliquas_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])

ge=np.argsort(exps)[::-1]

con=ea.connect()

def plot_SDSS(band,cid,bandname=None,connectpoints=True):
    SDSS_cols={'g': '#66ff66','u': 'purple', 'r': 'pink', 'i': 'brown', 'z': 'silver'}
    if bandname==None: bandname=band
    SDSSmag,SDSSmagerr=SDSSmagdict[band],SDSSmagerrdict[band]
    gcid=np.where(cID==cid)[0][0]
    gSDSSid=np.where((SDSScid==cid)&(60*SphDist(yra[gcid],ydec[gcid],SDSSra,SDSSdec)<2.))[0]
    #print SDF['THINGID'][gSDSSid]
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(SDSSmjd[gSDSSid])
        plt.plot(SDSSmjd[gSDSSid][gsort],SDSSmag[gSDSSid][gsort],color=curcol,lw=2)
    plt.errorbar(SDSSmjd[gSDSSid],SDSSmag[gSDSSid],yerr=SDSSmagerr[gSDSSid],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(SDSSmjd[gSDSSid],SDSSmag[gSDSSid],color=curcol,label='SDSS %s'%band,marker='d')
    

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


def plot_lightcurve(cid,band='all',plotSDSS=False,fname=None,connectpoints=True):
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
        if plotSDSS==True:
            for b in SDSSbands:
                plot_SDSS(b,cid,bandname=SDSS_colnames[b],connectpoints=connectpoints)
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
laststep=29
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

    SDSSquery='SELECT s.mjd_g as mjd,s.ra,s.dec,s.objid,s.numrow,s.psfmag_u,s.psfmag_g,s.psfmag_r,s.psfmag_i,s.psfmag_z,s.psfmagerr_u,s.psfmagerr_g,s.psfmagerr_r,s.psfmagerr_i,s.psfmagerr_z,s.run,s.rerun,s.stripe,s.thingid,m.mq_rownum,m.coadd_objects_id as cid,m.hpix FROM RUMBAUGH.MQ_SDSS_DR13_MATCH s, RUMBAUGH.MILLIQUAS_Y1A1_MATCH_ONLY m WHERE m.numrow=s.numrow and m.coadd_objects_id in (%s)'%idsstr

    SDF=con.query_to_pandas(SDSSquery)
    stags=np.zeros(len(SDF['RA']),dtype='|S12')
    stags[:]='NONE'
    stags[np.array(SDF['STRIPE'])==82]='Stripe82'

    #cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y1a1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','MGid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})
    mjd,mag,magerr,cID,bands,yra,ydec=np.array(DF['MJD_OBS']),np.array(DF['MAGPSF']),np.array(DF['MAGERR_PSF']),np.array(DF['COADD_OBJECTS_ID']),np.array(DF['BAND']),np.array(DF['RA']),np.array(DF['DEC'])
    SDSSmjd,SDSScid=np.array(SDF['MJD']),np.array(SDF['CID'])
    SDSSra,SDSSdec=np.array(SDF['RA']),np.array(SDF['DEC'])
    SDSSmagdict,SDSSmagerrdict={b: np.array(SDF['PSFMAG_%s'%(b.upper())]) for b in SDSSbands},{b: np.array(SDF['PSFMAGERR_%s'%(b.upper())]) for b in SDSSbands}


    for idcur,iid in zip(curIDs,np.arange(len(curIDs))):
        #print idcur
        DBID=curIDstep+iid
        gci=np.where(idcur==cID)[0]
        gsci=np.where(idcur==SDSScid)[0]
        plot_lightcurve(idcur,plotSDSS=True,fname='/home/rumbaugh/var_database/plots/DES+SDSS_lightcurve_%s.png'%idcur)
        gsci=np.where(idcur==SDSScid)[0]
