import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

vddf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.veldiffs.6.26.17.dat',delim_whitespace=True)
csdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clus_sigs_wZ.6.25.17.dat',delim_whitespace=True)
vdRFdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.veldiffs.RF.dat',delim_whitespace=True)
csRFdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clus_sigs_RF.dat',delim_whitespace=True)

df=pd.merge(vdRFdf,csRFdf,on=['#Field','Cluster'])
df=pd.merge(df,vddf,on=['#Field','Cluster'],suffixes=('_RF',''))
df=pd.merge(df,csdf,on=['#Field','Cluster'])


df=df[(df.Cluster.values!='Cl0849')&(df.Cluster.values!='1324+3013')&(df.Cluster.values!='RXJ1716A')]

plt.figure(1)
plt.clf()

plt.errorbar(df.Sig_red.values,df.Sig_blue.values,xerr=df.Sig_red_Error,yerr=df.Sig_blue_Error,color='b',fmt='o',capsize=3,mew=1,ms=4)
plt.errorbar(df.Sig_Q.values,df.Sig_SF.values,xerr=df.Sig_Q_Error,yerr=df.Sig_SF_Error,color='r',fmt='o',capsize=3,mew=1,ms=4)
ax=plt.gca()
for i in range(0,len(df)):
    ax.arrow(df.Sig_red.values[i],df.Sig_blue.values[i],df.Sig_Q.values[i]-df.Sig_red.values[i],df.Sig_SF.values[i]-df.Sig_blue.values[i],color='k',lw=2)
plt.xlabel('Red/Quiescent Velocity Dispersion (km/s)')
plt.ylabel('Blue/Star-Forming Velocity Dispersixon (km/s)')
plt.ylim(150,2200)
plt.savefig('/home/rumbaugh/Chandra/plots/veldiff_comp.SC_vs_SED.png')

plt.figure(1)
plt.clf()
plt.scatter(df.perc.values*100,df.perc_RF.values*100)
plt.xlabel('Chance of Red/Blue velocity difference occuring by chance(%)')
plt.ylabel('Chance of Q/SF velocity difference occuring by chance(%)')
plt.savefig('/home/rumbaugh/Chandra/plots/perc_comp.SC_vs_SED.png')
