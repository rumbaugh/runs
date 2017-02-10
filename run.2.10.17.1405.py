import numpy as np
import os

cr=np.loadtxt('/home/rumbaugh/MQ_SDSS_y3a1_tidplatemjdfiber.csv',delimiter=',',dtype='i8',skiprows=1)

outcr=np.zeros(np.shape(cr)[0],dtype='|S120')
for i in range(0,len(outcr)):
    if cr[i][1]<1963:
        redux='26'
    elif cr[i][1]<3140:
        redux='103'
    elif cr[i][1]<4190:
        redux='104'
    else:
        redux='v5_7_0'
    outcr[i]='wget https://dr12.sdss.org/sas/dr12/sdss/spectro/redux/%s/spectra/%i/spec-%04i-%05i-%04i.fits'%(redux,cr[i][1],cr[i][1],cr[i][2],cr[i][3])
np.savetxt('/home/rumbaugh/runs/run.2.10.17.1405.sh',outcr,fmt='%s')
os.system('chmod +x /home/rumbaugh/runs/run.2.10.17.1405.sh')
