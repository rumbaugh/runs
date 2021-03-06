execfile("/home/rumbaugh/FindCloseSources.py")

names = np.array(['0910'])
path = '/home/rumbaugh/LFC'

for i in range(0,len(names)):
    FILE = open('%s/%s/opt_match/mask_list.%s.dat'%(path,names[i],names[i]),"w")
    cr = read_file('%s/%s/opt_match/opt_Xray_matched_catalog_3high.twk.dat'%(path,names[i]))
    raopt = get_colvals(cr,'col1')
    raX = get_colvals(cr,'col2')
    decX = get_colvals(cr,'col3')
    nm = get_colvals(cr,'col5')
    raopt1 = get_colvals(cr,'col6')
    decopt1 = get_colvals(cr,'col7')
    idopt1 = get_colvals(cr,'col8')
    raopt2 = get_colvals(cr,'col11')
    decopt2 = get_colvals(cr,'col12')
    idopt2 = get_colvals(cr,'col13')
    raopt3 = get_colvals(cr,'col16')
    decopt3 = get_colvals(cr,'col17')
    idopt3 = get_colvals(cr,'col18')
    sigmax = get_colvals(cr,'col23')
    prob1 = get_colvals(cr,'col9')
    prob2 = get_colvals(cr,'col14')
    prob3 = get_colvals(cr,'col19')
    for j in range(0,len(nm)):
        if nm[j] > 0.1: FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt1[j]),raopt1[j],decopt1[j],raX[j],decX[j],prob1[j],sigmax[j]))
        if nm[j] > 1.1: FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt2[j]),raopt2[j],decopt2[j],raX[j],decX[j],prob2[j],sigmax[j]))
        if nm[j] > 2.1: FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt3[j]),raopt3[j],decopt3[j],raX[j],decX[j],prob3[j],sigmax[j]))
    cr2 = read_file('%s/%s/opt_match/opt_Xray_matched_catalog_3high.twk.dat.minsrch.dat'%(path,names[i]))
    raX2 = get_colvals(cr2,'col2')
    decX2 = get_colvals(cr2,'col3')
    nm2 = get_colvals(cr2,'col5')
    raopt12 = get_colvals(cr2,'col6')
    decopt12 = get_colvals(cr2,'col7')
    idopt12 = get_colvals(cr2,'col8')
    raopt22 = get_colvals(cr2,'col11')
    decopt22 = get_colvals(cr2,'col12')
    idopt22 = get_colvals(cr2,'col13')
    raopt32 = get_colvals(cr2,'col16')
    decopt32 = get_colvals(cr2,'col17')
    idopt32 = get_colvals(cr2,'col18')
    prob12 = get_colvals(cr2,'col9')
    prob22 = get_colvals(cr2,'col14')
    prob32 = get_colvals(cr2,'col19')
    g = np.where(nm2 > nm)
    g = g[0]
    for j in range(0,len(g)):
        if ((nm2[g[j]] > 0.1) and (idopt12[g[j]] != idopt1[g[j]]) and (idopt12[g[j]] != idopt2[g[j]]) and (idopt12[g[j]] != idopt3[g[j]])): FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt12[g[j]]),raopt12[g[j]],decopt12[g[j]],raX2[g[j]],decX2[g[j]],prob12[g[j]],sigmax[g[j]]))
        if ((nm2[g[j]] > 1.1) and (idopt22[g[j]] != idopt1[g[j]]) and (idopt22[g[j]] != idopt2[g[j]]) and (idopt22[g[j]] != idopt3[g[j]])): FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt22[g[j]]),raopt22[g[j]],decopt22[g[j]],raX2[g[j]],decX2[g[j]],prob22[g[j]],sigmax[g[j]]))
        if ((nm2[g[j]] > 2.1) and (idopt32[g[j]] != idopt1[g[j]]) and (idopt32[g[j]] != idopt2[g[j]]) and (idopt32[g[j]] != idopt3[g[j]])): FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(int(idopt32[g[j]]),raopt32[g[j]],decopt32[g[j]],raX2[g[j]],decX2[g[j]],prob32[g[j]],sigmax[g[j]]))
    FILE.close()
    crn = read_file('%s/%s/opt_match/mask_list.%s.dat'%(path,names[i],names[i]))
    c1 = get_colvals(crn,'col1')
    c2 = get_colvals(crn,'col2')
    c3 = get_colvals(crn,'col3')
    c4 = get_colvals(crn,'col4')
    c5 = get_colvals(crn,'col5')
    c6 = get_colvals(crn,'col6')
    c7 = get_colvals(crn,'col7')
    FILE=open('%s/%s/opt_match/mask_list_sort.%s.dat'%(path,names[i],names[i]),'w')
    g = np.argsort(-1*c7)
    for q in range(0,len(g)): FILE.write('%6i %10.5f %9.5f %10.5f %9.5f %6.4f %6.2f\n'%(c1[g[q]],c2[g[q]],c3[g[q]],c4[g[q]],c5[g[q]],c6[g[q]],c7[g[q]]))
    FILE.close()
