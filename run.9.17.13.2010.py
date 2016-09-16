import numpy as np
lenses = ['MG0414','J1030','B1152','B1127','B0712']
fields = ['1','3','5','7','12']

for lens,field in zip(lenses,fields):
    outbase = 'af377_5.12.01'
    lensname = lens
    fieldnum = field
    curvis = 'af377_5.12.01.ms'
    execfile('/mnt/data3/rumbaugh/VLA/scripts/export_lens.py')
    outbase = 'MG0414.5.25.01'
    lensname = lens
    fieldnum = field
    curvis = 'af377_5.25.01.ms'
    #execfile('/mnt/data3/rumbaugh/VLA/scripts/export_lens.py')
