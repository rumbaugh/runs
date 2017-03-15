import numpy as np

def coordtest(ntrials,d=0.1,ra0=33.2532,dec0=0.21414):
    d/=3600.
    ras,decs=np.random.normal(ra0,d,2*ntrials),np.random.normal(dec0,d,2*ntrials)

    dists=SphDist(ras[:ntrials],decs[:ntrials],ras[ntrials:],decs[ntrials:])

    return 60*dists
