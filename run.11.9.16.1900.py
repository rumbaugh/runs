import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])

numrows=30296

outcr=np.zeros((numrows,3))

for DBID in np.arange(0,numrows):
    outputdir='/home/rumbaugh/var_database'
    db_cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    gDES,gSDSS=np.where(db_cr['Survey']=='DES')[0],np.where(db_cr['Survey']=='SDSS')[0]
    if len(gDES)>0:
        cid=int(np.array([db_cr['SurveyCoaddID']])[gDES[0]])
    else:
        cid=0
    if len(gSDSS)>0:
        tid=int(np.array([db_cr['SurveyCoaddID']])[gSDSS[0]])
    else:
        tid=0
    outcr[DBID]=[DBID,cid,tid]
np.savetxt('%s/database_index.dat'%outputdir,outcr,fmt='%i %i %i',header='DatabaseID Y1A1_COADD_OBJECTS_ID DR13_thingid')
