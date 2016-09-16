import numpy as np

field='cl0023'
carr=['magenta','cyan']

for s in [1,2]:
    cr=np.loadtxt('/home/rumbaugh/Downloads/sample%i.cat'%s,dtype={'names':('Adam_ID','RA','Dec','mask','slit','iband','z','q','Roy_ID'),'formats':('|S24','f8','f8','|S24','|S24','f8','f8','i8','i8')})
    FILE1=open('/home/rumbaugh/sample%i_cl0023.WCS.reg'%s,'w')
    FILE1.write('fk5\n')
    FILE2=open('/home/rumbaugh/sample%i_rxj1716.WCS.reg'%s,'w')
    FILE2.write('fk5\n')
    for i in range(0,len(cr['RA'])):
        if cr['RA'][i]>200:
            FILE2.write('circle(%f,%f,5") #color=%s\n'%(cr['RA'][i],cr['Dec'][i],carr[s-1]))
        else:
            FILE1.write('circle(%f,%f,5") #color=%s\n'%(cr['RA'][i],cr['Dec'][i],carr[s-1]))
    FILE1.close()
    FILE2.close()
