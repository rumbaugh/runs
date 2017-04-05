import numpy as np

steps_arr=np.zeros(100)
nsteps_arr=np.arange(13,0,-1)
for n in range(1,14):
    steps_arr[np.sum(nsteps_arr[:n-1]):]+=1
    for i in range(0,nsteps_arr[n-1]):
        steps_arr[np.sum(nsteps_arr[:n-1])+i]+=1

floors=np.random.randint(0,100,10000)
expval=np.average(steps_arr[floors])
