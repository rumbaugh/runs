import numpy as np
import healpy as hp
import easyaccess as ea
import time
trst=time.time()
con=ea.connect()
try:
    istest
except NameError:
    istest=True
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

crm=np.loadtxt('/home/rumbaugh/milliquas+healpix.txt',dtype={'names':('mID','ra','dec','HP'),'formats':('i8','f8','f8','i8')})

print 'loaded milliquas+healpix'
#cr=np.loadtxt('/home/rumbaugh/y3a1_hpix.tab',dtype={'names':('cID','ra','dec','HP'),'formats':('f8','f8','f8','f8')},skiprows=1)
#cr['cID']=np.array(cr['cID'],dtype='i8')
#cr['HP']=np.array(cr['HP'],dtype='i8')

#matchinds=np.ones(len(cr),dtype='i8')*-1
outcr=np.zeros((0,5))
HPlist=np.unique(crm['HP'])
HPlist=HPlist[:100]
#newst=746954
#HPlist=HPlist[newst:]
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
    hps='%i, %s'%(HP,', '.join(np.array(nearHPs,dtype='|S30')))
    #for h in nearHPs: hps='%s, %i'%(hps,h)
    YQ='SELECT COADD_OBJECT_ID FROM DES_ADMIN.Y3A1_COADD_OBJECT_HPIX WHERE HPIX_16384 in (%s)'%hps
    YDF=con.query_to_pandas(YQ)
    MQ='SELECT * FROM RUMBAUGH.MILLIQUAS_HPIX WHERE HPIX=%i'%HP
    MDF=con.query_to_pandas(MQ)
    #gmHP,gyHP=np.where(crm['HP']==HP)[0],np.in1d(cr['HP'],np.append(nearHPs,HP))
    ra_mtmp,dec_mtmp=MDF['RA'],MDF['DEC']
    ra_ytmp,dec_ytmp=ra_mtmp+np.random.normal(np.mean(ra_mtmp),np.std(ra_mtmp),len(YDF)),dec_mtmp+np.random.normal(np.mean(dec_mtmp),np.std(dec_mtmp),len(YDF))
    crtmp=np.zeros((len(ra_mtmp),5))
    crtmp[:,0],crtmp[:,1],crtmp[:,2],crtmp[:,3]=MDF['MQ_ROWNUM'],MDF['RA'],MDF['DEC'],MDF['HPIX']
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
np.savetxt('/home/rumbaugh/test_milliquas_y3a1_match.csv',outcr,fmt='%i,%f,%f,%i,%i',header='MQ_ROWNUM,RA,DEC,HPIX,COADD_OBJECTS_ID',comments='')
print 'file saved'
trend=time.time()
print 'Total time taken: %.2f seconds. Expected time for full run: %.0f seconds.'%(trend-trst,trend-trst+((len(crm)-testruns)*lptime/testruns))
