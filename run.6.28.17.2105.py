import numpy as np
import pandas as pd
import pyfits as py
execfile('/home/rumbaugh/angconvert.py')

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data

df=pd.read_csv('/home/rumbaugh/Graham_et_al_2016_flare_candidates.dat',delim_whitespace=True,na_values='-')

g16ra=hms2deg(df.RAh.values,df.RAm.values,df.RAs.values)
g16dec=dms2deg(df.DECd.values,df.DECm.values,df.DECs.values)

try:
    indsdf=pd.read_csv('/home/rumbaugh/G16_DR7_match.csv')
except IOError:
    import pydl.pydlutils.spheregroup
    sout=pydl.pydlutils.spheregroup.spherematch(bhdata['RA'],bhdata['DEC'],g16ra,g16dec,0.3/3600)
    indsdf=pd.DataFrame({'DR7IND':sout[0],'G16IND':sout[1],'DIST':sout[2]})
    indsdf.to_csv('/home/rumbaugh/G16_DR7_match.csv')



