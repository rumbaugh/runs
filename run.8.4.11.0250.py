execfile("get_cols_batch.py")
import numpy as np
import sys


names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
msfiles = ['FINAL.matched.0023.specnXray.nov2010.rumbaugh.noser.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noser.noheader.cat','FINAL.matched.1322.specnXray.nov2010.rumbaugh.noser.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.noser.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noser.noheader.cat']
#mfiles = ['Cl0023.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','public_html/outgoing/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','public_html/outgoing/Cl1324.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP5281.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP200.opt_Xray_matched_catalog_3high.corrected.twk.11.19.10.dat']
mfiles = ['Cl0023.opt_match.correct1.dat','public_html/outgoing/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','Cl1324.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP5281.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP200.opt_Xray_matched_catalog_3high.corrected.twk.11.19.10.dat']

for i in range(0,5):
    attempt = 0.0
    conf = 0.0
    crms = read_file('/home/rumbaugh/' + msfiles[i])
    if i != 1: LFC_ID,mask,slit,RA_opt,dec_opt,rb, ib,zb,rs, z_err,q,old_ID, Xray_ID,RA_Xray,dec_Xray,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,19)
    if i == 1: LFC_ID,mask,slit,RA_opt,dec_opt,rb, ib,zb,rs, z_err,q,old_ID, maskACS,RA_ACS,dec_ACS,ACS_ID, F606W,F814W,Xray_ID,RA_Xray,dec_Xray,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,25)
    for j in range(0,len(mask)):
        if j == 0: 
            attempt += 1
            if q[j] > 2.3: conf += 1
            if q[j] < -0.3: conf += 1
            maxid = Xray_ID[j]
        else:
            if Xray_ID[j] > maxid+0.1: 
                if Xray_ID[j] > maxid: maxid = Xray_ID[j]
                attempt += 1
                if q[j] > 2.3: conf += 1
                if q[j] < -0.3: conf += 1
            else:
                print Xray_ID[j-1],Xray_ID[j],j,maxid
    print "%s  %i  %i\n"%(names[i],attempt,conf)
