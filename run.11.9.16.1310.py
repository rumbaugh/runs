import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/SDSSPOSS_Y1A1_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
IDs=IDs[:10]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

ge=np.argsort(exps)[::-1]

con=ea.connect()

def plot_POSS(band,cid,bandname=None,connectpoints=False):
    POSS_cols={'g': '003300', 'r': 'ffb3ff', 'i': 'cccc00'}
    if bandname==None: bandname=band
    POSSmag,POSSmagerr=POSSmagdict[band],POSSmagerrdict[band]
    POSSmjd=POSSmjddict[band]
    gcid=np.where(cID==cid)[0][0]
    gPOSSid=np.where(POSScid==cid)[0]
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(POSSmjd)
        plt.plot(POSSmjd[gsort],POSSmag[gsort],color=curcol,lw=2)
    plt.errorbar(POSSmjd,POSSmag,yerr=POSSmagerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(POSSmjd,POSSmag,color=curcol,label='POSS %s'%band,marker='d')
    
def plot_SDSS(band,cid,bandname=None,connectpoints=False):
    SDSS_cols={'g': '66ff66','u': 'purple', 'r': 'pink', 'i': 'brown', 'z': 'silver'}
    if bandname==None: bandname=band
    SDSSmag,SDSSmagerr=SDSSmagdict[band],SDSSmagerrdict[band]
    gcid=np.where(cID==cid)[0][0]
    gSDSSid=np.where(SDSScid==cid)[0]
    #print SDF['THINGID']
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(SDSSmjd)
        plt.plot(SDSSmjd[gsort],SDSSmag[gsort],color=curcol,lw=2)
    plt.errorbar(SDSSmjd,SDSSmag,yerr=SDSSmagerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(SDSSmjd,SDSSmag,color=curcol,label='SDSS %s'%band,marker='d')
    

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

cr=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra',' dec','G_POSS','R_POSS','I_POSS','G_POSS_err',' R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cry=np.loadtxt('SDSSPOSS_lightcurve_entries_Y1A1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','SPid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})

for curid in IDs:
    gid,gidy=np.where(cr['cid']==curid)[0],np.where(cry['cid']==curid)[0]
    mjd,mag,magerr,cID,bands,yra,ydec=cry['mjd'][gidy],cry['mag'][gidy],cry['magerr'][gidy],cry['cid'][gidy],cry['band'][gidy],cry['ra'][gidy],cry['dec'][gidy]
    SDSSmjd,SDSScid=cr['mjd_SDSS'][gid],cr['cid'][gid]
    SDSSra,SDSSdec=cr['ra'][gid],cr['dec'][gid]
    SDSSmagdict,SDSSmagerrdict={b: cr['%s_SDSS'%(b.upper())] for b in POSSbands},{b: cr['%s_SDSS_err'%(b.upper())] for b in POSSbands}
    POSScid=cr['cid'][gid]
    POSSra,POSSdec=cr['ra'][gid],cr['dec'][gid]
    POSSmagdict,POSSmagerrdict,POSSmjddict={b: cr['%s_POSS'%(b.upper())] for b in POSSbands},{b: cr['%s_POSS_err'%(b.upper())] for b in POSSbands},{b: 2450448.5+365.25*(cr['EPOCH%s'%(b.upper())]-1997) for b in POSSbands}


    plot_lightcurve(curid,plotSDSS=True,fname='/home/rumbaugh/var_database/plots/DES+SDSS+POSS_lightcurve_%s.png'%curid)
