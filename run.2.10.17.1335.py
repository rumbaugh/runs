import numpy as np
import healpy as hp
import easyaccess as ea
import time
trst=time.time()
con=ea.connect()
try:
    istest
except NameError:
    istest=False
try:
    testruns
except NameError:
    testruns=10
try:
    testID
except NameError:
    testID=None

nsides=16384

tol=2./3600 

crm=np.loadtxt('/home/rumbaugh/dr7_bh_hpix.tab',dtype={'names':('SDSSname','ra','dec','HP'),'formats':('|S24','f8','f8','i8')},skiprows=1)

outcr=np.zeros((0,5),dtype='object')
HPlist=np.unique(crm['HP'])
if istest:
    if testID:
        nearHPs=hp.get_all_neighbours(nsides,testID,nest=True)
        HPlist=np.append(nearHPs,testID)
    else:
        HPlist=HPlist[:testruns]
print 'starting loop'
st=time.time()
for iHP,HP in zip(np.arange(len(HPlist)),HPlist):
    if iHP%1000==1: 
        chktime=time.time()
        print '%.1f%% done. %.0f seconds elapsed. ETA: %.0f seconds'%(iHP*100./len(HPlist),chktime-st,(len(HPlist)-iHP)*(chktime-st)/iHP) 
    nearHPs=hp.get_all_neighbours(nsides,HP,nest=True)
    hps='%i'%HP
    for h in nearHPs: hps='%s, %i'%(hps,h)
    YQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE HPIX_16384 in (%s)'%hps
    BH='SELECT * FROM RUMBAUGH.DR7_BH_HPIX WHERE HPIX=%i'%HP
    YDF=con.query_to_pandas(YQ)
    MDF=con.query_to_pandas(BH)
    #gmHP,gyHP=np.where(crm['HP']==HP)[0],np.in1d(cr['HP'],np.append(nearHPs,HP))
    ra_mtmp,dec_mtmp,ra_ytmp,dec_ytmp=MDF['RA'],MDF['DEC'],YDF['RA'],YDF['DEC']
    crtmp=np.zeros((len(ra_mtmp),5))
    crtmp[:,0],crtmp[:,1],crtmp[:,2],crtmp[:,3]=MDF['SDSS_NAME'],MDF['RA'],MDF['DEC'],MDF['HPIX']
    #nearinds=np.ones(len(ra_mtmp),dtype='i8')*-1
    for i in range(0,len(ra_mtmp)):
        gn=np.where((np.abs(ra_mtmp[i]-ra_ytmp)*np.cos(dec_mtmp[i]*np.pi/180.)<tol)&(np.abs(dec_mtmp[i]-dec_ytmp)<tol))[0]
        if len(gn)>0:
            tmpdist=np.sqrt(((ra_mtmp[i]-ra_ytmp[gn])*np.cos(dec_mtmp[i]*np.pi/180.))**2+(dec_mtmp[i]-dec_ytmp[gn])**2)
            gd=np.where(tmpdist<tol)[0]
            if len(gd)>1:
                #nearinds[i]=gn[np.argsort(tmpdist[gd])[0]]
                crtmp[:,4][i]=YDF['COADD_OBJECT_ID'][gn[np.argsort(np.array(tmpdist[gd]))[0]]]
            elif len(gd)==1:
                crtmp[:,4][i]=YDF['COADD_OBJECT_ID'][gn[gd[0]]]
    outcr=np.concatenate((outcr,crtmp),axis=0)
endt=time.time()
lptime=endt-st
print 'loop done. Took %.2f seconds'%(endt-st)
np.savetxt('/home/rumbaugh/dr7_bh_y3a1_match.csv',outcr,fmt='%24s,%f,%f,%i,%i',header='SDSS_NAME,RA,DEC,HPIX,COADD_OJECTS_ID',comments='')
print 'file saved'
trend=time.time()
print 'Total time taken: %.2f seconds. Expected time for full run: %.0f seconds.'%(trend-trst,trend-trst+((len(crm)-testruns)*lptime/testruns))
