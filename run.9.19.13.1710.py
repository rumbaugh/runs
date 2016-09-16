import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')
calDict = {'5.08.01': {'ants': 'VA05,VA08', 'arch': ['AF377_CE010508.xp1']}, '5.12.01': {'ants': 'VA09,VA25', 'arch': ['AF377_CG010512.xp1']}, '5.14.01': {'ants': 'VA09,VA25', 'arch': ['AF377_CH010514.xp1']}, '5.17.01': {'ants': 'VA05,VA08,VA22', 'arch': ['AF377_CJ010517.xp1']}, '5.20.01': {'ants': 'VA22', 'arch': ['AF377_CL010520.xp1','AF377_CL010520.xp2']}}

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

for date in calDict:
    spwstr = ''
    os.system("rm -rf *%s*"%date)
    os.system("rm -rf *cal")
    vis = 'af377_%s.ms'%date
    curvis = vis
    importvla(vis=vis,archivefiles = calDict[date]['arch'])
    tflagdata(vis=vis,antenna=calDict[date]['ants'])
    execfile('/mnt/data3/rumbaugh/VLA/scripts/calib_VLA.py')
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
