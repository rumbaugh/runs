import numpy as np
import pandas as pd

def open_csv(fname):
    df=pd.read_csv(fname,delim_whitespace=True)
    if df.columns[0]=='#':
        newnames=df.columns[1:].tolist()
        df=pd.read_csv(fname,delim_whitespace=True,comment='#',names=newnames)
    return df

cendf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.csv')
dsdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.DStests.dat',comment='#',delim_whitespace=True,names=['field','cluster','DSstat','P_DS'])
sigsdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clus_sigs.dat',comment='#',names=['field','cluster','Sig_all','Sig_all_Error','Sig_all_N','Sig_all_cut','Sig_all_cut_Error','Sig_all_cut_N','Sig_red','Sig_red_Error','Sig_red_N','Sig_blue','Sig_blue_Error','Sig_blue_N','Zmin','Zmax'],delim_whitespace=True)
vcdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.veldiffs.dat',delim_whitespace=True,comment='#',names=['field','cluster','Blue_vel_cen','Red_vel_cen','perc','perc_bwl_BS'])
bcgdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.BCG_vels.csv')
prdf=open_csv('/home/rumbaugh/Chandra/ORELSE.power_ratios.dat')
srodf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.scaling_relation_offsets.tab',delim_whitespace=True,comment='#',names=['field','cluster','mindistlit_LxT','mindistfit_LxT','mindistlit_sigT','mindistfit_sigT','mindistlit_Lxsig','mindistfit_Lxsig'])
cbdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_bounds.dat')

for df in [cendf,dsdf,sigsdf,vcdf,bcgdf,prdf,srodf,cbdf]: 
    df['field'][df.field=='cl1324_north']='cl1324'
    df['field'][df.field=='cl1324_south']='cl1324'

master_df=pd.merge(cendf,dsdf,on=['field','cluster'],how='outer')
for right in [sigsdf,vcdf,bcgdf,prdf,srodf,cbdf]: 
    master_df=pd.merge(master_df,right,on=['field','cluster'],how='outer')

outdf=master_df[['field','cluster', 'dist_bcg2x', 'dist_bcg2lw', 'dist_lw2x', 'DSstat', 'P_DS',  'Sig_all', 'Sig_all_Error','Sig_all_N','Sig_red', 'Sig_red_Error', 'Sig_red_N', 'Sig_blue', 'Sig_blue_Error', 'Sig_blue_N', 'Blue_vel_cen','Red_vel_cen', 'perc','perc_bwl_BS', 'BCGvel', 'P3', 'P4','P3LB', 'P3UB', 'P4LB','P4UB', 'mindistlit_LxT', 'mindistfit_LxT', 'mindistlit_sigT', 'mindistfit_sigT', 'mindistlit_Lxsig', 'mindistfit_Lxsig','zcen','zmin','zmax','rad']]
outdf.to_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.csv',index=False)



