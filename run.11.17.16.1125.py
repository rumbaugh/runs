import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
DB_path='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/DES+SDSS+POSS_col_plots.pdf')
cre=np.loadtxt('/home/rumbaugh/SDSSPOSS_Y1A1_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
IDs=np.sort(np.random.choice(IDs,100,False))
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

ge=np.argsort(exps)[::-1]


def plot_POSS(ax,band,band2,cid,bandname=None,connectpoints=False):
    POSS_cols=coldict
    # POSS_cols={'g': '#003300', 'r': '#ffb3ff', 'i': '#cccc00'}
    if bandname==None: bandname=band
    POSSmag,POSSmagerr=POSSmagdict[band],POSSmagerrdict[band]
    POSSmag2,POSSmagerr2=POSSmagdict[band2],POSSmagerrdict[band2]
    POSScol,POSScolerr=POSSmag-POSSmag2,np.sqrt(POSSmagerr**2+POSSmagerr2**2)
    POSSmjd=POSSmjddict[band]
    gcid=np.where(cID==cid)[0][0]
    gPOSSid=np.where(POSScid==cid)[0]
    curcol=POSS_cols[band]
    if connectpoints:
        gsort=np.argsort(POSSmjd)
        ax.plot(POSSmjd[gsort],POSScol[gsort],color=curcol,lw=2)
    ax.errorbar(POSSmjd,POSScol,yerr=POSScolerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    ax.scatter(POSSmjd,POSScol,color=curcol,marker='d')#,label='POSS %s'%band)
    mjdout,colout=POSSmjd,POSScol
    return mjdout,colout
    
def plot_SDSS(ax,band,band2,cid,bandname=None,connectpoints=False):
    SDSS_cols=coldict
    #SDSS_cols={'g': '#66ff66','u': 'purple', 'r': 'pink', 'i': 'brown', 'z': 'silver'}
    if bandname==None: bandname=band
    SDSSmag,SDSSmagerr=SDSSmagdict[band],SDSSmagerrdict[band]
    SDSSmag2,SDSSmagerr2=SDSSmagdict[band2],SDSSmagerrdict[band2]
    SDSScol,SDSScolerr=SDSSmag-SDSSmag2,np.sqrt(SDSSmagerr**2+SDSSmagerr2**2)
    gcid=np.where(cID==cid)[0][0]
    gSDSSid=np.where(SDSScid==cid)[0]
    #print SDF['THINGID']
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(SDSSmjd)
        ax.plot(SDSSmjd[gsort],SDSScol[gsort],color=curcol,lw=2)
    ax.errorbar(SDSSmjd,SDSScol,yerr=SDSScolerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    ax.scatter(SDSSmjd,SDSScol,color=curcol,label='%s-%s'%(band,band2),marker='d')
    mjdout,colout=SDSSmjd,SDSScol
    return mjdout,colout
    

def plot_band(ax,gid,band,band2,connectpoints=True,nolabels=False):
    gband=np.where(bands[gid]==band)[0]
    gband2=np.where(bands[gid]==band2)[0]
    magplot=mag[gid][gband]
    magploterr=magerr[gid][gband]
    magplot2=mag[gid][gband2]
    magploterr2=magerr[gid][gband2]
    g100=np.where(magplot<100)[0]
    g100b=np.where(magplot2<100)[0]
    gbands=np.union1d(gband[g100],gband2[g100b])
    if ((len(gbands)>0)&(len(g100)>0)&(len(g100b)>0)):
        mag1,mag2=np.interp(mjd[gid][gbands],mjd[gid][gband][g100],magplot[g100]),np.interp(mjd[gid][gbands],mjd[gid][gband2][g100b],magplot2[g100b])
        magerr1,magerr2=np.interp(mjd[gid][gbands],mjd[gid][gband][g100],magploterr[g100]),np.interp(mjd[gid][gbands],mjd[gid][gband2][g100b],magploterr2[g100b])
        col,colerr=mag1-mag2,np.sqrt(magerr1**2+magerr2**2)
        try:
            curcol=coldict[band]
        except KeyError:
            print '%s is not a valid band'%band
            return
        if connectpoints:
            gsort=np.argsort(mjd[gid][gbands])
            ax.plot(mjd[gid][gbands][gsort],col[gsort],color=curcol,lw=2)
        ax.errorbar(mjd[gid][gbands],col,yerr=colerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
        if nolabels:
            ax.scatter(mjd[gid][gbands],col,color=curcol)
        else:
            ax.scatter(mjd[gid][gbands],col,color=curcol,label='%s-%s'%(band,band2))
        mjdout,colout=mjd[gid][gbands],col
    else:
        mjdout,colout=np.zeros(0),np.zeros(0)
    return mjdout,colout


def plot_lightcurve(cid,band='all',plotSDSS=False,fname=None,connectpoints=True):
    band=band.lower()
    g=np.where(cID==cid)[0]
    if len(g)==0:
        print 'No matches for %i'%cid
        return
    fig=plt.figure(1)
    fig.clf()
    ax=fig.add_subplot(2,1,2)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if band=='all':
        for b1,b2 in zip(POSSbands[:-1],POSSbands[1:]):
            plot_band(ax,g,b1,b2,connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        ax.legend()
    ax=fig.add_subplot(2,1,1)
    allmjd,allcols={b: np.zeros(0) for b in POSSbands[:-1]},{b: np.zeros(0) for b in POSSbands[:-1]}
    if band=='all':
        for b1,b2 in zip(POSSbands[:-1],POSSbands[1:]):
            mjdtmp,coltmp=plot_band(ax,g,b1,b2,connectpoints=connectpoints,nolabels=True)
            allmjd[b1],allcols[b1]=np.append(allmjd[b1],mjdtmp),np.append(allcols[b1],coltmp)
            #plot_band(ax,g,b1,b2,connectpoints=connectpoints,nolabels=True)
        if plotSDSS==True:
            for b1,b2 in zip(POSSbands[:-1],POSSbands[1:]):
                mjdtmp,coltmp=plot_SDSS(ax,b1,b2,cid,connectpoints=connectpoints)
                allmjd[b1],allcols[b1]=np.append(allmjd[b1],mjdtmp),np.append(allcols[b1],coltmp)
                mjdtmp,coltmp=plot_POSS(ax,b1,b2,cid,connectpoints=connectpoints)
                allmjd[b1],allcols[b1]=np.append(allmjd[b1],mjdtmp),np.append(allcols[b1],coltmp)
                #plot_SDSS(ax,b1,b2,cid,connectpoints=connectpoints)
                #plot_POSS(ax,b1,b2,cid,connectpoints=connectpoints)
        xlim=plt.xlim()
        for b in POSSbands[:-1]:
            allmjd[b],allcols[b]=np.sort(allmjd[b]),allcols[b][np.argsort(allmjd[b])]
            plt.plot(allmjd[b],allcols[b],color=coldict[b],lw=2)
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        ylim=plt.ylim()
        if ylim[1]>2:ylim=(ylim[0],2)
        if ylim[0]<-1: ylim=(-1,ylim[1])
        plt.ylim(ylim)
        ax.legend()
    else:
        plot_band(ax,g,band,connectpoints=connectpoints)
    ax.set_xlabel('MJD')
    ax.set_ylabel('Color')
    ax.set_title(cid)
    if fname!=None: plt.savefig(psfpdf,format='pdf')
    return
  

outputdir='/home/rumbaugh/var_database'

cr=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cry=np.loadtxt('SDSSPOSS_lightcurve_entries_Y1A1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','SPid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})

for curid in IDs:
    gid,gidy=np.where(cr['cid']==curid)[0],np.where(cry['cid']==curid)[0]
    mjd,mag,magerr,cID,bands,yra,ydec=cry['mjd'][gidy],cry['mag'][gidy],cry['magerr'][gidy],cry['cid'][gidy],cry['band'][gidy],cry['ra'][gidy],cry['dec'][gidy]
    SDSSmjd,SDSScid=cr['mjd_SDSS'][gid],cr['cid'][gid]
    SDSSra,SDSSdec=cr['ra'][gid],cr['dec'][gid]
    SDSSmagdict,SDSSmagerrdict={b: cr['%s_SDSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_SDSS_err'%(b.upper())][gid] for b in POSSbands}
    POSScid=cr['cid'][gid]
    POSSra,POSSdec=cr['ra'][gid],cr['dec'][gid]
    POSSmagdict,POSSmagerrdict,POSSmjddict={b: cr['%s_POSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_POSS_err'%(b.upper())][gid] for b in POSSbands},{b: 50448.+365.25*(cr['EPOCH%s'%(b.upper())][gid]-1997) for b in POSSbands}


    plot_lightcurve(curid,plotSDSS=True,fname='/home/rumbaugh/var_database/plots/DES+SDSS+POSS_lightcurve_colors_%s.png'%curid)
psfpdf.close()
