import math as m
import numpy as np
import matplotlib
import matplotlib.pylab as pylab

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'


cr = read_file('/home/rumbaugh/FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat')
id = get_colvals(cr,'col1')
RA = get_colvals(cr,'col4')
Dec = get_colvals(cr,'col5')
z = get_colvals(cr,'col9')
flag = get_colvals(cr,'col11')

gf = np.where(flag > 2.2)
gf = gf[0]


pylab.xlim(138,137)
pylab.ylim(54.2,54.55)
pylab.xlabel('RA')
pylab.ylabel('Dec')
pylab.title('Zoomed In')
gp0 = np.where((z[gf] > 1) & (z[gf] < 1.5))
pylab.scatter(RA[gf[gp0]],Dec[gf[gp0]],s=8)

gp1 = np.where((z[gf] > 1.12) & (z[gf] < 1.145))
pylab.scatter(RA[gf[gp1]],Dec[gf[gp1]],s=10,color='red')
pylab.savefig('/home/rumbaugh/testmap.0910.z_1.13.ps')
pylab.close('all')

pylab.xlim(138,137)
pylab.ylim(54.2,54.6)
pylab.xlabel('RA')
pylab.ylabel('Dec')
pylab.title('Zoomed Out')
gp0 = np.where((z[gf] > 1) & (z[gf] < 1.5))
pylab.scatter(RA[gf],Dec[gf],s=8)
gp2 = np.where((z[gf] > 0.41) & (z[gf] < 0.45))
pylab.scatter(RA[gf[gp2]],Dec[gf[gp2]],s=10,color=html_teal)
gp3 = np.where((z[gf] > 0.51) & (z[gf] < 0.55))
pylab.scatter(RA[gf[gp3]],Dec[gf[gp3]],s=10,color='blue')
gp4 = np.where((z[gf] > 0.55) & (z[gf] < 0.58))
pylab.scatter(RA[gf[gp4]],Dec[gf[gp4]],s=10,color=html_brwn)
gp5 = np.where((z[gf] > 0.75) & (z[gf] < 0.85))
pylab.scatter(RA[gf[gp5]],Dec[gf[gp5]],s=10,color='red')
gp6 = np.where((z[gf] > 0.87) & (z[gf] < 0.95))
pylab.scatter(RA[gf[gp6]],Dec[gf[gp6]],s=10,color=html_orng)
leg = pylab.legend(('all','0.43','0.52','0.56','0.8','0.91'),loc=4,markerscale=0.8,labelspacing=0.3)
pylab.savefig('/home/rumbaugh/testmap.0910.z_all.ps')
pylab.close('all')
