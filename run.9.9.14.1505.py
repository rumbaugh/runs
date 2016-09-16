import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
import smoothing_1d as sm

execfile("/home/rumbaugh/radmon_var_chisq_test.py")

execfile('/home/rumbaugh/LoadEVLA_2011.py')
execfile('/home/rumbaugh/LoadVLA_2001.py')

tau_disp = {'0712': -44., '1030': -88.5, '1938': 50.}
mu_disp = {'0712': 1./4.391267, '1030': 1/11.510428, '1938': 0.195245}

for lens in ['1030','0712','1938']:
    if lens == '1938': 
        crS = LoadEVLA_2011('B1938',normalize=True)
        crS['day'] -= crS['day'][0]
        ltime = crS['day']
        rms = crS['rms']
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
        errnames = np.copy(imgnames)
        for n in np.arange(0,len(errnames)): errnames[n] = 'err%s'%errnames[n][4:]
        fluxA1 = crS[imgnames[0]]
        A1err = crS[errnames[0]]
        fluxA2 = crS[imgnames[1]]
        A2err = crS[errnames[1]]
        fluxA = fluxA1+fluxA2
        Aerr = np.sqrt(A1err**2+A2err**2)
        fluxB = crS[imgnames[2]]
        Aflux,Bflux = fluxA,fluxB
        Berr = crS[errnames[2]]
    else:
        
        ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

        Aflux,Bflux = flux_arr[0],flux_arr[1]
        Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

        if lens == '0712': 
            Aflux += Bflux
            Aerr = np.sqrt(Aerr**2+Berr**2)
            Bflux,Berr = flux_arr[2],flux_err_arr[2]

        ltime = (ltime-ltime[0])#/86400
    st = time.time()
    tau,mu = tau_disp[lens],mu_disp[lens]
    g = np.where((Aflux > 0)&(Bflux>0)&(Aerr > 0)&(Berr>0))[0]
    if lens != '1938': g = np.where((Aflux > 0)&(Bflux>0)&(Aerr > 0)&(Berr>0)&(np.arange(len(ltime))<len(ltime)-10))[0]
    gl = np.where(ltime[g]>tau)[0]
    if tau < 0: gl = np.where(ltime[g]<=ltime[g][-1]+tau)[0]
    Aflux_mod = Aflux[g]*mu
    Aerr_mod = Aerr[g]*mu
    ltime_mod = ltime[g]+tau
    Aflux_sm,Avar_sm = sm.interpolate(ltime_mod,Aflux_mod,ltime[g[gl]],y_var=Aerr_mod**2)
    sub_lc = (Aflux_sm-Bflux[g[gl]])/np.mean(Bflux[g[gl]])
    sub_lc_err = np.sqrt(Avar_sm+(Berr[g[gl]])**2)/np.mean(Bflux[g[gl]])
    chisq,prob = calc_chi_sqrd(sub_lc,sub_lc_err,calcprob=True,exp=np.zeros(len(sub_lc)))
    print '%s - %f - %f'%(lens,chisq/len(sub_lc),prob)
    pylab.figure(1)
    pylab.clf()
    pylab.rc('axes',linewidth=2)
    pylab.fontsize = 14
    pylab.tick_params(which='major',length=8,width=2,labelsize=14)
    pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    avg_err = np.mean(sub_lc_err)
    rms_err = np.std(sub_lc)
    pylab.plot(ltime[g[gl]],sub_lc,color='blue',lw=2)
    pylab.errorbar(ltime[g[gl]],sub_lc,sub_lc_err,fmt='ro',lw=1,capsize=3,mew=1,color='blue')
    pylab.scatter(ltime[g[gl]],sub_lc,color='blue')
    xlim = pylab.xlim()
    pylab.plot(np.array(xlim),avg_err*np.ones(2),ls='dotted',c='k',lw=2)
    pylab.plot(np.array(xlim),rms_err*np.ones(2),ls='dashed',c='red',lw=2)
    pylab.plot(np.array(xlim),-avg_err*np.ones(2),ls='dotted',c='k',lw=2)
    pylab.plot(np.array(xlim),-rms_err*np.ones(2),ls='dashed',c='red',lw=2)
    pylab.xlim(xlim)
    pylab.ylim(-4*rms_err,4*rms_err)
    pylab.xlabel('Days',fontsize=14)
    pylab.ylabel('Normalized Flux Difference',fontsize=14)
    pylab.fontsize = 14
    pylab.savefig('/home/rumbaugh/sub_lc.%s.9.9.14.png'%(lens))
