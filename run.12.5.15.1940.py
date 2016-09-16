import numpy as np
import os
import matplotlib.pyplot as plt

date='11.10.15'

specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

namedict = {obsdict[x]['obsID']: x for x in obsdict.keys()}

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}
spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':0.756}, \
             'rxj1821': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':0.818}, \
             'cl0849': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':1.261}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':1.050}, \
             'cl0023': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':0.845}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':0.845}, \
             'cl1604': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':0.900}, \
             'cl1350': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.may2012.nodups.cat', 'loaddict': '','z':0.804}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':0.985}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':0}, \
             'rcs0224': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':0.772}, \
             'rxj1221': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.may2015.wdups.cat', 'loaddict': '','z':0.700}, \
             'rxj1716': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':0.813}, \
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':1.110}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':0.691}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':0}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':0.959}, \
             'rxj1053': {'file': 'spectroscopic.autocompile.blemaux.RXJ1053.apr2015.BCDXtargetsonly.cat', 'loaddict': '','z':1.140}}

fullcat=np.loadtxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',dtype={'names':('obsID','xrayID','RAX','DecX','Xflux_soft','Xflux_hard','Xflux_full','Xnetcnts_soft','Xnetcnts_hard','Xnetcnts_full','Xsig_soft','Xsig_hard','Xsig_full','Xwd_sig_soft','Xwd_sig_hard','Xwd_sig_full','Xdetcode','Xerr','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','redshift','zerr','magR','magI','magZ','Q'),'formats':('|S16','i8','f8','f8','e8','e8','e8','e8','e8','e8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','f8','f8','f8','f8','e8','i8')})

strucarr=np.array(['rcs0224','cl0849','rxj0910','rxj1053','rxj1221','cl1350','rxj1716','cl1604','cl0023','cl1324','rxj1757','rxj1821','cl1137'])


obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()

#FILE=open('/home/rumbaugh/Chandra/full_Xray_catalog.dat','w')

tol=0.2

for i in strucarr: 
    print i
    cr=np.loadtxt('/home/rumbaugh/Chandra/speccats/%s'%spec_dict[i]['file'],dtype={'names':('ID','mask','slit','ra','dec'),'formats':('|S8','|S8','|S8','f8','f8')})
    print np.average(cr['ra']),np.average(cr['dec'])
    arrtmp=np.zeros((len(cr['ra']),),dtype=[('ra','f8'),('dec','f8')])
    arrtmp['ra'],arrtmp['dec']=cr['ra'],cr['dec']
    np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/refcats/speccat.%s.radec.dat'%i,arrtmp,fmt='%f %f',header='RA DEC')
