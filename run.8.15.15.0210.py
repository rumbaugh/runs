import numpy as np

defdir='/home/rumbaugh/KAST/rusu_run_8.15'

blue_exp_nums = np.array([2028,2029,2030,2031,2032,2036,2037,2038,2043,2044,2045,2049,2050,2051,2052,2053])

red_exp_nums= np.array([1021,1022,1023,1029,1035,1036,1044,1053,1061,1062,1063,2030,2031,2038,2039,2040,2047,2054,2055,2056,2063,2064,2065,2072,2073,2074,2075])

FILESci=open('%s/science_list_8.15.15.2010.txt'%defdir,'w')
FILESky=open('%s/sky_list_8.15.15.2010.txt'%defdir,'w')
FILEout=open('%s/skysub_output_list_8.15.15.2010.txt'%defdir,'w')

for i in range(0,len(blue_exp_nums)):
    #if blue_exp_nums == 2036: 
    filetype='.fits'
    #else: 
    #    filetype='.fits.gz'
    FILESci.write('%s/Science/sci-b%i%s[0]\n'%(defdir,blue_exp_nums[i],filetype))
    FILESky.write('%s/Science/sci-b%i%s[2]\n'%(defdir,blue_exp_nums[i],filetype))
    FILEout.write('%s/Science/sci-b%i.skysub.fits\n'%(defdir,blue_exp_nums[i]))
for i in range(0,len(red_exp_nums)):
    #if red_exp_nums == 2036: 
    filetype='.fits'
    #else: 
    #    filetype='.fits.gz'
    FILESci.write('%s/Science/sci-r%i%s[0]\n'%(defdir,red_exp_nums[i],filetype))
    FILESky.write('%s/Science/sci-r%i%s[2]\n'%(defdir,red_exp_nums[i],filetype))
    FILEout.write('%s/Science/sci-r%i.skysub.fits\n'%(defdir,red_exp_nums[i]))
FILESci.close()
FILESky.close()
FILEout.close()
