import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys


try:
    date
except NameError:
    date = '2.24.14'

refcr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')

masterFILE = open('/home/rumbaugh/sim_ltcurve_testing/results/master_diftab.VLA_MCMC_%s.dat'%(date),'w')
masterFILE.write('kernel  use cov matrix?  use N_eff?  tau_dif_med  tau_dif_sig  tau_abs_dif_med  tau_abs_dif_sig  tau_sig_dif_med  tau_sig_dif_sig  tau_abs_sig_dif_med  tau_abs_sig_dif_sig  tau_frac_dif_med  tau_frac_dif_sig  tau_abs_frac_dif_med  tau_abs_frac_dif_sig  tau_low_err_med  tau_low_err_sig  tau_hi_err_med  tau_hi_err_sig  tau_avg_err_med  tau_avg_err_sig  tau_low_frac_err_med  tau_low_frac_err_sig  tau_hi_frac_err_med  tau_hi_frac_err_sig  tau_avg_frac_err_med  tau_avg_frac_err_sig\n')
for kernel in ['interp','boxcar']:
    if kernel == 'boxcar': ldate = '2.23.14'
    for use_cov_matrix in [True,False]:
        if use_cov_matrix: 
            cmstr = 'wcovmat'
            if kernel == 'interp': ldate = '2.25.14'
        else:
            cmstr = 'nocovmat'
        for use_Neff in [True,False]:
            if use_Neff: 
                Neffstr = '_Neff'
            else:
                Neffstr = '_noNeff'
            if not use_cov_matrix:
                if ((kernel == 'interp') & (not use_Neff)):
                    ldate = '2.24.14'
                else:
                    ldate = '2.23.14'
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
            FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/diftab.VLA_MCMC_%s_%s%s_%s.dat'%(kernel,cmstr,Neffstr,date),'w')
            FILE.write('#pair tau_dif tau_abs_dif tau_sig_dif tau_abs_sig_dif tau_frac_dif tau_abs_frac_dif\n')
            for pair in range(0,100):
                FILE.write('%3i %10.5f %9.5f %10.5f %9.5f %10.5f %9.5f\n'%(pair+1,tau_dif[pair],tau_abs_dif[pair],tau_sig_dif[pair],tau_abs_sig_dif[pair],tau_frac_dif[pair],tau_abs_frac_dif[pair]))
            FILE.close()
            masterFILE.write('%6s %5s %5s %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f\n'%(kernel,use_cov_matrix,use_Neff,np.median(tau_dif),np.std(tau_dif),np.median(tau_abs_dif),np.std(tau_abs_dif),np.median(tau_sig_dif),np.std(tau_sig_dif),np.median(tau_abs_sig_dif),np.std(tau_abs_sig_dif),np.median(tau_frac_dif),np.std(tau_frac_dif),np.median(tau_abs_frac_dif),np.std(tau_abs_frac_dif),np.median(tautmp-taulbtmp),np.std(tautmp-taulbtmp),np.median(tauubtmp-tautmp),np.std(tauubtmp-tautmp),np.median(0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp))),np.std(0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp))),np.median((tautmp-taulbtmp)/tautmp),np.std((tautmp-taulbtmp)/tautmp),np.median((tauubtmp-tautmp)/tautmp),np.std((tauubtmp-tautmp)/tautmp),np.median((0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)))/tautmp),np.std((0.5*(np.abs(tauubtmp-tautmp)+np.abs(tautmp-taulbtmp)))/tautmp)))
            
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
                plt.hist(dict_tmp[metric])
                plt.title(title_dict[metric])
                plt.rc('axes',linewidth=2)
                plt.fontsize = 14
                plt.tick_params(which='major',length=8,width=2,labelsize=14)
                plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
                plt.text(plt.axis()[0]+0.05*(plt.axis()[1]-plt.axis()[0]),plt.axis()[3]-0.1*(plt.axis()[3]-plt.axis()[2]),'Median: %10.5f\nStd:%10.5f'%(np.median(dict_tmp[metric]),np.std(dict_tmp[metric])))
                plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/hist.%s.VLA_MCMC_%s_%s%s_%s.png'%(metric,kernel,cmstr,Neffstr,date))


masterFILE.close()
