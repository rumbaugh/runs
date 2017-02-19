import numpy as np
import os
DB_path='/home/rumbaugh/var_database/Y3A1'

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

gdb=np.where((crdb['MQrownum']!=-1)&(crdb['SDSSNAME']!='-1'))[0]
gdb=gdb[:4]

tarlist=np.zeros(len(gdb),dtype='str')
for DBID,idb in zip(cr['DatabaseID'][gdb],np.arange(len(gdb))):
    os.system('cp -r %s/%s %s/../bkup_2.19.17/.'%(DB_path,DBID,DB_path))
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    g=np.where(cr['Survey']!='DES')[0]
    maxid=np.max(g)
    cr=cr[:maxid+1]
    np.savetxt('%s/%s/LC.tab'%(DB_path,DBID),cr,fmt=('%20s %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')
    tarlist[idb]='Y3A1/%s/LC.tab'%DBID
np.savetxt('/home/rumbaugh/var_database/tarlist.2.19.17.txt',tarlist,fmt='%s')
    
