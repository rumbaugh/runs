import numpy as np
import os
os.chdir('/mnt/data2/rumbaugh/VLA/AF377/data')

uvmax = 300
uvmin = 0

dates = ['10.08.00','10.10.00','10.15.00','10.17.00','10.21.00','10.22.00','10.25.00','10.28.00','10.31.00','11.02.00','11.04.00','11.07.00','11.09.00','11.18.00','11.20.00','11.26.00','11.30.00','12.03.00','12.07.00','12.10.00','12.15.00','12.21.00','12.27.00','12.29.00','1.03.01','1.05.01','1.07.01','1.10.01','1.13.01','1.15.01','1.18.01','1.23.01','1.27.01','1.30.01','2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.01.01','3.04.01','3.06.01','3.10.01','3.14.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','3.31.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

aips_dates = np.zeros(len(dates),dtype='|S8')
for i in range(0,len(dates)):
    date = dates[i]
    year,day = date[-2:],date[-5:-3]
    if year == '00':
        month = date[0:2]
    else:
        month = date[0]
    aips_dates[i] = '%02s%02i%2s'%(year,int(month),day)

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573']#,'1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']


FILE=open('/home/rumbaugh/runs/run.5.28.14.1350.sh','w')
FILE.write("#!/bin/csh\n")

opening_string = "difmap << EOF\ninteger mfitniter\nmfitniter = 7\nlogical varpos\nvarpos = false\n"
setup_string = "select I\nmapunits arcsec\nmapsize 256,0.05\n"
#fit_string = "uvrange %i,%i\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\n"%(uvmin,uvmax)
fit_string = "modelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\n"
end_string = "quit\nEOF\n"

for date,aipsdate in zip(dates,aips_dates):
    tsources,tCSOs = np.copy(sources),np.copy(CSOs)
    if date in ['1.15.01','11.20.00','12.07.00']: tsources,tCSOs = ['0414+573'],['1400+621']#,'1030+074','1127+385','0712+472'],['1400+621']
    if date == '4.10.01': tsources = []#['1127+385','0712+472']
    if date in ['11.26.00','12.03.00']: tsources = []#['1030+074','1127+385','1152+199','0712+472']
    if date == '3.06.01': tsources,tCSOs = ['0414+573'],['1400+621']#,'1127+385','0712+472'],['1400+621']
    for source in tsources:
        FILE.write(opening_string)
        uvfile = '/mnt/data2/rumbaugh/AIPS/FITS/AF377_%s_20%s'%(source,aipsdate)
        FILE.write('obs %s\n'%uvfile)
        FILE.write(setup_string)
        #if source == '0414+573':
        #    FILE.write('rmod /mnt/data2/rumbaugh/VLA/AF377/models/prelim_fit.0414+573.5.28.01.mod')
        #else:
        #FILE.write('rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_%s_g.mod\n'%(source[:4]))
        FILE.write('rmod /mnt/data2/rumbaugh/VLA/AF377/models/comp_fit_med_0414+534_g_gauss_A1A2varpos.mod\n')
        #FILE.write('rmod /mnt/data2/rumbaugh/EVLA/11A-138/scripts/model.0414.wgauss2.5.20.14.mod\n')
        FILE.write(fit_string)
        outfile = '/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVT_newpos_med_gauss_5.28.14.%s.A1A2varpos.%s.mod'%(source,date)
        FILE.write('wmod %s\n'%outfile)
        FILE.write(end_string)
FILE.close()
        
        
