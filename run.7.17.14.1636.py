import numpy as np
import time

st = time.time()
a = np.random.normal(size=100000000)
end1 = time.time()
print 'Random numbers generated. Elapsed time: %f seconds'%(end1-st)
st2=time.time()
i=0
for j in range(0,40000000):
    i += 1
end2 = time.time()
print 'Loop ended. Elapsed time: %f seconds'%(end2-st2)
