import numpy as np

crc=np.loadtxt('/home/rumbaugh/radecname_forDEScutouts.2.16.17.csv',dtype={'names':('ra','dec','name'),'formats':('f8','f8','|S64')},delimiter=',')
crdt=np.loadtxt('/home/rumbaugh/var_database/Y3A1/imagestamps/matched_161c13c4-300f-4dc3-801e-682a0b7cc4db.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})

DBID=crc['name']
for i in np.arange(len(DBID)):
    strtmp=DBID[i].split('_')
    DBID[i]=strtmp[0]
outcr=np.zeros((len(crc),),dtype={'names':('DBID','ra','dec','tile','fname'),'formats':('|S32','f8','f8','|S12','|S25')})
outcr['DBID'],outcr['ra'],outcr['dec'],outcr['tile'],outcr['fname']=DBID,crdt['ra'],crdt['dec'],crdt['tile'],crdt['fname']
np.savetxt('/home/rumbaugh/var_database/Y3A1/imagestamps/DESimagestamp_index.dat',outcr,header='DatabaseID RA DEC TILE FILENAME',fmt='%s %f %f %s %s')
