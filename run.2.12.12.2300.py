cr = read_file("/local3/rumbaugh/ChandraData/1662/opt_match/opt_Xray_matched_catalog_3high.1221.corrected.dat")


for i in range(0,1):
    ID = copy_colvals(cr,'col1')
    raX = copy_colvals(cr,'col2')
    decX = copy_colvals(cr,'col3')
    errX = copy_colvals(cr,'col4')
    nm = copy_colvals(cr,'col5')
    raopt1 = copy_colvals(cr,'col6')
    decopt1 = copy_colvals(cr,'col7')
    idopt1 = copy_colvals(cr,'col8')
    raopt2 = copy_colvals(cr,'col11')
    decopt2 = copy_colvals(cr,'col12')
    idopt2 = copy_colvals(cr,'col13')
    raopt3 = copy_colvals(cr,'col16')
    decopt3 = copy_colvals(cr,'col17')
    idopt3 = copy_colvals(cr,'col18')
    sigmax = copy_colvals(cr,'col23')
    prob1 = copy_colvals(cr,'col9')
    prob2 = copy_colvals(cr,'col14')
    prob3 = copy_colvals(cr,'col19')
FILE = open('/home/rumbaugh/opt_match.1221.dat','w')
for i in range(0,len(ID)):
    if ((nm[i] > 0.1) & (i != 85)): FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt1[i],raopt1[i],decopt1[i],ID[i]))
    if ((nm[i] > 1.1) & (i != 85) & (i != 61)): FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt2[i],raopt2[i],decopt2[i],ID[i]))
    if nm[i] > 2.1: FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt3[i],raopt3[i],decopt3[i],ID[i]))
FILE.close()
cr = read_file("/local3/rumbaugh/ChandraData/2229/opt_match/opt_Xray_matched_catalog_3high.1350.corrected.dat")


for i in range(0,1):
    ID = copy_colvals(cr,'col1')
    raX = copy_colvals(cr,'col2')
    decX = copy_colvals(cr,'col3')
    errX = copy_colvals(cr,'col4')
    nm = copy_colvals(cr,'col5')
    raopt1 = copy_colvals(cr,'col6')
    decopt1 = copy_colvals(cr,'col7')
    idopt1 = copy_colvals(cr,'col8')
    raopt2 = copy_colvals(cr,'col11')
    decopt2 = copy_colvals(cr,'col12')
    idopt2 = copy_colvals(cr,'col13')
    raopt3 = copy_colvals(cr,'col16')
    decopt3 = copy_colvals(cr,'col17')
    idopt3 = copy_colvals(cr,'col18')
    sigmax = copy_colvals(cr,'col23')
    prob1 = copy_colvals(cr,'col9')
    prob2 = copy_colvals(cr,'col14')
    prob3 = copy_colvals(cr,'col19')
FILE = open('/home/rumbaugh/opt_match.1350.dat','w')
for i in range(0,len(ID)):
    if ((nm[i] > 0.1) & (i != 85)): FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt1[i],raopt1[i],decopt1[i],ID[i]))
    if ((nm[i] > 1.1) & (i != 85) & (i != 61)): FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt2[i],raopt2[i],decopt2[i],ID[i]))
    if nm[i] > 2.1: FILE.write('%7i %12.8f %11.7f %4i\n'%(idopt3[i],raopt3[i],decopt3[i],ID[i]))
FILE.close()
