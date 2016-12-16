import numpy as np
import os

cr=np.loadtxt('/home/rumbaugh/MQ_SDSS_platemjdfiber.csv',dtype='|S30')

for i in range(0,11):
    g=np.arange(i,len(cr),11)
    np.savetxt('/home/rumbaugh/SASinput%i.csv'%i,cr[g],dtype='%s')
