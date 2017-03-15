import numpy as np
try:
    ntrials
except NameError:
    ntrials=10000

ra0,dec0=33.2532,0.21414

ras,decs=np.random.normal(ra0,0.1/3600,2*ntrials),np.random.normal(dec0,0.1/3600,2*ntrials)

dists=SphDist(ras[:ntrials],decs[:ntrials],ras[ntrials:],decs[ntrials:])

