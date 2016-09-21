import numpy as np
import pyfits as py

hdu=py.open('/home/rumbaugh/Downloads/OzDES_QSO_20160627.fits')
data=hdu[1].data

cr=np.loadtxt('/home/rumbaugh/Y1A1_idradecerrwinmagmagerr_SVA1cut.csv',delimiter=',',skiprows=1)

gmatch=np.ones(len(data),dtype='i8')*-1
y1a1_inds=np.ones(len(data),dtype='i8')*-1
for i in range(0,len(data)):
    if i%100==0: print i
    gcur=np.where((np.abs(data['RA'][i]-cr[:,1])<5./3600/np.cos(data['DEC'][i]))&(np.abs(data['Dec'][i]-cr[:,2])<5./3600))[0]
    if len(gcur)>0:
        tmpdist=np.sqrt(((data['RA'][i]-cr[:,1][gcur])*np.cos(data['DEC'][i]))**2+(data['DEC'][i]-cr[:,2][gcur])**2)
        gd=np.where(tmpdist<5./3600)[0]
        if len(gd)>0: 
            gd=gd[np.argsort(tmpdist[gd])][0]
            gmatch[i]=gcur[gd]
            y1a1_inds[i]=cr[:,0][gcur[gd]]
print 'loop done'
idsout=np.zeros((len(data),3),dtype='|S24')
idsout[:,2]=data['ID']
idsout[:,0]=data['ID']
for i in range(0,len(data)):
    if idsout[:,0][i][:4]=='SVA1':
        idsout[:,0][i]=idsout[:,0][i][11:]
    else:
        idsout[:,0][i]=-1
print 'column 0 done'
idsout[:,1]=y1a1_inds
#idsout[:,1][gmatch!=-1]=cr[:,0][gmatch[gmatch!=-1]]
#idsout[:,1][gmatch==-1]=-1
np.savetxt('/home/rumbaugh/match_OzDES2Y1A1_coadd_objects_ids.txt',idsout,fmt='%24s %20s %20s',header='SVA1_COADD_OBJECTS_ID Y1A1_COADD_OBJECTS_ID OZDES_ID')
np.savetxt('/home/rumbaugh/match_OzDES2Y1A1_coadd_objects_ids.csv',idsout,fmt='%24s,%20s,%20s',header='SVA1_COADD_OBJECTS_ID,Y1A1_COADD_OBJECTS_ID,OZDES_ID')

