import numpy as np

crc=np.loadtxt('/home/rumbaugh/radecname_forDEScutouts.4.20.17.csv',dtype={'names':('ra','dec','name'),'formats':('f8','f8','|S64')},delimiter=',')
crdt=np.loadtxt('/home/rumbaugh/var_database/Y3A1/imagestamps/matched_37042c82-426f-888f-d77e3181f49b.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})

DBID=crc['name']
for i in np.arange(len(DBID)):
    strtmp=DBID[i].split('_')
    DBID[i]=strtmp[0]
outcr=np.zeros((len(crc),),dtype={'names':('DBID','ra','dec','tile','fname'),'formats':('|S32','f8','f8','|S12','|S25')})
outcr['DBID'],outcr['ra'],outcr['dec'],outcr['tile'],outcr['fname']=DBID,crdt['ra'],crdt['dec'],crdt['tile'],crdt['fname']
np.savetxt('/home/rumbaugh/var_database/Y3A1/imagestamps/DR7_DESimagestamp_index.4.20.17.dat',outcr,header='DatabaseID RA DEC TILE FILENAME',fmt='%s %f %f %s %s')
np.savetxt('/home/rumbaugh/var_database/Y3A1/imagestamps/DESimagestamp_index.dat',outcr,header='DatabaseID RA DEC TILE FILENAME',fmt='%s %f %f %s %s')
