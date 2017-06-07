import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/butler_test_LC_wmodel.pdf')
cr=np.loadtxt('/home/rumbaugh/butler_test/model_params.dat',dtype={'names':('SDR5ID','tau','sigma'),'formats':('f8','f8','f8')})

for i in range(0,len(cr)):
    SDR5ID=int(cr['SDR5ID'][i])
    crlc=np.loadtxt('/home/rumbaugh/butler_test/LC_%i.dat'%SDR5ID,dtype={'names':('mjd','mag','magerr','model'),'formats':('f8','f8','f8','f8')})
    #mjd,mag,magerr,model=crlc[:,0],crlc[:,1],crlc[:,2],crlc[:,3]
    mjd,mag,magerr,model=crlc['mjd'],crlc['mag'],crlc['magerr'],crlc['model']
    fig=plt.figure(1)
    fig.clf()
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 20
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.errorbar(mjd,mag,yerr=magerr,color='k',fmt='ro',lw=2,capsize=3,mew=1,zorder=0)
    plt.scatter(mjd,model,color='r',zorder=1,s=12,edgecolor='None')
    plt.xlabel('MJD')
    plt.ylabel('g-band magnitude')
    plt.title('%i'%SDR5ID)
    fig.savefig(psfpdf,format='pdf')

psfpdf.close()
