print ' '
print 'Make sure you set strname equal to the string form of the chandra ID'
print ' '


import numpy as np
import os

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()
for i in range(0,7): 
    strname=names[i]
    os.chdir('/home/rumbaugh/Chandra/%s/photometry'%names[i])
    os.system('ln -sf ../CALDB_PHOT/%s_caldb_phot/soft/stats.radec_netcntscor_netcnts_cnts_sig_flux.soft.dat .'%(names[i]))
    os.system('ln -sf ../CALDB_PHOT/%s_caldb_phot/hard/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat .'%(names[i]))
    #### Read in Photometry catalogs
    photcat1 = np.loadtxt('stats.radec_netcntscor_netcnts_cnts_sig_flux.soft.dat')
    id_soft,ra_soft,dec_soft,netcnts_corr_soft,netcnts_soft,counts_soft,sig_soft,offaxis_soft,flux_soft,wmask_soft,wsigf_soft,wsigs_soft,wsigh_soft = photcat1[:,0],photcat1[:,1],photcat1[:,2],photcat1[:,3],photcat1[:,4],photcat1[:,5],photcat1[:,6],photcat1[:,7],photcat1[:,8],photcat1[:,9],photcat1[:,10],photcat1[:,11],photcat1[:,12]
    photcat2 = np.loadtxt('stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat')
    id_hard,ra_hard,dec_hard,netcnts_corr_hard,netcnts_hard,counts_hard,sig_hard,offaxis_hard,flux_hard,wmask_hard,wsigf_hard,wsigs_hard,wsigh_hard = photcat2[:,0],photcat2[:,1],photcat2[:,2],photcat2[:,3],photcat2[:,4],photcat2[:,5],photcat2[:,6],photcat2[:,7],photcat2[:,8],photcat2[:,9],photcat2[:,10],photcat2[:,11],photcat2[:,12]

    #### Set minimum counts to zero
    netcnts_corr_softz = netcnts_corr_soft.copy()
    netcnts_corr_hardz = netcnts_corr_hard.copy()
    netcnts_corr_softz[netcnts_corr_softz < 0.0] = 0.0
    netcnts_corr_hardz[netcnts_corr_hardz < 0.0] = 0.0

    netcnts_softz = netcnts_soft.copy()
    netcnts_hardz = netcnts_hard.copy()
    netcnts_softz[netcnts_softz < 0.0] = 0.0
    netcnts_hardz[netcnts_hardz < 0.0] = 0.0

    #### Get Full band counts & flux
    flux_softz = flux_soft.copy()
    flux_hardz = flux_hard.copy()
    flux_softz[flux_softz < 0.0] = 0.0
    flux_hardz[flux_hardz < 0.0] = 0.0

    netcnts_corr_fullz = netcnts_corr_softz + netcnts_corr_hardz 
    flux_fullz = flux_softz + flux_hardz

    #### Get full and composite signifigances
    sig_full = (netcnts_softz+netcnts_hardz)/(1.0 + np.sqrt(0.75 + ((counts_soft-netcnts_soft)+(counts_hard-netcnts_hard))))
    #sig_max = np.zeros(len(sig_soft))
    sig_max = sig_soft.copy()
    sig_max[sig_hard>sig_max]=sig_hard[sig_hard>sig_max]
    sig_max[sig_full>sig_max]=sig_full[sig_full>sig_max]
    sig_soft[sig_soft < 0] = 0
    sig_hard[sig_hard < 0] = 0


    #### Make flag which determines which band the position was measured (this is in the combined source list)
    crf = np.loadtxt('../sources.' + strname + '.full+soft+hard.srclist.dat',dtype='string')
    ra_temp_temp, dec_temp, mask_temp, sigf_temp, sigs_temp, sigh_temp, ncnts_f, ncnts_s, ncnts_h = np.array(crf[:,0],dtype='float'),np.array(crf[:,1]),crf[:,2],np.array(crf[:,3],dtype='float'),np.array(crf[:,4],dtype='float'),np.array(crf[:,5],dtype='float'),np.array(crf[:,6],dtype='float'),np.array(crf[:,7],dtype='float'),np.array(crf[:,8],dtype='float')


    #### output final catalog
    ra = ra_soft.copy()
    dec = dec_soft.copy()   # all ra,dec are the same by the time photometry gets carried out
    wsig_full = wsigf_hard.copy()
    wsig_soft = wsigs_hard.copy()
    wsig_hard = wsigh_hard.copy()
    wmask = wmask_soft.copy()

    FILE = open(strname + '.xray_phot.soft_hard_full.dat','w')
    for i in range(0,len(ra)):
        FILE.write("%f %f %E %E %E %E %E %E %f %f %f %f %f %f %i\n"%(ra[i], dec[i], flux_softz[i], flux_hardz[i], flux_fullz[i],  netcnts_corr_softz[i], netcnts_corr_hardz[i], netcnts_corr_fullz[i], sig_soft[i], sig_hard[i], sig_full[i], wsig_soft[i], wsig_hard[i], wsig_full[i], wmask[i]))
    FILE.close()
