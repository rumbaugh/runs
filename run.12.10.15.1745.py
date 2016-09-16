import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/SphDist.py')

def PlotUnity():
    xlims,ylims=plt.xlim(),plt.ylim()
    LB=xlims[0]
    if ylims[0]>xlims[0]:LB=ylims[0]
    UB=xlims[1]
    if ylims[1]<xlims[1]:UB=ylims[1]
    tmparr=np.array([LB,UB])
    plt.plot(tmparr,tmparr,color='k')

Ra_aim,Dec_aim=5.9623443990511,4.3820249628906

crd=py.open('/home/rumbaugh/Chandra/7914/Dale/cl0023_srclist_v1.1e-4.fits')
ddata=crd[1].data
crm=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE//cl0023/proc/cl0023/SRCv1/cl0023_srclist_v1.fits')
mdata=crm[1].data


d_ncnts_full = ddata['Full_net_cts']
m_ncnts_full= mdata['Full_net_cts']
mra,mdec,merr,mspsf95=mdata['RA'],mdata['Dec'],mdata['Pos_error'],mdata['Soft_95psf']
#r95s,r95h=np.average(mdata[:,-6:-4],axis=1),np.average(mdata[:,-3:-1],axis=1)
dra,ddec,derr,dspsf95=ddata['RA'],ddata['Dec'],ddata['Pos_error'],ddata['Soft_95psf']
#wsigf,msigs,msigh,msigf=mdata[:,13],mdata[:,8],mdata[:,9],mdata[:,10]

dcnts_comp,mcnts_comp,minds,dinds=np.zeros(0),np.zeros(0),np.zeros(0,dtype='int'),np.zeros(0,dtype='int')
FILE=open('/home/rumbaugh/Chandra/7914/Dale/reduc_comparison_full_12.10.15.dat','w')
for i in range(0,len(dra)):
    diststmp=SphDist(dra[i],ddec[i],mra,mdec)
    g=np.where(diststmp<derr[i])[0]
    if len(g)>0:
        g=g[np.argsort(diststmp[g])[0]]
        print 'Dale: %5.1f Me: %5.1f  Diff: %6.2f Perc: %6.1f Dist: %6.1f'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100,diststmp[g])
        #print '%9.5f %9.5f %9.5f %9.5f'%(dra[i],ddec[i],mra[g],mdec[g])
        FILE.write('%5.1f %5.1f %6.2f %6.1f\n'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100))
        dcnts_comp,mcnts_comp,minds,dinds=np.append(dcnts_comp,d_ncnts_full[i]),np.append(mcnts_comp,m_ncnts_full[g]),np.append(minds,g),np.append(dinds,i)
    else:
        print 'Dale: %5.1f Me: ---'%(d_ncnts_full[i])
        FILE.write('%5.1f    -1 -9999 -9999\n'%(d_ncnts_full[i]))
FILE.close()
