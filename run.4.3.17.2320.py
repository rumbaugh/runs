import numpy as np
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
psfpage=bpdf.PdfPages('/home/rumbaugh/DR7_OVV_test.pdf')
DBdir='/home/rumbaugh/var_database/Y3A1'

timethresh=90

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
yhdu=py.open('/home/rumbaugh/dr7_evq.fits')
ydata=yhdu[1].data
ydata=ydata[ydata['FIRST_FR_TYPE']>0]
maxvar=np.zeros(len(ydata))
medvar=np.zeros(len(ydata))
gy=np.zeros(len(ydata),dtype='i8')
for i in range(0,len(gy)):
    gy[i]=np.where(crdb['SDSSNAME']==ydata['SDSS_NAME'][i])[0][0]
    DBID=crdb['DatabaseID'][gy[i]]
    
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): 
        continue
    elif np.shape(cr)==():
        outlier_arr=np.zeros(1,dtype='bool')
        gorig=np.zeros(1,dtype='i8')[(np.array([cr['MAG']])>14)&(np.array([cr['MAG']])<30)&(np.array([cr['MAGERR']])<5)&(np.array([cr['Survey']])!='POSS')]
    else:
        outlier_arr=np.zeros(len(cr),dtype='bool')
        gorig=np.arange(len(cr))[(cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)&(cr['Survey']!='POSS')]
    ggood=np.where((cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)&(cr['Survey']!='POSS'))[0]#&(cr['FLAG']<16))[0]
    gmc=np.where(DBID==crmcm['DBID'])[0]
    if len(gmc)>0:
        s82flag[idb]=1
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        outlier_mac_arr=-np.ones(len(crmac),dtype='i8')
        gorigmac=np.arange(len(crmac))[(crmac['MAG']>14)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
        crmac=crmac[(crmac['MAG']>14)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
        gbmac=np.where(crmac['BAND']=='g')[0]
        if len(gbmac)<=0: 
            maclen=0
            gmac2=np.arange(0)
    else:
        s82flag[idb]=0
        maclen=0
        gmac2,gbmac,gorigmac=np.arange(0),np.arange(0),np.arange(0)
        outlier_mac_arr=np.zeros(0,dtype='bool')
    #SNflag=False
    if np.shape(cr)==():
        ra[idb],dec[idb]=cr['RA'],cr['DEC']
        if len(ggood)<1:
            mydblen=0
            gb0=np.zeros(0,dtype='i8')
            if len(gmc)>0:
                if len(gbmac)>0:
                    cr=crmac[gbmac]
                    gmac2=np.arange(len(gbmac))
                    maclen=len(cr)
                    mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.full(len(cr),'SDSS')
                    gb=np.where(bands=='g')[0]
                else:
                    gb=np.zeros(0,dtype='i8')
            else:
                gb=np.zeros(0,dtype='i8')
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
            gb=np.where(bands=='g')[0]
            if len(gb)==0:
                mjd,mag,magerr,bands,survey=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0,dtype='|S4'),np.zeros(0,dtype='|S4')
                mydblen=0
            else:
                mydblen=1
            if ((len(gmc)>0)&(len(gb)>0)):
                gb0=np.where((mjd>np.min(crmac['MJD'])-30)&(mjd<np.max(crmac['MJD'])+30))[0]    
                if ((len(gb0)>0)&(len(gbmac)>0)):
                    mjd0,mjdmac=mjd[gb0],mjd[gbmac]
                    mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                    mindists=np.min(mjddists,axis=1)
                    gmac2=np.where(mindists>mac_thresh)[0]
                else:
                    gmac2=np.arange(len(gbmac))
                surveymac=np.zeros(len(gmac2),dtype='|S8')
                surveymac[:]='SDSS'
                mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
                maclen=len(gmac2)
            elif ((len(gmc)>0)&(len(gb)==0)):
                gmac2=np.arange(len(gbmac))
                mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
                maclen=len(mjd)
            gb=np.where(bands=='g')[0]
    else:
        gSDSS=np.where(cr['Survey']=='SDSS')[0]
        if len(gSDSS)>0:
            ra[idb],dec[idb]=cr['RA'][gSDSS[0]],cr['DEC'][gSDSS[0]]
        else:
            ra[idb],dec[idb]=cr['RA'][0],cr['DEC'][0]
        cr=cr[ggood]
        gb=np.where(cr['BAND']=='g')[0]
        cr=cr[gb]
        gorig=gorig[gb]
        mydblen=len(gb)    
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
        if len(gmc)>0:
            gb0=np.where((cr['BAND']=='g')&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0]    
            if ((len(gb0)>0)&(len(gbmac)>0)):
                mjd0,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
                mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                mindists=np.min(mjddists,axis=1)
                gmac2=np.where(mindists>mac_thresh)[0]
            else:
                gmac2=np.arange(len(gbmac))
            surveymac=np.zeros(len(gmac2),dtype='|S8')
            surveymac[:]='SDSS'
            mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
            maclen=len(gmac2)
        gb=np.where(bands=='g')[0]
        #if len(cr)>1:
        #    initdists=SphDist(cr['RA'][0],cr['DEC'][0],cr['RA'][1:],cr['DEC'][1:])
        #    if np.max(initdists)>0.3: SNflag=True
    if maclen>0:outlier_mac_arr[gorigmac[gbmac[gmac2]]]=0
    var_array,mjd_array=np.zeros(0),np.zeros(0)
    if len(gb)>1:
        for ipt in np.arange(len(gb)):
            gthresh=np.where(np.abs(mjd[gb]-mjd[gb[ipt]])<outlier_window)[0]
            if len(gthresh)>1:
                if ipt<mydblen:
                    outlier_arr[gorig[gb[ipt]]]= np.abs(np.median(mag[gb[gthresh]])-mag[gb[ipt]]) > outlier_thresh
                else:
                    outlier_mac_arr[gorigmac[gbmac[gmac2[ipt-mydblen]]]]= np.abs(np.median(mag[gb[gthresh]])-mag[gb[ipt]]) > outlier_thresh
        #np.savetxt('%s/%s/outliers.tab'%(DBdir,DBID),outlier_arr,fmt='%2i')
        #if maclen>0:np.savetxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),outlier_mac_arr,fmt='%2i')
        outlier_arr=outlier_arr[gorig[gb[gb<mydblen]]]
        outlier_mac_arr=outlier_mac_arr[gorigmac[gbmac[gmac2]]]
        outlier_arr=np.append(outlier_arr,outlier_mac_arr)
        gb=gb[(False==outlier_arr)&(magerr[gb]<0.15)]
        for j in range(0,len(gb)-1):
            gtmp=np.where((mjd[gb]-mjd[gb[j]]<timethresh)&(mjd[gb]-mjd[gb[j]]>=0))[0]
            if len(gtmp)>1:
                var_array,mjd_array=np.append(var_array,np.max(mag[gb[gtmp]])-np.min(mag[gb[gtmp]])),np.append(mjd_array,mjd[gb[j]])
        if len(var_array)>0: 
            maxvar[i]=np.max(var_array)
            medvar[i]=np.median(var_array)
            plt.figure(1)
            plt.clf()
            plt.scatter(mjd_array,var_array,color='r')
            plt.axhline(np.median(var_array),ls='dashed',color='k',lw=2)
            plt.xlabel('MJD (days)')
            plt.ylabel('Largest g variability within %i days'%timethresh)
            plt.title('%s (%s)'%(DBID,ydata['SDSS_NAME'][i]))
            plt.savefig(psfpage,format='pdf')
    else:
        #no maxvar
        pass
outcr=np.zeros((len(ydata),),dtype={'names':('SDSSNAME','maxvar'),'formats':('|S24','f8')})
outcr['SDSSNAME'],outcr['maxvar'],outcr['medvar']=ydata['SDSS_NAME'],maxvar,medvar
np.savetxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_%i.dat'%timethresh,outcr,fmt='%24s %6.3f %6.3f',header='SDSS_NAME MaxVar MedVar')
psfpage.close()
