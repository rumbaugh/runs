import numpy as np
import healpy as hp
try:
    istest
except NameError:
    istest=True

nsides=16384

tol=5./3600

crm=np.loadtxt('/home/rumbaugh/milliquas+healpix.txt',dtype={'names':('ra','dec','HP'),'formats':('f8','f8','i8')})


cr=np.loadtxt('/home/rumbaugh/y1a1_hpix.tab',dtype={'names':('cID','ra','dec','HP'),'formats':('i8','f8','f8','i8')},skiprows=1)

matchinds=np.ones(len(cr),dtype='i8')*-1
HPlist=np.unique(crm['HP'])
if istest: HPlist=HPlist[:3]
for HP in HPlist:
    nearHPs=hp.get_all_neighbours(nsides,HP,nest=True)
    gmHP,gyHP=np.where(crm['HP']==HP)[0],np.in1d(cr['HP'],np.append(nearHPs,HP))
    ra_mtmp,dec_mtmp,ra_ytmp,dec_ytmp=crm['ra'][gmHP],crm['dec'][gmHP],cr['ra'][gyHP],cr['dec'][gyHP]
    nearinds=np.ones(len(gmHP),dtype='i8')*-1
    for i in range(0,len(gmHP)):
        gn=np.where((np.abs(ra_mtmp[i]-ra_ytmp)*np.cos(dec_mtmp[i]*np.pi/180.)<5./3600)&(np.abs(dec_mtmp[i]-dec_ytmp)<5./3600))[0]
        if len(gn)>0:
            tmpdist=np.sqrt(((ra_mtmp[i]-ra_ytmp[gn])*np.cos(dec_mtmp[i]*np.pi/180.))**2+(dec_mtmp[i]-dec_ytmp)**2)
            gd=np.where(tmpdist<5./3600)[0]
            if len(gd)>0:
                nearinds[i]=gyHP[gn[np.argsort(tmpdist[gd])[0]]]
    if np.sum(nearinds < 0)<len(nearinds): 
        matchinds[gmHP]=nearinds
cID_m=np.ones(len(cr),dtype='i8')*-1
cID_m[matchinds>-1]=cr['cID'][matchinds[matchinds>-1]]
np.savetxt('/home/rumbaugh/milliquas_y1a1_match.csv',cID_m,fmt='%i')
