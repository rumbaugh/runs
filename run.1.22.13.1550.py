import numpy as np
import time
import math as m

sample = np.random.randint(0,100,100000)

st1 = time.time()
test = np.zeros(0)
for i in range(0,len(sample)-1):
    if (sample[i] > 90): test = np.append(test,m.sqrt(sample[i]+sample[i+1]))
end1 = time.time()
print 'Time 1: %f seconds'%(end1-st1)
st2 = time.time()
test = np.zeros(0)
g = np.where(sample[:len(sample)-1] > 90)
g = g[0]
for i in range(0,len(g)): test = np.append(test,m.sqrt(sample[g[i]]+sample[g[i]+1]))
end2 = time.time()
print 'Time 2: %f seconds'%(end2-st2)
