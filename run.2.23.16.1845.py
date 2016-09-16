import numpy as np
import matplotlib.pyplot as plt

z=np.linspace(0.1,2,191)

cols=()
for i in range(0,len(z)): cols=cols+(i+1,)

crB=np.loadtxt('/home/rumbaugh/LFC_color_param/LFC_color_param_UV_output_graz13_ABlue.2.23.16.dat',usecols=cols)
crR=np.loadtxt('/home/rumbaugh/LFC_color_param/LFC_color_param_UV_output_graz13_ARed.2.23.16.dat',usecols=cols)


for i in range(0,np.shape(crB)[0]):
    g=np.where(((crB[i]==0)&(z>0.5)))[0]
    if len(g)>0:
        crB[i][np.arange(g[0],len(z))]=0
    else:
        print 'No zeros for %i'%i
    g=np.where(((crR[i]==0)&(z>0.5)))[0]
    if len(g)>0:
        crR[i][np.arange(g[0],len(z))]=0
    else:
        print 'No zeros for %i'%i
meanARed,meanABlue=np.mean(crR,axis=0),np.mean(crB,axis=0)
medARed,medABlue=np.median(crR,axis=0),np.median(crB,axis=0)
meanAComb=np.mean(0.5*(crB+crR),axis=0)
medAComb=0.5*(medARed+medABlue)
FILE=open('/home/rumbaugh/LFC_color_param/comb_LFC_param_UVs.graz13.2.23.16.dat','w')
FILE.write('# Color Comb_method A(Color):')
for zi in z: FILE.write(' %4.2f'%zi)
FILE.write('\nRed  Mean  ')
for i in range(0,len(z)): FILE.write(' %9.7f'%meanARed[i])
FILE.write('\nBlue Mean  ')
for i in range(0,len(z)): FILE.write(' %9.7f'%meanABlue[i])
FILE.write('\nRed  Median')
for i in range(0,len(z)): FILE.write(' %9.7f'%medARed[i])
FILE.write('\nBlue Median')
for i in range(0,len(z)): FILE.write(' %9.7f'%medABlue[i])
FILE.write('\nComb Mean  ')
for i in range(0,len(z)): FILE.write(' %9.7f'%meanAComb[i])
FILE.write('\nComb Median')
for i in range(0,len(z)): FILE.write(' %9.7f'%medAComb[i])
FILE.close()
    

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.plot(z,meanARed,lw=2,color='r',label='A(Red):Mean')
plt.plot(z,meanABlue,lw=2,color='b',label='A(Blue):Mean')
plt.plot(z,medARed,lw=2,color='magenta',ls='--',label='A(Red):Median')
plt.plot(z,medABlue,lw=2,color='cyan',ls='--',label='A(Blue):Median')
plt.plot(z,meanAComb,lw=2,color='green',ls='-.',label='A(Comb):Mean')
plt.plot(z,medAComb,lw=2,color='orange',ls='-.',label='A(Comb):Median')
plt.plot(z,medABlue-medARed,lw=2,color='brown',ls='dotted',label='A(Diff):Mean')
plt.xlim(0,2)
plt.ylim(-0.1,1.1)
plt.xlabel('Redshift')
plt.ylabel('A')
plt.legend()
plt.savefig('/home/rumbaugh/LFC_color_param/LFC_color_param_UV.combs.2.23.16.png')

