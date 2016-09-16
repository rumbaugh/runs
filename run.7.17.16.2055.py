import numpy as np
import pyfits as py

hdu1=py.open('/home/rumbaugh/Downloads/0848_clusters_jul2016.fits')
hdu2=py.open('/home/rumbaugh/Downloads/0848_groups_jul2016.fits')
data1,data2=hdu1[1].data,hdu2[1].data

outtxt=np.zeros((len(data1)+len(data2),5))
outtxt[:,0]=np.append(data1['ID'],data2['ID'])
outtxt[:,1]=np.append(data1['RA'],data2['RA'])
outtxt[:,2]=np.append(data1['DEC'],data2['DEC'])
outtxt[:,3]=np.append(data1['MAGZ850'],data2['MAGZ850'])
outtxt[:,4]=np.append(data1['specz'],data2['SPECZ'])

np.savetxt('/home/rumbaugh/Chandra/Cl0849_Mei_speczs.dat',outtxt,header='ID RA Dec MAGZ850 spec_z',fmt='%6i %10.6f %9.6f %8.4f %f')
