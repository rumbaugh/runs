import numpy as np
import time
execfile('/home/rumbaugh/get_cols_batch.py')
z = np.array(['soft','hard'])
nd = np.array(['0.5,2.0','2.0,8.0'])
ndL = np.array([0.5,2.0])
ndH = np.array([2.0,8.0])
nh = np.array([2.79,1.22,1.22,1.155,1.155,5.66,4.07])
mas0 = np.array(['7914','master','master','master','master','master','master'])
mas = np.array(['7914','6932','master','master','master','master','master'])
inum = np.array(['7914','6932','6933+7343','9403+9840','9404+9836','10444+10924','10443+11999'])
singnum = np.array([7914,6932,6933,9403,9404,10444,11999])
mas2 = np.array(['7914','6932','master','9403','9404','master','master'])
icnt = 0
zs = np.array([0.84,0.9,0.9,0.76,0.76,0.82,0.69])
exps = np.array([49383.247922195,49478.092354796,46103.507982594,48391.890220549,50399.00069391,49548.501183658,46451.792387024])
f2l = np.array([1.676,1.987,1.987,1.310,1.310,1.580,1.034])

mx = (43.2104078-43.348505)/(240.9472-241.28263)
cl1324rac = 0.5*(30.86373172217+30.279328719557)
icnt = -1
names = np.array(['Cl0023','Cl1604','Cl1604','Cl1324','Cl1324','NEP5281','RXJ1757'])
snames = np.array(['0023','1604','1604','1322','1322','N5281','N200'])
st = time.time()
tarr = np.zeros(8)
tarr[0] = st

zhb = [0.87,0.96,0.96,0.79,0.79,0.84,0.71]
zlb = [0.820,0.84,0.84,0.65,0.65,0.80,0.68]
#ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']

FILE = open("/home/rumbaugh/temp.4piDL2.8.9.11.dat",'w')
for i in range(0,len(zhb)):
    sfile = '/home/rumbaugh/LFC/FINAL.matched.' + snames[i]  + '.specnXray.nov2010.rumbaugh.noheader.cat'
    if ((i != 2) and (i != 4)): crs = read_file(sfile)
    if i != 1: LFC_ID,mask,slit,RA_opt,dec_opt,rband, iband, zband, z,z_err,q,old_ID, Xray_ID, RA_Xray,dec_Xray,poserr, Num_opt, Rel,Sig = get_cols_batch(crs,19)
    if icnt == 1: 
        LFC_ID,mask,slit,RA_opt,dec_opt,rband, iband, zband, z,z_err,q,old_ID, maskACS, RA_ACS, dec_ACS,ACS_ID, F606W, F814W, Xray_ID, RA_Xray,dec_Xray,poserr, Num_opt, Rel,Sig = get_cols_batch(crs,25)
    g = np.where((z > zlb[i]) & (z < zhb[i]) & (q > 2.3))
    g = g[0]
    if ((i != 1) and (i != 3)):
        for j in range(0,len(g)): FILE.write('%f\n'%(z[g[j]]))
FILE.close()
    
