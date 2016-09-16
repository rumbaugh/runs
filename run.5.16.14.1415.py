import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/LoadEVLA_2011.py')

crCSOs = LoadEVLA_2011('CSOs')

f1,f2 = crCSOs['Early']['J0204+0903'],crCSOs['Early']['J0754+5324']
g = np.where((f1>0) & (f2>0))[0]
fr1 = np.std(f1[g]/f2[g])
fr2 = np.std(f2[g]/f1[g])
print fr1,fr2,np.mean(f1[g]/f2[g])
