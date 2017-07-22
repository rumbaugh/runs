import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('/home/rumbaugh/SN_fields.S1.AUTO_RMS.csv')
df1['field']='S1'
df2=pd.read_csv('/home/rumbaugh/SN_fields.S2.AUTO_RMS.csv')
df2['field']='S2'
df=df1.append(df2)

plt.figure(1)
plt.clf()
plt.hist(df.
