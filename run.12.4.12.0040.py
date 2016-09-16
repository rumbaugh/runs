import numpy as np
import math as m
import sys
import arrconv

CSO_arr = np.array(['J0003+4807','J1400+6210','J1414+4554','J1545+4751','J1734+0926','J1816+3457','J1823+7938','J1826+1831','J1927+7358','J1945+7055'])

compareto = 'J1945+7055'
compto = compareto
CSOload = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.8.17.12.dat'%compareto,dtype='string')
CSOload2 = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.11.5.12.dat'%compareto,dtype='string')
SBgrouparrt1 = CSOload[:,1].copy()
SBnumarrt1 = CSOload[:,2].copy()
SBgrouparrt2 = CSOload2[:,1].copy()
SBnumarrt2 = CSOload2[:,2].copy()
fluxest1 = CSOload[:,6].copy()
fluxest2 = CSOload2[:,6].copy()
compto_SBgrouparr,compto_SBnumarr,compto_fluxes = np.append(SBgrouparrt1,SBgrouparrt2),np.append(SBnumarrt1,SBnumarrt2),np.append(fluxest1,fluxest2)
compto_fluxes = arrconv.str2float(compto_fluxes)

fluxratios_dict = dict.fromkeys(CSO_arr,np.zeros(0))
norm_fluxratios_dict = dict.fromkeys(CSO_arr,np.zeros(0))
allnfr = np.zeros(0)

for i in range(0,len(CSO_arr)-1):
    CSOload = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.8.17.12.dat'%CSO_arr[i],dtype='string')
    CSOload2 = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.11.5.12.dat'%CSO_arr[i],dtype='string')
    fluxest = arrconv.str2float(CSOload[:,6].copy())
    SBgrouparrt = CSOload[:,1].copy()
    SBnumarrt = CSOload[:,2].copy()
    if len(CSOload2.shape) > 1:
        fluxest2 = arrconv.str2float(CSOload2[:,6].copy())
        fluxes = np.append(fluxest,fluxest2)
        SBgrouparrt2 = CSOload2[:,1].copy()
        SBnumarrt2 = CSOload2[:,2].copy()
        SBgrouparr,SBnumarr = np.append(SBgrouparrt,SBgrouparrt2),np.append(SBnumarrt,SBnumarrt2)
    else:
        fluxest2 = CSOload2[6]
        SBgrouparrt2 = CSOload2[1]
        SBnumarrt2 = CSOload2[2]
        SBgrouparr,SBnumarr = np.append(SBgrouparrt,SBgrouparrt2),np.append(SBnumarrt,SBnumarrt2)
        fluxes = np.append(fluxest,float(fluxest2))
    fluxratios = np.zeros(0,dtype='float')
    for j in range(0,len(fluxes)):
        if ((SBnumarr[j] != '13') & (SBnumarr[j] != '15')):
            g1 = np.where(compto_SBgrouparr == SBgrouparr[j])
            g1 = g1[0]
            g2 = np.where(compto_SBnumarr[g1] == SBnumarr[j])
            g2 = g2[0]
            if len(g2) > 1.1: sys.exit("g2 has more than one element")
            fluxratios = np.append(fluxratios,fluxes[j]/compto_fluxes[g1[g2[0]]])
    fluxratios_dict[CSO_arr[i]] = fluxratios
    normfluxratios = fluxratios/np.average(fluxratios)
    norm_fluxratios_dict[CSO_arr[i]] = normfluxratios
    print '%s - %i,%f'%(CSO_arr[i],len(fluxratios),np.std(normfluxratios))
    allnfr = np.append(allnfr,normfluxratios)
print 'All - %f'%np.std(allnfr)
shuff_allnfr = np.copy(allnfr)
np.random.shuffle(shuff_allnfr)
lengths = np.array([3,7,7,7,8,11,11,18,18])
maxind = 0
for i in range(0,len(lengths)):
    maxind += lengths[i]
    print lengths[i],np.std(shuff_allnfr[maxind-lengths[i]:maxind])
