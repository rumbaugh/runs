import numpy as np
import pyfits as py
import pandas as pd

outlier_window,outlier_thresh,mac_thresh=100,0.5,5

DBdir='/home/rumbaugh/var_database/Y3A1'
crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drops=np.abs(crd['glo']-crd['ghi'])

hdubh=py.open('dr7_bh_Nov19_2013.fits')
data=hdubh[1].data

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

try:
    SN2DR7
except:
    DBID2SN={crdb['DatabaseID'][x]:crdb['SDSSNAME'][x] for x in np.arange(len(crdb))[crdb['SDSSNAME']!='-1']}

    SN2DR7={data['SDSS_NAME'][x]:x for x in np.arange(0,len(data))}

    sdssname=np.array([DBID2SN[x] for x in crd['DBID']])
    DR7ID=np.array([SN2DR7[x] for x in sdssname],dtype='i8')

gsort=np.argsort(DR7ID)
DR7ID,sdssname,crd=DR7ID[gsort],sdssname[gsort],crd[gsort]

maxgfixed=np.zeros(len(DR7ID))
for i in range(0,len(DR7ID)):
    DBID=crd['DBID'][i]
    
    tmpcr=np.loadtxt('%s/%s/LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    cr=np.zeros(len(tmpcr),dtype={'names':('Survey','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S20','f8','|S12','f8','f8','i8')})
    cr['Survey'],cr['MJD'],cr['BAND'],cr['MAG'],cr['MAGERR'],cr['FLAG']=tmpcr['Survey'],tmpcr['MJD'],tmpcr['BAND'],tmpcr['MAG'],tmpcr['MAGERR'],tmpcr['FLAG']
    crout=np.loadtxt('%s/%s/outliers.tab'%(DBdir,DBID),dtype='i8')*-2
    if len(crout)!=len(cr):crout=np.zeros(len(cr),dtype='i8')
    crout[(cr['MAG']<14)|(cr['MAG']>30)|(cr['MAGERR']>=5)]=-1
    for b in ['g','r','i']:
        gb=np.where((cr['BAND']==b)&(crout>=0))[0]
        if len(gb)>0:
            mag,mjd=cr['MAG'][gb],cr['MJD'][gb]
            for ipt in np.arange(0,len(gb)):
                gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
                if len(gthresh)>1:
                    if ((np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh)&(crout[gb[ipt]]!=-4)):
                        crout[gb[ipt]]=-2
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        macflags=np.ones(len(crmac),dtype='i8')
        for b in ['g','r','i','z','u']:
            gb=np.where((cr['BAND']==b)&(crout!=-1)&(crout!=-2))[0]
            gbmac=np.where(crmac['BAND']==b)[0]
            if len(gb)>0:
                gb0=np.where((cr['BAND']==b)&(crout!=-1)&(crout!=-2)&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0]
                if ((len(gb0)>0)&(len(gbmac)>0)):
                    mjd0,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
                    mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                    mindists=np.min(mjddists,axis=1)
                    gmac2=np.where(mindists<mac_thresh)[0]
                    macflags[gbmac[gmac2]]=-3
        try:
            croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),dtype='i8')
        except IOError:
            croutmac=np.zeros(len(crmac))
        macflags[croutmac==1]=-4
    except IOError:
        crmac=None
    if crmac!=None: 
        tmpcrmac=np.zeros(len(crmac),dtype={'names':('Survey','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S20','f8','|S12','f8','f8','i8')})
        tmpcrmac['Survey'],tmpcrmac['MJD'],tmpcrmac['BAND'],tmpcrmac['MAG'],tmpcrmac['MAGERR'],tmpcrmac['FLAG']=np.full(len(crmac),"SDSS",dtype='|S20'),crmac['MJD'],crmac['BAND'],crmac['MAG'],crmac['MAGERR'],crmac['FLAG']
        cr=np.append(cr,tmpcrmac)
        crout=np.append(crout,macflags)
    crout[(cr['MAG']<14)|(cr['MAG']>30)|(cr['MAGERR']>=.15)]=-1
    for b in ['g','r','i']:
        gb=np.where((cr['BAND']==b)&(crout>=0))[0]
        if len(gb)>0:
            mag,mjd=cr['MAG'][gb],cr['MJD'][gb]
            for ipt in np.arange(0,len(gb)):
                gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
                if len(gthresh)>1:
                    if ((np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh)&(crout[gb[ipt]]!=-4)):
                        crout[gb[ipt]]=-2
    crout=crout[cr['Survey']!='POSS']
    cr=cr[cr['Survey']!='POSS']
    try:
        maxgfixed[i]=np.max(cr['MAG'][(cr['BAND']=='g')&(crout>=0)])-np.min(cr['MAG'][(cr['BAND']=='g')&(crout>=0)])
    except ValueError:
        maxgfixed[i]=0
    for b in ['g','r','i']:
        outdf=pd.DataFrame({x:cr[x][cr['BAND']==b] for x in ['MJD','MAG','MAGERR']})
        outdf['FLAG']=crout[cr['BAND']==b]
        outdf=outdf[['MJD','MAG','MAGERR','FLAG']]
        outdf.to_csv('/home/rumbaugh/EVQ_DB/{}_{}'.format(DR7ID[i],b),index=False)
