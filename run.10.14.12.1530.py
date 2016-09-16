import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m

try:
    rewrite
except NameError:
    rewrite = False

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])

namef = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/acis10444+10924.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/RXJ1757/master/RXJ1757.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/Cl1604/master/acis6932.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.vig_corr.nops.fits","/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.vig_corr.nops.fits"])

anninner = np.array([120,100,160,100,160,150,100,100,100])*1.0
annouter1 = anninner + 100
annouter1[3] -= 20
annouter1[5:7] -= 20
annouter2 = annouter1 + 50
#annouter2 = anninner + 150

ai = ((anninner/5)-1)

#nharr = np.array([5.66,4.07,1.15,1.16,1.23,1.23])
#I need to use Dale's value forit to be compatible
nharr = np.array([5.66,4.07,1.15,1.16,1.16,7.57,7.57,2.05,2.05])/100.0
rsarr = np.array([0.84,0.69,0.69,0.76,0.76,0.898,0.866,1.1,1.1])
times = np.array([49548.501183658,46451.792387024,48391.890220549,50399.00069391,50399.00069391,49478.092354796,49478.092354796,171046.89083577,171046.89083577])
cnt2flux = np.zeros(len(nharr))
cnt2flux2 = np.zeros(len(nharr))

crc = read_file("/home/rumbaugh/cc_out.6.29.12.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Hz = np.append(Hz,Hz[len(Hz)-1])
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
mpc = np.append(mpc,mpc[len(mpc)-1])
mpccm = get_colvals(crc,'col13')*0.7
mpccm = np.append(mpccm,mpccm[len(mpccm)-1])
lumdists = get_colvals(crc,'col9')/0.7
lumdists = np.append(lumdists,lumdists[len(lumdists)-1])
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
fourpiDL2 = 1e-57*get_colvals(crc,'col10')/(0.7*0.7)
fourpiDL2 = np.append(fourpiDL2,fourpiDL2[len(fourpiDL2)-1])
tcnts = np.zeros(len(nharr))
netcnts = np.zeros(len(nharr))
bgcnts = np.zeros(len(nharr))
bgSB = np.zeros(len(nharr))
bgSBas = np.zeros(len(nharr))
lums = np.zeros(len(nharr))
fluxs = np.zeros(len(nharr))
fluxs2 = np.zeros(len(nharr))
lumerr = np.zeros(len(nharr))

sigma = np.array([921,652,880,914,819,619,811,675,1028])
load_data(str(namef[0]))

crb = read_file('/home/rumbaugh/DE_counts.bkg_data.10.13.12.dat')
bgcnts = copy_colvals(crb,'col2')
bgSBas = copy_colvals(crb,'col4')
bgann1,bgann2 = copy_colvals(crb,'col7'),copy_colvals(crb,'col8')
bgSBas_err = np.zeros(len(bgSBas))
for i in range(0,len(bgSBas)): 
    if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
        bgSBas_err[i] = m.sqrt(bgcnts[i])/(m.pi*(bgann2[i]**2-bgann1[i]**2))
    else:
        bgSBas_err[i] = m.sqrt(bgcnts[i])/(m.pi*(bgann2[i-1]**2-bgann1[i-1]**2))
for i in range(0,len(names)):
    print names[i]
    cr = read_file('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arr = copy_colvals(cr,'col3')
    ncnts_off = cnts_arr[int(ai[i])]-bgSBas[i]*m.pi*0.25*anninner[i]**2
    ncnts_off_err = m.sqrt(cnts_arr[int(ai[i])]+bgSBas_err[i]**2*m.pi*m.pi*0.25*0.25*anninner[i]**4)
    cum_cnts = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = np.sum(cnts_arr[0:j])
    SB_arr = copy_colvals(cr,'col5')
    SB_err_arr = copy_colvals(cr,'col7')
    ann_arr = copy_colvals(cr,'col2')
    #r0 = 2*0.18*(mpc[i]*60)
    r0 = 0.18*(mpc[i]*60)
    #r500 = 2*(mpc[i]*60)*2*sigma[i]/(m.sqrt(500)*Hz[i])
    r500 = (mpc[i]*60)*2*sigma[i]/(m.sqrt(500)*Hz[i])
    if ((i == 2) | (i == 3) | (i == 5)| (i == 6)):
        ann_arr = np.arange(12)*10+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    elif ((i == 4)):
        ann_arr = np.arange(12)*10+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    else:
        ann_arr = np.arange(16)*7.5+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[3*j+3]
    cum_ncnts = np.zeros(len(cnts_arr))
    cum_ncnts_err = np.zeros(len(cnts_arr))
    cum_ncnts_ext = np.zeros(len(cnts_arr))
    cum_ncnts_ext_err = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): 
        cum_ncnts[j] = cnts_arr[j]-bgSBas[i]*m.pi*ann_arr[j]**2
        cum_ncnts_err[j] = m.sqrt(cum_cnts[j]+m.pi*m.pi*ann_arr[j]**4*bgSBas_err[i]**2)
        cum_ncnts_ext[j] = ncnts_off*m.fabs((1-1.0/m.sqrt(1+ann_arr[j]**2*r0**(-2)))/(1-1.0/m.sqrt(1+0.25*anninner[i]**2*r0**(-2))))
        cum_ncnts_ext_err[j] = ncnts_off_err*m.fabs((1-1.0/m.sqrt(1+ann_arr[j]**2*r0**(-2)))/(1-1.0/m.sqrt(1+0.25*anninner[i]**2*r0**(-2))))
    area_arr = np.zeros(len(ann_arr))
    area_arr[0] = m.pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = m.pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = np.append(np.zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (m.sqrt(cnts_arr[j])+m.sqrt(cnts2[j]))/area_arr[j]
    #if rewrite:
        #FILE = open('/home/rumbaugh/DE_counts_profile.%s.10.14.12.dat'%names[i],'w')
        #for j in range(0,len(ann_arr)): FILE.write('%3i %3i %f %f %f %f %f\n'%(ann_arr[j],0.5*ann_arr[j],cnts_arr[j],SB_arr[j],4*SB_arr[j],SB_err_arr[j],4*SB_err_arr[j]))
        #FILE.close()
    #if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
    #    netcnts[i] = cnts_arr[i]
    #else:
     #   netcnts[i] = calc_data_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,anninner[i])) - bgSB[i]*anninner[i]**2
    pylab.xlim(0,140)
    pylab.xlabel('Radius (arcseconds)')
    pylab.ylabel('Net counts')
    pylab.errorbar(ann_arr,cum_ncnts,cum_ncnts_err,color='blue',fmt=None)
    pylab.errorbar(ann_arr,cum_ncnts_ext,cum_ncnts_ext_err,color='red',fmt=None)
    pylab.scatter(ann_arr,cum_ncnts,color='blue',label='No extrapolation')
    pylab.scatter(ann_arr,cum_ncnts_ext,color='red',label='Extrapolated')
    pylab.legend(loc=4)
    pylab.plot(np.zeros(2)+r500,np.array([0,200]),linestyle='dashed')
    pylab.savefig('/home/rumbaugh/DE_counts_profile_err_comp.%s.10.14.12.png'%names[i])
    pylab.close()

    
