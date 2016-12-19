import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'

#os.chdir(DB_path)
#os.system('ls -d *[0-9][0-9][0-9][0-9][0-9][0-9][0-9] > tmpls.dat')
#crls=np.loadtxt('tmpls.dat',dtype='i8')
#os.system('rm tmpls.dat')
crls=np.loadtxt('%s/crls.12.18.16.txt'%DB_path,dtype='i8')

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])

numrows=len(crls)

outcr=np.zeros((numrows,4),dtype='i8')

for iDB,DBID in zip(np.arange(0,numrows),crls):
    outputdir='/home/rumbaugh/var_database'
    db_cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    gDES,gSDSS,gPOS=np.where(db_cr['Survey']=='DES')[0],np.where(db_cr['Survey']=='SDSS')[0],np.where(db_cr['Survey']=='POSS')[0]
    if len(gDES)>0:
        try:
            cid=int(np.array(db_cr['SurveyCoaddID'])[gDES[0]])
        except:
            cid=int(np.array([db_cr['SurveyCoaddID']])[gDES[0]])
    else:
        cid=0
    if len(gSDSS)>0:
        try:
            tid=int(np.array(db_cr['SurveyCoaddID'])[gSDSS[0]])
        except:
            tid=int(np.array([db_cr['SurveyCoaddID']])[gSDSS[0]])
    else:
        tid=0
    dr7id=0
    if len(gPOSS)>0:
        dr7id=DBID-3000000
    outcr[iDB]=[DBID,cid,tid,dr7id]
np.savetxt('%s/database_index.dat'%outputdir,outcr,fmt='%i %i %i',header='DatabaseID Y1A1_COADD_OBJECTS_ID DR13_thingid')
