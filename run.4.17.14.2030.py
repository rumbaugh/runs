import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys
execfile('/home/rumbaugh/LinReg.py')

try:
    date
except NameError:
    date = '4.17.14'

try:
    maxseasonfrac
except NameError:
    maxseasonfrac=0.75

refcr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')
scr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/season_lens.txt')
masterFILE = open('/home/rumbaugh/sim_ltcurve_testing/results/master_diftab.TDC_MCMC_%s.dat'%(date),'w')
masterFILE.write('kernel  use cov matrix?  use N_eff?  tau_dif_med  tau_dif_sig  tau_abs_dif_med  tau_abs_dif_sig  tau_sig_dif_med  tau_sig_dif_sig  tau_abs_sig_dif_med  tau_abs_sig_dif_sig  tau_frac_dif_med  tau_frac_dif_sig  tau_abs_frac_dif_med  tau_abs_frac_dif_sig  tau_low_err_med  tau_low_err_sig  tau_hi_err_med  tau_hi_err_sig  tau_avg_err_med  tau_avg_err_sig  tau_low_frac_err_med  tau_low_frac_err_sig  tau_hi_frac_err_med  tau_hi_frac_err_sig  tau_avg_frac_err_med  tau_avg_frac_err_sig perc_stuck\n')
kernel = 'boxcar'
ldate = '4.15.14'
Neffstr = '_Neff'
crwc = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/results/TDC_MCMC_%s_wcovmat%s_%s.dat'%(kernel,Neffstr,ldate))
crnc = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/results/TDC_MCMC_%s_nocovmat%s_%s.dat'%(kernel,Neffstr,ldate))

tau_wctmp,tau_wclbtmp,tau_wcubtmp = crwc[:,1],crwc[:,2],crwc[:,3]
tau_wc_dif = refcr-tau_wctmp
tau_wc_abs_dif = np.abs(tau_wc_dif)
tau_wc_sig_dif = tau_wc_dif/(tau_wctmp-tau_wclbtmp)
g = np.where(tau_wc_dif>0)[0]
tau_wc_sig_dif[g] = tau_wc_dif[g]/(tau_wcubtmp[g]-tau_wctmp[g])
tau_wc_abs_sig_dif = np.abs(tau_wc_sig_dif)
tau_wc_frac_dif = tau_wc_dif/refcr
tau_wc_abs_frac_dif = np.abs(tau_wc_frac_dif)
tau_wc_low_err,tau_wc_hi_err,tau_wc_avg_err,tau_wc_low_frac_err,tau_wc_hi_frac_err,tau_wc_avg_frac_err = tau_wctmp-tau_wclbtmp,tau_wcubtmp-tau_wctmp,0.5*(np.abs(tau_wcubtmp-tau_wctmp)+np.abs(tau_wctmp-tau_wclbtmp)),(tau_wctmp-tau_wclbtmp)/tau_wctmp,(tau_wcubtmp-tau_wctmp)/tau_wctmp,(0.5*(np.abs(tau_wcubtmp-tau_wctmp)+np.abs(tau_wctmp-tau_wclbtmp)))/tau_wctmp
wc_tmp_stuck = np.zeros(100)
nc_tmp_stuck = np.zeros(100)
for i in range(0,100):
    wc_tmp_stuck[i] = np.min((tau_wc_low_err[i],tau_wc_hi_err[i]))
            #perc_stuck = len(tmp_stuck[tmp_stuck<1])/100.
wc_perc_stuck = len(np.where((wc_tmp_stuck<1) & (tau_wc_abs_sig_dif>5))[0])/100.
wc_perc_stuck_but_not_impossible =  len(np.where(((wc_tmp_stuck<1) & (tau_wc_abs_sig_dif>5) & (scr[:,2]<maxseasonfrac)))[0])/100.
            

tau_nctmp,tau_nclbtmp,tau_ncubtmp = crnc[:,1],crnc[:,2],crnc[:,3]
tau_nc_dif = refcr-tau_nctmp
tau_nc_abs_dif = np.abs(tau_nc_dif)
tau_nc_sig_dif = tau_nc_dif/(tau_nctmp-tau_nclbtmp)
g = np.where(tau_nc_dif>0)[0]
tau_nc_sig_dif[g] = tau_nc_dif[g]/(tau_ncubtmp[g]-tau_nctmp[g])
tau_nc_abs_sig_dif = np.abs(tau_nc_sig_dif)
tau_nc_frac_dif = tau_nc_dif/refcr
tau_nc_abs_frac_dif = np.abs(tau_nc_frac_dif)
tau_nc_low_err,tau_nc_hi_err,tau_nc_avg_err,tau_nc_low_frac_err,tau_nc_hi_frac_err,tau_nc_avg_frac_err = tau_nctmp-tau_nclbtmp,tau_ncubtmp-tau_nctmp,0.5*(np.abs(tau_ncubtmp-tau_nctmp)+np.abs(tau_nctmp-tau_nclbtmp)),(tau_nctmp-tau_nclbtmp)/tau_nctmp,(tau_ncubtmp-tau_nctmp)/tau_nctmp,(0.5*(np.abs(tau_ncubtmp-tau_nctmp)+np.abs(tau_nctmp-tau_nclbtmp)))/tau_nctmp
tmp_stuck = np.zeros(100)
for i in range(0,100):
    nc_tmp_stuck[i] = np.min((tau_nc_low_err[i],tau_nc_hi_err[i]))
            #perc_stuck = len(tmp_stuck[tmp_stuck<1])/100.
nc_perc_stuck = len(np.where((nc_tmp_stuck<1) & (tau_nc_abs_sig_dif>5))[0])/100.
nc_perc_stuck_but_not_impossible =  len(np.where(((nc_tmp_stuck<1) & (tau_nc_abs_sig_dif>5) & (scr[:,2]<maxseasonfrac)))[0])/100.
            
keys_wc = ('tau_wc_dif','tau_wc_abs_dif','tau_wc_sig_dif','tau_wc_abs_sig_dif','tau_wc_frac_dif','tau_wc_abs_frac_dif','tau_wc_low_err','tau_wc_hi_err','tau_wc_avg_err','tau_wc_low_frac_err','tau_wc_hi_frac_err','tau_wc_avg_frac_err')
keys_nc = ('tau_nc_dif','tau_nc_abs_dif','tau_nc_sig_dif','tau_nc_abs_sig_dif','tau_nc_frac_dif','tau_nc_abs_frac_dif','tau_nc_low_err','tau_nc_hi_err','tau_nc_avg_err','tau_nc_low_frac_err','tau_nc_hi_frac_err','tau_nc_avg_frac_err')
ans_wc = (tau_wc_dif,tau_wc_abs_dif,tau_wc_sig_dif,tau_wc_abs_sig_dif,tau_wc_frac_dif,tau_wc_abs_frac_dif,tau_wc_low_err,tau_wc_hi_err,tau_wc_avg_err,tau_wc_low_frac_err,tau_wc_hi_frac_err,tau_wc_avg_frac_err)
ans_nc = (tau_nc_dif,tau_nc_abs_dif,tau_nc_sig_dif,tau_nc_abs_sig_dif,tau_nc_frac_dif,tau_nc_abs_frac_dif,tau_nc_low_err,tau_nc_hi_err,tau_nc_avg_err,tau_nc_low_frac_err,tau_nc_hi_frac_err,tau_nc_avg_frac_err)
titles = ('Difference','Absolute Difference','Difference (sigma)','Absolute Difference (sigma)','Fractional Difference','Absolute Fractional Difference','Lower Error','High Error','Average Error','Lower Fractional Error','High Fractional Error','Average Fractional Error')

dict_wc_tmp = dict(zip(keys_wc,ans_wc))
dict_nc_tmp = dict(zip(keys_nc,ans_nc))
title_dict = dict(zip(keys_wc,titles))
for metric in ['tau_avg_err','tau_abs_dif']:
    metric_wc,metric_nc = 'tau_wc%s'%metric[3:],'tau_nc%s'%metric[3:]
    plt.figure(1)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.clf()
    nbins = 40
    if metric == 'tau_abs_dif':
        trange = (0,200)
    else:
        trange = None
#plt.hist(dict_tmp[metric],bins=nbins,range=trange)
    plt.plot([0,np.max(dict_wc_tmp[metric_wc])],[0,np.max(dict_wc_tmp[metric_wc])],c='k')
    plt.scatter(dict_wc_tmp[metric_wc],dict_nc_tmp[metric_nc])
    plt.title(title_dict[metric_wc])
    plt.ylabel('No covariance matrix')
    plt.xlabel('With covariance matrix')
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/plot.%s_vs_%s.TDC_MCMC_%s_%s_%s.png'%(metric_wc,metric_nc,kernel,Neffstr,date))
    plt.xlim(-1,10)
    plt.ylim(-1,10)
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/plot_zoom.%s_vs_%s.TDC_MCMC_%s_%s_%s.png'%(metric_wc,metric_nc,kernel,Neffstr,date))
    print metric_wc
    A,B,Aerr,Berr = LinReg(dict_wc_tmp[metric_wc],dict_nc_tmp[metric_nc],err=True)
    print A,B,Aerr,Berr
