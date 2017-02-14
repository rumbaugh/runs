import numpy as np

ntrials=10000

draws=np.zeros((15,ntrials))

for Ndup in np.arange(1,16):
    deck=np.arange(30)
    deck[30-Ndup:]=deck[:Ndup]
    drawtrials=np.zeros(ntrials)
    for n in range(0,ntrials):
        tdeck=np.copy(deck)
        np.random.shuffle(tdeck)
        i=Ndup
        while len(np.unique(tdeck[i:]))!=len(tdeck[i:]): i+=1
        drawtrials[n]=i+1
    draws[Ndup-1]=drawtrials
    print '%2i duplicates: %4.1f'%(Ndup,np.mean(draws[Ndup-1]))
