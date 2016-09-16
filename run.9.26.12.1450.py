import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m

try:
    rewrite
except NameError:
    rewrite = False

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])

for i in range(0,len(names)):
    print names[i]
    cr = read_file('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arr = copy_colvals(cr,'col3')
    SB_arr = copy_colvals(cr,'col5')
    SB_err_arr = copy_colvals(cr,'col7')
    ann_arr = copy_colvals(cr,'col2')
    if ((i == 2) | (i == 3) | (i == 5)| (i == 6)):
        ann_arr = np.arange(16)*7.5+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[3*j+3]
    elif ((i == 4)):
        ann_arr = np.arange(11)*10+20
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+7]
    else:
        ann_arr = np.arange(24)*5+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[2*j+3]
    area_arr = np.zeros(len(ann_arr))
    area_arr[0] = m.pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = m.pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = np.append(np.zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (m.sqrt(cnts_arr[j])+m.sqrt(cnts2[j]))/area_arr[j]
    if rewrite:
        FILE = open('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i],'w')
        for j in range(0,len(ann_arr)): FILE.write('%3i %3i %f %f %f %f %f\n'%(ann_arr[j],0.5*ann_arr[j],cnts_arr[j],SB_arr[j],4*SB_arr[j],SB_err_arr[j],4*SB_err_arr[j]))
        FILE.close()
    pylab.errorbar(ann_arr,SB_arr,SB_err_arr,fmt=None)
    pylab.scatter(ann_arr,SB_arr)
    pylab.savefig('/home/rumbaugh/DE_counts_profile.%s.9.25.12.png'%names[i])
    pylab.close()

    
