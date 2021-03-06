import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys
import pappy


date = '5.12.14'

try:
    maxseasonfrac
except NameError:
    maxseasonfrac=0.75

refcr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')
scr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/season_lens.txt')
for kernel in ['boxcar']:
    ldate = '4.15.14'
    for use_cov_matrix in [True,False]:
        if use_cov_matrix: cmstr = 'wcovmat'
        else: cmstr = 'nocovmat'
        for use_Neff in [True]:
            Neffstr = '_Neff'
            cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/results/TDC_MCMC_%s_%s%s_%s.dat'%(kernel,cmstr,Neffstr,ldate))
            tautmp,taulbtmp,tauubtmp = cr[:,1],cr[:,2],cr[:,3]
            tau_dif = refcr-tautmp
            tau_abs_dif = np.abs(tau_dif)
            tau_sig_dif = tau_dif/(tautmp-taulbtmp)
            g = np.where(tau_dif>0)[0]
            tau_sig_dif[g] = tau_dif[g]/(tauubtmp[g]-tautmp[g])
            tau_abs_sig_dif = np.abs(tau_sig_dif)
            tau_frac_dif = tau_dif/refcr
            tau_abs_frac_dif = np.abs(tau_frac_dif)
            tau_low_err,tau_hi_err,tau_avg_err,tau_low_frac_err,tau_hi_frac_err,tau_avg_frac_err = tautmp-taulbtmp,tauubtmp-tautmp,0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)),(tautmp-taulbtmp)/tautmp,(tauubtmp-tautmp)/tautmp,(0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)))/tautmp
            tmp_stuck = np.zeros(100)
            for i in range(0,100):
                tmp_stuck[i] = np.min((tau_low_err[i],tau_hi_err[i]))
            #perc_stuck = len(tmp_stuck[tmp_stuck<1])/100.
            perc_stuck = len(np.where((tmp_stuck<1) & (tau_abs_sig_dif>5))[0])/100.
            perc_stuck_but_not_impossible =  len(np.where(((tmp_stuck<1) & (tau_abs_sig_dif>5) & (scr[:,2]<maxseasonfrac)))[0])/100.
            
            keys = ('tau_dif','tau_abs_dif','tau_sig_dif','tau_abs_sig_dif','tau_frac_dif','tau_abs_frac_dif','tau_low_err','tau_hi_err','tau_avg_err','tau_low_frac_err','tau_hi_frac_err','tau_avg_frac_err')
            ans = (tau_dif,tau_abs_dif,tau_sig_dif,tau_abs_sig_dif,tau_frac_dif,tau_abs_frac_dif,tau_low_err,tau_hi_err,tau_avg_err,tau_low_frac_err,tau_hi_frac_err,tau_avg_frac_err)
            titles = ('Difference','Absolute Difference','Difference (sigma)','Absolute Difference (sigma)','Fractional Difference','Absolute Fractional Difference','Lower Error','High Error','Average Error','Lower Fractional Error','High Fractional Error','Average Fractional Error')

            dict_tmp = dict(zip(keys,ans))
            title_dict = dict(zip(keys,titles))
            plt.figure(1)
            plt.rc('axes',linewidth=2)
            plt.fontsize = 14
            plt.tick_params(which='major',length=8,width=2,labelsize=14)
            plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
            plt.clf()
            plt.scatter(tau_abs_dif,tau_avg_err)
            #plt.title('Absolute Difference vs. Average Error')
            plt.xlabel('Absolute Difference (days)')
            plt.ylabel('Average Error (days)')
            plt.ylim(-2,50)
            plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/plot.tau_abs_dif_vs_tau_avg_err.TDC_MCMC_%s_%s%s_%s.png'%(kernel,cmstr,Neffstr,date))


