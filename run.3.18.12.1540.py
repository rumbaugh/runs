FILE = open("BCLmatching.test.reg",'w')
FILE.write("# Region file format: DS9 version 4.1\n")
FILE.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
crp = read_file("VVDS_D+UD.RAdecnSpitzermags.wphotonspecz.IRAC1+2detonly.cat")
ra_opt = copy_colvals(crp,'col2')
dec_opt = copy_colvals(crp,'col3')
crm = read_file("IRAC_SPIRE_matched_catalog_3high.twk.dat")
nm = copy_colvals(crm,'col5')
raX = copy_colvals(crm,'col2')
decX = copy_colvals(crm,'col3')
errX = copy_colvals(crm,'col4')
ra_opt1 = copy_colvals(crm,'col6')
dec_opt1 = copy_colvals(crm,'col7')
ra_opt2 = copy_colvals(crm,'col11')
dec_opt2 = copy_colvals(crm,'col12')
ra_opt3 = copy_colvals(crm,'col16')
dec_opt3 = copy_colvals(crm,'col17')
for i in range(0,len(nm)):
    if nm[i] == 0:
        FILE.write("circle(" + str(raX[i]) + "," + str(decX[i]) + "," + str(errX[i]) + '") # color=orange \n')
    else:
        FILE.write("circle(" + str(raX[i]) + "," + str(decX[i]) + "," + str(errX[i]) + '") # color=red \n')
        if nm[i] == 1:
            FILE.write('circle(%f,%f,1.0") # color = magenta\n'%(ra_opt1[i],dec_opt1[i]))
        if nm[i] == 2:
            FILE.write('circle(%f,%f,1.0") # color = teal\n'%(ra_opt2[i],dec_opt2[i]))
        if nm[i] == 3:
            FILE.write('circle(%f,%f,1.0") # color = green\n'%(ra_opt3[i],dec_opt3[i]))
for i in range(0,len(ra_opt)): FILE.write('circle(%f,%f,1.0") # color = yellow\n'%(ra_opt[i],dec_opt[i])) 
FILE.close()
        

