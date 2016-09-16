import numpy as np
import os
import matplotlib.pyplot as plt

date='11.17.15'

specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

matchloaddict={'names':('ID','ra','dec','err'),'formats':('i8','f8','f8','f8')}

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

namedict = {obsdict[x]['obsID']: x for x in obsdict.keys()}

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}
spec_dict= { \
             'X1': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':0.756}, \
             'X2': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':0.818}, \
             '927+1708': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':1.261}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':1.050}, \
             'X4': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':0.845}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':0.845}, \
             'X6': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':0.900}, \
             '2229': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.may2012.nodups.cat', 'loaddict': '','z':0.804}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':0.985}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':0}, \
             '3181+4987': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':0.772}, \
             '1662': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.may2015.wdups.cat', 'loaddict': '','z':0.700}, \
             '548': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':0.813}, \
             '2227+2452': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':1.110}, \
             'X9': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':0.691}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':0}, \
             'X11': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':0.959}, \
             '4936': {'file': 'spectroscopic.autocompile.blemaux.RXJ1053.apr2015.BCDXtargetsonly.cat', 'loaddict': '','z':1.140}}

fullcat=np.loadtxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',dtype={'names':('obsID','xrayID','RAX','DecX','Xflux_soft','Xflux_hard','Xflux_full','Xnetcnts_soft','Xnetcnts_hard','Xnetcnts_full','Xsig_soft','Xsig_hard','Xsig_full','Xwd_sig_soft','Xwd_sig_hard','Xwd_sig_full','Xdetcode','Xerr','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','redshift','zerr','magR','magI','magZ','Q'),'formats':('|S16','i8','f8','f8','e8','e8','e8','e8','e8','e8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','f8','f8','f8','f8','e8','i8')})



obj_dict=dict(zip(np.array(["927+1708"]),np.zeros(1)))
names=obj_dict.keys()

#FILE=open('/home/rumbaugh/Chandra/full_Xray_catalog.dat','w')

tol=0.025

for i in range(0,1): 
    strname=names[i]
    crs=np.loadtxt('/home/rumbaugh/Chandra/speccats/%s'%spec_dict[strname]['file'],dtype=specloaddict)
    all_zs,all_ras,all_decs=crs['z'][crs['Q']>2.5],crs['ra'][crs['Q']>2.5],crs['dec'][crs['Q']>2.5]
    zoom_ras,zoom_decs=all_ras[np.abs(all_zs-spec_dict[strname]['z'])<tol],all_decs[np.abs(all_zs-spec_dict[strname]['z'])<tol]
    fore_ras,fore_decs=all_ras[np.abs(all_zs-0.55)<tol],all_decs[np.abs(all_zs-0.55)<tol]
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(all_ras,all_decs,s=4,color='k')
    plt.scatter(zoom_ras,zoom_decs,s=15,color='r')
    plt.scatter(fore_ras,fore_decs,s=15,color='cyan')
    plt.xlabel('RA')
    plt.ylabel('DEC')
    plt.title(namedict[strname])
    plt.savefig('/home/rumbaugh/Chandra/plots/spatial_plot.%s.%s.png'%(strname,date))
    
    
