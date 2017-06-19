import numpy as np
import time
import carmcmc as cm
nsamples=20000
try:
    ntrials
except NameError:
    ntrials=10

times=np.random.uniform(50000,56000,200)
y=np.random.normal(19,0.1,200)
yerr=np.random.uniform(0.01,0.03,200)
y+=np.random.normal(0,yerr)

st=time.time()
for i in range(0,ntrials):
    DRWmodel=cm.CarmaModel(times,y,yerr,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsamples)
    lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
end=time.time()
print (end-st)/ntrials
