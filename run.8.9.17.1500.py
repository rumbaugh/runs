import numpy as np
import pandas as pd

def open_csv(fname):
    df=pd.read_csv(fname,delim_whitespace=True)
    if df.columns[0]=='#':
        newnames=df.columns[1:].tolist()
        df=pd.read_csv(fname,delim_whitespace=True,comment='#',names=newnames)
    return df

cendf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.RF.csv')
dsdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.DStests.6.25.17.dat',comment='#',delim_whitespace=True,names=['field','cluster','DSstat','P_DS'])
sigsdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.clus_sigs_RF.dat',comment='#',names=['field','cluster','Sig_all','Sig_all_Error','Sig_all_N','Sig_Q','Sig_Q_Error','Sig_Q_N','Sig_SF','Sig_SF_Error','Sig_SF_N'],delim_whitespace=True)
vcdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.veldiffs.RF.dat',delim_whitespace=True,comment='#',names=['field','cluster','SF_vel_cen','Q_vel_cen','perc','perc_bwl_BS'])
mmcgdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.MMCG_vels.csv')
sfdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.SFfrac.csv')
prdf=open_csv('/home/rumbaugh/Chandra/ORELSE.power_ratios.dat')
srodf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.scaling_relation_offsets.6.25.17.tab',delim_whitespace=True,comment='#',names=['field','cluster','mindistlit_LxT','mindistfit_LxT','mindistlit_sigT','mindistfit_sigT','mindistlit_Lxsig','mindistfit_Lxsig'])
cbdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_bounds.6.26.17.dat')

for df in [cendf,dsdf,sigsdf,vcdf,mmcgdf,prdf,srodf,cbdf]: 
    df['field'][df.field=='cl1324_north']='cl1324'
    df['field'][df.field=='cl1324_south']='cl1324'

master_df=pd.merge(cendf,dsdf,on=['field','cluster'],how='outer')
for right in [sigsdf,vcdf,mmcgdf,prdf,srodf,cbdf,sfdf]: 
    master_df=pd.merge(master_df,right,on=['field','cluster'],how='outer')

outdf=master_df[['field','cluster', 'dist_mmcg2x', 'dist_mmcg2lw', 'dist_lw2x','LWerr', 'DSstat', 'P_DS',  'Sig_all', 'Sig_all_Error','Sig_all_N','Sig_Q', 'Sig_Q_Error', 'Sig_Q_N', 'Sig_SF', 'Sig_SF_Error', 'Sig_SF_N', 'SF_vel_cen','Q_vel_cen', 'perc','perc_bwl_BS', 'MMCGvel', 'P3', 'P4','P3LB', 'P3UB', 'P4LB','P4UB', 'mindistlit_LxT', 'mindistfit_LxT', 'mindistlit_sigT', 'mindistfit_sigT', 'mindistlit_Lxsig', 'mindistfit_Lxsig','zcen','zmin','zmax','rad','qfracspec','qfracspecerr','qfrac','qfracerr']]
outdf.to_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.8.9.17.csv',index=False)



