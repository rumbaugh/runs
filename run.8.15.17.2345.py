import numpy as np
import pandas as pd
execfile('angconvert.py')

df1=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.RF.csv')
df2=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.6.26.17.csv')

df=pd.merge(df1,df2,on=['field','cluster'],suffixes=('','_old'))
            
name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

clusters=df.cluster.values
for i in np.arange(len(clusters)): 
    try:
        name_dict[clusters[i]]
    except KeyError:
        name_dict[clusters[i]]=clusters[i]

df.set_index('cluster',inplace=True)

FILE=open('/home/rumbaugh/centroid_table.txt','w')
for cluster in clusters:
    FILE.write('{} & {:02d}:{:02d}:{:04.1f} & {:+02d}:{:02d}:{:04.2f} & {:02d}:{:02d}:{:04.1f} & {:+02d}:{:02d}:{:04.2f} & {:02d}:{:02d}:{:04.1f} & {:+02d}:{:02d}:{:04.2f} & {:02d}:{:02d}:{:04.1f} & {:+02d}:{:02d}:{:04.2f} & {:02d}:{:02d}:{:04.1f} & {:+02d}:{:02d}:{:04.2f} \\\\\n'.format(name_dict[cluster],deg2hms(df.loc[cluster].Xray_ra)[0],deg2hms(df.loc[cluster].Xray_ra)[1],deg2hms(df.loc[cluster].Xray_ra)[2],deg2dms(df.loc[cluster].Xray_dec)[0],deg2dms(df.loc[cluster].Xray_dec)[1],deg2dms(df.loc[cluster].Xray_dec)[2],  deg2hms(df.loc[cluster].MWM_ra)[0],deg2hms(df.loc[cluster].MWM_ra)[1],deg2hms(df.loc[cluster].MWM_ra)[2],deg2dms(df.loc[cluster].MWM_dec)[0],deg2dms(df.loc[cluster].MWM_dec)[1],deg2dms(df.loc[cluster].MWM_dec)[2],  deg2hms(df.loc[cluster].LWM_ra)[0],deg2hms(df.loc[cluster].LWM_ra)[1],deg2hms(df.loc[cluster].LWM_ra)[2],deg2dms(df.loc[cluster].LWM_dec)[0],deg2dms(df.loc[cluster].LWM_dec)[1],deg2dms(df.loc[cluster].LWM_dec)[2],   deg2hms(df.loc[cluster].MMCG_ra)[0],deg2hms(df.loc[cluster].MMCG_ra)[1],deg2hms(df.loc[cluster].MMCG_ra)[2],deg2dms(df.loc[cluster].MMCG_dec)[0],deg2dms(df.loc[cluster].MMCG_dec)[1],deg2dms(df.loc[cluster].MMCG_dec)[2],  deg2hms(df.loc[cluster].BCG_ra)[0],deg2hms(df.loc[cluster].BCG_ra)[1],deg2hms(df.loc[cluster].BCG_ra)[2],deg2dms(df.loc[cluster].BCG_dec)[0],deg2dms(df.loc[cluster].BCG_dec)[1],deg2dms(df.loc[cluster].BCG_dec)[2]))
FILE.close()
            
