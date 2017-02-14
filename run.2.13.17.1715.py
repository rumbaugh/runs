import numpy as np

cr=np.loadtxt('/home/rumbaugh/milliquas_Y3A1_tilenames.csv',dtype={'names':('MQ_ROWNUM','RA','DEC','TILENAME'),'formats':('i8','f8','f8','|S64')},skiprows=1,delimiter=',')


crm=np.loadtxt('/home/rumbaugh/milliquas_y3a1_match_pass2.csv',dtype={'names':('mID','ra','dec','HP','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1,delimiter=',')

cr=cr[np.argsort(cr[:,0])]
crm=crm[np.argsort(crm['mID'])]

outcr=np.zeros((len(cr),),dtype={'names':('mID','ra','dec','HP','cid','tilename'),'formats':('i8','f8','f8','i8','i8','|S32')})
outcr['mID'],outcr['ra'],outcr['dec'],outcr['HP'],outcr['cid'],outcr['tilename']=crm['mID'],crm['ra'],crm['dec'],crm['HP'],crm['cid'],cr['TILENAME']

np.savetxt('/home/rumbaugh/milliquas_y3a1_match_wtiles.csv',outcr,header=('MQ_ROWNUM,RA,DEC,HPIX,COADD_OBJECT_ID,TILENAME'),fmt='%i,%f,%f,%i,%i,%s',comments='')
