import numpy as np
import os

cr=np.loadtxt('/home/rumbaugh/MQ_SDSS_y3a1_tidplatemjdfiber.csv',delimiter=',',dtype='i8',skiprows=1)
cr2=np.loadtxt('/home/rumbaugh/DR7_BH_SDSS_tidplatemjdfiber.csv',delimiter=',',dtype='i8',skiprows=1)
cr=np.concatenate((cr,cr2),axis=0)

tids,gtid=np.unique(cr[:,0],return_index=True)
cr=cr[gtid]

outcr=np.zeros(np.shape(cr)[0]+2,dtype='|S120')
outcr[0],outcr[1]='mkdir -p /home/rumbaugh/var_database/Y3A1/spec','cd /home/rumbaugh/var_database/Y3A1/spec'
for i in range(0,len(outcr)):
    if cr[i][1]<1963:
        redux='26'
    elif cr[i][1]<3140:
        redux='103'
    elif cr[i][1]<4190:
        redux='104'
    else:
        redux='v5_7_0'
    outcr[i+2]='wget https://dr12.sdss.org/sas/dr12/sdss/spectro/redux/%s/spectra/%i/spec-%04i-%05i-%04i.fits'%(redux,cr[i][1],cr[i][1],cr[i][2],cr[i][3])
np.savetxt('/home/rumbaugh/runs/run.2.16.17.2110.sh',outcr,fmt='%s')
os.system('chmod +x /home/rumbaugh/runs/run.2.16.17.2110.sh')
