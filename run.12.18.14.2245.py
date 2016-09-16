import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text

tan = '#CC9900'

#plt.figure(figsize=(7,3))
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

B0218 = {'tau': 11.46, 'err': 0.16}
biggs = {'tau': 10.5, 'err': 0.2}
cohen = {'tau': 10.1, 'err':0.8}


plt.xlim(9.,12.0)
plt.ylim(0,4)

ax1=plt.axes(frameon=False)
ax1.axes.get_xaxis().tick_bottom()
ax1.axes.get_yaxis().set_visible(False)

plt.xlim(9.,12.0)
plt.ylim(0,4)
#xmin, xmax = ax1.get_xaxis().get_view_interval()
#ymin, ymax = ax1.get_yaxis().get_view_interval()
xmin,xmax,ymin,ymax = 9.,12.,0.,4.
ax1.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

plt.errorbar([B0218['tau']],[0.5],xerr=[B0218['err']],c=tan,lw=4,capsize=6,capthick=2,fmt='--o')
plt.errorbar([cohen['tau']],[1.25],xerr=[cohen['err']],c=tan,lw=4,capsize=6,capthick=2,fmt='--o')
plt.errorbar([biggs['tau']],[2.],xerr=[biggs['err']],c=tan,lw=4,capsize=6,capthick=2,fmt='--o')

plt.text(B0218['tau']-B0218['err']-0.9,0.5-0.05,'Cheung et al. (2014)')
plt.text(cohen['tau']+cohen['err']+0.1,1.25-0.05,'Cohen et al. (2000)')
plt.text(biggs['tau']+biggs['err']+0.1,2.-0.05,'Biggs et al. (1999)')

plt.xlabel('B0218 Time Delay (days)')


plt.savefig('/home/rumbaugh/B0218_TD_comp_plot.ps')
plt.savefig('/home/rumbaugh/B0218_TD_comp_plot.png')
