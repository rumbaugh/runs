import numpy as np
import pyfits as py
import pandas as pd
import pydl.pydlutils.spheregroup
mdf=pd.read_csv('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/cl1604/proc/cl1604/cl1604_optmatch_comb.1.19.16.dat',names=['indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'],delim_whitespace=True)
mdf=mdf[(mdf.raopt1.values>=0)&(mdf.probnone.values<.15)]
sdf=pd.read_csv('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat',delim_whitespace=True)
sdf=sdf[sdf.Q.values>=3]
sdf['RA'],sdf['DEC']=np.copy(sdf.ACS_RA.values),np.copy(sdf.ACS_DEC.values)
if len(sdf.RA[sdf.RA.values==0])>0:
    sdf.DEC[sdf.RA.values==0]=sdf.LFC_DEC.values[sdf.RA.values==0]
    sdf.RA[sdf.RA.values==0]=sdf.LFC_RA.values[sdf.RA.values==0]

sout=pydl.pydlutils.spheregroup.spherematch(mdf.raopt1.values,mdf.decopt1.values,sdf.RA.values,sdf.DEC.values,0.3/3600)

outdf=sdf.iloc[sout[1]][['#LFC_ID','MASK','SLIT','LFC_RA','LFC_DEC','r','i','z','redshift','red_err','Q','OLDIDs','PHOT_FLAGS','ACS_RA','ACS_DEC','ACS_ID','F606W','F814W']]
outdf.to_csv('/home/rumbaugh/SC1604_AGN_wSpecz.csv',index=False)




