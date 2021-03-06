import numpy as np
import pyfits as py
execfile('/home/rumbaugh/SphDist.py')
crd=py.open('/home/rumbaugh/Chandra/7914/Dale/cl0023_srclist_v1.1e-6.fits')
ddata=crd[1].data
crm=py.open('/home/rumbaugh/Chandra/7914/sources.7914.0.5-8.0.1e6.b1.1-16.wexp20.fits')
mdata=crm[1].data
d_ncnts_full = ddata['Full_net_cts']
m_ncnts_full= mdata['NET_COUNTS']
mra,mdec=mdata['RA'],mdata['DEC']
dra,ddec,derr=ddata['RA'],ddata['Dec'],ddata['Pos_error']

match_ncnts=np.ones(len(dra))*-1.


FILE=open('/home/rumbaugh/Chandra/7914/Dale/reduc_WD_comparison_full.dat','w')
for i in range(0,len(dra)):
    diststmp=SphDist(dra[i],ddec[i],mra,mdec)
    g=np.where(diststmp<derr[i])[0]
    if len(g)>0:
        g=g[np.argsort(diststmp[g])[0]]
        print 'Dale: %5.1f Me: %5.1f  Diff: %6.2f Perc: %6.1f'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100)
        FILE.write('%5.1f %5.1f %6.2f %6.1f\n'%(d_ncnts_full[i],m_ncnts_full[g],d_ncnts_full[i]-m_ncnts_full[g],(d_ncnts_full[i]-m_ncnts_full[g])/d_ncnts_full[i]*100))
    else:
        print 'Dale: %5.1f Me: ---'%(d_ncnts_full[i])
        FILE.write('%5.1f    -1 -9999 -9999\n'%(d_ncnts_full[i]))
FILE.close()
        
