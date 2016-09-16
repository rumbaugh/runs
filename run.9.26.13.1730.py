import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

try:
    startind
except NameError:
    sys.exit("Set startind")
startind = 9*(startind)

dates = ['2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.06.01','3.14.01','3.16.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

calDict = {'0414+573':'0424+020','1030+074':'1041+061','1152+199':'1150+242','1127+385':'1130+382','0712+472':'0710+475'}

applyind = True
#for date in dates:
    #spwstr = ''
    #os.system("rm -rf *%s*"%date)
    #os.system("rm -rf *cal")
    #vis = 'af377_%s.ms'%date
    #curvis = vis
    #execfile('/mnt/data3/rumbaugh/VLA/scripts/calib_VLA.py')
for date in dates[startind:startind+9]:
    vis = 'af377_%s.ms'%date
    curvis = vis
    for source in sources:
        outbase = 'af377_%s'%date
        lensname = source
        fieldnum = source
        execfile("/mnt/data3/rumbaugh/VLA/scripts/export_lens.py")
    for source in CSOs:
        outbase = 'af377_%s'%date
        lensname = source
        fieldnum = source
        execfile("/mnt/data3/rumbaugh/VLA/scripts/export_lens.py")
