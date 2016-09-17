import numpy as np
import pyfits as py

hdu=py.open('/home/rumbaugh/Downloads/OzDES_QSO_20160627.fits')
data=hdu[1].data

cr=np.loadtxt('/home/rumbaugh/Y1A1_idradecerrwinmagmagerr.csv',delimiter=',')

gmatch=np.ones(len(data),dtype='i8')*-1

for i in range(0,len(data)):
    gcur=np.where((np.abs(data['RA'][i]-cr[:,1])<5./3600/np.cos(data['DEC'][i]))&(np.abs(data['Dec'][i]-cr[:,2])<5./3600))[0]
    if len(gcur)>0:
        tmpdist=np.sqrt(((data['RA'][i]-cr[:,1][gcur])*np.cos(data['DEC'][i]))**2+(data['DEC'][i]-cr[:,2][gcur])**2)
        gd=np.where(tmpdist<5./3600)[0]
        if len(gd)>0: 
            gd=gd[np.argsort(tmpdist[gd])][0]
            gmatch[i]=gd
idsout=np.zeros(len(data),dtype='|S256')
idsout[gcur!=-1]=cr[:,0]
idsout[gcur==-1]='NONE'
np.savetxt('/home/rumbaugh/match_OzDES2Y1A1_coadd_objects_ids.txt',idsout,fmt='%|S256')

