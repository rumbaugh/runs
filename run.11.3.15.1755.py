import numpy as np

defdir='/home/rumbaugh/KAST/rusu_run_10.15'

blue_exp_nums = np.arange(1030,1047)

red_exp_nums= np.array([1030,1031,1032,1039,1040,1041,1048,1049,1050,1051,1058,1059,1066,1067,1068,1069,1070])

FILESci=open('%s/science_list_11.3.15.1755.txt'%defdir,'w')
FILESky=open('%s/sky_list_11.3.15.1755.txt'%defdir,'w')
FILEout=open('%s/skysub_output_list_11.3.15.1755.txt'%defdir,'w')

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
    FILESci.write('%s/Science/sci-r%i_fixedhdr%s[0]\n'%(defdir,red_exp_nums[i],filetype))
    FILESky.write('%s/Science/sci-r%i_fixedhdr%s[2]\n'%(defdir,red_exp_nums[i],filetype))
    FILEout.write('%s/Science/sci-r%i.skysub.fits\n'%(defdir,red_exp_nums[i]))
FILESci.close()
FILESky.close()
FILEout.close()
