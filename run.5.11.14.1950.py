import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import time

date = '5.11.14'
ldate = '4.21.14'

quads = np.arange(158)+1
quadsA,quadsB = np.zeros(len(quads),dtype='|S4'),np.zeros(len(quads),dtype='|S4')
for q in range(0,len(quads)):
    quadsA[q],quadsB[q] = str(quads[q])+'A',str(quads[q])+'B'
quads = np.array([y for x in zip(quadsA,quadsB) for y in x])

noquads = ['11A','11B','15A','15B','67A','67B','94A','94B','126A','126B','138A','138B']

rungs=np.array([0,1,2,3,4])
st = time.time()
for rung in rungs:
    FILE = open('/mnt/data2/rumbaugh/TDC/tdc1/results/results.tdc1.rung%i.%s.dat'%(rung,date),'w')
    commonbase = 'tdc1_rung'
    ltype = 'double'
    for pair in np.arange(1,721):
        spair = '%s%i_%s_pair%i'%(commonbase,rung,ltype,pair)
        cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1/rung%i/emcee/%s.emcee_output_full_chain.nocovmat.%s.dat'%(rung,spair,ldate))
        tau = np.sort(cr[:,0])
        tau_med,tau_LB,tau_UB = np.median(tau),tau[int(0.31731*0.5*len(tau))],tau[int((1-0.31731*0.5)*len(tau))]
        FILE.write('%4i %6.2f %6.2f %6.2f\n'%(pair,tau_med,tau_LB,tau_UB))
    ltype = 'quad'
    for quad in quads:
        if not(quad in noquads): 
            spair = '%s%i_%s_pair%s'%(commonbase,rung,ltype,quad)
            cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1/rung%i/emcee/%s.emcee_output_full_chain.nocovmat.%s.dat'%(rung,spair,ldate))
            tau = np.sort(cr[:,0])
            tau_med,tau_LB,tau_UB = np.median(tau),tau[int(0.31731*0.5*len(tau))],tau[int((1-0.31731*0.5)*len(tau))]
            FILE.write('%4s %6.2f %6.2f %6.2f\n'%(quad,tau_med,tau_LB,tau_UB))

