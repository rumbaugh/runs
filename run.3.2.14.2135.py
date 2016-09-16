import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys


try:
    date
except NameError:
    date = '3.2.14'

try:
    maxseasonfrac
except NameError:
    maxseasonfrac=0.75

refcr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')
scr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/season_lens.txt')
masterFILE = open('/home/rumbaugh/sim_ltcurve_testing/results/master_diftab.VLA_MCMC_%s.dat'%(date),'w')
masterFILE.write('kernel  use cov matrix?  use N_eff?  tau_dif_med  tau_dif_sig  tau_abs_dif_med  tau_abs_dif_sig  tau_sig_dif_med  tau_sig_dif_sig  tau_abs_sig_dif_med  tau_abs_sig_dif_sig  tau_frac_dif_med  tau_frac_dif_sig  tau_abs_frac_dif_med  tau_abs_frac_dif_sig  tau_low_err_med  tau_low_err_sig  tau_hi_err_med  tau_hi_err_sig  tau_avg_err_med  tau_avg_err_sig  tau_low_frac_err_med  tau_low_frac_err_sig  tau_hi_frac_err_med  tau_hi_frac_err_sig  tau_avg_frac_err_med  tau_avg_frac_err_sig perc_stuck perc_stuck&possible\n')
for kernel in ['interp','boxcar']:
    if kernel == 'boxcar': 
        ldate = '2.23.14'
    else:
        ldate = '2.26.14'
    for use_cov_matrix in [True,False]:
        if use_cov_matrix: 
            cmstr = 'wcovmat'
        else:
            cmstr = 'nocovmat'
        for use_Neff in [True,False]:
            if use_Neff: 
                Neffstr = '_Neff'
            else:
                Neffstr = '_noNeff'
            cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/results/VLA_MCMC_%s_%s%s_%s.dat'%(kernel,cmstr,Neffstr,ldate))
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
            FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/diftab.VLA_MCMC_%s_%s%s_%s.dat'%(kernel,cmstr,Neffstr,date),'w')
            FILE.write('#pair tau_dif tau_abs_dif tau_sig_dif tau_abs_sig_dif tau_frac_dif tau_abs_frac_dif\n')
            for pair in range(0,100):
                FILE.write('%3i %10.5f %9.5f %10.5f %9.5f %10.5f %9.5f\n'%(pair+1,tau_dif[pair],tau_abs_dif[pair],tau_sig_dif[pair],tau_abs_sig_dif[pair],tau_frac_dif[pair],tau_abs_frac_dif[pair]))
            FILE.close()
            masterFILE.write('%6s %5s %5s %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %4.2f %4.2f\n'%(kernel,use_cov_matrix,use_Neff,np.median(tau_dif),np.std(tau_dif),np.median(tau_abs_dif),np.std(tau_abs_dif),np.median(tau_sig_dif),np.std(tau_sig_dif),np.median(tau_abs_sig_dif),np.std(tau_abs_sig_dif),np.median(tau_frac_dif),np.std(tau_frac_dif),np.median(tau_abs_frac_dif),np.std(tau_abs_frac_dif),np.median(tautmp-taulbtmp),np.std(tautmp-taulbtmp),np.median(tauubtmp-tautmp),np.std(tauubtmp-tautmp),np.median(0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp))),np.std(0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp))),np.median((tautmp-taulbtmp)/tautmp),np.std((tautmp-taulbtmp)/tautmp),np.median((tauubtmp-tautmp)/tautmp),np.std((tauubtmp-tautmp)/tautmp),np.median((0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)))/tautmp),np.std((0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)))/tautmp),perc_stuck,perc_stuck_but_not_impossible))
            
            keys = ('tau_dif','tau_abs_dif','tau_sig_dif','tau_abs_sig_dif','tau_frac_dif','tau_abs_frac_dif','tau_low_err','tau_hi_err','tau_avg_err','tau_low_frac_err','tau_hi_frac_err','tau_avg_frac_err')
            ans = (tau_dif,tau_abs_dif,tau_sig_dif,tau_abs_sig_dif,tau_frac_dif,tau_abs_frac_dif,tau_low_err,tau_hi_err,tau_avg_err,tau_low_frac_err,tau_hi_frac_err,tau_avg_frac_err)
            titles = ('Difference','Absolute Difference','Difference (sigma)','Absolute Difference (sigma)','Fractional Difference','Absolute Fractional Difference','Lower Error','High Error','Average Error','Lower Fractional Error','High Fractional Error','Average Fractional Error')

            dict_tmp = dict(zip(keys,ans))
            title_dict = dict(zip(keys,titles))
            for metric in dict_tmp:
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
                plt.hist(dict_tmp[metric],bins=nbins,range=trange)
                plt.title(title_dict[metric])
                plt.rc('axes',linewidth=2)
                plt.fontsize = 14
                plt.tick_params(which='major',length=8,width=2,labelsize=14)
                plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
                plt.text(plt.axis()[0]+0.05*(plt.axis()[1]-plt.axis()[0]),plt.axis()[3]-0.1*(plt.axis()[3]-plt.axis()[2]),'Median: %10.5f\nStd:%10.5f'%(np.median(dict_tmp[metric]),np.std(dict_tmp[metric])))
                plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/hist.%s.VLA_MCMC_%s_%s%s_%s.png'%(metric,kernel,cmstr,Neffstr,date))
                if metric == 'tau_abs_dif':
                    sm_err_only = tau_abs_dif[tau_avg_err < 10]
                    plt.figure(1)
                    plt.rc('axes',linewidth=2)
                    plt.fontsize = 14
                    plt.tick_params(which='major',length=8,width=2,labelsize=14)
                    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
                    plt.clf()
                    plt.hist(sm_err_only,bins=nbins,range=trange)
                    plt.title(title_dict[metric])
                    plt.rc('axes',linewidth=2)
                    plt.fontsize = 14
                    plt.tick_params(which='major',length=8,width=2,labelsize=14)
                    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
                    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/hist.%s.sm_err_only.VLA_MCMC_%s_%s%s_%s.png'%(metric,kernel,cmstr,Neffstr,date))
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
            plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/plot.tau_abs_dif_vs_tau_avg_err.VLA_MCMC_%s_%s%s_%s.png'%(kernel,cmstr,Neffstr,date))


masterFILE.close()
