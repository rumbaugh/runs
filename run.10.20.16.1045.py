import easyaccess as ea
import numpy as np

yt='aaa'
cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y1a1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','MGid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})
IDs=np.unique(cr['cid'])
exps=np.zeros(len(IDs))
for i in range(0,len(IDs)): exps[i]=len(np.where(cr['cid']==IDs[i])[0])

crout=np.zeros((len(IDs),2),dtype='i8')

crout[:,0],crout[:,1]=IDs,exps

np.savetxt('/home/rumbaugh/milliquas_num_epochs.dat',crout,fmt='%i %i')
