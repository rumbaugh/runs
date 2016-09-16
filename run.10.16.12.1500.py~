import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m

try:
    rewrite
except NameError:
    rewrite = False

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
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
    cum_cnts = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = np.sum(cnts_arr[0:j])
    SB_arr = copy_colvals(cr,'col5')
    SB_err_arr = copy_colvals(cr,'col7')
    ann_arr = copy_colvals(cr,'col2')
    if ((i == 0) | (i == 1) | (i == 2) | (i == 3) | (i == 6) | (i == 7) | (i == 8)):
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
        ann_arr = np.arange(8)*15+15
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[3*j+3]
    cum_ncnts = np.zeros(len(cnts_arr))
    cum_ncnts_err = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): 
        cum_ncnts[j] = cnts_arr[j]-bgSBas[i]*m.pi*ann_arr[j]**2
        cum_ncnts_err[j] = m.sqrt(cum_cnts[j]+m.pi*m.pi*ann_arr[j]**4*bgSBas_err[i]**2)
    area_arr = np.zeros(len(ann_arr))
    area_arr[0] = m.pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = m.pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = np.append(np.zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (m.sqrt(cnts_arr[j])+m.sqrt(cnts2[j]))/area_arr[j]
    if rewrite:
        FILE = open('/home/rumbaugh/DE_counts_profile.%s.10.14.12.dat'%names[i],'w')
        for j in range(0,len(ann_arr)): FILE.write('%3i %3i %f %f %f %f %f\n'%(ann_arr[j],0.5*ann_arr[j],cnts_arr[j],SB_arr[j],4*SB_arr[j],SB_err_arr[j],4*SB_err_arr[j]))
        FILE.close()
    pylab.rc('axes',linewidth=2)
    pylab.rc('font',size=16)
    pylab.tick_params(which='major',length=8,width=2,labelsize=16)
    pylab.tick_params(which='minor',length=4,width=1.5,labelsize=16)
    pylab.xlim(0,118)
    pylab.xlabel('Radius (arcseconds)',fontsize=25)
    if i < 4: 
        pylab.ylabel('Surface Brightness',fontsize=25)
    else:
        pylab.ylabel('(counts per sq. arcsecond)',fontsize=25)
    pylab.errorbar(ann_arr,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    pylab.scatter(ann_arr,SB_arr,s=5)
    pylab.savefig('/home/rumbaugh/DE_counts_profile.%s.10.14.12.png'%names[i])
    pylab.close()

    
