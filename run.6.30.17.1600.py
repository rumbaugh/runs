import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import matplotlib.backends.backend_pdf as bpdf
p=6
psfpdf=bpdf.PdfPages('/home/rumbaugh/SN_CAR1_fits.p_%i.S1.OR.6.30.17.pdf'%p)

outlier_window=300
outlier_thresh=0.5
num=3

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

df=pd.read_csv('/home/rumbaugh/Eric_LC_S1.csv',skipinitialspace=True,names=['COADD_OBJECT_ID','RA','DEC','MJD','MAG','MAGERR','BAND','FLAGS'])

df=df[df.BAND.values=='g']

df.reset_index(inplace=True)

cids=df.COADD_OBJECT_ID.unique()

cids_rand=np.random.choice(cids,num,replace=False)

df=df[np.in1d(df.COADD_OBJECT_ID.values,cids_rand)]

df.reset_index(inplace=True)

for ind in np.arange(len(cids_rand)):
    DBID=df.COADD_OBJECT_ID.values[ind]
    LCdf=df[df.COADD_OBJECT_ID.values==DBID]
    try:
        outlier_arr=pickle.load(open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.outliers_g.pickle'%DBID,'rb'))
    except IOError:
        outlier_arr= np.zeros(len(LCdf.MAG.values),dtype='bool')
        for ipt in np.arange(len(outlier_arr)):
            gthresh=np.where(np.abs(LCdf.MJD.values-LCdf.MJD.values[ipt])<outlier_window)[0]
            if len(gthresh)>1:
                outlier_arr[ipt]= np.abs(np.median(LCdf.MAG.values[gthresh])-LCdf.MAG.values[ipt]) > outlier_thresh
        pickle.dump(outlier_arr,open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.outliers_g.pickle'%DBID,'wb'))
    LCdf=LCdf[outlier_arr==False]
    DRWmodel=cm.CarmaModel(LCdf.MJD.values,LCdf.MAG.values,LCdf.MAGERR.values,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsamples)
    pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.DRWsample_OR.p_%p.pickle'%(DBID,p),'wb'))

    plt.figure(1)
    plt.clf()
    sample.assess_fit(doShow=False)
    plt.subplots_adjust(hspace=0.25)
    plt.subplots_adjust(top=0.92)
    fig=plt.gcf()
    plt.text(0.5,0.95,'%i'%(DBID),fontsize=15,transform=fig.transFigure,horizontalalignment='center')
    fig.savefig(psfpdf,format='pdf',dpi=400)
    plt.clf()
    plt.close('all')
psfpdf.close()
