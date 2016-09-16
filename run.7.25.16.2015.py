import numpy as np
import matplotlib.pyplot as plt

z=np.linspace(0,5,5000)
zstep=z[1]-z[0]

Pz=np.exp(-(z-0.46)**2/(2.*0.1**2))+0.5*np.exp(-(z-1.04)**2/(2.*0.3**2))
Pz*=2*np.random.rand(len(z))

Pz/=np.sum(Pz)
zstep=1
zPz=np.sum(z*Pz)*zstep
dz=0.2
zPzd=np.sum((z+dz/(1.+z))*Pz*(1-dz/(1.+z)**2))*zstep
print zPz,zPzd,zPz+dz/(1+zPz)
