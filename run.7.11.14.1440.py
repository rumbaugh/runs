execfile('/mnt/data2/rumbaugh/Fermi/scripts/MockBlazarLightcurves.py')
execfile('/home/rumbaugh/LinReg.py')
import matplotlib.pyplot as plt

def CalcMeanErr(derr):
    merr = np.sqrt(np.sum(np.array(derr)**2))/len(derr)
    return merr

def CalcSTDErr(d,derr):
    merr = CalcMeanErr(derr)
    dstd,dmean = np.std(d),np.mean(d)
    tsum = np.sum((2*(np.array(d)-dmean))**2*((np.array(derr)**2+merr**2)))
    return 0.5/len(d)/dstd*np.sqrt(tsum)

date = '7.11.14'

try:
    mtrials
except NameError:
    mtrials = 1000

frate,ftime_std,skew_mean,skew_std,Tfl_mean,Tfl_std = np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10)
frate_err,ftime_std_err,skew_mean_err,skew_std_err,Tfl_mean_err,Tfl_std_err = np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10),np.zeros(10)
amp_mean,amp_std,amp_mean_err,amp_std_err = np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
famp_mean,famp_std,famp_mean_err,famp_std_err = np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
fsep_mean,fsep_std = np.zeros(10),np.zeros(10)


for source,i in zip(Abdo_data_dict,np.arange(10)):
    frate[i] = len(Abdo_data_dict[source]['ftime'])/325.
    frate_err[i] = np.sqrt(len(Abdo_data_dict[source]['ftime']))/325.
    ftime_std[i] = np.std(Abdo_data_dict[source]['ftime'])
    fseps = Abdo_data_dict[source]['ftime'][1:]-Abdo_data_dict[source]['ftime'][:-1]
    fsep_mean[i],fsep_std[i] = np.mean(fseps),np.std(fseps)
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

#mskew,skewSTD = GenerateSkew(mtrials)
#mTfl,TflSTD = GenerateTfl(mtrials)
#mAmp,AmpSTD = GenerateAmp(mtrials)

def setupplt():
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

setupplt()
plt.scatter(fsep_mean,fsep_std)
plt.xlabel('Mean Flare Separations (days)',fontsize=14)
plt.ylabel('Flare Separation STD (days)',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testmock.fsep_vs_fsepstd.%s.png'%date)

setupplt()
plt.scatter(fsep_mean,Tfl_mean)
plt.xlabel('Mean Flare Separations (days)',fontsize=14)
plt.ylabel('Tfl',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testmock.fsep_vs_Tfl.%s.png'%date)

setupplt()
plt.scatter(fsep_std,Tfl_mean)
plt.xlabel('Flare Separation STD (days)',fontsize=14)
plt.ylabel('Tfl',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/testmock.fsepstd_vs_Tfl.%s.png'%date)
