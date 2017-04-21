import numpy as np

r=np.arange(1,762085)
np.random.shuffle(r)
outcr=np.zeros((len(r),2),dtype='i8')
outcr[:,0],outcr[:,1]=r,np.arange(1,len(r)+1)
np.savetxt('/home/rumbaugh/Y3A1_Star_index.csv',outcr,fmt='%i,%i',header='RANDI,NORMI',comments='')
