import numpy as np
import os
import pyfits as py


band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

obj_dict=dict(zip(np.array(["927+1708","2227+2452","3181+4987"]),np.zeros(3)))
names=obj_dict.keys()
for i in range(0,3): 
    strname=names[i]
    for band in band_dict.keys():
        sfile='/home/rumbaugh/Chandra/%s/sources.%s.%s.1e6.b1.1-16.wexp20.fits'%(strname,strname,band_dict[band]['erange'])
        cr_src=py.open(sfile)
        data=cr_src[1].data
        ra,dec=data['RA'],data['DEC']
        FILE=open('/home/rumbaugh/Chandra/%s/ra_dec_list.%s_%s.dat'%(strname,strname,band),'w')
        for j in range(0,len(ra)): FILE.write('%f %f\n'%(ra[j],dec[j]))
        FILE.close()
