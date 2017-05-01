import numpy as np
import matplotlib
import matplotlib.pyplot as plt

closethresh,nearthresh=10,100

DBdir='/home/rumbaugh/var_database/Y3A1'

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID','y3a1_mag_auto_g'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24','f8')})

ilo,ihi,rlo,rhi=np.zeros(len(crd)),np.zeros(len(crd)),np.zeros(len(crd)),np.zeros(len(crd))

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SP_rownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

for DBID,idb in zip(crd['DBID'],np.arange(len(crd))):
    cr=np.loadtxt('%s/%s/LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    try:
        crout=np.loadtxt('%s/%s/outliers.tab'%(DBdir,DBID),dtype='i8')
    except:
        crout=np.zeros(len(cr))
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        try:
            croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),dtype='i8')
            try:
                crmac=crmac[croutmac>-1]
                croutmac=croutmac[croutmac>-1]
            except:
                if croutmac==-1: croutmac,crmac=np.ones(0),cr[np.zeros(0,dtype='i8')]
            outlier_arr=np.array(np.append(crout,croutmac),dtype='bool')
        except:
            croutmac,crmac=np.ones(0),cr[np.zeros(0,dtype='i8')]
            outlier_arr=np.array(crout,dtype='bool')
    except:
        crmac=None
        outlier_arr=np.array(crout,dtype='bool')
    if crmac!=None:
        newcr=np.zeros((len(cr),),dtype={'names':('DatabaseID','Survey','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','|S4','f8','f8','f8','|S4','f8','f8','i8')})
        newcr['DatabaseID'],newcr['Survey'],newcr['RA'],newcr['DEC'],newcr['MJD'],newcr['BAND'],newcr['MAG'],newcr['MAGERR'],newcr['FLAG']=cr['DatabaseID'],cr['Survey'],cr['RA'],cr['DEC'],cr['MJD'],cr['BAND'],cr['MAG'],cr['MAGERR'],cr['FLAG']
        newcrmac=np.zeros((len(crmac),),dtype={'names':('DatabaseID','Survey','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','|S4','f8','f8','f8','|S4','f8','f8','i8')})
        newcrmac['DatabaseID'],newcrmac['Survey'],newcrmac['RA'],newcrmac['DEC'],newcrmac['MJD'],newcrmac['BAND'],newcrmac['MAG'],newcrmac['MAGERR'],newcrmac['FLAG']=crmac['DatabaseID'],np.full(len(crmac),'SDSS',dtype='|S4'),crmac['RA'],crmac['DEC'],crmac['MJD'],crmac['BAND'],crmac['MAG'],crmac['MAGERR'],crmac['FLAG']
        cr=np.append(newcr,newcrmac)
    cr=cr[outlier_arr==0]
    for b,lo_arr,hi_arr in zip(['r','i'],[rlo,ilo],[rhi,ihi]):
        gb=np.where((cr['BAND']==b)&(cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<.15))[0]
        if len(gb)>0:
            glo_close=np.where(np.abs(crd['mjdlo'][idb]-cr['MJD'][gb])<closethresh)[0]
            if len(glo_close)>0:
                glo_close=glo_close[np.argsort(np.abs(crd['mjdlo'][idb]-cr['MJD'][gb[glo_close]]))[0]]
                lo_arr[idb]=cr['MAG'][gb[glo_close]]
            else:
                glo_close=np.where(np.abs(crd['mjdlo'][idb]-cr['MJD'][gb])<nearthresh)[0]
                lo_arr[idb]=np.sum(cr['MAG'][gb[glo_close]]/np.abs(crd['mjdlo'][idb]-cr['MJD'][gb[glo_close]]))/np.sum(1./np.abs(crd['mjdlo'][idb]-cr['MJD'][gb[glo_close]]))
            ghi_close=np.where(np.abs(crd['mjdhi'][idb]-cr['MJD'][gb])<closethresh)[0]
            if len(ghi_close)>0:
                ghi_close=ghi_close[np.argsort(np.abs(crd['mjdhi'][idb]-cr['MJD'][gb[ghi_close]]))[0]]
                hi_arr[idb]=cr['MAG'][gb[ghi_close]]
            else:
                ghi_close=np.where(np.abs(crd['mjdhi'][idb]-cr['MJD'][gb])<nearthresh)[0]
                hi_arr[idb]=np.sum(cr['MAG'][gb[ghi_close]]/np.abs(crd['mjdhi'][idb]-cr['MJD'][gb[ghi_close]]))/np.sum(1./np.abs(crd['mjdhi'][idb]-cr['MJD'][gb[ghi_close]]))

outcr=np.zeros((len(crdb),),dtype={'names':('RA','DEC','Redshift','MJD_lo','g_lo','sig_lo','flag_lo','MJD_hi','g_hi','sig_hi','flag_hi','RA_DES','DEC_DES','DBID','y3a1_mag_auto_g','ilo','ihi','rlo','rhi'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24','f8','f8','f8','f8','f8')})
outcr['RA'],outcr['DEC'],outcr['Redshift'],outcr['MJD_lo'],outcr['g_lo'],outcr['sig_lo'],outcr['flag_lo'],outcr['MJD_hi'],outcr['g_hi'],outcr['sig_hi'],outcr['flag_hi'],outcr['RA_DES'],outcr['DEC_DES'],outcr['DBID'],outcr['y3a1_mag_auto_g'],outcr['ilo'],outcr['ihi'],outcr['rlo'],outcr['rhi']=crd['RA'],crd['DEC'],crd['z'],crd['MJDlo'],crd['glo'],crd['siglo'],crd['flaglo'],crd['MJDhi'],crd['ghi'],crd['sighi'],crd['flaghi'],crd['RA_DES'],crd['DEC_DES'],crd['DBID'],crd['y3a1_mag_auto_g'],ilo,ihi,rlo,rhi
np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.30.17.tab',outcr,header='RA DEC Redshift MJD_lo g_lo sig_lo flag_lo MJD_hi g_hi sig_hi flag_hi RA_DES DEC_DES DBID y3a1_mag_auto_g i_lo i_hi r_lo r_hi',fmt='%f %f %f %f %f %f %i %f %f %f %i %f %f %24s %f %f %f %f %f')
