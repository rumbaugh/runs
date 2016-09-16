import numpy as np
import os
os.chdir('/home/rumbaugh/Chandra/0849')
cr = np.loadtxt("sources.927+1708.full+soft+hard.1e6.b1.1-16.wexp20.xsradecsigncnts.hdat")
#, mask, RAf, RAs, RAh, DECf, DECs, DECh, sf, ss, sh, ncnts_f, ncnts_s, ncnts_h, xsxf, xsxs, xsxh, xsyf, xsys, xsyh,  format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D'
sig,ra,dec,ra_out,dec_out = np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0])
sig[:,0] = cr[:,7]
sig[:,1] = cr[:,8]
sig[:,2] = cr[:,9]
ra[:,0] = cr[:,1]
ra[:,1] = cr[:,2]
ra[:,2] = cr[:,3]
dec[:,0] = cr[:,4]
dec[:,1] = cr[:,5]
dec[:,2] = cr[:,6]

# sig[0,*] = sf  &  sig[1,*] = ss  &  sig[2,*] = sh  
# ra[0,*] = raf  &  ra[1,*] = ras  &  ra[2,*] = rah  
# dec[0,*] = decf  &  dec[1,*] = decs  &  dec[2,*] = dech  
FILE = open("sources.927+1708.full+soft+hard.srclist.dat",'w')
for i in range(0,np.shape(cr)[0]):
    g = np.where((sig[i] == np.max(sig[i])))[0]
    ra_out[i] = ra[i][g[0]]
    dec_out[i] = dec[i][g[0]]
    FILE.write('%f %f %i %f %f %f %f %f %f\n'%(ra_out[i], dec_out[i], int(mask[i]), sf[i],ss[i],sh[i], ncnts_f[i], ncnts_s[i], ncnts_h[i]))
FILE.close()
