execfile('/home/rumbaugh/LoadVLA_2001.py')
execfile('/home/rumbaugh/Load1938.py')
import matplotlib.pyplot as plt

CSO1days,CSO1S,CSO2days,CSO2S = LoadVLA_2001(loadCSOs=True)

CSO1S /= np.mean(CSO1S)
CSO2S /= np.mean(CSO2S)

d0 = CSO1S[0]
CSO1S -= d0
CSO2S -= d0

plt.figure(1)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.clf()
plt.plot(CSO1days,CSO1S,lw=2,color='r',label='CSO 1244')
plt.plot(CSO2days,CSO2S,lw=2,color='b',ls='dashed',label='CSO 1400')
plt.legend(loc=3)
plt.scatter(CSO1days,CSO1S,color='r')
plt.scatter(CSO2days,CSO2S,color='b')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_VLA_2001.normfluxplot.3.17.14.png')

CSO_out_flux_dict,CSO_time_dict,CSO_norm_flux_dict = Load1938(returnCSOs=True)

CSOs = CSO_out_flux_dict.keys()

minday = np.zeros(len(CSOs))
for CSO,i in zip(CSOs,np.arange(len(CSOs))):
    minday[i] = np.min(CSO_time_dict[CSO])
    CSO_out_flux_dict[CSO] /= np.mean(CSO_out_flux_dict[CSO])
d0 = np.min(minday)

markers = np.array(["o","<",">","D","s","p","*","h","+","x"])
colors = np.array(['b','r','c','m','k','b','r','c','m','k'])
sizes = np.array([1.,1.,1.,1.,1.,1.,1.,1.,3.,1.])*25

plt.clf()
for CSO,i in zip(np.sort(CSOs),np.arange(len(CSOs))):
    plt.scatter((CSO_time_dict[CSO]-d0)/86400,CSO_out_flux_dict[CSO],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
plt.ylim(0.8,1.06)
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.legend(loc=3)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.normfluxplot.3.17.14.png')
