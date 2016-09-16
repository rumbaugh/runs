import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/LoadEVLA_2011.py')

CSOs_dict = LoadEVLA_2011('CSOs')
globalmean = {'Early': np.zeros(0), 'Late': np.zeros(0)}
for EorL in ['Late','Early']:
    CSO_meds = np.zeros(len(CSOs_dict['time'][EorL]))
    for i in range(0,len(CSO_meds)):
        CSOntemp = np.zeros(len(CSOs_dict[EorL].keys()))
        for j in range(0,len(CSOntemp)):
            CSO = CSOs_dict[EorL].keys()[j]
            gCSOtmp = np.where(CSOs_dict[EorL][CSO] > 0)[0]
            CSOntemp[j] = CSOs_dict[EorL][CSO][i]/np.mean(CSOs_dict[EorL][CSO][gCSOtmp])
        if len(CSOntemp[CSOntemp > 0]) > 0: CSO_meds[i] = np.median(CSOntemp[CSOntemp > 0])
    globalmean[EorL] = CSO_meds.copy()

for EorL in ['Late','Early']:
    allpoints = np.zeros(0)
    for CSO in CSOs_dict[EorL]:
        tflux = CSOs_dict[EorL][CSO].copy()
        gCSOtmp = np.where(tflux > 0)[0]
        allpoints = np.append(allpoints,tflux[gCSOtmp]/np.mean(tflux[gCSOtmp])/globalmean[EorL][gCSOtmp])
    print EorL,np.std(allpoints[allpoints>0])
