import numpy as np
x=np.linspace(0.5,1.5,1000)
A=1-1.925*(x-0.66)
A[x<0.66],A[x>1.18]=1,0
B=1-A
plot(x,A)
plot(x,B)
#-2.5 log[A 10**(-mr/2.5) + B 10**(-mi/2.5)]
