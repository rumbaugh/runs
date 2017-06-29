import numpy as np
import pandas as pd
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

ntrials=10000
normfrac=0.317310507863
iUB=int(ntrials*(1-normfrac))

def open_csv(fname,names=None):
    df=pd.read_csv(fname,delim_whitespace=True)
    if df.columns[0]=='#':
        if names!=None:
            newnames=names
        else:
            newnames=df.columns[1:].tolist()
        df=pd.read_csv(fname,delim_whitespace=True,comment='#',names=newnames)
    return df

xdf=open_csv('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',names=['field','cluster','RA(deg)','Dec(deg)','rah','ram','ras','dech','decm','decs'])
xdf['field']=xdf.field.str.lower()
xdf['field'][np.in1d(xdf.field.values,['cl1324_north','cl1324_south'])]='cl1324'
clbdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_bounds.6.26.17.dat')
clmdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_members.6.26.17.dat')
bcgdf=open_csv('/home/rumbaugh/Chandra/ORELSE_cluster_member_info_all.6.26.17.dat')
tbcgdf=bcgdf[bcgdf.isBCG_tot==1].set_index(['cluster'])

clbdf=pd.merge(clbdf,xdf,on=['cluster','field'])

bcgra,bcgdec,lwra,lwdec,lwN=np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf),dtype='i8')
dist_bcg2x,dist_bcg2lw,dist_lw2x=np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf))
LWerr=np.zeros(len(clbdf))
for cluster,ic in zip(clbdf.cluster.unique(),np.arange(len(clbdf.cluster.unique()))):
    bcgra[ic],bcgdec[ic]=tbcgdf.loc[cluster].ra,tbcgdf.loc[cluster].dec
    lw_wt=(1./clmdf[clmdf.cluster==cluster].Mred).sum()
    lwra[ic],lwdec[ic]=(clmdf[clmdf.cluster==cluster].ra/clmdf[clmdf.cluster==cluster].Mred).sum()/lw_wt,(clmdf[clmdf.cluster==cluster].dec/clmdf[clmdf.cluster==cluster].Mred).sum()/lw_wt
    lwN[ic]=len(clmdf[clmdf.cluster==cluster])
    tmpdf=clmdf[clmdf.cluster==cluster]
    dist_bcg2x[ic],dist_bcg2lw[ic],dist_lw2x[ic]=SphDist(bcgra[ic],bcgdec[ic],clbdf["RA(deg)"][ic],clbdf["Dec(deg)"][ic])*60,SphDist(bcgra[ic],bcgdec[ic],lwra[ic],lwdec[ic],)*60,SphDist(lwra[ic],lwdec[ic],clbdf["RA(deg)"][ic],clbdf["Dec(deg)"][ic])*60
    grand=np.random.choice(np.arange(len(tmpdf)),((ntrials,len(tmpdf))))
    tmplw_wt=np.sum(1./tmpdf.Mred.values[grand],axis=1)
    tmplwra,tmplwdec=np.sum(tmpdf.ra.values[grand]/tmpdf.Mred.values[grand],axis=1)/tmplw_wt,np.sum(tmpdf.dec.values[grand]/tmpdf.Mred.values[grand],axis=1)/tmplw_wt
    tmpracen,tmpdeccen=np.median(tmplwra),np.median(tmplwdec)
    tmpdists=np.sort(SphDist(tmplwra,tmplwdec,tmpracen,tmpdeccen)*60)
    LWerr[ic]=tmpdists[iUB]
outdf=pd.DataFrame({'field':clbdf.field,'cluster':clbdf.cluster.unique(),'Xray_ra':clbdf["RA(deg)"],'Xray_dec':clbdf["Dec(deg)"],'BCG_ra':bcgra,'BCG_dec':bcgdec,'LWM_ra':lwra,'LWM_dec':lwdec,'LWM_Ngal':lwN,'dist_bcg2x':dist_bcg2x,'dist_bcg2lw':dist_bcg2lw,'dist_lw2x':dist_lw2x,'LWerr':LWerr})
outdf=outdf[['field','cluster','Xray_ra','Xray_dec','BCG_ra','BCG_dec','LWM_ra','LWM_dec','LWM_Ngal','dist_bcg2x','dist_bcg2lw','dist_lw2x','LWerr']]
outdf.to_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.6.26.17.csv',index=False)
