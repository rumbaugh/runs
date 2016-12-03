import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/milliquas_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'psfmag_%s'%b for b in SDSSbands}
bands = np.array(['g','r','i','z'])
POSSbands = np.array(['g','r','i'])

maxDBID=87846
outcr=np.zeros((maxDBID+1,17))
outcr[:,0]=np.arange(0,maxDBID+1)
totdiffs=np.zeros(0)
for i in range(0,maxDBID+1):
    cr=np.loadtxt('/home/rumbaugh/var_database/%i/LC.tab'%i,dtype={'names':('DBID','Survey','CoaddID','ObjID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','Flag'),'formats':('i8','|S6','i8','i8','f8','f8','f8','|S12','|S4','|S8','f8','f8','i8')},skiprows=1)
    try:
        ggoodmag=np.where((cr['MAG']>0)&(cr['MAG']<31))[0]
        cr=cr[ggoodmag]
    except:
        pass
    if ((np.shape(cr)!=())&(np.shape(cr)!=(0,))):
        goodbands=np.zeros(0,dtype='|S2')
        for ib,band in zip(np.arange(len(bands)),bands):
            gb=np.where((cr['BAND']==band)&(np.isnan(cr['MAG'])==False))[0]
            if len(gb)>0: goodbands=np.append(goodbands,band)
        totmagdict={b: np.zeros(0) for b in bands}
        gDES,gSDSS,gPOSS=np.where(cr['Survey']=='DES')[0],np.where(cr['Survey']=='SDSS')[0],np.where(cr['Survey']=='POSS')[0]
        if len(gDES)>0:
            outcr[i][1]=cr['CoaddID'][gDES][0]
            for ib,band in zip(np.arange(len(bands)),bands):
                gb=np.where((cr['BAND'][gDES]==band)&(np.isnan(cr['MAG'][gDES])==False))[0]
                if len(gb)>0:
                    totmagdict[band]=np.append(totmagdict[band],cr['MAG'][gDES][gb])
                    outcr[i][3+ib]=np.median(cr['MAG'][gDES][gb])
        if len(gPOSS)>0:
            mjdstmp=np.zeros(0)
            POSSmagdict,POSSmjddict={b: np.zeros(0) for b in POSSbands},{b: np.zeros(0) for b in POSSbands}
            for band in POSSbands:
                gb=np.where((cr['BAND'][gPOSS]==band)&(np.isnan(cr['MAG'][gPOSS])==False))[0]
                POSSmagdict[band]=np.append(POSSmagdict[band],cr['MAG'][gPOSS][gb])
                mjdstmp=np.append(mjdstmp,cr['MJD'][gPOSS][gb])
            allmjds=np.sort(np.unique(mjdstmp))
            for band in POSSbands:
                if len(POSSmagdict[band])>0:POSSmagdict[band]=np.array([np.median(POSSmagdict[band])])
            if (len(POSSmagdict['g'])>0)&(len(POSSmagdict['r'])>0):
                POSSmagdict['g'],POSSmagdict['r']=POSSmagdict['g']+0.392*(POSSmagdict['g']-POSSmagdict['r'])-0.28,  POSSmagdict['r']+0.127*(POSSmagdict['g']-POSSmagdict['r'])+0.1
            else: 
                POSSmagdict['g'],POSSmagdict['r']=np.zeros(0),np.zeros(0)
            if (len(POSSmagdict['i'])>0)&(len(POSSmagdict['r'])>0):   
                POSSmagdict['i']=POSSmagdict['i']+0.27*(POSSmagdict['r']-POSSmagdict['i'])+0.32
            else:
                POSSmagdict['i']=np.zeros(0)
            for band in POSSbands: totmagdict[band]=np.append(totmagdict[band],POSSmagdict[band])
        if len(gSDSS)>0: 
            raDES,decDES,mjdDES,raSDSS,decSDSS,mjdSDSS=cr['RA'][gDES],cr['DEC'][gDES],cr['MJD'][gDES],cr['RA'][gSDSS],cr['DEC'][gSDSS],cr['MJD'][gSDSS]
            raDES,decDES,raSDSS,decSDSS=raDES[np.argsort(mjdDES)],decDES[np.argsort(mjdDES)],raSDSS[np.argsort(mjdSDSS)],decSDSS[np.argsort(mjdSDSS)]
            raDEScen,decDEScen=np.mean(raDES),np.mean(decDES)
            raSDSScen,decSDSScen=np.mean(raSDSS),np.mean(decSDSS)
            outcr[i][2]=cr['CoaddID'][gSDSS][0]
            outcr[i][-2]=np.sqrt(((raDEScen-raSDSScen)*np.cos(decDEScen*np.pi/180))**2+(decDEScen-decSDSScen)**2)*3600
            for ib,band in zip(np.arange(len(bands)),bands):
                gb=np.where(cr['BAND'][gSDSS]==band)[0]
                if len(gb)>0:
                    totmagdict[band]=np.append(totmagdict[band],cr['MAG'][gSDSS][gb])
                    outcr[i][7+ib]=np.median(cr['MAG'][gSDSS][gb])
                    if outcr[i][3+ib]!=0:
                        outcr[i][11+ib]=outcr[i][3+ib]-outcr[i][7+ib]
        totdiffdict={b: np.max(totmagdict[b])-np.min(totmagdict[b]) for b in goodbands}
        totdiffarr=[np.max(totmagdict[b])-np.min(totmagdict[b]) for b in goodbands]
        totdiffs=np.append(totdiffs,np.max([totdiffarr]))
maxes=np.max(np.abs(outcr[:,-6:-2]),axis=1)
newoutcr=outcr[np.argsort(np.max(np.abs(outcr[:,-6:-2]),axis=1))[::-1]]
newoutcr=newoutcr[(np.max(newoutcr[:,-6:-2],axis=1)<30)&(newoutcr[:,-2]<1)]
np.savetxt('/home/rumbaugh/var_database/mag_changes.POSS+SDSS+DES.dat',newoutcr,fmt='%5i %15i %15i %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %5.3f %2i',header='DBID COADD_OBJECTS_ID THINGID DES_g DES_r DES_i DES_z SDSS_g SDSS_r SDSS_i SDSS_z MAGDIFF_g MAGDIFF_r MAGDIFF_i MAGDIFF_z DISTANCE INTERESTING_FLAG',comments='')
    
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist(totdiffs,range=(0,6),bins=12)
plt.xlabel('Max Difference')
plt.ylabel('Number of objects')
plt.savefig('/home/rumbaugh/var_database/plots/max_diffs.hist.png')
