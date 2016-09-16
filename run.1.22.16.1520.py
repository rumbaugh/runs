import numpy as np

imdict={'cl1324_south': 'sc1322_1i_shift_norm.fits', 'cl1324_north': 'sc1322_2i_shift_norm.fits', 'cl0023': 'cl0023_i_shift_norm.fits', "rcs0224": "rcs0224_i.fits","cl0849":"cl0849_i_shift.fits","rxj0910":"cl0910_i_shift_norm.fits","rxj1221":"rxj1221_i_shift_norm.fits","cl1350":"cl1350_i_shift_norm.fits","rxj1757":"nep200_i_shift_norm.fits","rxj1821":"nep5281_i_shift_norm.fits","cl1137":"cl1137_i_trim_fix.fits","rxj1716":"rxj1716_i.fits","rxj1053":"rxj1053_i_fix_trim.fits"}

FILE=open('/home/rumbaugh/runs/run.1.22.16.1520','w')
FILE.write('cd /home/rumbaugh/Chandra/optimages\n')
for field in imdict.keys():
    FILE.write('ln -s %s %s_I.fits\n'%(imdict[field],field))
FILE.close()
