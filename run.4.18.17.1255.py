import numpy as np
crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
crmi=crmi[(crmi['SDSS_NAME']!='-1')&(crmi['COADD_OBJECTS_ID']==0)&(crmi['TILENAME']!='None')]


outcr=np.zeros((len(crmi),),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','|S64')})
outcr_radec=np.zeros((len(crmi),2))
outcr['RA'],outcr['DEC'],outcr['Name']=crmi['RA'],crmi['DEC'],crmi['SDSS_NAME']
outcr_radec[:,0],outcr_radec[:,1]=crmi['RA'],crmi['DEC']
np.savetxt('/home/rumbaugh/radecname_forDEScutouts.4.18.17.csv',outcr,fmt='%f,%f,%s_DEScutout')
np.savetxt('/home/rumbaugh/radec_forDEScutouts.4.18.17.csv',outcr_radec,fmt='%f,%f')

FILE=open('/home/rumbaugh/runs/run.4.18.17.1255.sql','w')
win=.2/60
for i in range(0,len(outcr)):
    FILE.write('SELECT RA,DEC,COADD_OBJECT_ID FROM Y3A1_COADD_OBJECT_SUMMARY where RA>%.6f AND RA<%.6f AND DEC> %.6f AND DEC<%.6f;\n'%(outcr['RA'][i]-win,outcr['RA'][i]+win,outcr['DEC'][i]-win,outcr['DEC'][i]+win))
FILE.close()
