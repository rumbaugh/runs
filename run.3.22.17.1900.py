import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
psfpage=bpdf.PdfPages('/home/rumbaugh/DR7_Macleod_comp.g_closeup_cuttest.3.22.17.pdf')
DBdir='/home/rumbaugh/var_database/Y3A1'
crmcm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_Macleod_S82_match.dat',dtype={'names':('DBID','MCID'),'formats':('|S24','i8')},skiprows=1)


crmcm=crmcm[crmcm['MCID']>-1]
matplotlib.rcParams['figure.figsize']=[20,7]


crmd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','flag'),'formats':('|S32','f8','|S8','|S8','i8','i8')},skiprows=1)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

for i in range(0,len(crmd)):
    DBID=crmd['DBID'][i]
    gdb=np.where(DBID==crdb['DBID'])[0][0]
    if ((DBID[:2]!='SP')&(crdb['SPrownum'][gdb]>-1)):
        crmd['DBID'][i]='SDSSPOSS%i'%crdb['SPrownum'][gdb]
    if ((DBID[:2]!='MQ')&(crdb['MQrownum'][gdb]>-1)):
        crmd['DBID'][i]='MQ%i'%crdb['MQrownum'][gdb]

ggd=np.zeros(len(crmcm),dtype='bool')
for i in range(0,len(ggd)): 

    if crmcm['DBID'][i] in crmd['DBID']: ggd[i]=True
crmcm=crmcm[ggd]

for DBID,MCID in zip(crmcm['DBID'],crmcm['MCID']):
    plt.figure(1)
    plt.clf()
    cr=np.loadtxt('%s/%s/LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
    crmac=crmac[(crmac['MAG']>0)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
    cr=cr[(cr['MAG']>0)&(cr['MAG']<30)&(cr['MAGERR']<5)]

    gb,gbmac=np.where((cr['BAND']=='g')&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0],np.where(crmac['BAND']=='g')[0]
    if ((len(gb)>0)&(len(gbmac)>0)):
        mjd,mjdmac=cr['MJD'][gb],crmac['MJD'][gbmac]
        mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd.reshape((1,len(mjd)))*np.ones((len(mjdmac),1)))
        mindists=np.min(mjddists,axis=1)
        gmac2=np.where(mindists<1)[0]
    else:
        gmac2=np.arange(len(gmac2))
    plt.errorbar(cr['MJD'][gb],cr['MAG'][gb],yerr=cr['MAGERR'][gb],fmt='o',color='r')
    plt.errorbar(crmac['MJD'][gbmac[gmac2]],crmac['MAG'][gbmac[gmac2]],yerr=crmac['MAGERR'][gbmac[gmac2]],fmt='d',color='g')
    ylim=plt.ylim()
    plt.ylim(ylim[1],ylim[0])
    plt.xlabel('MJD')
    plt.ylabel('Mag.')
    plt.title(DBID)
    plt.savefig(psfpage,format='pdf')
psfpage.close()
