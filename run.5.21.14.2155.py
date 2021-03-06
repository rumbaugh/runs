import numpy as np
import matplotlib.pylab as plt
source = '0414+573'

fluxes = {'A1': '0.188723v', 'A2': '0.167714v', 'B': '0.0719444v', 'C': '0.0269058v'}

dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

Adates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01']
Bdates = ['2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

Bcutoff = 2025-1839.

days4months_dict  = {5: 28, 4: 28+30, 3: 28+30+31, 2: 28+30+31+28, 1: 28+30+31+28+31, 12: 28+30+31+28+31+31, 11: 28+30+31+28+31+31+30, 10: 28+30+31+28+31+31+30+31}

tdates = np.array(np.copy(dates))
gdel = np.zeros(0,dtype='int')
gdel = np.where((tdates == '4.10.01') | (tdates == '11.26.00') | (tdates == '12.03.00'))[0]
FILE = open('/mnt/data2/rumbaugh/VLA/AF377/models/comp_fit_%s_g.mod','w')
imgnames = ['A1','A2','B','C']
rads,thetas = {x: np.zeros(0) for x in imgnames},{x: np.zeros(0) for x in imgnames}
Arads,Athetas = {x: np.zeros(0) for x in imgnames},{x: np.zeros(0) for x in imgnames}
Brads,Bthetas = {x: np.zeros(0) for x in imgnames},{x: np.zeros(0) for x in imgnames}
for date in tdates:
    if date[1] == '.':
        month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
    else:
        month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
    daytot = 2058-days4months_dict[month]+day
        #if date not in ['3.06.01','3.16.01','4.10.01']:
    if date not in tdates[gdel]:
        cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVT_varpos_5.21.14.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!',usecols=(0,1,2))
        for img,j in zip(imgnames,np.arange(4)):
            rads[img] = np.append(rads[img],float(cr[:,1][j][:-1]))
            thetas[img] = np.append(thetas[img],float(cr[:,2][j][:-1]))
            if date in Adates:
                Arads[img] = np.append(Arads[img],float(cr[:,1][j][:-1]))
                Athetas[img] = np.append(Athetas[img],float(cr[:,2][j][:-1]))
            if date in Bdates:
                Brads[img] = np.append(Brads[img],float(cr[:,1][j][:-1]))
                Bthetas[img] = np.append(Bthetas[img],float(cr[:,2][j][:-1]))
for img in imgnames:
    rad,theta = np.mean(rads[img]),np.mean(thetas[img])
    FILE.write('%s   %f   %f\n'%(fluxes[img],rad,theta))


    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    X,Y = rads[img]*np.sin(np.pi/180.*thetas[img]),rads[img]*np.cos(np.pi/180.*thetas[img])
    AX,AY = Arads[img]*np.sin(np.pi/180.*Athetas[img]),Arads[img]*np.cos(np.pi/180.*Athetas[img])
    BX,BY = Brads[img]*np.sin(np.pi/180.*Bthetas[img]),Brads[img]*np.cos(np.pi/180.*Bthetas[img])
    plt.scatter(X,Y,c='k',s=5)
    plt.scatter(AX,AY,c='b',s=12)
    plt.scatter(BX,BY,c='r',s=12)
    plt.title('%s'%img)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/varpos_fits_positions_0414_%s.VLA_2001.5.21.14.png'%img)
FILE.close()
