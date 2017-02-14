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
try:
    calcmatchlist
except NameError:
    calcmatchlist=False

def calc_tmpdist(ra1,dec1,ra2,dec2):
    return np.sqrt((ra1-ra2)**2+(dec1-dec2)**2)

nsides=16384

tol=2./3600 

crm=np.loadtxt('/home/rumbaugh/milliquas+healpix.txt',dtype={'names':('mID','ra','dec','HP'),'formats':('i8','f8','f8','i8')})

print 'loaded milliquas+healpix'

crmd=np.loadtxt('/home/rumbaugh/milliquas_y3a1_match.csv',dtype={'names':('MQ_ROWNUM','RA','DEC','HPIX','COADD_OBJECTS_ID'),'formats':('i8','f8','f8','i8','i8')},delimiter=',',skiprows=1)
#cr=np.loadtxt('/home/rumbaugh/y3a1_hpix.tab',dtype={'names':('cID','ra','dec','HP'),'formats':('f8','f8','f8','f8')},skiprows=1)
#cr['cID']=np.array(cr['cID'],dtype='i8')
#cr['HP']=np.array(cr['HP'],dtype='i8')

matchlist=np.ones(len(crmd['RA']),dtype='bool')
matchlist[crmd['COADD_OBJECTS_ID']<1]=False
mCIDs=np.unique(crmd['COADD_OBJECTS_ID'][matchlist])
#pstr='%i'%mCIDs[0]
#for cs in mCIDs[1:]: pstr='%s, %i'%(pstr,cs)
#PYQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE COADD_OBJECTS_ID in (%s)'%pstr
#PDF=con.query_to_pandas(PYQ)
#pcids,pras,pdecs=np.array(PDF['COADD_OBJECTS_ID']),np.array(PDF['RA']),np.array(PDF['DEC'])
if calcmatchlist:
    for cid in mCIDs:
        g=np.where(cid==crmd['COADD_OBJECTS_ID'])[0]
        if len(g)==1:
            matchlist[crmd['COADD_OBJECTS_ID']==cid]=False
        elif len(g)>1:
            PYQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE COADD_OBJECT_ID=%i'%cid
            PDF=con.query_to_pandas(PYQ)
            tmpdist=calc_tmpdist(PDF['RA'][0],PDF["DEC"][0],crmd['RA'][g],crmd['DEC'][g])*60
            gas=np.argsort(tmpdist)
            matchlist[g][gas[0]]=False
        else:
            print 'Impossible!',cid
            break
    np.savetxt('/home/rumbaugh/matchlist_1.28.17.dat',matchlist,fmt='%i')
else:
    matchlist=np.loadtxt('/home/rumbaugh/matchlist_1.28.17.dat',dtype='bool')
#matchinds=np.ones(len(cr),dtype='i8')*-1
HPlist=np.unique(crmd['HPIX'][matchlist])
gnom=np.in1d(np.array(crmd['COADD_OBJECTS_ID']),HPlist,invert=True)
outcr=np.zeros((len(crmd[matchlist==False]),5))
outcr[:,0],outcr[:,1],outcr[:,2],outcr[:,3],outcr[:,4]=crmd['MQ_ROWNUM'][matchlist==False],crmd['RA'][matchlist==False],crmd['DEC'][matchlist==False],crmd['HPIX'][matchlist==False],crmd['COADD_OBJECTS_ID'][matchlist==False]
incr=crmd[matchlist]
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
    if iHP%10000==1: 
        chktime=time.time()
        print '%.1f%% done. %.0f seconds elapsed. ETA: %.0f seconds'%(iHP*1000./len(HPlist),chktime-st,(len(HPlist)-iHP)*(chktime-st)/iHP) 
    nearHPs=hp.get_all_neighbours(nsides,HP,nest=True)
    hps='%i'%HP
    for h in nearHPs: hps='%s, %i'%(hps,h)
    MDF=incr[incr['HPIX']==HP]
    #gmHP,gyHP=np.where(crm['HP']==HP)[0],np.in1d(cr['HP'],np.append(nearHPs,HP))
    ra_mtmp,dec_mtmp=MDF['RA'],MDF['DEC']
    crtmp=np.zeros((len(ra_mtmp),5))
    crtmp[:,0],crtmp[:,1],crtmp[:,2],crtmp[:,3]=MDF['MQ_ROWNUM'],MDF['RA'],MDF['DEC'],MDF['HPIX']
    YQ='SELECT * FROM MCARRAS2.Y3A1_HPIX WHERE HPIX_16384 in (%s)'%hps
    YDF=con.query_to_pandas(YQ)
    gk=np.in1d(YDF['COADD_OBJECT_ID'],mCIDs,invert=True)
    if np.max(gk)>0:
        ra_ytmp,dec_ytmp=YDF['RA'][gk],YDF['DEC'][gk]
        #nearinds=np.ones(len(ra_mtmp),dtype='i8')*-1
        for i in range(0,len(ra_mtmp)):
            gn=np.where((np.abs(ra_mtmp[i]-ra_ytmp)*np.cos(dec_mtmp[i]*np.pi/180.)<tol)&(np.abs(dec_mtmp[i]-dec_ytmp)<tol))[0]
            if len(gn)>0:
                tmpdist=np.sqrt(((ra_mtmp[i]-ra_ytmp[gn])*np.cos(dec_mtmp[i]*np.pi/180.))**2+(dec_mtmp[i]-dec_ytmp[gn])**2)
                gd=np.where(tmpdist<tol)[0]
                if len(gd)>0:
                    #nearinds[i]=gn[np.argsort(tmpdist[gd])[0]]
                    crtmp[:,4][i]=YDF['COADD_OBJECT_ID'][gk][gn[np.argsort(np.array(tmpdist[gd]))[0]]]
    outcr=np.concatenate((outcr,crtmp),axis=0)
endt=time.time()
lptime=endt-st
print 'loop done. Took %.2f seconds'%(endt-st)
np.savetxt('/home/rumbaugh/milliquas_y3a1_match_pass2.csv',outcr,fmt='%i,%f,%f,%i,%i',header='MQ_ROWNUM,RA,DEC,HPIX,COADD_OBJECTS_ID',comments='')
print 'file saved'
trend=time.time()
print 'Total time taken: %.2f seconds. Expected time for full run: %.0f seconds.'%(trend-trst,trend-trst+((len(crm)-testruns)*lptime/testruns))
