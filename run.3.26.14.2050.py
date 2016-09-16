execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
import matplotlib.pyplot as plt

def CalcMeanErr(derr):
    merr = np.sqrt(np.sum(np.array(derr)**2))/len(derr)
    return merr

def CalcSTDErr(d,derr):
    merr = CalcMeanErr(derr)
    dstd,dmean = np.std(d),np.mean(d)
    tsum = np.sum((2*(np.array(d)-dmean))**2*((np.array(derr)**2+merr**2)))
    return 0.5/len(d)/dstd*np.sqrt(tsum)

date = '3.26.14'

frate,ftime_std,skew_mean,skew_std,Tfl_mean,Tfl_std = np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10)
frate_err,ftime_std_err,skew_mean_err,skew_std_err,Tfl_mean_err,Tfl_std_err = np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10)
amp_mean,amp_std,amp_mean_err,amp_std_err = np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
famp_mean,famp_std,famp_mean_err,famp_std_err = np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
bases,bases_err = np.zeros(0),np.zeros(0)

for source,i in zip(Abdo_data_dict,np.arange(10)):
    frate[i] = len(Abdo_data_dict[source]['ftime'])/325.
    frate_err[i] = np.sqrt(len(Abdo_data_dict[source]['ftime']))/325.
    ftime_std[i] = np.std(Abdo_data_dict[source]['ftime'])
    #ftime_std_err[i] = CalcSTDErr(Abdo_data_dict[source]['ftime'],Abdo_data_dict[source]['ftime err'])
    Tfl_std[i] = np.std(Abdo_data_dict[source]['Tfl'])
    Tfl_std_err[i] = CalcSTDErr(Abdo_data_dict[source]['Tfl'],Abdo_data_dict[source]['Tfl err'])
    skew_std[i] = np.std(Abdo_data_dict[source]['skew'])
    skew_std_err[i] = CalcSTDErr(Abdo_data_dict[source]['skew'],Abdo_data_dict[source]['skew err'])
    Tfl_mean[i] = np.mean(Abdo_data_dict[source]['Tfl'])
    skew_mean[i] = np.mean(Abdo_data_dict[source]['skew'])
    skew_mean_err[i] = CalcMeanErr(Abdo_data_dict[source]['skew err'])
    Tfl_mean_err[i] = CalcMeanErr(Abdo_data_dict[source]['Tfl err'])
    if 'amp' in Abdo_data_dict[source]:
        famp_errs = Abdo_data_dict[source]['amp']/Abdo_data_dict[source]['base']*np.sqrt((Abdo_data_dict[source]['amp err']/Abdo_data_dict[source]['amp'])**2+(Abdo_data_dict[source]['base err']/Abdo_data_dict[source]['base'])**2)
        amp_mean_err = np.append(amp_mean_err,CalcMeanErr(np.sqrt(Abdo_data_dict[source]['amp err']**2+Abdo_data_dict[source]['base err']**2)))
        amp_std_err = np.append(amp_std_err,CalcSTDErr(Abdo_data_dict[source]['amp']-Abdo_data_dict[source]['base'],np.sqrt(Abdo_data_dict[source]['amp err']**2+Abdo_data_dict[source]['base err']**2)))
        amp_std = np.append(amp_std,np.std(Abdo_data_dict[source]['amp']-Abdo_data_dict[source]['base']))
        amp_mean = np.append(amp_mean,np.mean(Abdo_data_dict[source]['amp']-Abdo_data_dict[source]['base']))
        famp_mean_err = np.append(famp_mean_err,CalcMeanErr(famp_errs))
        famp_std_err = np.append(famp_std_err,CalcSTDErr(Abdo_data_dict[source]['amp']/Abdo_data_dict[source]['base'],famp_errs))
        famp_std = np.append(famp_std,np.std(Abdo_data_dict[source]['amp']/Abdo_data_dict[source]['base']))
        famp_mean = np.append(famp_mean,np.mean(Abdo_data_dict[source]['amp']/Abdo_data_dict[source]['base']))
        bases = np.append(bases,Abdo_data_dict[source]['base'])
        bases_err = np.append(bases_err,Abdo_data_dict[source]['base err'])

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(frate,ftime_std,yerr=None,xerr=frate_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(frate,ftime_std)
plt.xlabel('Flare Rate (1/days)',fontsize=14)
plt.ylabel('Flare Separation STD (days)',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.frt_vs_ftimestd.%s.png'%date)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(skew_mean,skew_std,xerr=skew_mean_err,yerr=skew_std_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(skew_mean,skew_std)
plt.xlabel('Skew mean',fontsize=14)
plt.ylabel('Skew STD',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.skewavg_vs_skewstd.%s.png'%date)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(Tfl_mean,Tfl_std,xerr=Tfl_mean_err,yerr=Tfl_std_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(Tfl_mean,Tfl_std)
plt.xlabel('Mean Flare Length (days)',fontsize=14)
plt.ylabel('Flare Length STD (days)',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.Tflavg_vs_Tflstd.%s.png'%date)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(amp_mean,amp_std,xerr=amp_mean_err,yerr=amp_std_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(amp_mean,amp_std)
plt.xlabel('Mean Flare Amplitude',fontsize=14)
plt.ylabel('Flare Amplitude STD',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.ampavg_vs_ampstd.%s.png'%date)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(amp_mean,bases,xerr=amp_mean_err,yerr=bases_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(amp_mean,bases)
plt.xlabel('Mean Flare Amplitude',fontsize=14)
plt.ylabel('Base Amplitude',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.ampavg_vs_base.%s.png'%date)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(famp_mean,famp_std,xerr=famp_mean_err,yerr=famp_std_err,fmt='ro',lw=2,capsize=3,mew=1)

plt.scatter(famp_mean,famp_std)
plt.xlabel('Mean Normalized Flare Amplitude',fontsize=14)
plt.ylabel('Normalized Flare Amplitude STD',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/Abdo2010.nampavg_vs_nampstd.%s.png'%date)
