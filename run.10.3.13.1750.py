import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

dates = ['2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.06.01','3.14.01','3.16.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']


FILE=open('/home/rumbaugh/runs/run.10.3.13.1750.sh','w')
FILE.write("#!/bin/csh\n")

opening_string = "difmap << EOF\ninteger mfitniter\nmfitniter = 7\nlogical varpos\nvarpos = false\n"
setup_string = "select I\nmapunits arcsec\nmapsize 256,0.05\n"
fit_string = "modelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false, 60\nmodelfit mfitniter\n"
end_string = "quit\nEOF\n"

for date in dates:
    for source in sources:
        FILE.write(opening_string)
        uvfile = '/mnt/data3/rumbaugh/VLA/AF377/data/af377_%s.%s.uvfits'%(date,source)
        FILE.write('obs %s\n'%uvfile)
        FILE.write(setup_string)
        FILE.write('rmod /mnt/data3/rumbaugh/VLA/AF377/models/prelim_fit.%s.5.28.01.mod\n'%source)
        FILE.write(fit_string)
        outfile = '/mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.%s.fixpos.%s.mod'%(source,date)
        FILE.write('wmod %s\n'%outfile)
        FILE.write(end_string)
    for source in CSOs:
        FILE.write(opening_string)
        uvfile = '/mnt/data3/rumbaugh/VLA/AF377/data/af377_%s.%s.uvfits'%(date,source)
        FILE.write('obs %s\n'%uvfile)
        FILE.write(setup_string)
        FILE.write('addcmp 0.1,true,0,0,varpos\n')
        FILE.write(fit_string)
        outfile = '/mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.%s.fixpos.%s.mod'%(source,date)
        FILE.write('wmod %s\n'%outfile)
        FILE.write(end_string)
FILE.close()
        
        
