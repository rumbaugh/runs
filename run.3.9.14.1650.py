import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt
import sys


try:
    date
except NameError:
    date = '3.9.14'

try:
    maxseasonfrac
except NameError:
    maxseasonfrac=0.75

refcr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nicktruth.txt')
refcr *= -1
scr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/season_lens.txt')
masterFILE = open('/home/rumbaugh/sim_ltcurve_testing/results/master_diftab.VLA_Dispgrid_%s.dat'%(date),'w')
masterFILE.write('tau_dif_med  tau_dif_sig  tau_abs_dif_med  tau_abs_dif_sig  tau_sig_dif_med  tau_sig_dif_sig  tau_abs_sig_dif_med  tau_abs_sig_dif_sig  tau_frac_dif_med  tau_frac_dif_sig  tau_abs_frac_dif_med  tau_abs_frac_dif_sig  tau_low_err_med  tau_low_err_sig  tau_hi_err_med  tau_hi_err_sig  tau_avg_err_med  tau_avg_err_sig  tau_low_frac_err_med  tau_low_frac_err_sig  tau_hi_frac_err_med  tau_hi_frac_err_sig  tau_avg_frac_err_med  tau_avg_frac_err_sig perc_stuck\n')
ldate = '3.7.14'
cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/results/VLA_Dispgrid_%s.dat'%(ldate))
tautmp = cr[:,1]
tau_dif = refcr-tautmp
tau_abs_dif = np.abs(tau_dif)
g = np.where(tau_dif>0)[0]
tau_frac_dif = tau_dif/refcr
tau_abs_frac_dif = np.abs(tau_frac_dif)
FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/test.diftab.VLA_Dispgrid_%s.dat'%(date),'w')
FILE.write('#pair tau_dif tau_abs_dif tau_frac_dif tau_abs_frac_dif\n')
for pair in range(0,100):
    FILE.write('%3i %10.5f %9.5f %10.5f %9.5f\n'%(pair+1,tau_dif[pair],tau_abs_dif[pair],tau_frac_dif[pair],tau_abs_frac_dif[pair]))
FILE.close()
masterFILE.write('%10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f %10.5f\n'%(np.median(tau_dif),np.std(tau_dif),np.median(tau_abs_dif),np.std(tau_abs_dif),np.median(tau_frac_dif),np.std(tau_frac_dif),np.median(tau_abs_frac_dif),np.std(tau_abs_frac_dif)))        
keys = ('tau_dif','tau_abs_dif','tau_frac_dif','tau_abs_frac_dif')
ans = (tau_dif,tau_abs_dif,tau_frac_dif,tau_abs_frac_dif)
titles = ('Difference','Absolute Difference','Fractional Difference','Absolute Fractional Difference')

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
    plt.savefig('/home/rumbaugh/sim_ltcurve_testing/results/plots/test.hist.%s.VLA_Dispgrid_%s.png'%(metric,date))


masterFILE.close()
