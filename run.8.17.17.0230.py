import numpy as np
import pandas as pd

name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.8.9.17.csv')
df=df[:17]
df=df[df.field.values!='rxj1053']
            
FILE=open('/home/rumbaugh/SRoffset_table.txt','w')
for i in range(0,len(df)):
    try:
        name=name_dict[df.cluster.iloc[i]]
    except KeyError:
        name=df.cluster.iloc[i]
    FILE.write("%s & %.2f & %.2f & %.2f \\\\\n"%(name,df.mindistlit_LxT.iloc[i],df.mindistlit_sigT.iloc[i],df.mindistlit_Lxsig.iloc[i]))
FILE.close()
