import os
r0 = np.array(['12','98'])
r = np.array(['32.4','46.27','46.27','44.15','48.84','46.27','47.17'])
names = np.array(['0910','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1324','Cl1324'])
n_ids = np.array(['acis2227+2452','acis9403+9840','RXJ1757','acis10444+10924','acis6932','acis9404+9836','acis9404+9836'])
xlo = np.array([3850,3000,4560,4175,4320,3000,3000])
ylo = np.array([3380,3975,3185,4570,4080,3975,3975])
xhi = np.array([4350,3580,5030,5000,5135,3580,3580])
yhi = np.array([3750,4350,3560,5030,4530,4350,4350])
FILEstat = open("/home/rumbaugh/status.run.5.10.12.1635.txt",'w')
FILEstat.close()
FILE1 = open("/home/rumbaugh/baselines.test.5.10.12.dat",'w')
for i in range(5,5):
    baseline = np.zeros(2)
    for j in range(0,1):
        load_data("/home/rumbaugh/ChandraData/%s/master/test.conv.%s.soft.r_%s.5.8.12.fits"%(names[i],n_ids[i],r0[j]))
        set_coord("physical")
        baseline[j] = calc_data_sum2d("RECT(%i,%i,%i,%i)"%(xlo[i],ylo[i],xhi[i],yhi[i]))/((xhi[i]-xlo[i])*(yhi[i]-ylo[i])*1.0)
        ostemp = os.system('dmimgcalc infile=/home/rumbaugh/ChandraData/%s/master/test.conv.%s.soft.r_%s.5.8.12.fits infile2=none op="imgout=img1-%f" out=/home/rumbaugh/ChandraData/%s/master/tempbaseline.fits mode=h clob+'%(names[i],n_ids[i],r0[j],baseline[j],names[i]))
        FILEstat = open("/home/rumbaugh/status.run.5.10.12.1635.txt",'a')
        FILEstat.write("%i - /home/rumbaugh/ChandraData/%s/master/tempbaseline.fits\n"%(ostemp,names[i]))
        FILEstat.close()
        ostemp = os.system('dmimgcalc infile=/home/rumbaugh/ChandraData/%s/master/tempbaseline.fits,/home/rumbaugh/ChandraData/%s/master/test.conv.var.%s.soft.r_%s.5.8.12.fits infile2=none op="imgout=img1/(img2**0.5)" out=/home/rumbaugh/ChandraData/%s/master/test.conv.sig.%s.soft.r_%s.5.8.12.fits mode=h clob+'%(names[i],names[i],n_ids[i],r0[j],names[i],n_ids[i],r0[j]))
        FILEstat = open("/home/rumbaugh/status.run.5.10.12.1635.txt",'a')
        FILEstat.write("%i - /home/rumbaugh/ChandraData/%s/master/test.conv.sig.%s.soft.r_%s.5.8.12.fits\n"%(ostemp,names[i],n_ids[i],r0[j]))
        FILEstat.close()
        rmtemp = os.system("rm /home/rumbaugh/ChandraData/%s/master/tempbaseline.fits"%(names[i]))
    FILE1.write('%s %f %f\n'%(n_ids[i],baseline[0],baseline[1]))
FILE1.close()
FILE2 = open("/home/rumbaugh/baselines.5.10.12.dat",'w')
for i in range(0,7):
    if i != 6: load_data("/home/rumbaugh/ChandraData/%s/master/conv.%s.soft.r_%s.5.8.12.fits"%(names[i],n_ids[i],r[i]))
    set_coord("physical")
    baseline = calc_data_sum2d("RECT(%i,%i,%i,%i)"%(xlo[i],ylo[i],xhi[i],yhi[i]))/((xhi[i]-xlo[i])*(yhi[i]-ylo[i])*1.0)
    ostemp = os.system('dmimgcalc infile=/home/rumbaugh/ChandraData/%s/master/conv.%s.soft.r_%s.5.8.12.fits infile2=none op="imgout=img1-%f" out=/home/rumbaugh/ChandraData/%s/master/tempbaseline.fits mode=h clob+'%(names[i],n_ids[i],r[i],baseline,names[i]))
    FILEstat = open("/home/rumbaugh/status.run.5.10.12.1635.txt",'a')
    FILEstat.write("%i - /home/rumbaugh/ChandraData/%s/master/tempbaseline.fits\n"%(ostemp,names[i]))
    FILEstat.close()
    #ostemp = os.system('dmimgcalc infile=/home/rumbaugh/ChandraData/%s/master/tempbaseline.fits,/home/rumbaugh/ChandraData/%s/master/conv.var.%s.soft.r_%s.5.8.12.fits infile2=none op="imgout=img1/(0.5*img2**0.5)" out=/home/rumbaugh/ChandraData/%s/master/conv.sigx2.%s.soft.r_%s.5.8.12.fits mode=h clob+'%(names[i],names[i],n_ids[i],r[i],names[i],n_ids[i],r[i]))
    #FILEstat.write("%i - /home/rumbaugh/ChandraData/%s/master/conv.sigx2.%s.soft.r_%s.5.8.12.fits\n"%(ostemp,names[i],n_ids[i],r[i]))
    ostemp = os.system('dmimgcalc infile=/home/rumbaugh/ChandraData/%s/master/tempbaseline.fits,/home/rumbaugh/ChandraData/%s/master/conv.var.%s.soft.r_%s.5.8.12.fits infile2=none op="imgout=img1/(img2**0.5)" out=/home/rumbaugh/ChandraData/%s/master/conv.sig.%s.soft.r_%s.5.8.12.fits mode=h clob+'%(names[i],names[i],n_ids[i],r[i],names[i],n_ids[i],r[i]))
    FILEstat = open("/home/rumbaugh/status.run.5.10.12.1635.txt",'a')
    FILEstat.write("%i - /home/rumbaugh/ChandraData/%s/master/conv.sig.%s.soft.r_%s.5.8.12.fits\n"%(ostemp,names[i],n_ids[i],r[i]))
    FILEstat.close()
    rmtemp = os.system("rm /home/rumbaugh/ChandraData/%s/master/tempbaseline.fits"%(names[i]))
    FILE2.write("%s %f\n"%(names[i],baseline))
