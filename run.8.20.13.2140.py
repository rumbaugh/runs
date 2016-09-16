import numpy as np
import sys
execfile('/home/rumbaugh/arrconv.py')
fields = ['Cl1604','Cl1324','Cl0023','RXJ1757','RXJ1821','RXJ1053','Cl1137','RXJ1716','RXJ1221','Cl1350','Cl0849','Cl0910']

match_cat_name_dict = {x: x for x in fields}
phot_cat_name_dict = {x: x for x in fields}
match_cat_name_dict['RXJ1757'] = 'NEP200'
match_cat_name_dict['RXJ1821'] = 'NEP5281'
phot_cat_name_dict['RXJ1821'] = 'NEP5281'
match_cat_name_dict['RXJ1221'] = '1221'
phot_cat_name_dict['RXJ1221'] = '1221'
match_cat_name_dict['Cl1350'] = '1350'
phot_cat_name_dict['Cl1350'] = '1350'
phot_cat_name_dict['Cl0910'] = '2227+2452'
phot_cat_name_dict['Cl0849'] = '927+1708'

FILE = open('/home/rumbaugh/ORELSE/ORELSE.Xray_combined_phot+matching.8.20.13.dat','w')
FILE.write('# Field Xray_dec Xray_RA Pos_err flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full sig_soft sig_hard sig_full num_matched opt_RA opt_Dec Opt_src_name P_match P_no_match\n')
for field in fields:
    crp = np.loadtxt('/home/rumbaugh/ChandraData/photometry_files/%s.xray_phot.soft_hard_full.dat'%(phot_cat_name_dict[field]))
    if field in ['Cl1604','Cl1324','Cl0023','RXJ1757','RXJ1821']:
        crm = np.loadtxt('/home/rumbaugh/ORELSE/paperstuff/%s.opt_Xray_matched_catalog_3high.corrected.twk.8.8.11.dat'%(match_cat_name_dict[field]),dtype='string')
    elif field in ['Cl0910','Cl0849']:
        crm = np.loadtxt('/home/rumbaugh/ORELSE/paperstuff/%s.opt_Xray_matched_catalog_3high.corrected.twk.8.20.13.dat'%(match_cat_name_dict[field]),dtype='string')
    else:
        crm = np.loadtxt('/home/rumbaugh/ORELSE/paperstuff/%s.opt_Xray_matched_catalog_3high.corrected.twk.dat'%(match_cat_name_dict[field]),dtype='string')
    if field == 'Cl1604':
        g1604 = str2int(crm[:,24])
        crp = crp[g1604]
    if np.shape(crp)[0] != np.shape(crm)[0]: sys.exit('cats have different lengths for %s'%field)
    for i in range(0,np.shape(crp)[0]):
        cpl,cml = crp[i],crm[i]
        if cml[7] == 'NNNNNNNNNNNNNNN': cml[7] = '-1'
        FILE.write('%10s %9.5f %9.5f %5.2f %5.3E %5.3E %5.3E %6.1f %6.1f %6.1f %6.2f %6.2f %6.2f %2i %9.5f %9.5f %15s %6.3f %6.3f\n'%(field,float(cml[1]),float(cml[2]),float(cml[3]),cpl[2],cpl[3],cpl[4],cpl[5],cpl[6],cpl[7],cpl[8],cpl[9],cpl[10],int(cml[4]),float(cml[5]),float(cml[6]),cml[7],float(cml[8]),float(cml[20])))
FILE.close()
