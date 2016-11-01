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

maxDBID=30295
outcr=np.zeros((maxDBID+1,15))
outcr[:,0]=np.arange(0,maxDBID+1)
for i in range(0,maxDBID+1):
    cr=np.loadtxt('/home/rumbaugh/var_database/%i/LC.tab'%i,dtype={'names':('DBID','Survey','CoaddID','ObjID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','Flag'),'formats':('i8','|S6','i8','i8','f8','f8','f8','|S12','|S4','|S8','f8','f8','i8')},skiprows=1)
    if np.shape(cr)!=():
        gDES,gSDSS=np.where(cr['Survey']=='DES')[0],np.where(cr['Survey']=='SDSS')[0]
        outcr[i][1]=cr['CoaddID'][gDES][0]
        for ib,band in zip(np.arange(len(bands)),bands):
            gb=np.where(cr['BAND'][gDES]==band)[0]
            if len(gb)>0:
                outcr[i][3+ib]=np.median(cr['MAG'][gDES][gb])
        if len(gSDSS)>0: 
            outcr[i][2]=cr['CoaddID'][gSDSS][0]
            for ib,band in zip(np.arange(len(bands)),bands):
                gb=np.where(cr['BAND'][gSDSS]==band)[0]
                if len(gb)>0:
                    outcr[i][7+ib]=np.median(cr['MAG'][gSDSS][gb])
                    if outcr[i][3+ib]!=0:
                        outcr[11+ib]=outcr[i][3+ib]-outcr[i][7+ib]
newoutcr=outcr[np.argsort(np.max(np.abs(outcr[:,:-4]),axis=1))[::-1]]
np.savetxt('/home/rumbaugh/var_database/mag_changes.SDSS-DESS.dat',newoutcr,fmt='%5i %15i %15i %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f',header='DBID COADD_OBJECTS_ID THINGID DES_g DES_r DES_i DES_z SDSS_g SDSS_r SDSS_i SDSS_z MAGDIFF_g MAGDIFF_r MAGDIFF_i MAGDIFF_z',comments='')
    
