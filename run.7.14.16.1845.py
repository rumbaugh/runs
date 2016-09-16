import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
patches = []

region1x = [1.21, 1.21, 0.9, 1.06]
region1y = [4.2, -2.5, -2.5, 6.05]
region2x = [1.06, 1.26,1.47,1.21]
region2y = [6.05,9.6, 3.6, 4.2]
region3x = [1.38, 1.26, 1.61]
region3y = [4.3, 9.6, 1.95]
region4x = [1.38,1.72, 1.5]
region4y = [5.3, 1.3, 1.8]

q=np.zeros((4,2))
q[:,0]=region1x
q[:,1]=region1y
patches.append(Polygon(q))
q=np.zeros((4,2))
q[:,0]=region2x
q[:,1]=region2y
patches.append(Polygon(q))
q=np.zeros((3,2))
q[:,0]=region3x
q[:,1]=region3y
patches.append(Polygon(q))
q=np.zeros((3,2))
q[:,0]=region4x
q[:,1]=region4y
patches.append(Polygon(q))

p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
colors=np.array([43,15,75,90])
p.set_array(np.array(colors))

ax.add_collection(p)

#plt.show()

plt.scatter([0],[1],color=(0.1588235294117647, 1.0,1),s=256,edgecolors='None',alpha=0.4,marker='s',label='0-0.1 Gyr')
plt.scatter([0],[6.5],color=(0.3, 0.3,0.96737967914438499),s=256,edgecolors='None',alpha=0.4,marker='s',label='0.1-0.5 Gyr')
plt.scatter([0],[4.94],color='orange',s=256,edgecolors='None',alpha=0.4,marker='s',label='0.5-1 Gyr')
plt.scatter([0],[2.5],color=(1,0.2,0),s=256,edgecolors='None',alpha=0.4,marker='s',label='1-3 Gyr')

plt.xlim(0.95,1.7)
plt.ylim(-2.3,10)

plt.legend(loc='upper right',scatterpoints=1)

