import numpy as np
import pandas as pd

name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.8.9.17.csv')
df2=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.7.16.17.csv')
df=pd.merge(df,df2,on=['field','cluster'],suffixes=('_RF',''))
df=df[:17]
df=df[df.field.values!='rxj1053']
            
FILE=open('/home/rumbaugh/test_table.txt','w')
for i in range(0,len(df)):
    try:
        name=name_dict[df.cluster.iloc[i]]
    except KeyError:
        name=df.cluster.iloc[i]
    FILE.write("%s & $%i\pm%i$ & $%i\pm%i$ & %.3f & $%i\pm%i$ & $%i\pm%i$ & %.3f & %.3f & %.3f & %.3f  & %.3f  & %.3f  & %.3f  & %.3f  & %.3f \\\\\n"%(name,np.round(df.Sig_red.iloc[i],-1),np.round(df.Sig_red_Error.iloc[i],-1),np.round(df.Sig_blue.iloc[i],-1),np.round(df.Sig_blue_Error.iloc[i],-1),df.perc.iloc[i],np.round(df.Sig_Q.iloc[i],-1),np.round(df.Sig_Q_Error.iloc[i],-1),np.round(df.Sig_SF.iloc[i],-1),np.round(df.Sig_SF_Error.iloc[i],-1),df.perc_RF.iloc[i],df.DSstat.iloc[i],df.P_DS.iloc[i],10**7*df.P3_RF.iloc[i],10**7*df.P4_RF.iloc[i],10**7*df.P3UB_RF.iloc[i],10**7*df.P3LB_RF.iloc[i],10**7*df.P4UB_RF.iloc[i],10**7*df.P4LB_RF.iloc[i]))
FILE.close()
