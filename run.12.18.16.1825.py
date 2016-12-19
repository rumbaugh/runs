import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
import itertools as it
DB_path='/home/rumbaugh/var_database'
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'psfmag_%s'%b for b in SDSSbands}
bands = np.array(['g','r','i','z'])
POSSbands = np.array(['g','r','i'])

crdb=np.loadtxt('%s/database_index.dat'%DB_path,dtype='i8')
#maxDBID=87846
maxDBID=np.shape(crdb)[0]
outcr=np.zeros((maxDBID,17))
#outcr[:,0]=np.arange(0,maxDBID+1)
outcr[:,0]=crdb[:,0]
totdiffs=np.zeros(0)
totDBIDs=np.zeros(0,dtype='i8')
for i,DBID in zip(np.arange(0,maxDBID),crdb[:,0]):
    cr=np.loadtxt('/home/rumbaugh/var_database/%i/LC.tab'%DBID,dtype={'names':('DBID','Survey','CoaddID','ObjID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','Flag'),'formats':('i8','|S6','i8','i8','f8','f8','f8','|S12','|S4','|S8','f8','f8','i8')},skiprows=1)
    try:
        ggoodmag=np.where((cr['MAG']>0)&(cr['MAG']<31)&(cr['MAGERR']<0.5))[0]
        cr=cr[ggoodmag]
    except:
        pass
    if ((np.shape(cr)!=())&(np.shape(cr)!=(0,))):
        goodbands=np.zeros(0,dtype='|S2')
        for ib,band in zip(np.arange(len(bands)),bands):
            gb=np.where((cr['BAND']==band)&(np.isnan(cr['MAG'])==False))[0]
            if len(gb)>0: goodbands=np.append(goodbands,band)
        totmagdict={b: np.zeros(0) for b in bands}
        totmagerrdict={b: np.zeros(0) for b in bands}
        gDES,gSDSS,gPOSS=np.where(cr['Survey']=='DES')[0],np.where(cr['Survey']=='SDSS')[0],np.where(cr['Survey']=='POSS')[0]
        if len(gDES)>0:
            outcr[i][1]=cr['CoaddID'][gDES][0]
            for ib,band in zip(np.arange(len(bands)),bands):
                gb=np.where((cr['BAND'][gDES]==band)&(np.isnan(cr['MAG'][gDES])==False))[0]
                if len(gb)>0:
                    totmagdict[band]=np.append(totmagdict[band],cr['MAG'][gDES][gb])
                    totmagerrdict[band]=np.append(totmagdict[band],cr['MAGERR'][gDES][gb])
                    outcr[i][3+ib]=np.median(cr['MAG'][gDES][gb])
        if len(gPOSS)>0:
            mjdstmp=np.zeros(0)
            POSSmagdict,POSSmagerrdict,POSSmjddict={b: np.zeros(0) for b in POSSbands},{b: np.zeros(0) for b in POSSbands},{b: np.zeros(0) for b in POSSbands}
            for band in POSSbands:
                gb=np.where((cr['BAND'][gPOSS]==band)&(np.isnan(cr['MAG'][gPOSS])==False))[0]
                POSSmagdict[band]=np.append(POSSmagdict[band],cr['MAG'][gPOSS][gb])
                POSSerrmagdict[band]=np.append(POSSmagdict[band],cr['MAGERR'][gPOSS][gb])
                mjdstmp=np.append(mjdstmp,cr['MJD'][gPOSS][gb])
            allmjds=np.sort(np.unique(mjdstmp))
            for band in POSSbands:
                if len(POSSmagdict[band])>0:POSSmagdict[band]=np.array([np.median(POSSmagdict[band])])
            if (len(POSSmagdict['g'])>0)&(len(POSSmagdict['r'])>0):
                POSSmagdict['g'],POSSmagdict['r']=POSSmagdict['g']+0.392*(POSSmagdict['g']-POSSmagdict['r'])-0.28,  POSSmagdict['r']+0.127*(POSSmagdict['g']-POSSmagdict['r'])+0.1
                POSSmagerrdict['g'],POSSmagerrdict['r']=np.sqrt(1.392**2*POSSmagerrdict['g']**2+0.392**2*POSSmagerrdict['r']**2),  np.sqrt(POSSmagerrdict['r']**2+0.127**2*(POSSmagerrdict['g']**2+POSSmagerrdict['r']**2))
            else: 
                POSSmagdict['g'],POSSmagdict['r']=np.zeros(0),np.zeros(0)
            if (len(POSSmagdict['i'])>0)&(len(POSSmagdict['r'])>0):   
                POSSmagdict['i']=POSSmagdict['i']+0.27*(POSSmagdict['r']-POSSmagdict['i'])+0.32
                POSSmagerrdict['i']=np.sqrt(POSSmagerrdict['i']**2+0.27**2*(POSSmagerrdict['r']**2+POSSmagerrdict['i']**2))
            else:
                POSSmagdict['i']=np.zeros(0)
            for band in POSSbands: 
                totmagdict[band]=np.append(totmagdict[band],POSSmagdict[band])
                totmagerrdict[band]=np.append(totmagerrdict[band],POSSmagerrdict[band])
        if len(gSDSS)>0: 
            raDES,decDES,mjdDES,raSDSS,decSDSS,mjdSDSS=cr['RA'][gDES],cr['DEC'][gDES],cr['MJD'][gDES],cr['RA'][gSDSS],cr['DEC'][gSDSS],cr['MJD'][gSDSS]
            raDES,decDES,raSDSS,decSDSS=raDES[np.argsort(mjdDES)],decDES[np.argsort(mjdDES)],raSDSS[np.argsort(mjdSDSS)],decSDSS[np.argsort(mjdSDSS)]
            raDEScen,decDEScen=np.mean(raDES),np.mean(decDES)
            raSDSScen,decSDSScen=np.mean(raSDSS),np.mean(decSDSS)
            outcr[i][2]=cr['CoaddID'][gSDSS][0]
            outcr[i][-2]=np.sqrt(((raDEScen-raSDSScen)*np.cos(decDEScen*np.pi/180))**2+(decDEScen-decSDSScen)**2)*3600
            distflag=True
            if len(gDES)>0:
                if np.sqrt(((raDEScen-raSDSScen)*np.cos(decDEScen*np.pi/180))**2+(decDEScen-decSDSScen)**2)*3600>0.6: distflag=False
            for ib,band in zip(np.arange(len(bands)),bands):
                gb=np.where(cr['BAND'][gSDSS]==band)[0]
                if len(gb)>0:
                    if distflag: 
                        totmagdict[band]=np.append(totmagdict[band],cr['MAG'][gSDSS][gb])
                        totmagerrdict[band]=np.append(totmagerrdict[band],cr['MAGERR'][gSDSS][gb])
                    outcr[i][7+ib]=np.median(cr['MAG'][gSDSS][gb])
                    if outcr[i][3+ib]!=0:
                        outcr[i][11+ib]=outcr[i][3+ib]-outcr[i][7+ib]
        stillgoodbands=np.zeros(0)
        for b in goodbands: 
            if len(totmagdict[b])>0: stillgoodbands=np.append(stillgoodbands,b)
        #totdiffdict={b: np.max(totmagdict[b])-np.min(totmagdict[b]) for b in stillgoodbands}
        totdiffar=[]
        for b in stillgoodbands:
            combis=np.array(list(it.combinations(np.arange(len(totmagdict[b])),2)))
            i1,i2=combis[:,0],combis[:,1]
            sigma=np.abs((totmagdict[b][i1]-totmagdict[b][i2])/np.sqrt(totmagerrdict[b][i1]**2+totmagerrdict[b][i2]**2))
            totdiffs=np.abs(totmagdict[b][i1]-totmagdict[b][i2])
            ggooddiff=np.where((sigma>=3)&(totmagdict[b][i1]>1)&(totmagdict[b][i1]<30)&(totmagdict[b][i2]>1)&(totmagdict[b][i2]<30))[0]
            bestdiff=0
            if len(ggooddiff)>0:
                totdiffarr=np.append(totdiffarr,np.max(totdiffs[ggooddiff]))
        #totdiffarr=[np.max(totmagdict[b])-np.min(totmagdict[b]) for b in stillgoodbands]
        if len(totdiffarr)>0:
            totdiffs=np.append(totdiffs,np.max([totdiffarr]))
            totDBIDs=np.append(totDBIDs,DBID)

tcr=np.zeros((len(totdiffs),2))#,dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})
#tcr['DBID'],tcr['maxdiff']=totDBIDs,totdiffs
tcr[:,0],tcr[:,1]=totDBIDs,totdiffs
np.savetxt('/home/rumbaugh/var_database/maxdiffs_sig_DBID.12.18.16.txt',tcr,fmt='%7i %f',header='DatabasedID  Max_Mag_Difference')

print np.shape(crdb)[0],len(totdiffs),len(totdiffs[totdiffs>2])*1./len(totdiffs)
