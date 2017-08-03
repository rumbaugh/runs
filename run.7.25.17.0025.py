import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mmcgdf=pd.read_csv('Chandra/ORELSE.MMCG_vels.csv')
bcgdf=pd.read_csv('Chandra/ORELSE.BCG_vels.csv')
df=pd.merge(mmcgdf,bcgdf,on=['field','cluster'],suffixes=('_MMCG',''))

plt.figure(1)
plt.clf()
plt.scatter(df.BCGvel.values,df.BCGvel_MMCG.values)
ax=plt.gca()
for i in range(0,len(df)):
    plt.text(df.BCGvel.values[i]+10,df.BCGvel_MMCG.values[i]+10,df.cluster.iloc[i],horizontalalignment='left',verticalalignment='bottom')
plt.xlabel('BCG Velocity (km/s)')
plt.ylabel('MMCG Velocity (km/s)')
xlim=plt.xlim()
ylim=plt.ylim()
dummy=[np.min([xlim[0],ylim[0]]),np.max([xlim[1],ylim[1]])]
plt.plot(dummy,dummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.savefig('/home/rumbaugh/Chandra/plots/velcomp.BCG_vs_MMCG.png')
