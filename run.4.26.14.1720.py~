import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

days4months_dict  = {5: 28, 4: 28+30, 3: 28+30+31, 2: 28+30+31+28, 1: 28+30+31+28+31, 12: 28+30+31+28+31+31, 11: 28+30+31+28+31+31+30, 10: 28+30+31+28+31+31+30+31}

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

for source in sources:
    tdates = np.array(np.copy(dates))
    gdel = np.zeros(0,dtype='int')
    if source == '0414+573':
        gdel = np.where((tdates == '4.10.01') | (tdates == '11.26.00') | (tdates == '12.03.00'))[0]
        #tdates = np.delete(tdates,gdel)
    elif source == '1030+074':
        gdel = np.where((tdates == '4.10.01') | (tdates == '3.06.01'))[0]
        #tdates = np.delete(tdates,gdel)
    elif source == '1152+199':
        gdel = np.where((tdates == '1.15.01') | (tdates == '11.20.00') | (tdates == '12.07.00') | (tdates == '4.10.01') | (tdates == '3.06.01'))[0]
        #tdates = np.delete(tdates,gdel)
    FILE = open('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_%s.dat'%source,'w')
    for date in tdates:
        if date[1] == '.':
            month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
        else:
            month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
        daytot = 2058-days4months_dict[month]+day
        #if date not in ['3.06.01','3.16.01','4.10.01']:
        if date not in tdates[gdel]:
            FILE.write('%f'%daytot)
            cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!')
            num_img = np.shape(cr)[0]
            for img in range(0,num_img):
                fluxstr = cr[img][0]
                FILE.write(' ' + fluxstr[:len(fluxstr)-1])
            FILE.write('\n')
        else:
            FILE.write('%f'%daytot)
            if source in ['0414+573','0712+472']: num_img = 4
            else: num_img = 2
            for img in range(0,num_img):
                FILE.write(' 0.')
            FILE.write('\n')
    FILE.close()
for source in np.append(CSOs,'1035+564'):
    tdates = np.array(np.copy(dates))
    if source == '1244+408':
        gdel = np.where((tdates == '10.08.00') | (tdates == '1.15.01') | (tdates == '11.20.00') | (tdates == '12.07.00') | (tdates == '3.06.01'))[0]
        #tdates = np.delete(tdates,gdel)
    FILE = open('/home/rumbaugh/EVLA/light_curves/VLA_lc_aipsredux_LR_4.14.14_%s.dat'%source,'w')
    for date in tdates:
        if date[1] == '.':
            month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
        else:
            month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
        daytot = 2058-days4months_dict[month]+day
        #if date not in ['3.06.01','3.16.01','4.10.01']:
        if date not in tdates[gdel]:
            FILE.write('%f'%daytot)
            cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!')
            fluxstr = cr[0]
            FILE.write(' ' + fluxstr[:len(fluxstr)-1])
            FILE.write('\n')
        else:
            FILE.write('%f 0.\n'%daytot)
    FILE.close()
            
            
