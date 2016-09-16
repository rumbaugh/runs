import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys
import pappy
execfile('/home/rumbaugh/git/pappy/CornerPlotterMod.py')

date = '5.14.14'

try:
    maxseasonfrac
except NameError:
    maxseasonfrac=0.75

cadence,slengths = np.zeros(100),np.zeros(100)
for pair in range(1,101):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/Nickrung0_pair%i.txt'%pair)
    ltime = cr[:,0]
    gsb = np.where(ltime[1:]-ltime[:-1] > 30)[0]
    gsb = np.sort(np.append(gsb,gsb+1))
    seasonbounds = np.append(0,np.append(gsb,len(ltime)-1))
    slengths[pair-1] = np.average(ltime[seasonbounds[np.arange(len(seasonbounds)/2)*2+1]]-ltime[seasonbounds[np.arange(len(seasonbounds)/2)*2]])
    diffs = ltime[1:]-ltime[:-1]
    cadence[pair-1] = np.average(diffs[diffs<30])

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
            err_skew = np.abs(tau_hi_err-tau_low_err)
            tmp_stuck = np.zeros(100)
            for i in range(0,100):
                tmp_stuck[i] = np.min((tau_low_err[i],tau_hi_err[i]))
            #perc_stuck = len(tmp_stuck[tmp_stuck<1])/100.
            perc_stuck = len(np.where((tmp_stuck<1) & (tau_abs_sig_dif>5))[0])/100.
            perc_stuck_but_not_impossible =  len(np.where(((tmp_stuck<1) & (tau_abs_sig_dif>5) & (scr[:,2]<maxseasonfrac)))[0])/100.
            
            keys = ('tau','tau_abs_dif','tau_abs_frac_dif','tau_avg_err','err_skew','cadence','season_length')
            ans = (tautmp,tau_abs_dif,tau_abs_sig_dif,tau_avg_err,err_skew,cadence,slengths)
            titles = ('Tau','Abs. Diff.','Frac. Diff.','Avg. Error','Error Skew','Cadence','Season')

            dict_tmp = dict(zip(keys,ans))
            title_dict = dict(zip(keys,titles))
            input_dict = {keys[x]: {'data': ans[x], 'labels': titles[x]} for x in np.arange(len(keys))}
            CornerPlotter(input_dict,outfile='/home/rumbaugh/sim_ltcurve_testing/results/plots/cornerplotter_%s.%s.png'%(cmstr,date),verbose=True)
