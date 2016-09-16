import carmcmc as cm
import numpy as np
import matplotlib.pyplot as plt

def setup_t(ny,dt_low,dt_hi):
    t=np.zeros(ny)
    dt=np.random.uniform(dt_low,dt_hi,ny)
    t=np.cumsum(dt)
    t-=t[0]
    return t


def exp_carmapack(t,lag=0,mu=1.,sigmay=2.3,p=5,mn=17.,qpo_width=np.array([1.0/100.0, 1.0/300.0, 1.0/200.0]),qpo_cent=np.array([1.0/5.0, 1.0/25.0]),ma_coefs=np.array([1.0, 4.5, 1.25, 0.0, 0.0])):
    # set the CARMA model parameters
    #sigmay = 2.3  # dispersion in the time series
    #p = 5  # order of the AR polynomial
    #mu = 17.0  # mean of the time series
    #qpo_width = np.array([1.0/100.0, 1.0/300.0, 1.0/200.0])  # widths of of Lorentzian components
    #qpo_cent = np.array([1.0/5.0, 1.0/25.0])  # centroids of Lorentzian components
    ar_roots = cm.get_ar_roots(qpo_width, qpo_cent) # compute the roots r_k from the Lorentzian function parameters
    ar_coefs = np.poly(ar_roots)
    #ma_coefs = np.array([1.0, 4.5, 1.25, 0.0, 0.0])
    # convert CARMA model variance to variance in the driving white noise
    sigsqr = sigmay ** 2 / cm.carma_variance(1.0, ar_roots, ma_coefs=ma_coefs)  # carma_variance computes the autcovariance function
    plt.clf()
    if lag == 0:
        y = mn + cm.carma_process(t,sigsqr,ar_roots,ma_coefs=ma_coefs)
    else:
        t2=t+lag
        t_comb = np.append(t,t2)
        g_sort = np.argsort(t_comb)
        print np.min(t_comb[g_sort[1:]]-t_comb[g_sort[:-1]])
        flags_arr = np.append(np.zeros(len(t)),np.ones(len(t2)))[g_sort]
        g_t,g_t2 = np.where(flags_arr==0)[0],np.where(flags_arr==1)[0]
        cmp_tmp=mn+cm.carma_process(t_comb[g_sort],sigsqr,ar_roots,ma_coefs=ma_coefs)
        #print t_comb[g_sort],t_comb[g_sort][g_t],t_comb[g_sort][g_t2],cmp_tmp
        #print cmp_tmp
        print isnan(np.sum(cmp_tmp))
        #y,y2=cmp_tmp[:len(t)],mu*cmp_tmp[len(t):]
        y,y2=cmp_tmp[g_t],mu*cmp_tmp[g_t2]
        plt.plot(t,y2,'k')
        plt.plot(t,y2,'r.')
    plt.plot(t,y,'k')
    plt.plot(t,y,'b.')
    plt.xlabel('Time')
    plt.ylabel('CARMA(5,3) Process')
    plt.xlim(0, t.max())
