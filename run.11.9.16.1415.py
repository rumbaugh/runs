import easyaccess as ea
import numpy as np

yt='aaa'
cr=np.loadtxt('/home/rumbaugh/SDSSPOSS_lightcurve_entries.tab',skiprows=1,dtype={'names':('cid','SPRN'),'formats':('i8','i8')},usecols=(0,1))
IDs=np.unique(cr['cid'])
exps=np.zeros(len(IDs))
for i in range(0,len(IDs)): exps[i]=len(np.where(cr['cid']==IDs[i])[0])

crout=np.zeros((len(IDs),2),dtype='i8')

crout[:,0],crout[:,1]=IDs,exps

np.savetxt('/home/rumbaugh/SDSSPOSS_Y1A1_num_epochs.dat',crout,fmt='%i %i')
