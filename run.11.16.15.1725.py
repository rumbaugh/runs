import numpy as np

crold=np.loadtxt('/home/rumbaugh/Chandra/548/oldtest_optmatch.548.dat',dtype={'names':('ID','ra','dec','err','nm','raopt','decopt','optID','P','like','dum1','dum2','dum3','dum4','dum5','dum6','dum7','dum8','dum9','dum10','PN'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S8','f8','f8','f8','f8','|S8','f8','f8','f8','f8','|S8','f8','f8','f8')})
crnew=np.loadtxt('/home/rumbaugh/Chandra/548/newtest_optmatch.548.dat',dtype={'names':('ID','ra','dec','err','nm','raopt','decopt','optID','P','like','dum1','dum2','dum3','dum4','dum5','dum6','dum7','dum8','dum9','dum10','PN'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S8','f8','f8','f8','f8','|S8','f8','f8','f8','f8','|S8','f8','f8','f8')})
diffP,diffPN=np.zeros(0),np.zeros(0)
for i in range(0,len(crold['ra'])):
    if ((crnew['nm'][i]==0)&(crold['nm'][i]==0)):
        print '%3i: No match'%i
    elif ((crnew['nm'][i]!=0)&(crold['nm'][i]==0)):
        print '%3i: Match in old, no match in new'
    elif ((crnew['nm'][i]==0)&(crold['nm'][i]!=0)):
        print '%3i: No match in old, match in new'
    else:
        print '%3i: Old - P = %.4f P(None) = %.4f\n New - P = %.4f P(None) = %.4f\n Diff:  P = %.4f P(None) = %.4f'%(i,crold['P'][i],crold['PN'][i],crnew['P'][i],crnew['PN'][i],crold['P'][i]-crnew['P'][i],crold['PN'][i]-crnew['PN'][i])
        diffP,diffPN=np.append(diffP,crold['P'][i]-crnew['P'][i]),np.append(diffPN,crold['PN'][i]-crnew['PN'][i])
print 'Average Prob Diff - %.4f (%.4f)\nAverage PN Diff - %.4f (%.4f)'%(np.average(diffP),np.average(diffPN),np.average(np.abs(diffP)),np.average(np.abs(diffPN)))
