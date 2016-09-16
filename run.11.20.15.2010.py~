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

crd=py.open('/home/rumbaugh/Chandra/7914/Dale/cl0023_srclist_v1.1e-6.fits')
ddata=crd[1].data
mdata=np.loadtxt('/home/rumbaugh/Chandra/7914/photometry/7914.xray_phot.soft_hard_full.dat')

d_ncnts_full = ddata['Full_net_cts']
m_ncnts_soft,m_ncnts_hard,m_ncnts_full= mdata[:,5],mdata[:,6],mdata[:,7]
mra,mdec=mdata[:,0],mdata[:,1]
dra,ddec,derr,dspsf95=ddata['RA'],ddata['Dec'],ddata['Pos_error'],ddata['Soft_95psf']
wsigf,msigs,msigh,msigf=mdata[:,13],mdata[:,8],mdata[:,9],mdata[:,10]

sigma_matrix = np.concatenate((np.reshape(msigs,(len(msigs),1)),np.reshape(msigh,(len(msigh),1)),np.reshape(msigf,(len(msigf),1))),axis=1)
wflagX=np.argsort(sigma_matrix)[:,-1]
ncnts_corrX = np.concatenate((np.reshape(m_ncnts_soft,(len(m_ncnts_soft),1)),np.reshape(m_ncnts_hard,(len(m_ncnts_hard),1)),np.reshape(m_ncnts_full,(len(m_ncnts_full),1))),axis=1)
off_axisX = SphDist(Ra_aim,Dec_aim,mra,mdec)
xwnetcnts = ncnts_corrX[(np.arange(len(wflagX)),wflagX)]

thetas=SphDist(Ra_aim,Dec_aim,mra,mdec)
cr95,cr90=np.loadtxt('/home/rumbaugh/Chandra/interp_r95_list.txt'),np.loadtxt('/home/rumbaugh/Chandra/interp_r90_list.txt')
r95s,r90s=np.interp(thetas,cr95[:,0],cr95[:,1])*0.492,np.interp(thetas,cr90[:,0],cr90[:,1])*0.492

match_ncnts=np.ones(len(dra))*-1.

d_xerr = np.zeros(len(mra))
d_xerr[xwnetcnts<=137.816] = 10**(0.1145*off_axisX[xwnetcnts<=137.816] - 0.4958*np.log10(xwnetcnts[xwnetcnts<=137.816])+0.1932)
d_xerr[xwnetcnts>137.816] = 10**(((0.0968*off_axisX[xwnetcnts>137.816] - 0.2064*np.log10(xwnetcnts[xwnetcnts>137.816])-0.4260)))
d_xerr[off_axisX>=15.] = 60.*np.ones(len(off_axisX[off_axisX>=15.]))
d_xerr[xwnetcnts<=0] = 60.*np.ones(len(xwnetcnts[xwnetcnts<=0]))
d_xerr[d_xerr<1.5] = 1.5*np.ones(len(d_xerr[d_xerr<1.5]))

crc=np.loadtxt("/home/rumbaugh/Chandra/7914/chandra_psf_file.7914.dat")
r95c=crc[:,8]
r95c_low=crc[:,7]

dcnts_comp,mcnts_comp,minds,dinds=np.zeros(0),np.zeros(0),np.zeros(0,dtype='int'),np.zeros(0,dtype='int')
FILE=open('/home/rumbaugh/Chandra/7914/Dale/reduc_comparison_full.dat','w')
for i in range(0,len(dra)):
    diststmp=SphDist(dra[i],ddec[i],mra,mdec)
    g=np.where(diststmp<derr[i])[0]
    if len(g)>0:
        g=g[np.argsort(diststmp[g])[0]]
        print 'Dale: %5.1f Me: %5.1f  Diff: %6.2f Perc: %6.1f'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100)
        FILE.write('%5.1f %5.1f %6.2f %6.1f\n'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100))
        dcnts_comp,mcnts_comp,minds,dinds=np.append(dcnts_comp,d_ncnts_full[i]),np.append(mcnts_comp,m_ncnts_full[g]),np.append(minds,g),np.append(dinds,i)
    else:
        print 'Dale: %5.1f Me: ---'%(d_ncnts_full[i])
        FILE.write('%5.1f    -1 -9999 -9999\n'%(d_ncnts_full[i]))
FILE.close()

msig=msigf[minds]
wsig=wsigf[minds]
cntdiff,percdiff=dcnts_comp-mcnts_comp,(dcnts_comp-mcnts_comp)/dcnts_comp
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(msig,cntdiff)
plt.xlabel('Detection Significance')
plt.ylabel('Difference in net counts')
plt.title('Photometry Code Results')
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/diff_ncnts_vs_sig.7914.png')

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(wsig,cntdiff)
plt.xlabel('Detection Significance')
plt.ylabel('Difference in net counts')
plt.title('wavdetect Results')
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/diff_ncnts_vs_wsig.7914.png')
    
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(msig,percdiff)
plt.xlabel('Detection Significance')
plt.ylabel('Difference in net counts (%)')
plt.title('Photometry Code Results')
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/percdiff_ncnts_vs_sig.7914.png')

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(wsig,percdiff)
plt.xlabel('Detection Significance')
plt.ylabel('Difference in net counts (%)')
plt.title('wavdetect Results')
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/percdiff_ncnts_vs_wsig.7914.png')
    

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(derr[dinds],d_xerr[minds])
PlotUnity()
plt.xlabel("Dale's Positional Error (arcsec)")
plt.ylabel('My Positional Error')
plt.title('Photometry Code Results')
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/poserr_corr.7914.png')
    

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(dspsf95[dinds],r95s[minds])
PlotUnity()
plt.xlabel("Dale's R95 (arcsec)")
plt.ylabel('My R95')
plt.title('Soft 95% flux enclosed regions')
plt.xlim(0,17)
plt.ylim(0,17)
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/psf95_soft_corr.7914.png')
    


plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(dspsf95[dinds],r95c[minds])
PlotUnity()
plt.xlabel("Dale's R95 (arcsec)")
plt.ylabel('My R95 (1.5 keV chandra PSF)')
plt.title('Soft 95% flux enclosed regions')
plt.xlim(0,17)
plt.ylim(0,17)
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/psf95_soft_chandra_corr.7914.png')
    


plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(dspsf95[dinds],r95c_low[minds])
PlotUnity()
plt.xlabel("Dale's R95 (arcsec)")
plt.ylabel('My R95 (1.25 keV chandra PSF)')
plt.title('Soft 95% flux enclosed regions')
plt.xlim(0,17)
plt.ylim(0,17)
plt.savefig('/home/rumbaugh/Chandra/7914/Dale/plots/psf95_soft_1.25_chandra_corr.7914.png')
    
