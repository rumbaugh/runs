import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

true_len,true_CKP_perc,ntrials,ndraw,nAGN,convfrac=50,.5,10000,18,10,0.3
true_CKP=int(true_len*true_CKP_perc)
a1=np.arange(0,true_len/2*5,5)
a2=np.arange((true_len-true_CKP)/2*5,(true_len-true_CKP/2)*5,5)+1
a=np.sort(np.append(a1,a2))
a=np.append(np.zeros(int(true_len*(1-true_CKP_perc))),np.ones(int(0.5*true_len*true_CKP_perc)))

CKPtests=np.zeros(ntrials)
CKPfracs=np.zeros(ntrials)
AGNtests=np.zeros(ntrials)
for i in range(0,ntrials):
    atmp=np.sort(rand.choice(a,ndraw,replace=False))
    test=rand.rand(len(atmp[atmp==1]))
    nAGNtmp=len(test[test<convfrac])
    atmp=np.append(np.zeros(len(atmp)-nAGNtmp),np.ones(2*nAGNtmp))
    #mintmp=np.ones((ndraw,2))*99
    #mintmp[:-1,0],mintmp[1:,1]=atmp[1:]-atmp[:-1],atmp[1:]-atmp[:-1]
    #mintmp=np.min(mintmp,axis=1)
    #gkAGN=np.where(mintmp==1)[0]
    #dtmp=np.zeros(ndraw)
    #dtmp[gkAGN]=1
    #CKPtests[i]=2*np.sum(atmp[1:]-atmp[:-1]==1)
    AGNtmp=rand.choice(atmp,nAGN,replace=False)
    AGNtests[i]=np.sum(AGNtmp)
    CKPtests[i]=np.sum(atmp)
    CKPfracs[i]=np.sum(atmp)*1./len(atmp)
plt.figure(1)
plt.clf()
plt.hist(CKPfracs,range=(0,0.45),bins=15)

plt.figure(2)
plt.clf()
plt.hist(AGNtests,range=(0,15),bins=15)

print np.mean(CKPtests),np.median(CKPtests),np.std(CKPtests),0.5*(np.sort(CKPtests)[int(0.84*ntrials)]-np.sort(CKPtests)[int(0.16*ntrials)])
print np.mean(CKPfracs),np.median(CKPfracs),np.std(CKPfracs),0.5*(np.sort(CKPfracs)[int(0.84*ntrials)]-np.sort(CKPfracs)[int(0.16*ntrials)])
print np.mean(AGNtests),np.median(AGNtests),np.std(AGNtests),0.5*(np.sort(AGNtests)[int(0.84*ntrials)]-np.sort(AGNtests)[int(0.16*ntrials)])
