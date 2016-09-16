import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

ntrials=10000
rands=rand.random((ntrials,4))

sum1=np.copy(rands[:,0])
g1=np.where(rands[:,1]>=rands[:,0])[0]
sum1[g1]+=rands[:,1][g1]
comptmp=np.copy(rands[:,0])
comptmp[g1]=rands[:,1][g1]
g2=np.where(rands[:,2]>=comptmp)[0]
sum1[g2]+=rands[:,2][g2]

sum2=np.copy(rands[:,1])
g3=np.where(rands[:,2]>=rands[:,1])[0]
sum2[g3]+=rands[:,2][g3]

plt.figure(1)
plt.clf()
plt.scatter(rands[:,0],sum1-sum2,s=2)
plt.axhline(0,color='r',lw=2,ls='dashed')
plt.xlim(0,1)
plt.xlabel('Initial Fish Weight')
plt.ylabel('Advantage in taking first fish (of 3)')

comptmp[g2]=rands[:,2][g2]
g4=np.where(rands[:,3]>=comptmp)[0]
sum1[g4]+=rands[:,3][g4]

comptmp2=np.copy(rands[:,1])
comptmp2[g3]=rands[:,2][g3]
g5=np.where(rands[:,3]>=comptmp2)[0]
sum2[g5]+=rands[:,3][g5]

plt.figure(2)
plt.clf()
plt.scatter(rands[:,0],sum1-sum2,s=2)
plt.axhline(0,color='r',lw=2,ls='dashed')
plt.xlim(0,1)
plt.xlabel('Initial Fish Weight')
plt.ylabel('Advantage in taking first fish (of 4)')
