import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import time

st = time.time()

try:
    runs
except NameError:
    runs = 10

try:
    date
except NameError:
    date = '4.15.14'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.5

execfile('/home/rumbaugh/MCMC_delaylnprob.py')
execfile('/home/rumbaugh/set_TDC_dict.py')

def runtemplate(base,rung):
    commonbase = 'tdc1_rung'
    basenames = np.array(['double_pair20','double_pair30','double_pair32','double_pair34','double_pair38','double_pair40','double_pair50','quad_pairA','quad_pairB'])
    basenums = np.array([1,1,1,1,1,1,1,6,6])

    basenames_dict = {'double_pair20': 1,'double_pair30': 1,'double_pair32': 1,'double_pair34': 1,'double_pair38': 1,'double_pair40': 1,'double_pair50': 1,'quad_pairA': 6,'quad_pairB': 6}
    pair = '%s%i_%s%i'%(commonbase,rung,base,basenames_dict[base]+rung)
    if basenames_dict[base] == 6: pair = '%s%i_%s%i%s'%(commonbase,rung,base[:len(base)-1],basenames_dict[base]+rung,base[len(base)-1])
    mintime,maxtime = ref_dict['rung'][rung][pair]['range'][0],ref_dict['rung'][rung][pair]['range'][1]
    cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/%s.txt'%(rung,pair))
    ltime,A,B,Aerr,Berr = cr[:,0],cr[:,1],cr[:,3],cr[:,2],cr[:,4]
    tau_init,mu_init = 0.5*(mintime+maxtime),np.mean(B)/np.mean(A)
    gsb = np.where(ltime[1:]-ltime[:-1] > 30)[0]
    gsb = np.sort(np.append(gsb,gsb+1))
    seasonbounds = np.append(0,np.append(gsb,len(ltime)-1))
    ndim,nwalkers = 2,10
    #if group > 0:
    #    crl = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/emcee/%s.emcee_output_full_chain.%s.dat'%(rung,pair,date))
    #    p0 = crl[np.shape(crl)[0]-10:,:]
    #else:
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[B,A,Berr,Aerr,ltime,mu_init,mintime,maxtime,False,True,True,'boxcar',10.,0.5,seasonbounds])
    #pos,prob,state=sampler.run_mcmc(p0,runs)
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    #tau_sort = np.sort(sampler.flatchain[:,0])
    FILE = open('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/emcee/%s.emcee_output_full_chain.%s.dat'%(rung,pair,date),'w')
#for i in range(0,len(tau_sort)): FILE.write(str(sampler.flatchain[:,0][i]) + '\n')
    for i in range(0,runs):
        for j in range(0,nwalkers):
            FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
    FILE.close()
    print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)

rungs=np.array([0,1,2,3,4])
pairs=np.array(['double_pair20','double_pair30','double_pair32','double_pair34','double_pair38','double_pair40','double_pair50','quad_pairA','quad_pairB'])
st = time.time()
for rung in rungs:
    for pair in pairs[0:1]:
        runtemplate(pair,rung)
        print 'Rung %i finished\nElapsed Time: %f seconds'%(rung,time.time()-st)
