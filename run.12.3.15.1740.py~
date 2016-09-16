import numpy as np
import os
import pyfits as py
import scipy.interpolate as interp

crp=py.open('/home/rumbaugh/Chandra/psftable.fits')
d=crp[1].data
dh=crp[3].data
psfA=d['PSF95'][:,0]
psfB=d['PSF95'][:,1]
ang=d['PSF95'][:,2]
psfAh=dh['PSF90'][:,0]
psfBh=dh['PSF90'][:,1]
angh=dh['PSF90'][:,2]
xinh=dh['X']
yinh=dh['Y']
xin=d['X']
yin=d['Y']

interp_psfA,interp_psfB,interp_ang = interp.RectBivariateSpline(xin[np.arange(0,211*211,211)],yin[:211],np.reshape(psfA,((211,211)))),interp.RectBivariateSpline(xin[np.arange(0,211*211,211)],yin[:211],np.reshape(psfB,((211,211)))),interp.RectBivariateSpline(xin[np.arange(0,211*211,211)],yin[:211],np.reshape(ang,((211,211))))
interp_psfAh,interp_psfBh,interp_angh = interp.RectBivariateSpline(xinh[np.arange(0,211*211,211)],yinh[:211],np.reshape(psfAh,((211,211)))),interp.RectBivariateSpline(xinh[np.arange(0,211*211,211)],yinh[:211],np.reshape(psfBh,((211,211)))),interp.RectBivariateSpline(xinh[np.arange(0,211*211,211)],yinh[:211],np.reshape(angh,((211,211))))

gc=15

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

obj_dict=dict(zip(np.array(["7914"]),np.zeros(1)))
names=obj_dict.keys()
for j in range(0,1): 
    os.chdir('/home/rumbaugh/Chandra/%s'%names[j])
    cr = np.loadtxt("sources.%s.full+soft+hard.1e6.b1.1-16.wexp20.xsradecxysigncnts.hdat"%names[j])
    #, mask, RAf, RAs, RAh, DECf, DECs, DECh, sf, ss, sh, ncnts_f, ncnts_s, ncnts_h, xsxf, xsxs, xsxh, xsyf, xsys, xsyh,  format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D'
    sig,ncnts,ra,dec,x,y,x_out,y_out,ra_out,dec_out,psfA_out,psfB_out,ang_out,psfAh_out,psfBh_out,angh_out = np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros((np.shape(cr)[0],3)),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0]),np.zeros(np.shape(cr)[0])
    mask=cr[:,0]
    sig[:,0] = cr[:,13]
    sig[:,1] = cr[:,14]
    sig[:,2] = cr[:,15]
    ncnts[:,0] = cr[:,16]
    ncnts[:,1] = cr[:,17]
    ncnts[:,2] = cr[:,18]
    ra[:,0] = cr[:,1]
    ra[:,1] = cr[:,2]
    ra[:,2] = cr[:,3]
    dec[:,0] = cr[:,4]
    dec[:,1] = cr[:,5]
    dec[:,2] = cr[:,6]
    x[:,0] = cr[:,7]
    x[:,1] = cr[:,8]
    x[:,2] = cr[:,9]
    y[:,0] = cr[:,10]
    y[:,1] = cr[:,11]
    y[:,2] = cr[:,12]
    

    # sig[0,*] = sf  &  sig[1,*] = ss  &  sig[2,*] = sh  
    # ra[0,*] = raf  &  ra[1,*] = ras  &  ra[2,*] = rah  
    # dec[0,*] = decf  &  dec[1,*] = decs  &  dec[2,*] = dech  
    FILE = open("sources.%s.full+soft+hard.srclist+errors.dat"%names[j],'w')
    for i in range(0,np.shape(cr)[0]):
        g = np.where((sig[i] == np.max(sig[i])))[0]
        ra_out[i] = ra[i][g[0]]
        dec_out[i] = dec[i][g[0]]
        x_out[i] = x[i][g[0]]
        y_out[i] = y[i][g[0]]
    psfA_out=interp_psfA.ev(x_out,y_out)
    psfB_out=interp_psfB.ev(x_out,y_out)
    ang_out=interp_ang.ev(x_out,y_out)
    psfAh_out=interp_psfAh.ev(x_out,y_out)
    psfBh_out=interp_psfBh.ev(x_out,y_out)
    angh_out=interp_angh.ev(x_out,y_out)
    for i in range(0,np.shape(cr)[0]):
        FILE.write('%f %f %f %f %i %f %f %f %f %f %f %f %f %f %f %f %f\n'%(ra_out[i], dec_out[i],x_out[i], y_out[i], mask[i], sig[i][0],sig[i][1],sig[i][2], ncnts[i][0], ncnts[i][1], ncnts[i][2], psfA_out[i],psfB_out[i], ang_out[i], psfAh_out[i],psfBh_out[i], angh_out[i]))
    FILE.close()
