import numpy as np
import healpy as hp
import easyaccess as ea
import time
import pandas as pd
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
try:
    calcmatchlist
except NameError:
    calcmatchlist=False


nsides=16384

tol=2./3600 
mdf=pd.read_csv('/home/rumbaugh/DR12Q_notinDR7_hpix.csv')

mddf=pd.read_csv('/home/rumbaugh/dr12_y3a1_match.csv')

matchlist=np.ones(len(mddf['RA']),dtype='bool')
matchlist[mddf['CID']<1]=False
mCIDs=np.unique(mddf['CID'][matchlist])
if calcmatchlist:
    for cid in mCIDs:
        g=np.where(cid==mddf['CID'])[0]
        if len(g)==1:
            matchlist[mddf['CID']==cid]=False
        elif len(g)>1:
            PYQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE COADD_OBJECT_ID=%i'%cid
            PDF=con.query_to_pandas(PYQ)
            tmpdist=calc_tmpdist(PDF['RA'][0],PDF["DEC"][0],mddf['RA'][g],mddf['DEC'][g])*60
            gas=np.argsort(tmpdist)
            matchlist[g][gas[0]]=False
        else:
            print 'Impossible!',cid
            break
    np.savetxt('/home/rumbaugh/matchlist_2.13.17.dat',matchlist,fmt='%i')
else:
    matchlist=np.loadtxt('/home/rumbaugh/matchlist_2.13.17.dat',dtype='bool')

#outcr=np.zeros((0,5),dtype='object')
outdf=pd.DataFrame()
HPlist=np.unique(mddf['HPIX'][matchlist])
outcr=np.zeros((len(mddf[matchlist==False]),5),dtype='object')
outcr[:,0],outcr[:,1],outcr[:,2],outcr[:,3],outcr[:,4]=mddf['SDSS_NAME'][matchlist==False],mddf['RA'][matchlist==False],mddf['DEC'][matchlist==False],mddf['HPIX'][matchlist==False],mddf['CID'][matchlist==False]
incr=mddf[matchlist]
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
    MDF=incr[incr['HPIX']==HP]
    YQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE HPIX_16384 in (%s)'%hps
    YDF=con.query_to_pandas(YQ)
    #gmHP,gyHP=np.where(mdf['HP']==HP)[0],np.in1d(cr['HP'],np.append(nearHPs,HP))
    ra_mtmp,dec_mtmp,ra_ytmp,dec_ytmp=MDF['RA'],MDF['DEC'],YDF['RA'],YDF['DEC']
    dftmp=MDF.copy()
    #crtmp=np.zeros((len(ra_mtmp),5),dtype='object')
    #crtmp[:,0],crtmp[:,1],crtmp[:,2],crtmp[:,3]=MDF['SDSS_NAME'],MDF['RA'],MDF['DEC'],MDF['HPIX']
    #nearinds=np.ones(len(ra_mtmp),dtype='i8')*-1
    cidstmp=np.zeros(len(ra_mtmp),dtype='i8')
    gk=np.in1d(YDF['COADD_OBJECT_ID'],mCIDs,invert=True)
    if np.max(gk)>0:
        ra_ytmp,dec_ytmp=YDF['RA'][gk],YDF['DEC'][gk]
        for i in range(0,len(ra_mtmp)):
            gn=np.where((np.abs(ra_mtmp[i]-ra_ytmp)*np.cos(dec_mtmp[i]*np.pi/180.)<tol)&(np.abs(dec_mtmp[i]-dec_ytmp)<tol))[0]
            if len(gn)>0:
                tmpdist=np.sqrt(((ra_mtmp[i]-ra_ytmp[gn])*np.cos(dec_mtmp[i]*np.pi/180.))**2+(dec_mtmp[i]-dec_ytmp[gn])**2)
                gd=np.where(tmpdist<tol)[0]
                if len(gd)>1:
                    #nearinds[i]=gn[np.argsort(tmpdist[gd])[0]]
                    dftmp[:,4][i]=YDF['COADD_OBJECT_ID'][gn[np.argsort(np.array(tmpdist[gd]))[0]]]
    outcr=np.concatenate((outcr,crtmp),axis=0)
endt=time.time()
lptime=endt-st
print 'loop done. Took %.2f seconds'%(endt-st)
np.savetxt('/home/rumbaugh/dr7_bh_y3a1_match_pass2.csv',outcr,fmt='%24s,%f,%f,%i,%i',header='SDSS_NAME,RA,DEC,HPIX,COADD_OJECTS_ID',comments='')
print 'file saved'
trend=time.time()
print 'Total time taken: %.2f seconds. Expected time for full run: %.0f seconds.'%(trend-trst,trend-trst+((len(mdf)-testruns)*lptime/testruns))
