import numpy as np
import pandas as pd
execfile('/home/rumbaugh/angconvert.py')

name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.6.26.17.csv')
RFdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.RF.csv')

df=pd.merge(df,RFdf,on=['field','cluster'],suffixes=('','_RF'))

FILE=open('/home/rumbaugh/centroid_table.txt','w')
for i in range(0,len(df)):
    try:
        name=name_dict[df.cluster.iloc[i]]
    except KeyError:
        name=df.cluster.iloc[i]
    FILE.write("%s & %02i$^h$%02i$^h$%02.0f & %+02i$^h$%02i$^h$%04.1f & %02i$^h$%02i$^h$%02.0f & %+02i$^h$%02i$^h$%04.1f & %02i$^h$%02i$^h$%02.0f & %+02i$^h$%02i$^h$%04.1f & %02i$^h$%02i$^h$%02.0f & %+02i$^h$%02i$^h$%04.1f & %02i$^h$%02i$^h$%02.0f & %+02i$^h$%02i$^h$%04.1f \\\\\n"%(name,deg2hms(df.Xray_ra.iloc[i])[0],deg2hms(df.Xray_ra.iloc[i])[1],deg2hms(df.Xray_ra.iloc[i])[2],deg2dms(df.Xray_dec.iloc[i])[0],deg2dms(df.Xray_dec.iloc[i])[1],deg2dms(df.Xray_dec.iloc[i])[2],deg2hms(df.LWM_ra.iloc[i])[0],deg2hms(df.LWM_ra.iloc[i])[1],deg2hms(df.LWM_ra.iloc[i])[2],deg2dms(df.LWM_dec.iloc[i])[0],deg2dms(df.LWM_dec.iloc[i])[1],deg2dms(df.LWM_dec.iloc[i])[2],deg2hms(df.MWM_ra.iloc[i])[0],deg2hms(df.MWM_ra.iloc[i])[1],deg2hms(df.MWM_ra.iloc[i])[2],deg2dms(df.MWM_dec.iloc[i])[0],deg2dms(df.MWM_dec.iloc[i])[1],deg2dms(df.MWM_dec.iloc[i])[2],deg2hms(df.BCG_ra.iloc[i])[0],deg2hms(df.BCG_ra.iloc[i])[1],deg2hms(df.BCG_ra.iloc[i])[2],deg2dms(df.BCG_dec.iloc[i])[0],deg2dms(df.BCG_dec.iloc[i])[1],deg2dms(df.BCG_dec.iloc[i])[2],deg2hms(df.MMCG_ra.iloc[i])[0],deg2hms(df.MMCG_ra.iloc[i])[1],deg2hms(df.MMCG_ra.iloc[i])[2],deg2dms(df.MMCG_dec.iloc[i])[0],deg2dms(df.MMCG_dec.iloc[i])[1],deg2dms(df.MMCG_dec.iloc[i])[2]))
FILE.close()

