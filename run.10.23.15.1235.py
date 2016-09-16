import numpy as np

execfile("/home/rumbaugh/check_wavdetect_regs.py")

band_dict={'soft': {'erange': '0.5-2.0','n': '500-2000','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','n':'2000-8000','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','n':'500-8000','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()

dum=os.system('ds9 &')

os.chdir('/home/rumbaugh/Chandra/548/test')
ffile='acis548.img.0.5-2.0.vig_corr.fits'
sfile='test_srclist.dat'
rfile='test_srcs.reg'
tfile='test_theta.dat'
check_wavdetect_regs(ffile,sfile,rfile,False,thetafile='test_theta.dat',zoom=4)
