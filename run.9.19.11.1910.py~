import numpy as np
import os


crc = read_file("/home/rumbaugh/cosmocalc_out.4bm.nh.dat")
mpc = get_colvals(crc,'col12')*0.7
namef = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/acis10444+10924.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/RXJ1757/master/RXJ1757.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.nops.fits","/scratch/rumbaugh/ciaotesting/Cl1604/6932/acis6932.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.nops.fits"])

for i in range(0,len(mpc)):
    load_data(str(namef[i]))
    set_model(beta2d.b)
    b.xpos = 500
    b.ypos = 500
    b.r0 = 2*0.18*(mpc[i]*60)
    b.alpha = 1.5
    save_model("/home/rumbaugh/ChandraData/bmodels/temp/tmpmodel.r0_%7.4f.alpha_1.5.fits"%(b.r0.val))
    ostemp = os.system('dmcopy "/home/rumbaugh/ChandraData/bmodels/temp/tmpmodel.r0_%7.4f.alpha_1.5.fits[(#1,#2)=circle(500,500,150)]" /home/rumbaugh/ChandraData/bmodels/beta_model.r0_%5.2f.alpha_1.5.fits clob+'%(b.r0.val,b.r0.val))
    
