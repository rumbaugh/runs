%matplotlib inline
import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pyplot as plt
import emcee

import carmcmc as cm
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

execfile('/home/rumbaugh/MCMC_delaylnprob.py')

oneminussigma = 0.317310507863
try:
    justone
except NameError:
    justone = False
try:
    timestep
except NameError:
    timestep = 0.5
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

try:
    lens
except NameError:
    lens = '1030'

date = '12.11.14'

try:
    runs
except NameError:
    runs = 10

try:
    ntrials
except NameError:
    ntrials=10

execfile("/home/rumbaugh/LoadVLA_2001.py")

for lens in ['1030']:
    mu_trials,tau_trials,mu_err_trials,tau_err_trials = np.zeros(ntrials),np.zeros(ntrials),np.zeros(ntrials),np.zeros(ntrials)

    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

    if lens == '0712': 
        Aflux += Bflux
        Aerr = np.sqrt(Aerr**2+Berr**2)
        Bflux,Berr = flux_arr[2],flux_err_arr[2]

    st = time.time()
    ltime = (ltime-ltime[0])#/86400
#find time delays
    g = np.arange(len(ltime))[:len(ltime)-10]
    cadence=ltime[g[1:]]-ltime[g[:-1]]
    A_avg,B_avg,Aerr_avg,Berr_avg=np.average(Aflux[g]),np.average(Bflux[g]),np.average(Aerr[g]),np.average(Berr[g])

    model = cm.CarmaModel(ltime[g],Aflux[g],Aerr[g],p=6,q=0)
    %%capture capt
    sample = model.ruun_mcmc(runs)
    sample.assess_fit()
