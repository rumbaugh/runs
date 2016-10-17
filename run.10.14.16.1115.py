import numpy as np
import numpy.random as rand

def gametrial(ntrials=10000,seed=None,verbose=True):
    if np.shape(seed)==():
        seed=rand.randint(1,10001,3)
    if verbose: print seed
    rolls=rand.randint(1,7,(ntrials,10000))
    hits=np.cumsum(rolls,axis=1)
    wins=np.in1d(hits,seed).reshape((ntrials,10000))
    swins=np.sum(wins,axis=1)
    winperc=np.sum(swins>0)*1./ntrials
    return winperc

    
