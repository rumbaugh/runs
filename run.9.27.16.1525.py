import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/setup_adam_cats.py')
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_wACS.9.27.16.pdf')

fc=24
try:
    plot4labels
except NameError:
    plot4labels=True
if plot4labels:
    lblsize=20
else:
    lblsize=4

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})
crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.3.6.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRS['field'])): crRS['field'][i]=target_dir[crRS['field'][i]]

crall=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_all.9.26.16.dat',dtype={'names':('mag','col','field'),'formats':('f8','f8','|S16')})
cragn=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_AGN.9.26.16.dat',dtype={'names':('mag','col','field'),'formats':('f8','f8','|S16')})
for field in targets[np.argsort(zlist)]:
    gall,gAGN=np.where(crall['field']==field)[0],np.where(cragn['field']==field)[0]    
    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    if field=='cl1604':y0,m,sig=crRS_ACS['y0']+0,crRS_ACS['m']+0,crRS_ACS['sig']+0
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.rc('xtick',labelsize=20)
    plt.rc('ytick',labelsize=20)
    plt.fontsize = 20
    plt.rcParams.update({'font.size':28})
    plt.tick_params(which='major',length=8,width=2,labelsize=lblsize)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=lblsize)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(crall['mag'][gall],crall['col'][gall])
    ax.scatter(cragn['mag'][gAGN],cragn['col'][gAGN],color='magenta',marker='d',s=96)
    ax.set_title(field,fontsize=10)
    if field == 'cl1604':
        plt.xticks(np.arange(21,26))
        ax.set_xlim(20.5,25.5)
        ax.set_ylim(-0.5,2.6)
        ax.set_xlabel('F814W',fontsize=fc)
        ax.set_ylabel('F606W-F814W',fontsize=fc)
    else:
        ax.set_xlim(-27,-19.5)
        ax.set_ylim(-0.5,1.72)
        ax.set_xlabel(r'$M_{red}$',fontsize=fc)
        ax.set_ylabel(r'$M_{blue} - M_{red}$',fontsize=fc)
    xlim=plt.xlim()
    ylim=plt.ylim()
    xspace=np.linspace(xlim[0],xlim[1],1000)
    ydummy=m*(xspace)+y0
    ax.plot(xspace,ydummy+0.5*width,ls='--',lw=2,color='r')
    ax.plot(xspace,ydummy-0.5*width,ls='--',lw=2,color='r')
    if field == 'cl1604':
        ax.set_xlim(20.5,25)
        ax.set_ylim(0,2.1)
    else:
        ax.set_xlim(-25.7,-19.5)
        ax.axvline(-20.9,color='k',ls='dotted',lw=2)
        ax.set_ylim(0,1.72)
    fig.savefig(psfpdf,format='pdf')
    
psfpdf.close()
#FILERS.close()
