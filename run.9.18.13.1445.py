import numpy as np
lenses = ['MG0414','J1030','B1152','B1127','B0712']
fields = ['1','3','5','7','12']
dates = ['5.08.01','5.12.01','5.14.01','5.17.01']
for date in dates:
    outbase = 'af377_%s'%date
    curvis = 'af377_%s.ms'%date
    for lens,field in zip(lenses,fields):
        lensname = lens
        fieldnum = field
        execfile('/mnt/data3/rumbaugh/VLA/scripts/export_lens.py')
