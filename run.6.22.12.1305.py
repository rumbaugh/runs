import numpy as np
import sys
lsarr = np.loadtxt('archive.nrao.edu/secured/TR4746/ls.6.22.12.txt',dtype='string')
msarr = np.array([])
for i in range(0,len(lsarr)):
    tempstr = lsarr[i]
    if ((tempstr[len(tempstr)-3:len(tempstr)] == '.ms') & (tempstr[0:3] == '11A')): 
        msarr = np.append(msarr,tempstr[0:len(tempstr)])
        print tempstr[0:len(tempstr)-1]
i,endloop = 0,0
while ((i < len(msarr)) & (endloop < 0.5)):
    listobs(vis=str(msarr[i]))
    print '\nlistobs executed for %s\n'%(msarr[i])
    if i < len(msarr)-1.1:
        con = raw_input("Continue? (y/n)\n")
        if ((con != 'y') & (con != 'yes') & (con != 'Y') & (con != 'Yes')): 
            print '\nEnding script...'
            endloop = 1
    i += 1
if endloop < 0.4: print '\nAll done!'
