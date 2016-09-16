from numpy import *

try: 
    MCtrials
except NameError:
    MCtrials = 1000

try:
    NStrials
except NameError:
    NStrials = 200

try:
    numopts
except NameError:
    numopts = 53

random.seed()

numzeros = zeros(MCtrials)
numgtr8,numgtr9,numgtr10,numgtr11,numgtr12,numgtr13,numgtr14 = zeros(MCtrials),zeros(MCtrials),zeros(MCtrials),zeros(MCtrials),zeros(MCtrials),zeros(MCtrials),zeros(MCtrials)
for i in range(0,MCtrials):
    temparr = zeros(numopts)
    for j in range(0,NStrials):
        temparr[random.randint(0,numopts)] += 1
    wherezero,wgtr8,wgtr9,wgtr10,wgtr11,wgtr12,wgtr13,wgtr14 = where(temparr < 0.5),where(temparr > 7.5),where(temparr > 8.5),where(temparr > 9.5),where(temparr > 10.5),where(temparr > 11.5),where(temparr > 12.5),where(temparr > 14.5)
    numzeros[i],numgtr8[i],numgtr9[i],numgtr10[i],numgtr11[i],numgtr12[i],numgtr13[i],numgtr14[i] = len(wherezero[0]),len(wgtr8[0]),len(wgtr9[0]),len(wgtr10[0]),len(wgtr11[0]),len(wgtr12[0]),len(wgtr13[0]),len(wgtr14[0])
wzero1T,wzero2T,wzero3T,wzero4T,wzero5T,wzero6T = where(numzeros > 0.5),where(numzeros > 1.5),where(numzeros > 2.5),where(numzeros > 3.5),where(numzeros > 4.5),where(numzeros > 5.5)
wgtr8,wgtr9,wgtr10,wgtr11,wgtr12,wgtr13,wgtr14 = where(numgtr8 > 0.5),where(numgtr9 > 0.5),where(numgtr10 > 0.5),where(numgtr11 > 0.5),where(numgtr12 > 0.5),where(numgtr13 > 0.5),where(numgtr14 > 0.5)
print "Number of MC Trials: %i\nNumber of NS trials: %i\nProb of 1+ zeros: %f\nProb of 2+ zeros: %f\nProb of 3+ zeros: %f\nProb of 4+ zeros: %f\nProb of 5+ zeros: %f\nProb of 6+ zeros: %f\nProb of  8+ hits: %f\nProb of  9+ hits: %f\nProb of 10+ hits: %f\nProb of 11+ hits: %f\nProb of 12+ hits: %f\nProb of 13+ hits: %f\nProb of 14+ hits: %f\n"%(MCtrials,NStrials,len(wzero1T[0])*1.0/MCtrials,len(wzero2T[0])*1.0/MCtrials,len(wzero3T[0])*1.0/MCtrials,len(wzero4T[0])*1.0/MCtrials,len(wzero5T[0])*1.0/MCtrials,len(wzero6T[0])*1.0/MCtrials,len(wgtr8[0])*1.0/MCtrials,len(wgtr9[0])*1.0/MCtrials,len(wgtr10[0])*1.0/MCtrials,len(wgtr11[0])*1.0/MCtrials,len(wgtr12[0])*1.0/MCtrials,len(wgtr13[0])*1.0/MCtrials,len(wgtr14[0])*1.0/MCtrials)
