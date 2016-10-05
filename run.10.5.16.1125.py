import easyaccess as ea
execfile('/home/rumbaugh/runs/run.10.2.16.1930.py')

IDs=np.unique(cr['cid'])
exps=np.zeros(len(IDs))
for i in range(0,len(IDs)): exps[i]=len(np.where(cr['cid']==IDs[i])[0])

crout=np.zeros((len(IDs),2),dtype='i8')

crout[:,0],crout[:,1]=IDs,exps

np.savetxt('/home/rumbaugh/milliquas_num_epochs.dat',crout,fmt='%i %i')
