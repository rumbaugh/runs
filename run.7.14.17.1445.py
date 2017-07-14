import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/SN_fields.S2_CAR1_fits.specobjs.7.14.17.pdf')

outlier_window=300
outlier_thresh=0.5
num=5000

ri=30122
normfrac=0.317310507863
nsamples=20000

iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)


specdf=pd.read_csv('/home/rumbaugh/SNfields_S2_cen_30122_spec.csv')

fitdf=pd.read_csv('/home/rumbaugh/SN_fields.S2.cen_{}.CAR1fits.csv'.format(ri))

fulldf=pd.merge(fitdf,specdf,left_on=['DataID','cid'],right_on=['dataid','coadd_object_id'],suffixes=('_DR7','_DR13'))
fulldf=fulldf[fulldf.numepoch.values>5]

try:
    fulldf.sigma_hat
except AttributeError:
    fulldf['sigma_hat']=fulldf.sig.values
    fulldf['sigma']=0.5*(fulldf.sigma_hat.values**2)*fulldf.tau.values
cdict={x:y for x,y in zip(['STAR','QSO','GALAXY'],['red','cyan','green'])}
for i in range(0,len(fulldf)):
    DBID=fulldf.cid.values[i]
    sample=pickle.load(open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.DRWsample_OR.pickle'%DBID,'rb'))

    plt.figure(1)
    plt.clf()
    sample.assess_fit(doShow=False)    
    fig=plt.gcf()
    curaxes=fig.get_axes()
    try:
        fig.delaxes(curaxes[3])
    except:
        pass
    fig.delaxes(curaxes[2])
    fig.delaxes(curaxes[1])
    ax1=curaxes[0]
    ax1.change_geometry(1,1,1)
    ax1.errorbar(sample.time,sample.y,sample.ysig,color='r',fmt='o',capsize=2,mew=0,ms=3)
    plt.subplots_adjust(hspace=0)
    plt.subplots_adjust(top=0.92)
    plt.text(0.5,0.95,'%i - %s: ltau=%.1f(%.1f),lsig=%.1f'%(DBID,fulldf['class'].values[i],np.log10(fulldf.tau[i]),-np.log(fulldf.tau[i]),np.log10(fulldf.sigma[i])),fontsize=15,transform=fig.transFigure,horizontalalignment='center',color=cdict[fulldf['class'].values[i]])
    fig.savefig(psfpdf,format='pdf',dpi=400)

    plt.clf()
    plt.close('all')
    plt.figure(1)
    sample.plot_2dkde('log_omega','sigma',doPlotStragglers=False)
    fig=plt.gcf()
    ax0=fig.get_axes()[0]
    ax0.text(0.5,0.9,'%i - %s: ltau=%.1f(%.1f),lsig=%.1f'%(DBID,fulldf['class'].values[i],np.log10(fulldf.tau[i]),-np.log(fulldf.tau[i]),np.log10(fulldf.sigma[i])),fontsize=15,transform=fig.transFigure,horizontalalignment='center',color=cdict[fulldf['class'].values[i]])
    fig.savefig(psfpdf,format='pdf')
    plt.clf()
    plt.close('all')

psfpdf.close()
