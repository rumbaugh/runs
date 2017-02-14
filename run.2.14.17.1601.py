import numpy as np

cr=np.loadtxt('/home/rumbaugh/SDSSPOSS_Y3A1_tilenames.csv',dtype={'names':('SP_ROWNUM','RA','DEC','TILENAME'),'formats':('i8','f8','f8','|S64')},skiprows=1,delimiter=',')


crm=np.loadtxt('/home/rumbaugh/sdssposs_y3a1_match.csv',dtype={'names':('spID','ra','dec','HP','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1,delimiter=',')

cr=cr[np.argsort(cr['SP_ROWNUM'])]
crm=crm[np.argsort(crm['spID'])]

outcr=np.zeros((len(cr),),dtype={'names':('spID','ra','dec','HP','cid','tilename'),'formats':('i8','f8','f8','i8','i8','|S32')})
outcr['spID'],outcr['ra'],outcr['dec'],outcr['HP'],outcr['cid'],outcr['tilename']=crm['spID'],crm['ra'],crm['dec'],crm['HP'],crm['cid'],cr['TILENAME']

np.savetxt('/home/rumbaugh/sdssposs_y3a1_match_wtiles.csv',outcr,header=('SP_ROWNUM,RA,DEC,HPIX,COADD_OBJECT_ID,TILENAME'),fmt='%i,%f,%f,%i,%i,%s',comments='')

 
cr=np.loadtxt('/home/rumbaugh/DR7_BH_Y3A1_tilenames.csv',dtype={'names':('SDSS_NAME','RA','DEC','TILENAME'),'formats':('|S32','f8','f8','|S64')},skiprows=1,delimiter=',')


crm=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match.csv',dtype={'names':('spID','ra','dec','HP','cid'),'formats':('|S32','f8','f8','i8','i8')},skiprows=1,delimiter=',')

cr=cr[np.argsort(cr['SDSS_NAME'])]
crm=crm[np.argsort(crm['spID'])]

outcr=np.zeros((len(cr),),dtype={'names':('spID','ra','dec','HP','cid','tilename'),'formats':('|S32','f8','f8','i8','i8','|S32')})
outcr['spID'],outcr['ra'],outcr['dec'],outcr['HP'],outcr['cid'],outcr['tilename']=crm['spID'],crm['ra'],crm['dec'],crm['HP'],crm['cid'],cr['TILENAME']

np.savetxt('/home/rumbaugh/dr7_bh_y3a1_match_wtiles.csv',outcr,header=('SDSS_NAME,RA,DEC,HPIX,COADD_OBJECT_ID,TILENAME'),fmt='%s,%f,%f,%i,%i,%s',comments='')
